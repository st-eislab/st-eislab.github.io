#!/usr/bin/env python3
"""Generate published-publication sections from publications/references.bib.

No external BibTeX package is required; this parser is intentionally small but
handles nested braces/quoted values used in this site's bibliography.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIB_FILE = ROOT / "publications" / "references.bib"
OUT_FILE = ROOT / "publications" / "_generated.md"
HIGHLIGHT_NAME = "Obregon"
SECTION_ORDER = [
    "Journal Articles",
    "Book Chapters",
    "International Conference Papers",
    "Domestic Conference Papers",
    "Domestic Journal Articles",
    "Other Publications",
]


def clean(text: str) -> str:
    if not text:
        return ""
    text = text.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", text).strip()


def split_top_level(text, delimiter=","):
    parts, buf = [], []
    depth = 0
    quote = False
    escape = False
    for ch in text:
        if escape:
            buf.append(ch); escape = False; continue
        if ch == "\\":
            buf.append(ch); escape = True; continue
        if ch == '"' and depth == 0:
            quote = not quote; buf.append(ch); continue
        if not quote:
            if ch == "{": depth += 1
            elif ch == "}" and depth > 0: depth -= 1
            elif ch == delimiter and depth == 0:
                parts.append("".join(buf).strip()); buf=[]; continue
        buf.append(ch)
    if buf:
        parts.append("".join(buf).strip())
    return parts


def strip_value(v):
    v = v.strip().rstrip(",").strip()
    if len(v) >= 2 and ((v[0] == "{" and v[-1] == "}") or (v[0] == '"' and v[-1] == '"')):
        v = v[1:-1]
    return v.strip()


def parse_bib(text):
    entries = []
    i = 0
    n = len(text)
    while i < n:
        at = text.find("@", i)
        if at < 0: break
        m = re.match(r"@([A-Za-z_]+)\s*([\{(])", text[at:])
        if not m:
            i = at + 1; continue
        etype = m.group(1).lower()
        if etype in {"string", "comment", "preamble"}:
            i = at + len(m.group(0)); continue
        open_ch = m.group(2); close_ch = "}" if open_ch == "{" else ")"
        body_start = at + m.end()
        depth = 1; quote = False; escape = False; j = body_start
        while j < n and depth:
            ch = text[j]
            if escape: escape = False
            elif ch == "\\": escape = True
            elif ch == '"': quote = not quote
            elif not quote:
                if ch == open_ch: depth += 1
                elif ch == close_ch: depth -= 1
            j += 1
        if depth != 0:
            break
        body = text[body_start:j-1].strip()
        chunks = split_top_level(body)
        if not chunks:
            i = j; continue
        entry = {"ENTRYTYPE": "incollection" if etype == "book_section" else ("phdthesis" if etype == "thesis" else etype), "ID": chunks[0].strip()}
        for chunk in chunks[1:]:
            if "=" not in chunk: continue
            key, val = chunk.split("=", 1)
            entry[key.strip().lower()] = strip_value(val)
        entries.append(entry)
        i = j
    return entries


def format_authors(raw: str) -> str:
    authors = [clean(a) for a in re.split(r"\s+and\s+", raw or "")]
    out = []
    for a in authors:
        if "," in a:
            last, first = [p.strip() for p in a.split(",", 1)]
            a = f"{first} {last}"
        if HIGHLIGHT_NAME.lower() in a.lower():
            a = f'<span class="pub-me">{a}</span>'
        out.append(a)
    return ", ".join(out)


def get_venue(entry: dict) -> str:
    for key in ("journal", "booktitle", "publisher", "school", "institution"):
        if entry.get(key): return clean(entry[key])
    return ""


def section_for(entry: dict) -> str:
    etype = entry.get("ENTRYTYPE", "").lower()
    domestic = clean(entry.get("scope", "")).lower() in {"domestic", "local", "korea", "korean"}
    if etype == "article": return "Domestic Journal Articles" if domestic else "Journal Articles"
    if etype in {"inproceedings", "conference"}: return "Domestic Conference Papers" if domestic else "International Conference Papers"
    if etype in {"incollection", "book_section", "inbook"}: return "Book Chapters"
    if etype in {"phdthesis", "mastersthesis", "thesis"}: return ""
    return "Other Publications"


def make_card(entry: dict) -> str:
    title = clean(entry.get("title", "Untitled")); year = clean(entry.get("year", ""))
    authors = format_authors(entry.get("author", "")); venue = get_venue(entry)
    extras = []
    if clean(entry.get("volume", "")): extras.append(f"vol. {clean(entry['volume'])}")
    if clean(entry.get("pages", "")): extras.append(f"pp. {clean(entry['pages'])}")
    venue_line = venue + (f", {', '.join(extras)}" if extras else "")
    links = []
    doi = clean(entry.get("doi", ""))
    if doi: links.append(f'<a href="https://doi.org/{doi}" target="_blank">DOI</a>')
    for key, label in (("pdf", "PDF"), ("code", "Code")):
        value = clean(entry.get(key, ""))
        if value: links.append(f'<a href="{value}" target="_blank">{label}</a>')
    url = clean(entry.get("url", ""))
    if url and not doi: links.append(f'<a href="{url}" target="_blank">Link</a>')
    links_html = f' <span class="pub-links">{"".join(links)}</span>' if links else ""
    return f'''<div class="pub-item">\n<span class="pub-year">{year}</span>\n<div class="pub-body">\n<span class="pub-title">{title}.</span>\n<span class="pub-meta">{authors}. <em>{venue_line}</em>.</span>{links_html}\n</div>\n</div>'''


def main():
    entries = parse_bib(BIB_FILE.read_text(encoding="utf-8"))
    groups = {name: [] for name in SECTION_ORDER}
    for entry in entries:
        section = section_for(entry)
        if section:
            groups[section].append(entry)
    def year_key(e):
        try: return int(clean(e.get("year", "0")))
        except ValueError: return 0
    parts = ["<!-- AUTO-GENERATED: edit publications/references.bib, not this file. -->\n"]
    total = 0
    for title in SECTION_ORDER:
        es = sorted(groups[title], key=year_key, reverse=True)
        if not es: continue
        parts.append(f"\n## {title} {{.pub-section-title}}\n")
        parts.extend(make_card(e) for e in es); total += len(es)
    OUT_FILE.write_text("\n".join(parts), encoding="utf-8")
    print(f"[build_publications] Wrote {total} publications")

if __name__ == "__main__": main()
