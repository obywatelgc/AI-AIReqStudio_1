#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
tools/search_kb.py

Minimalne, czytelne wyszukiwanie full-text po chunkach JSON:
- domyślny katalog KB: kb/chunks/EBP
- przeszukuje: text + section_title + heading_path[].title
- proste punktowanie (score) oparte o wystąpienia tokenów
- wynik jako tekst (domyślnie) lub JSON
- opcjonalny filtr po ścieżce pliku źródłowego: --file-contains

Przykłady:
  python tools/search_kb.py "logowanie hasło maskowane SMS" --top 10
  python tools/search_kb.py "miniaplikacja rachunki historia operacji" --file-contains miniapps/ --top 15
  python tools/search_kb.py "filtrowanie IP logowanie" --format json --top 20 > spec/_evidence/WM-01.search.json
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple


WORD_RE = re.compile(r"[A-Za-zĄĆĘŁŃÓŚŻŹąćęłńóśżź0-9]+")


def tokenize(text: str) -> List[str]:
    """
    Prosta tokenizacja: wyciąga słowa/numery, lower-case.
    """
    return [m.group(0).lower() for m in WORD_RE.finditer(text or "")]


def build_snippet(text: str, tokens: List[str], max_len: int = 240) -> str:
    """
    Buduje snippet w okolicach pierwszego trafienia tokenu.
    Jeśli brak trafienia, zwraca początek tekstu.
    """
    if not text:
        return ""
    lower = text.lower()
    first_pos = None
    first_tok = None
    for t in tokens:
        pos = lower.find(t)
        if pos != -1 and (first_pos is None or pos < first_pos):
            first_pos = pos
            first_tok = t

    if first_pos is None:
        s = text.strip().replace("\n", " ")
        return (s[:max_len] + "…") if len(s) > max_len else s

    start = max(0, first_pos - max_len // 3)
    end = min(len(text), start + max_len)
    snippet = text[start:end].strip().replace("\n", " ")

    # jeśli ucięliśmy z obu stron, dodaj elipsy
    if start > 0:
        snippet = "…" + snippet
    if end < len(text):
        snippet = snippet + "…"

    return snippet


def safe_get_heading_path_titles(obj: Dict) -> List[str]:
    hp = obj.get("heading_path") or []
    titles = []
    if isinstance(hp, list):
        for it in hp:
            if isinstance(it, dict) and isinstance(it.get("title"), str):
                titles.append(it["title"])
    return titles


def should_keep_by_file_filter(
    obj: Dict,
    file_contains: Optional[str],
    case_sensitive: bool = False,
) -> bool:
    """
    Jeśli podano file_contains, ograniczamy wyniki do chunków, których:
    - primary_source_file zawiera ten substring, lub
    - którykolwiek provenance[].source_file zawiera ten substring
    """
    if not file_contains:
        return True

    def norm_path(text: str) -> str:
        val = text.replace("\\", "/")
        return val if case_sensitive else val.lower()

    fc = norm_path(file_contains)

    primary = (obj.get("primary_source_file") or "")
    if isinstance(primary, str) and fc in norm_path(primary):
        return True

    prov = obj.get("provenance") or []
    if isinstance(prov, list):
        for p in prov:
            if isinstance(p, dict):
                sf = p.get("source_file") or ""
                if isinstance(sf, str) and fc in norm_path(sf):
                    return True

    return False


def compute_score(
    query_tokens: List[str],
    text: str,
    section_title: str,
    heading_titles: List[str],
) -> int:
    """
    Proste punktowanie:
    - za każdy token:
      - +3 jeśli występuje w section_title
      - +2 jeśli występuje w którymkolwiek heading_path title
      - +1 za każdą obecność w text
      - + (freq-1) za dodatkowe wystąpienia w text (czyli łącznie freq punktów za text)
    """
    if not query_tokens:
        return 0

    text_l = (text or "").lower()
    sec_l = (section_title or "").lower()
    headings_l = " ".join(heading_titles or []).lower()

    score = 0
    for t in query_tokens:
        if not t:
            continue

        # bonusy za tytuły
        if t in sec_l:
            score += 3
        if t in headings_l:
            score += 2

        # punkty za treść (liczba wystąpień)
        freq = text_l.count(t)
        if freq > 0:
            score += freq  # 1 za pierwsze +1 za kolejne, prosto

    return score


@dataclass
class SearchHit:
    chunk_id: str
    score: int
    section_title: str
    heading_path: List[str]
    primary_source_file: str
    provenance: List[Dict]
    snippet: str


def load_chunk_json(path: Path) -> Tuple[Optional[Dict], Optional[str]]:
    try:
        obj = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except Exception as e:
        return None, str(e)

    if not isinstance(obj, dict):
        return None, "top-level JSON is not an object"

    return obj, None


def iter_chunk_files(kb_dir: Path) -> List[Path]:
    files = [p for p in kb_dir.glob("DOC-*.json") if p.is_file()]
    files.sort()
    return files


def search_kb(
    kb_dir: Path,
    query: str,
    top_n: int,
    file_contains: Optional[str],
    case_sensitive: bool,
    min_score: int,
) -> List[SearchHit]:
    query_tokens = tokenize(query)
    if not query_tokens:
        return []

    hits: List[SearchHit] = []

    for fp in iter_chunk_files(kb_dir):
        obj, load_error = load_chunk_json(fp)
        if load_error:
            print(f"WARN: skipping invalid chunk JSON {fp}: {load_error}", file=sys.stderr)
            continue

        if not should_keep_by_file_filter(obj, file_contains, case_sensitive=case_sensitive):
            continue

        chunk_id = obj.get("chunk_id") or fp.stem
        text = obj.get("text") or ""
        section_title = obj.get("section_title") or ""
        heading_titles = safe_get_heading_path_titles(obj)
        primary = obj.get("primary_source_file") or ""
        prov = obj.get("provenance") or []

        score = compute_score(query_tokens, text, section_title, heading_titles)
        if score < min_score:
            continue

        snippet = build_snippet(text, query_tokens)

        hits.append(SearchHit(
            chunk_id=str(chunk_id),
            score=score,
            section_title=str(section_title),
            heading_path=heading_titles,
            primary_source_file=str(primary),
            provenance=prov if isinstance(prov, list) else [],
            snippet=snippet
        ))

    # sort: score desc, chunk_id asc (stabilnie)
    hits.sort(key=lambda h: (-h.score, h.chunk_id))
    return hits[:top_n]


def print_hits_text(hits: List[SearchHit]) -> None:
    if not hits:
        print("No results.")
        return

    for idx, h in enumerate(hits, start=1):
        hp = " > ".join(h.heading_path) if h.heading_path else "(no heading_path)"
        print(f"{idx}) {h.chunk_id}  score={h.score}")
        print(f"   section: {h.section_title}")
        print(f"   path:    {hp}")
        print(f"   source:  {h.primary_source_file}")
        if h.provenance:
            # pokaż max 2 wpisy provenance, żeby nie zaśmiecać
            prov_show = h.provenance[:2]
            prov_txt = "; ".join([f"{p.get('source_file')}:{p.get('line_start')}-{p.get('line_end')}" for p in prov_show])
            more = " (+more)" if len(h.provenance) > 2 else ""
            print(f"   prov:    {prov_txt}{more}")
        print(f"   snippet: {h.snippet}")
        print("")


def main() -> int:
    ap = argparse.ArgumentParser(description="Simple full-text search over kb/chunks JSON files.")
    ap.add_argument("query", help="Search query (string). Use quotes if it contains spaces.")
    ap.add_argument("--kb-dir", default="kb/chunks/EBP", help="KB chunks directory.")
    ap.add_argument("--top", type=int, default=10, help="Number of top results to return.")
    ap.add_argument("--min-score", type=int, default=1, help="Minimum score threshold.")
    ap.add_argument("--file-contains", default=None, help="Filter: only chunks whose source file path contains this substring.")
    ap.add_argument("--case-sensitive", action="store_true", help="Use case-sensitive matching for --file-contains.")
    ap.add_argument("--format", choices=["text", "json"], default="text", help="Output format.")
    args = ap.parse_args()

    kb_dir = Path(args.kb_dir)
    if not kb_dir.exists():
        print(f"ERROR: kb dir not found: {kb_dir}")
        return 2

    hits = search_kb(
        kb_dir=kb_dir,
        query=args.query,
        top_n=max(1, args.top),
        file_contains=args.file_contains,
        case_sensitive=args.case_sensitive,
        min_score=max(0, args.min_score),
    )

    if args.format == "json":
        out = {
            "query": args.query,
            "kb_dir": str(kb_dir).replace("\\", "/"),
            "top": args.top,
            "min_score": args.min_score,
            "file_contains": args.file_contains,
            "case_sensitive": args.case_sensitive,
            "results": [asdict(h) for h in hits],
        }
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print_hits_text(hits)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
