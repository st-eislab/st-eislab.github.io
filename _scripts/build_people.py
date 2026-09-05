#!/usr/bin/env python3
from pathlib import Path
import html
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_data" / "people.yml"
STYLES = ROOT / "_data" / "topic_styles.yml"
OUT = ROOT / "people" / "_generated.md"

CATEGORY_LABELS = {"phd": "PhD Student", "masters": "Master's Student", "msc": "Master's Student"}
GROUPS = [
    ("phd", "PhD Students"),
    ("masters", "Master's Students"),
]


def esc(v):
    return html.escape(str(v), quote=True) if v not in (None, "") else ""


def month_label(value):
    if not value:
        return ""
    s = str(value)
    months = {"01":"Jan", "02":"Feb", "03":"Mar", "04":"Apr", "05":"May", "06":"Jun",
              "07":"Jul", "08":"Aug", "09":"Sep", "10":"Oct", "11":"Nov", "12":"Dec"}
    if len(s) >= 7 and s[4] == "-":
        return f"{months.get(s[5:7], s[5:7])} {s[:4]}"
    return s


def link_icon(url, icon, label):
    if not url:
        return ""
    href = str(url)
    if label == "Email" and not href.startswith("mailto:"):
        href = "mailto:" + href
    return f'<a href="{esc(href)}" aria-label="{label}" title="{label}"><i class="bi {icon}"></i></a>'


def badge(topic, styles):
    group = styles.get(topic, "neutral")
    return f'<span class="topic-badge topic-{esc(group)}">{esc(topic)}</span>'


def card(p, styles, alumni=False):
    name = esc(p.get("name"))
    raw_photo = str(p.get("photo") or "assets/img/placeholder_member.svg")
    if raw_photo.startswith("assets/"):
        raw_photo = "../" + raw_photo
    photo = esc(raw_photo)
    pos = p.get("photo_position")
    style = f' style="object-position:{esc(pos)};"' if pos else ""
    category = CATEGORY_LABELS.get(str(p.get("category", "")).lower(), esc(p.get("category", "Student")))
    since = month_label(p.get("since"))
    graduated = month_label(p.get("graduated"))
    institution = esc(p.get("institution"))

    if alumni:
        years = f"{since} – {graduated}" if since and graduated else graduated or since
        role = f"{category} · {years}" if years else category
    else:
        role = f"{category} · since {since}" if since else category
    if institution and institution.lower() != "seoultech":
        role += f" · {institution}"

    topics = p.get("topics") or []
    badges = "".join(badge(t, styles) for t in topics)
    details = []
    if alumni and p.get("thesis"):
        details.append(f'<div class="member-detail"><strong>Thesis:</strong> {esc(p["thesis"])}</div>')
    if alumni and p.get("current_position"):
        details.append(f'<div class="member-detail"><strong>Current:</strong> {esc(p["current_position"])}</div>')

    links = "".join([
        link_icon(p.get("email"), "bi-envelope-fill", "Email"),
        link_icon(p.get("github"), "bi-github", "GitHub"),
        link_icon(p.get("linkedin"), "bi-linkedin", "LinkedIn"),
        link_icon(p.get("website"), "bi-globe", "Website"),
    ])

    return f'''::: {{.member-card}}
![]({photo}){{.member-photo{style} fig-alt="Portrait of {name}"}}
<div class="member-name">{name}</div>
<div class="member-role">{role}</div>
<div class="member-topics">{badges}</div>
{''.join(details)}
<div class="member-links">{links}</div>
:::
'''


def grid(cards):
    return "::: {.member-grid}\n" + "\n".join(cards) + "\n:::\n"


def main():
    people = yaml.safe_load(DATA.read_text(encoding="utf-8")) or {}
    styles = yaml.safe_load(STYLES.read_text(encoding="utf-8")) or {}
    students = people.get("students") or []
    current = [p for p in students if not p.get("graduated")]
    alumni = [p for p in students if p.get("graduated")]

    parts = ["<!-- AUTO-GENERATED: edit _data/people.yml, not this file. -->\n"]
    for category, heading in GROUPS:
        subset = [p for p in current if str(p.get("category", "")).lower() in ({category} if category != "masters" else {"masters","msc"})]
        if subset:
            parts += [f"\n## {heading}\n", grid([card(p, styles) for p in subset])]

    external = [p for p in (people.get("external") or []) if not p.get("graduated")]
    if external:
        parts += ["\n## External & Co-advised Students\n", grid([card(p, styles) for p in external])]

    if alumni:
        alumni_sorted = sorted(alumni, key=lambda p: str(p.get("graduated", "")), reverse=True)
        parts += ["\n## Alumni\n", grid([card(p, styles, alumni=True) for p in alumni_sorted])]

    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"[build_people] Wrote {len(current)} current students and {len(alumni)} alumni")

if __name__ == "__main__":
    main()
