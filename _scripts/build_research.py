#!/usr/bin/env python3
from pathlib import Path
import html
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_data" / "research.yml"
PROJECTS = ROOT / "_data" / "projects.yml"
OUT = ROOT / "research" / "_generated.md"
HOME = ROOT / "research" / "_home.md"


def esc(v):
    return html.escape(str(v), quote=True) if v not in (None, "") else ""


def md_text(v):
    return str(v or "").strip()


def buttons(item):
    specs = [("paper","Paper"),("doi","DOI"),("preprint","Preprint"),("code","Code"),("dataset","Dataset"),("project_url","Project")]
    out = []
    for key, label in specs:
        value = item.get(key)
        if not value:
            continue
        href = str(value)
        if key == "doi" and not href.startswith("http"):
            href = "https://doi.org/" + href
        out.append(f'<a class="research-link" href="{esc(href)}">{label}</a>')
    return '<div class="research-links">' + ''.join(out) + '</div>' if out else ""


def topic_card(t):
    image = esc(t.get("image") or "assets/img/placeholder_research.svg")
    alt = esc(t.get("image_alt") or t.get("title"))
    status = str(t.get("status") or "active").lower()
    status_badge = '<span class="research-status research-status-emerging">Emerging</span>' if status == "emerging" else ""
    kws = t.get("keywords") or []
    tags = ''.join(f'<span class="research-tag">{esc(k)}</span>' for k in kws)
    return f''':::: {{.research-card}}
![]({image}){{.research-fig fig-alt="{alt}"}}

::: {{.research-body}}
### {md_text(t.get('title'))} {status_badge}

{md_text(t.get('description') or t.get('summary'))}

<div class="research-tags">{tags}</div>
{buttons(t)}
:::
::::
'''


def main():
    data = yaml.safe_load(DATA.read_text(encoding="utf-8")) or {}
    directions = data.get("directions") or []
    topics = data.get("topics") or []
    parts = ["<!-- AUTO-GENERATED: edit _data/research.yml, not this file. -->\n"]
    for d in directions:
        did = d.get("id")
        parts += [f"\n## {md_text(d.get('title'))} {{#{esc(did)}}}\n", md_text(d.get("intro")) + "\n"]
        for t in topics:
            if t.get("public", True) is False:
                continue
            if t.get("direction") == did:
                parts.append(topic_card(t))

    emerging = data.get("emerging") or []
    if emerging:
        parts += ["\n## Emerging Research\n", "Exploratory directions that are developing into larger research lines.\n"]
        for t in emerging:
            if t.get("public", True) is not False:
                parts.append(topic_card(t))

    proj = yaml.safe_load(PROJECTS.read_text(encoding="utf-8")) or {}
    projects = proj.get("projects") or []
    if projects:
        parts += ["\n## Funded Projects\n"]
        for p in projects:
            meta = []
            for label, key in [("Funder","funder"),("Program","program"),("Role","role"),("Duration","duration"),("Amount","amount")]:
                if p.get(key): meta.append(f"**{label}:** {md_text(p[key])}")
            if not p.get("duration") and (p.get("start") or p.get("end")):
                meta.append(f"**Duration:** {md_text(p.get('start'))} – {md_text(p.get('end'))}")
            url = p.get("url")
            link = f' [Project page]({url})' if url else ''
            parts += [f"### {md_text(p.get('title'))}\n", "  \n".join(meta) + link + "\n"]

    OUT.write_text("\n".join(parts), encoding="utf-8")

    # Emit the homepage cards as an explicit raw-HTML block.
    # Without the {=html} fence, Pandoc can repair the final closing <a> tag
    # into an extra empty anchor, which appears as a phantom fourth card.
    home_parts = [
        "<!-- AUTO-GENERATED homepage research directions -->",
        "```{=html}",
        '<div class="pillar-grid">',
    ]
    for d in directions:
        if not d.get("homepage"):
            continue
        cls = {"accent":" pillar-accent", "neutral":" pillar-neutral", "process":" pillar-process", "graph":" pillar-graph"}.get(str(d.get("style")), "")
        home_parts.append(
            f'<a class="pillar-card{cls}" href="research.html#{esc(d.get("id"))}">'
            f'<div class="pillar-icon"><i class="bi {esc(d.get("icon") or "bi-lightbulb")}"></i></div>'
            f'<h3>{esc(d.get("title"))}</h3>'
            f'<p>{esc(d.get("summary"))}</p>'
            '</a>'
        )
    home_parts.extend(["</div>", "```"] )
    HOME.write_text("\n".join(home_parts) + "\n", encoding="utf-8")
    print(f"[build_research] Wrote {len(topics)} research topics and {len(emerging)} emerging topics")

if __name__ == "__main__":
    main()
