#!/usr/bin/env python3
"""
Convert a DOCX/DOCM file to Markdown.

Usage:
  python tools/docx_to_markdown.py -i input.docx -o output.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable, Optional, Tuple, Union

try:
    import docx
    from docx.document import Document as DocumentType
    from docx.table import _Cell, Table
    from docx.text.paragraph import Paragraph
except ImportError as exc:  # pragma: no cover - runtime dependency guard
    raise SystemExit(
        "Missing dependency: python-docx\n"
        "Install with: pip install python-docx"
    ) from exc


BlockItem = Union[Paragraph, Table]


def escape_markdown(text: str) -> str:
    if not text:
        return ""
    text = text.replace("\\", "\\\\")
    return re.sub(r"([`*_{}\[\]()#+\-.!|>])", r"\\\1", text)


def paragraph_text(paragraph: Paragraph) -> str:
    parts: list[str] = []
    for run in paragraph.runs:
        run_text = run.text or ""
        if not run_text:
            continue
        run_text = escape_markdown(run_text)
        if run.bold and run.italic:
            run_text = f"***{run_text}***"
        elif run.bold:
            run_text = f"**{run_text}**"
        elif run.italic:
            run_text = f"*{run_text}*"
        parts.append(run_text)
    if not parts:
        return escape_markdown(paragraph.text.strip())
    return "".join(parts).strip()


def heading_level(paragraph: Paragraph) -> Optional[int]:
    style_name = getattr(paragraph.style, "name", "") or ""
    match = re.match(r"Heading\s+([1-9][0-9]*)$", style_name, flags=re.IGNORECASE)
    if match:
        return min(int(match.group(1)), 6)
    if style_name == "Title":
        return 1
    if style_name == "Subtitle":
        return 2
    return None


def list_info(paragraph: Paragraph) -> Tuple[Optional[str], int]:
    p_pr = paragraph._element.pPr
    if p_pr is None or p_pr.numPr is None:
        return None, 0

    level = 0
    if p_pr.numPr.ilvl is not None:
        level = int(p_pr.numPr.ilvl.val)

    style_name = getattr(paragraph.style, "name", "") or ""
    if "number" in style_name.lower():
        return "ordered", level
    return "unordered", level


def cell_text(cell: _Cell) -> str:
    lines: list[str] = []
    for p in cell.paragraphs:
        text = paragraph_text(p)
        if text:
            lines.append(text)
    return " ".join(lines).strip()


def markdown_table(table: Table) -> str:
    rows = [[cell_text(c) for c in row.cells] for row in table.rows]
    if not rows:
        return ""

    col_count = max((len(r) for r in rows), default=0)
    if col_count == 0:
        return ""

    normalized = [r + [""] * (col_count - len(r)) for r in rows]
    header = normalized[0]
    separator = ["---"] * col_count

    output = [
        f"| {' | '.join(header)} |",
        f"| {' | '.join(separator)} |",
    ]
    for row in normalized[1:]:
        output.append(f"| {' | '.join(row)} |")
    return "\n".join(output)


def iter_block_items(parent: Union[DocumentType, _Cell]) -> Iterable[BlockItem]:
    if isinstance(parent, DocumentType):
        parent_element = parent.element.body
    else:
        parent_element = parent._tc

    for child in parent_element.iterchildren():
        if child.tag.endswith("}p"):
            yield Paragraph(child, parent)
        elif child.tag.endswith("}tbl"):
            yield Table(child, parent)


def convert_docx_to_markdown(input_path: Path, include_metadata: bool = False) -> str:
    document = docx.Document(str(input_path))
    out: list[str] = []

    if include_metadata:
        props = document.core_properties
        metadata_rows = []
        if props.title:
            metadata_rows.append(f"- Title: {escape_markdown(str(props.title))}")
        if props.author:
            metadata_rows.append(f"- Author: {escape_markdown(str(props.author))}")
        if props.subject:
            metadata_rows.append(f"- Subject: {escape_markdown(str(props.subject))}")
        if props.created:
            metadata_rows.append(f"- Created: {props.created.isoformat()}")
        if props.modified:
            metadata_rows.append(f"- Modified: {props.modified.isoformat()}")

        if metadata_rows:
            out.append("# Document Metadata")
            out.extend(metadata_rows)
            out.append("")

    for block in iter_block_items(document):
        if isinstance(block, Paragraph):
            text = paragraph_text(block)
            if not text:
                continue

            level = heading_level(block)
            list_type, list_level = list_info(block)

            if level:
                out.append(f"{'#' * level} {text}")
                out.append("")
                continue

            if list_type:
                indent = "  " * list_level
                marker = "1." if list_type == "ordered" else "-"
                out.append(f"{indent}{marker} {text}")
                continue

            out.append(text)
            out.append("")
        else:
            table_md = markdown_table(block)
            if table_md:
                out.append(table_md)
                out.append("")

    while out and out[-1] == "":
        out.pop()
    return "\n".join(out) + ("\n" if out else "")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert DOCX/DOCM to Markdown.")
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Path to input .docx or .docm file",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Path to output .md file (default: same name as input with .md extension)",
    )
    parser.add_argument(
        "--with-metadata",
        action="store_true",
        help="Include core document metadata in markdown output",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).expanduser().resolve()
    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        return 2
    if input_path.suffix.lower() not in {".docx", ".docm"}:
        print("Input must be a .docx or .docm file.", file=sys.stderr)
        return 2

    output_path = (
        Path(args.output).expanduser().resolve()
        if args.output
        else input_path.with_suffix(".md")
    )

    try:
        markdown = convert_docx_to_markdown(input_path, include_metadata=args.with_metadata)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
    except Exception as exc:
        print(f"Conversion failed: {exc}", file=sys.stderr)
        return 1

    print(f"OK: {input_path} -> {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
