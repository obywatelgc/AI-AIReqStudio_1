#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import hashlib
import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Tuple


H2_RE = re.compile(r"^(#{2})\s+(.+?)\s*$")
H3_RE = re.compile(r"^(#{3})\s+(.+?)\s*$")

# Start wymagania: **WM-01 Tytuł**
REQ_RE = re.compile(r"^\s*\*\*(WM-\d{1,2})\s+(.+?)\*\*\s*$")

IGNORED_LINE_RE = re.compile(r"^\s*\*\*Opis wymagań\*\*\s*$", re.IGNORECASE)


def sha256_text(text: str) -> str:
    h = hashlib.sha256()
    h.update(text.encode("utf-8"))
    return "sha256:" + h.hexdigest()


def slugify_pl(text: str) -> str:
    """Prosty slug: usuwa polskie znaki, zamienia na lowercase, spacje na '-'."""
    repl = str.maketrans({
        "ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n", "ó": "o", "ś": "s", "ż": "z", "ź": "z",
        "Ą": "a", "Ć": "c", "Ę": "e", "Ł": "l", "Ń": "n", "Ó": "o", "Ś": "s", "Ż": "z", "Ź": "z",
    })
    t = text.translate(repl).lower()
    # usuń znaki nie-alfanum i spacje -> myślniki
    t = re.sub(r"[^a-z0-9\s-]", "", t)
    t = re.sub(r"\s+", "-", t).strip("-")
    t = re.sub(r"-{2,}", "-", t)
    return t


def normalize_wm_id(raw_id: str, zero_pad_to: int = 2) -> str:
    """
    Normalizuje WM-1 -> WM-01 (dla zero_pad_to=2).
    Jeśli już WM-01, zostawia.
    """
    m = re.match(r"^(WM-)(\d{1,2})$", raw_id.strip())
    if not m:
        return raw_id.strip()
    prefix, num = m.group(1), m.group(2)
    return prefix + num.zfill(zero_pad_to)


def trim_empty_lines(lines: List[str]) -> List[str]:
    """Usuwa puste linie na początku i końcu."""
    start = 0
    end = len(lines)
    while start < end and lines[start].strip() == "":
        start += 1
    while end > start and lines[end - 1].strip() == "":
        end -= 1
    return lines[start:end]


@dataclass
class Requirement:
    req_id: str
    req_id_raw: str
    req_type: str
    title: str
    section_h2: Optional[str]
    section_h3: Optional[str]
    line_start: int
    line_end: int
    anchor: str
    body_markdown: str
    body_sha256: str


