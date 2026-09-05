#!/usr/bin/env python3
from pathlib import Path
import html
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_data" / "manuscripts.yml"
OUT = ROOT / "publications" / "_manuscripts.md"


def esc(v):
    return html.escape(str(v), quote=True) if v not in (None, "") else ""


def links(item):
    out = []
    for key, label in (("preprint","Preprint"),("code","Code")):
        if item.get(key): out.append(f'<a href="{esc(item[key])}" target="_blank">{label}</a>')
    return f'<span class="pub-links">{"".join(out)}</span>' if out else ""


def submitted_card(x):
    venue = esc(x.get("venue"))
    meta = []
    if venue: meta.append(f"Submitted to <em>{venue}</em>")
    if x.get("submitted_date"): meta.append(esc(x.get("submitted_date")))
    if x.get("quartile"): meta.append(f'<span class="venue-badge">{esc(x.get("quartile"))}</span>')
    return f'''<div class="pub-item manuscript-item">
<div class="pub-body">
<span class="pub-title">{esc(x.get('title'))}.</span>
<span class="pub-meta">{' · '.join(meta)}</span>{links(x)}
</div>
</div>'''


def working_card(x):
    return f'''<div class="pub-item manuscript-item">
<div class="pub-body"><span class="pub-title">{esc(x.get('title'))}.</span></div>
</div>'''


def main():
    data = yaml.safe_load(DATA.read_text(encoding="utf-8")) or {}
    submitted = data.get("submitted") or []
    working = data.get("working") or []
    parts = ["<!-- AUTO-GENERATED: edit _data/manuscripts.yml, not this file. -->\n"]
    if working:
        parts += ["\n## Working Papers {.pub-section-title}\n"] + [working_card(x) for x in working]
    if submitted:
        parts += ["\n## Submitted / Under Review {.pub-section-title}\n"] + [submitted_card(x) for x in submitted]
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"[build_manuscripts] Wrote {len(working)} working and {len(submitted)} submitted manuscripts")

if __name__ == "__main__":
    main()
