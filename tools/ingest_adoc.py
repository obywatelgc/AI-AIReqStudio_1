#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
tools/ingest_adoc.py

Minimalny, czytelny ingestion dokumentacji AsciiDoc z obsługą:
- include::ścieżka[...]
- leveloffset=+N / -N w include
- rekurencyjne rozwijanie include (z ochroną przed cyklem)
- chunkowanie po nagłówkach AsciiDoc (=,==,===,...)
- dodatkowe cięcie długich sekcji na części o max_chars z overlap
- zapis chunków jako JSON do kb/chunks/EBP (domyślnie)
- zapis manifestu kb/chunks/EBP/_manifest.json

Uruchomienie (domyślnie):
  python tools/ingest_adoc.py

Jawnie:
  python tools/ingest_adoc.py --doc-dir doc/EBP --root CustomerWebUserGuide.adoc --out-dir kb/chunks/EBP
"""

import argparse
import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple


# Nagłówki AsciiDoc: = Tytuł, == Tytuł, === Tytuł ...
ADOC_HEADING_RE = re.compile(r"^(={1,6})\s+(.+?)\s*$")

# include::ścieżka[atrybuty]
INCLUDE_RE = re.compile(r"^\s*include::([^\[]+)\[([^\]]*)\]\s*$")


def should_skip_include(include_target: str) -> bool:
    """
    Pomija include do wspolnego katalogu shared, np.:
      include::../../shared/typografia.adoc[]
      include::../../shared/footer.adoc[]
    """
    norm = include_target.replace("\\", "/").strip()
    return norm == "../../shared" or norm.startswith("../../shared/")


def parse_leveloffset(attrs: str) -> int:
    """
    Szuka leveloffset w atrybutach include.
    Przykłady:
      leveloffset=+1
      leveloffset=-2
      leveloffset=+1,foo=bar
    Brak -> 0
    """
    m = re.search(r"leveloffset\s*=\s*([+-]?\d+)", attrs)
    if not m:
        return 0
    return int(m.group(1))


@dataclass
class FlatLine:
    """
    Jedna linia dokumentu po rozwinięciu include.
    - text: treść linii
    - source_file: ścieżka relatywna od doc_dir (np. chapters/Main.adoc)
    - source_line: numer linii w source_file (1-based)
    - level_offset: skumulowany offset poziomu nagłówków wynikający z include
    """
    text: str
    source_file: str
    source_line: int
    level_offset: int


def read_text_lines(path: Path) -> List[str]:
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def flatten_includes(
    doc_dir: Path,
    root_relpath: str,
    max_depth: int = 30,
) -> List[FlatLine]:
    """
    Rozwija include::...[] rekurencyjnie zaczynając od root_relpath.
    Zwraca listę FlatLine.

    - include ścieżka jest interpretowana względem katalogu pliku, w którym wystąpił include
    - leveloffset z include jest sumowany (dziedziczony) dla całego włączanego pliku
    - wykrywa cykle include
    """
    visited_stack: List[str] = []

    def rec(file_rel: str, base_dir: Path, depth: int, inherited_offset: int) -> List[FlatLine]:
        if depth > max_depth:
            raise RuntimeError(f"Max include depth exceeded at {file_rel}")

        if file_rel in visited_stack:
            cycle = " -> ".join(visited_stack + [file_rel])
            raise RuntimeError(f"Include cycle detected: {cycle}")

        visited_stack.append(file_rel)

        full_path = (doc_dir / file_rel).resolve()
        if not full_path.exists():
            raise FileNotFoundError(f"Included file not found: {file_rel} (resolved: {full_path})")

        lines = read_text_lines(full_path)
        out: List[FlatLine] = []

        for idx, line in enumerate(lines, start=1):
            m = INCLUDE_RE.match(line)
            if m:
                include_target = m.group(1).strip()
                if should_skip_include(include_target):
                    print(f"WARN: skipping include {include_target} (from {file_rel}:{idx})")
                    continue
                attrs = m.group(2).strip()
                inc_offset = parse_leveloffset(attrs)

                # include_target jest względem base_dir (katalog pliku, w którym jest include)
                target_full = (base_dir / include_target).resolve()
                if not target_full.exists():
                    raise FileNotFoundError(
                        f"Included file not found: {include_target} "
                        f"(from {file_rel}:{idx}, resolved: {target_full})"
                    )

                # relpath od doc_dir
                target_rel = target_full.relative_to(doc_dir.resolve()).as_posix()

                out.extend(rec(
                    file_rel=target_rel,
                    base_dir=target_full.parent,
                    depth=depth + 1,
                    inherited_offset=inherited_offset + inc_offset
                ))
            else:
                out.append(FlatLine(
                    text=line,
                    source_file=file_rel,
                    source_line=idx,
                    level_offset=inherited_offset
                ))

        visited_stack.pop()
        return out

    root_full = (doc_dir / root_relpath).resolve()
    root_base = root_full.parent
    return rec(root_relpath, root_base, depth=0, inherited_offset=0)


def detect_heading(line: str) -> Optional[Tuple[int, str]]:
    """
    Zwraca (level, title) jeśli linia jest nagłówkiem AsciiDoc.
    level: 1..6 (liczba '=')
    """
    m = ADOC_HEADING_RE.match(line)
    if not m:
        return None
    level = len(m.group(1))
    title = m.group(2).strip()
    return level, title


def normalize_ws(text: str) -> str:
    """
    Minimalna normalizacja:
    - usuwa spacje końcowe w liniach
    - zapewnia końcowy newline
    """
    t = "\n".join([ln.rstrip() for ln in text.splitlines()]).strip()
    return (t + "\n") if t else ""


def split_by_max_chars(text: str, max_chars: int, overlap: int) -> List[str]:
    """
    Jeśli tekst jest dłuższy niż max_chars, tnie na kawałki z overlap.
    Prosto i przewidywalnie: tnie po znakach.
    """
    text = text.strip()
    if not text:
        return []
    if len(text) <= max_chars:
        return [text + "\n"]

    parts: List[str] = []
    start = 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        parts.append(text[start:end].strip() + "\n")
        if end == len(text):
            break
        start = max(0, end - overlap)
    return parts


@dataclass
class Chunk:
    """
    Jeden chunk do /kb/chunks.
    - chunk_id: DOC-000001...
    - root_file: root (np. CustomerWebUserGuide.adoc)
    - heading_path: stos nagłówków (po uwzględnieniu leveloffset)
    - section_title: tytuł sekcji (ostatni nagłówek)
    - text: treść chunku
    - primary_source_file: plik, z którego pochodzi najwięcej linii
    - provenance: lista bloków źródłowych (file + range linii)
    """
    chunk_id: str
    root_file: str
    heading_path: List[Dict]
    section_title: str
    text: str
    primary_source_file: str
    provenance: List[Dict]


def build_provenance(flat_lines: List[FlatLine]) -> Tuple[str, List[Dict]]:
    """
    Zwraca:
      - primary_source_file: plik z największą liczbą linii w sekcji
      - provenance: spójne zakresy linii dla kolejnych fragmentów z tych samych plików
    """
    if not flat_lines:
        return "(none)", []

    counts: Dict[str, int] = {}
    for fl in flat_lines:
        counts[fl.source_file] = counts.get(fl.source_file, 0) + 1
    primary = max(counts.items(), key=lambda x: x[1])[0]

    prov: List[Dict] = []
    cur_file = flat_lines[0].source_file
    start = flat_lines[0].source_line
    prev = flat_lines[0].source_line

    for fl in flat_lines[1:]:
        if fl.source_file == cur_file and fl.source_line == prev + 1:
            prev = fl.source_line
            continue
        prov.append({"source_file": cur_file, "line_start": start, "line_end": prev})
        cur_file = fl.source_file
        start = fl.source_line
        prev = fl.source_line

    prov.append({"source_file": cur_file, "line_start": start, "line_end": prev})
    return primary, prov


def chunk_flat_document(flat: List[FlatLine], root_file: str, max_chars: int, overlap: int) -> List[Chunk]:
    """
    Tnie “spłaszczony” dokument (FlatLine) na sekcje po nagłówkach.
    Uwaga: leveloffset wpływa na efektywny poziom nagłówka w heading_path.
    """
    chunks: List[Chunk] = []
    heading_stack: List[Dict] = []

    current_section_title = "(no heading)"
    current_lines: List[FlatLine] = []
    saw_heading = False
    counter = 0

    def flush_section():
        nonlocal counter, current_lines, current_section_title
        if not current_lines:
            return
        section_text = "\n".join(fl.text for fl in current_lines).strip()
        if not section_text:
            current_lines = []
            return

        primary, prov = build_provenance(current_lines)
        parts = split_by_max_chars(section_text, max_chars=max_chars, overlap=overlap)

        for part in parts:
            counter += 1
            chunks.append(Chunk(
                chunk_id=f"DOC-{counter:06d}",
                root_file=root_file,
                heading_path=heading_stack.copy(),
                section_title=current_section_title,
                text=normalize_ws(part),
                primary_source_file=primary,
                provenance=prov,
            ))

        current_lines = []

    for fl in flat:
        hd = detect_heading(fl.text)
        if hd:
            saw_heading = True
            flush_section()

            base_level, title = hd
            eff_level = base_level + fl.level_offset
            if eff_level < 1:
                eff_level = 1
            if eff_level > 6:
                eff_level = 6

            while heading_stack and heading_stack[-1]["level"] >= eff_level:
                heading_stack.pop()
            heading_stack.append({"level": eff_level, "title": title})

            current_section_title = title
            continue

        current_lines.append(fl)

    flush_section()

    if not saw_heading:
        whole = "\n".join(fl.text for fl in flat).strip()
        if whole:
            primary, prov = build_provenance(flat)
            parts = split_by_max_chars(whole, max_chars=max_chars, overlap=overlap)
            for part in parts:
                counter += 1
                chunks.append(Chunk(
                    chunk_id=f"DOC-{counter:06d}",
                    root_file=root_file,
                    heading_path=[],
                    section_title="(whole document)",
                    text=normalize_ws(part),
                    primary_source_file=primary,
                    provenance=prov,
                ))

    return chunks


def main() -> int:
    ap = argparse.ArgumentParser(description="Ingest AsciiDoc with include:: into kb/chunks.")
    ap.add_argument("--doc-dir", default="doc/EBP", help="Directory with AsciiDoc documentation.")
    ap.add_argument("--root", default="CustomerWebUserGuide.adoc", help="Root AsciiDoc file (relative to doc-dir).")
    ap.add_argument("--out-dir", default="kb/chunks/EBP", help="Output directory for chunks.")
    ap.add_argument("--max-chars", type=int, default=6000, help="Max chars per chunk part.")
    ap.add_argument("--overlap", type=int, default=500, help="Overlap chars for large section splitting.")
    ap.add_argument("--max-depth", type=int, default=30, help="Max recursion depth for include expansion.")
    args = ap.parse_args()

    doc_dir = Path(args.doc_dir).resolve()
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    root_rel = args.root.replace("\\", "/")
    root_path = (doc_dir / root_rel).resolve()

    if not root_path.exists():
        print(f"ERROR: root file not found: {root_path}")
        return 2

    print(f"Doc dir:   {doc_dir}")
    print(f"Root file: {root_path}")
    print(f"Out dir:   {out_dir}")

    try:
        flat = flatten_includes(doc_dir=doc_dir, root_relpath=root_rel, max_depth=args.max_depth)
    except Exception as e:
        print(f"ERROR during include flattening: {e}")
        return 2

    chunks = chunk_flat_document(
        flat=flat,
        root_file=root_rel,
        max_chars=args.max_chars,
        overlap=args.overlap
    )

    # zapis chunków
    for ch in chunks:
        (out_dir / f"{ch.chunk_id}.json").write_text(
            json.dumps(asdict(ch), ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    manifest = {
        "schema_version": "1.0.0",
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "source": {
            "doc_dir": str(doc_dir).replace("\\", "/"),
            "root_file": root_rel
        },
        "settings": {
            "max_chars": args.max_chars,
            "overlap": args.overlap,
            "max_depth": args.max_depth
        },
        "statistics": {
            "flat_lines": len(flat),
            "chunks": len(chunks)
        },
        "chunks": [
            {
                "chunk_id": c.chunk_id,
                "section_title": c.section_title,
                "primary_source_file": c.primary_source_file
            }
            for c in chunks
        ]
    }

    (out_dir / "_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"Flattened lines: {len(flat)}")
    print(f"Chunks created:  {len(chunks)}")
    print(f"Manifest:        {out_dir / '_manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