def parse_requirements(md_path: Path) -> Tuple[List[Requirement], List[Dict], List[Dict]]:
    """
    Zwraca:
      - listę wymagań (Requirement)
      - listę warnings
      - listę errors
    """
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    requirements: List[Requirement] = []
    warnings: List[Dict] = []
    errors: List[Dict] = []

    current_h2: Optional[str] = None
    current_h3: Optional[str] = None

    current_req_id_raw: Optional[str] = None
    current_req_id_norm: Optional[str] = None
    current_req_title: Optional[str] = None
    current_req_start: Optional[int] = None
    current_body_lines: List[str] = []

    def close_current(end_line_index: int) -> None:
        nonlocal current_req_id_raw, current_req_id_norm, current_req_title
        nonlocal current_req_start, current_body_lines, current_h2, current_h3

        if current_req_id_norm is None or current_req_start is None or current_req_title is None:
            return

        # body = zebrane linie po nagłówku WM
        body_lines = trim_empty_lines(current_body_lines)

        # usuń "**Opis wymagań**" jeżeli jest na początku body
        if body_lines and IGNORED_LINE_RE.match(body_lines[0]):
            body_lines = trim_empty_lines(body_lines[1:])

        body_md = "\n".join(body_lines).rstrip() + ("\n" if body_lines else "")
        body_hash = sha256_text(body_md)

        anchor = slugify_pl(f"{current_req_id_norm} {current_req_title}")

        if body_md.strip() == "":
            warnings.append({
                "code": "EMPTY_BODY",
                "message": f"Requirement {current_req_id_norm} has empty body.",
                "req_id": current_req_id_norm,
                "source_ref": {"file": str(md_path), "line": current_req_start + 1},
                "severity": "warning",
            })

        req = Requirement(
            req_id=current_req_id_norm,
            req_id_raw=current_req_id_raw,
            req_type="WM",
            title=current_req_title,
            section_h2=current_h2,
            section_h3=current_h3,
            line_start=current_req_start + 1,      # ludzkie numerowanie od 1
            line_end=end_line_index + 1,           # jw.
            anchor=anchor,
            body_markdown=body_md,
            body_sha256=body_hash,
        )
        requirements.append(req)

        # wyczyść bieżące
        current_req_id_raw = None
        current_req_id_norm = None
        current_req_title = None
        current_req_start = None
        current_body_lines = []

    for i, line in enumerate(lines):
        m2 = H2_RE.match(line)
        m3 = H3_RE.match(line)
        mr = REQ_RE.match(line)

        if m2:
            # nowa sekcja H2 -> zamknij wymaganie (jeśli otwarte)
            close_current(i - 1)
            current_h2 = m2.group(2).strip()
            current_h3 = None
            continue

        if m3:
            # nowa sekcja H3 -> zamknij wymaganie (jeśli otwarte)
            close_current(i - 1)
            current_h3 = m3.group(2).strip()
            continue

        if mr:
            # start nowego wymagania -> zamknij poprzednie (jeśli otwarte)
            close_current(i - 1)

            raw_id = mr.group(1).strip()
            title = mr.group(2).strip()

            norm_id = normalize_wm_id(raw_id, zero_pad_to=2)

            # walidacja: WM poza H3
            if current_h3 is None:
                warnings.append({
                    "code": "REQ_OUTSIDE_H3",
                    "message": f"Requirement {norm_id} found without an active H3 (###) section.",
                    "req_id": norm_id,
                    "source_ref": {"file": str(md_path), "line": i + 1},
                    "severity": "warning",
                })

            current_req_id_raw = raw_id
            current_req_id_norm = norm_id
            current_req_title = title
            current_req_start = i
            current_body_lines = []
            continue

        # zwykła linia: jeśli jesteśmy w trakcie wymagania, dodaj do body
        if current_req_id_norm is not None:
            current_body_lines.append(line)

    # koniec pliku -> zamknij ostatnie
    close_current(len(lines) - 1)

    # walidacja duplikatów po req_id
    seen: Dict[str, int] = {}
    for req in requirements:
        if req.req_id in seen:
            errors.append({
                "code": "DUPLICATE_REQ_ID",
                "message": f"Duplicate requirement id {req.req_id}.",
                "req_id": req.req_id,
                "source_ref": {"file": str(md_path), "line": req.line_start},
                "severity": "error",
            })
        else:
            seen[req.req_id] = req.line_start

    return requirements, warnings, errors


def write_work_items(requirements: List[Requirement], out_dir: Path, source_file: str) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for req in requirements:
        p = out_dir / f"{req.req_id}.md"
        frontmatter = {
            "req_id": req.req_id,
            "title": req.title,
            "req_type": req.req_type,
            "source_file": source_file,
            "line_start": req.line_start,
            "line_end": req.line_end,
            "section_h2": req.section_h2,
            "section_h3": req.section_h3,
            "anchor": req.anchor,
            "hash": req.body_sha256,
        }
        fm_lines = ["---"]
        for k, v in frontmatter.items():
            fm_lines.append(f'{k}: {json.dumps(v, ensure_ascii=False)}')
        fm_lines.append("---\n")

        content = "\n".join(fm_lines) + "## Requirement body (raw)\n\n" + (req.body_markdown or "")
        p.write_text(content, encoding="utf-8")


def write_index(requirements: List[Requirement], warnings: List[Dict], errors: List[Dict],
                input_file: Path, output_file: Path) -> None:
    output_file.parent.mkdir(parents=True, exist_ok=True)

    doc_hash = sha256_text(input_file.read_text(encoding="utf-8"))

    by_type: Dict[str, int] = {}
    by_section: Dict[str, int] = {}

    for r in requirements:
        by_type[r.req_type] = by_type.get(r.req_type, 0) + 1
        key = r.section_h3 or "(no_h3)"
        by_section[key] = by_section.get(key, 0) + 1

    index = {
        "schema_version": "1.0.0",
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "generator": {"tool": "tools/parse_requirements.py", "tool_version": "0.1.0"},
        "source": {
            "file": str(input_file).replace("\\", "/"),
            "format": "markdown",
            "encoding": "utf-8",
            "document_hash": doc_hash,
        },
        "statistics": {
            "total_requirements": len(requirements),
            "requirements_by_type": by_type,
            "requirements_by_section_h3": [
                {"section_h3": k, "count": v} for k, v in sorted(by_section.items(), key=lambda x: x[0])
            ],
            "warnings_count": len(warnings),
            "errors_count": len(errors),
        },
        "warnings": warnings,
        "errors": errors,
        "requirements": [asdict(r) for r in requirements],
    }

    output_file.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


def write_report(warnings: List[Dict], errors: List[Dict], report_file: Path) -> None:
    report_file.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# Raport parsowania wymagań\n")
    lines.append(f"- Ostrzeżenia: {len(warnings)}")
    lines.append(f"- Błędy: {len(errors)}\n")

    if errors:
        lines.append("## Błędy\n")
        for e in errors:
            sr = e.get("source_ref", {})
            lines.append(f"- **{e['code']}**: {e['message']} ({sr.get('file')}:{sr.get('line')})")
        lines.append("")

    if warnings:
        lines.append("## Ostrzeżenia\n")
        for w in warnings:
            sr = w.get("source_ref", {})
            lines.append(f"- **{w['code']}**: {w['message']} ({sr.get('file')}:{sr.get('line')})")
        lines.append("")

    report_file.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Parse WM requirements from a markdown file.")
    ap.add_argument("--input", default="src/wymagania.md", help="Input markdown file with requirements.")
    ap.add_argument("--output", default="spec/_trace/requirements_index.json", help="Output index JSON path.")
    ap.add_argument("--work-items-dir", default="spec/_trace/work_items", help="Directory for per-requirement files.")
    ap.add_argument("--no-work-items", action="store_true", help="Do not generate work item files.")
    ap.add_argument("--report", default="spec/_trace/requirements_parse_report.md", help="Output parse report path.")
    ap.add_argument("--fail-on-error", action="store_true", help="Exit with code 2 if errors were found.")
    args = ap.parse_args()

    input_file = Path(args.input)
    output_file = Path(args.output)
    work_items_dir = Path(args.work_items_dir)
    report_file = Path(args.report)

    if not input_file.exists():
        print(f"ERROR: input file not found: {input_file}")
        return 2

    requirements, warnings, errors = parse_requirements(input_file)

    write_index(requirements, warnings, errors, input_file=input_file, output_file=output_file)
    write_report(warnings, errors, report_file=report_file)

    if not args.no_work_items:
        write_work_items(requirements, out_dir=work_items_dir, source_file=str(input_file).replace("\\", "/"))

    print(f"Parsed requirements: {len(requirements)}")
    print(f"Warnings: {len(warnings)}; Errors: {len(errors)}")
    print(f"Index written to: {output_file}")
    if not args.no_work_items:
        print(f"Work items written to: {work_items_dir}")
    print(f"Report written to: {report_file}")

    if args.fail_on_error and errors:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
