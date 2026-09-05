# EIS Lab Website — Maintenance Guide

This file is intended to live in the website repository as:

```text
_docs/MAINTENANCE.md
```

The site is deliberately **data-driven**. For normal updates, edit YAML, BibTeX, QMD, and image files. You should almost never need to edit generated Markdown, HTML, or CSS.

---

## 1. Quick reference

| Task | File / folder to edit |
|---|---|
| Add a current student | `_data/people.yml` |
| Graduate a student / move to Alumni | `_data/people.yml` |
| Change student research-topic badges | `_data/people.yml` |
| Control badge color family | `_data/topic_styles.yml` |
| Add / edit a research direction | `_data/research.yml` |
| Add / edit a research topic | `_data/research.yml` |
| Hide / reveal a research topic | `_data/research.yml` |
| Change the three homepage research highlights | `_data/research.yml` |
| Add a working paper | `_data/manuscripts.yml` |
| Add a submitted / under-review manuscript | `_data/manuscripts.yml` |
| Add a published journal article | `publications/references.bib` |
| Add a published conference paper | `publications/references.bib` |
| Add a book chapter | `publications/references.bib` |
| Add a news item | `news/YYYY-MM-DD-short-slug.qmd` |
| Add a representative news image | `assets/img/news/` |
| Add photos to an existing gallery album | the relevant `gallery/<album>/` folder + its `index.qmd` |
| Create a new gallery album | create `gallery/<new-album>/index.qmd` + add a card in `gallery/index.qmd` |
| Add a funded project later | `_data/projects.yml` |
| Edit PI block / PI links | `people/index.qmd` |
| Edit homepage headline / text / hero image | `index.qmd` |
| Edit Teaching page | `teaching.qmd` |

---

## 2. Files you should **not** edit manually

These are generated automatically and can be overwritten whenever the site renders:

```text
people/_generated.md
research/_generated.md
research/_home.md
publications/_generated.md
publications/_manuscripts.md
_site/
```

If something in one of those pages needs to change, edit its source YAML/BibTeX file instead.

---

# People

## 3. Add a new current student

Edit:

```text
_data/people.yml
```

Add a record under `students:`. For example:

```yaml
- name: New Student
  category: masters
  institution: SeoulTech
  since: "2026-09"
  graduated:
  photo: assets/img/people/new_student.jpg
  photo_position:
  topics:
    - XAI for GNNs
    - Smart Manufacturing
  thesis:
  current_position:
  email:
  github:
  linkedin:
  website:
```

### Required / useful fields

- `name`: displayed name.
- `category`: normally `phd` or `masters`.
- `institution`: normally `SeoulTech`.
- `since`: recommended format `YYYY-MM`.
- `graduated`: **leave empty for a current student**.
- `photo`: path to the portrait.
- `topics`: list of research-topic badges.

All link fields are optional. Empty optional fields are not shown.

### Add the portrait

Put the image in:

```text
assets/img/people/
```

Example:

```text
assets/img/people/new_student.jpg
```

Then use that exact path in `photo:`.

If the portrait framing is poor, use `photo_position`, for example:

```yaml
photo_position: "center 30%"
```

---

## 4. Graduate a student / move them to Alumni

Do **not** move the record manually.

In `_data/people.yml`, simply fill the `graduated` field:

```yaml
graduated: "2026-08"
```

The site automatically moves that student from Current Members to Alumni.

You can optionally add:

```yaml
thesis: "Title of the master's thesis"
current_position: "Research Engineer at Company X"
```

If either field is empty, it is not rendered.

### Example

Before graduation:

```yaml
graduated:
thesis:
current_position:
```

After graduation:

```yaml
graduated: "2026-08"
thesis: "Explainable AI for ..."
current_position:
```

That is enough to move the student automatically.

---

## 5. Add or change research-topic badges for a person

In `_data/people.yml`:

```yaml
topics:
  - Process Mining
  - Industrial IoT
  - Smart Manufacturing
```

Reuse the **same spelling** for the same topic. This ensures that the same badge receives the same visual style everywhere.

The central topic-to-style mapping is in:

```text
_data/topic_styles.yml
```

Example:

```yaml
XAI: xai
Smart Manufacturing: manufacturing
Battery SOH: energy
Process Mining: process
XAI for GNNs: graph
Multimodal AI: method
Ontologies: neutral
```

Available style families currently include:

```text
xai
manufacturing
energy
process
graph
method
neutral
```

When adding a new topic label, add it to `_data/topic_styles.yml` only if you want explicit control over its visual family. Otherwise it falls back to the neutral style.

---

## 6. Add an external / co-advised student

Edit `_data/people.yml` under:

```yaml
external:
```

Use the same fields as a regular student. For example:

```yaml
external:
  - name: External Student
    category: phd
    institution: Another University
    since: "2026-03"
    graduated:
    photo: assets/img/people/external_student.jpg
    topics:
      - Ontologies
    thesis:
    current_position:
    email:
    github:
    linkedin:
    website:
```

---

# Research

## 7. Add a new research topic

Edit:

```text
_data/research.yml
```

Add a record under `topics:`.

Example:

```yaml
- id: xai-for-gnns
  title: Explainable AI for Graph Neural Networks
  direction: graph-learning-explainability
  status: emerging
  public: true

  summary: Short one-sentence description.

  description: >
    Longer description shown on the Research page. Explain the research
    problem, the methodological idea, and why it matters.

  image: assets/img/research/xai-gnn.png
  image_alt: Explainable graph neural networks

  keywords:
    - XAI for GNNs
    - graph explainability
    - graph neural networks

  paper:
  doi:
  preprint:
  code:
  dataset:
  project_url:
```

### Important fields

- `id`: unique lowercase identifier; use hyphens, no spaces.
- `title`: title shown publicly.
- `direction`: must match the `id` of one research direction.
- `status`: normally `active` or `emerging`.
- `public`: `true` or `false`.
- `summary`: short description.
- `description`: longer Research-page description.
- `image`: conceptual/research image path.
- `keywords`: small tags shown on the research card.

Optional links only appear when populated.

Examples:

```yaml
doi: "10.1016/j.example.2026.123456"
preprint: "https://arxiv.org/abs/..."
code: "https://github.com/..."
dataset: "https://..."
```

For `doi`, either a bare DOI or full URL works.

---

## 8. Hide a research topic without deleting it

Set:

```yaml
public: false
```

The topic stays in `_data/research.yml` but is not published.

When you are ready to show it:

```yaml
public: true
```

This is useful for exploratory research or ideas you do not yet want on the public website.

---

## 9. Change a research topic's image

Put the new image in:

```text
assets/img/research/
```

Then change only:

```yaml
image: assets/img/research/new-image.png
```

You can therefore use a conceptual illustration while a paper is unpublished and replace it later with a published figure without touching the page layout.

---

## 10. Change the three research directions shown on the homepage

At the beginning of `_data/research.yml`, each item under `directions:` has:

```yaml
homepage: true
```

or:

```yaml
homepage: false
```

The current homepage design expects **exactly three** directions with:

```yaml
homepage: true
```

Example: to remove Sustainable Energy from the homepage and show Graph Learning instead:

```yaml
- id: sustainable-energy-intelligence
  homepage: false
```

and:

```yaml
- id: graph-learning-explainability
  homepage: true
```

You do **not** edit `research/_home.md`; it is regenerated automatically.

---

## 11. Add a completely new research direction

In `_data/research.yml`, add a record under `directions:`:

```yaml
- id: new-direction
  title: New Research Direction
  homepage: false
  icon: bi-diagram-3
  style: graph
  summary: Short homepage-style description.
  intro: >
    Introductory paragraph shown under this direction on the Research page.
```

Then assign research topics to it using:

```yaml
direction: new-direction
```

If you later want it on the homepage, set `homepage: true` and set another direction to `false` so the total remains three.

---

# Manuscripts and Publications

## 12. Add a working paper

Edit:

```text
_data/manuscripts.yml
```

A working paper only needs a title:

```yaml
working:
  - title: "Tentative title of the paper"
```

Multiple papers:

```yaml
working:
  - title: "Tentative Paper A"
  - title: "Tentative Paper B"
```

Working papers appear under **Working Papers**.

---

## 13. Add a submitted / under-review manuscript

Edit:

```text
_data/manuscripts.yml
```

Example:

```yaml
submitted:
  - title: "Probabilistic Rule Extraction from Tree Ensembles"
    venue: "Expert Systems with Applications"
    submitted_date: "2026-09"
    preprint: "https://arxiv.org/abs/..."
    code:
    quartile: "Q1"
```

Only `title` is essential. The others are optional.

Supported fields currently are:

```yaml
title:
venue:
submitted_date:
preprint:
code:
quartile:
```

The page heading is generated automatically as:

```text
Submitted / Under Review
```

If the list is empty, the section disappears.

---

## 14. When a submitted paper becomes published

Do two things:

1. Remove it from `submitted:` in `_data/manuscripts.yml`.
2. Add the final bibliographic record to `publications/references.bib`.

Optionally, also create a News item announcing the acceptance/publication.

---

## 15. Add a published journal article

Edit:

```text
publications/references.bib
```

Example:

```bibtex
@article{Obregon2027Example,
  author  = {Josue Obregon and Coauthor Name},
  title   = {Title of the Article},
  journal = {Journal Name},
  year    = {2027},
  volume  = {10},
  pages   = {1--15},
  doi     = {10.xxxx/xxxxx},
  pdf     = {https://...},
  code    = {https://github.com/...}
}
```

The publication generator places `@article` entries under **Journal Articles** automatically.

Supported optional links include:

```bibtex
doi  = {...}
pdf  = {...}
code = {...}
url  = {...}
```

If a DOI exists, the site creates the DOI link automatically.

---

## 16. Add an international conference paper

Use `@inproceedings`:

```bibtex
@inproceedings{Obregon2027Conference,
  author    = {Josue Obregon and Coauthor Name},
  title     = {Title of the Conference Paper},
  booktitle = {Proceedings of the Conference Name},
  year      = {2027},
  pages     = {100--108},
  doi       = {10.xxxx/xxxxx}
}
```

It automatically appears under:

```text
International Conference Papers
```

---

## 17. Add a domestic conference paper

Use the normal `@inproceedings` record and add:

```bibtex
scope = {domestic},
```

Example:

```bibtex
@inproceedings{Obregon2027Domestic,
  author    = {Josue Obregon and Coauthor Name},
  title     = {Paper Title},
  booktitle = {Conference Name},
  year      = {2027},
  scope     = {domestic}
}
```

It automatically appears under **Domestic Conference Papers**.

---

## 18. Add a domestic journal article

Use `@article` and add:

```bibtex
scope = {domestic},
```

It automatically appears under **Domestic Journal Articles**.

---

## 19. Add a book chapter

Use standard BibTeX `@incollection`:

```bibtex
@incollection{Obregon2027Chapter,
  author    = {Josue Obregon and Coauthor Name},
  title     = {Chapter Title},
  booktitle = {Book Title},
  publisher = {Publisher},
  year      = {2027},
  pages     = {1--20},
  doi       = {10.xxxx/xxxxx}
}
```

It automatically appears under **Book Chapters**.

---

# News

## 20. Add a news item

Create a new file directly inside:

```text
news/
```

Use this naming convention:

```text
YYYY-MM-DD-short-slug.qmd
```

Example:

```text
news/2026-08-28-two-msc-graduates.qmd
```

Template:

```yaml
---
title: "Two EIS Lab students complete their master's degrees"
date: 2026-08-28
categories: [graduation]
description: "Hayat Hassanpour and Jostin Jerico Rosal completed their master's degrees at SeoulTech."
image: ../assets/img/news/graduation-2026.jpg
---

Hayat Hassanpour and Jostin Jerico Rosal successfully completed their master's studies ...
```

The `image:` line is optional.

Put news images in:

```text
assets/img/news/
```

The News page automatically discovers files whose names begin with `20...` and sorts them by date. The homepage also automatically shows the newest items.

Useful categories include:

```text
new members
graduation
conference
publication
award
lab life
grant
software
```

### Good things to use News for

- student joins the lab;
- thesis defense / graduation;
- paper accepted or published;
- conference participation or presentation;
- award;
- grant / funded project;
- software or dataset release;
- Open Lab Day or another meaningful lab event.

A routine manuscript submission normally does **not** need to be a news item.

---

## 21. A conference can appear in three different places

These three things are different and can all be used for the same conference:

### A. Published conference paper

Add the paper to:

```text
publications/references.bib
```

### B. Lab news about attending / presenting

Create:

```text
news/YYYY-MM-DD-conference-name.qmd
```

### C. Conference photos

Add them to:

```text
gallery/conferences/
```

This is intentional: Publications = scholarly output, News = chronological lab activity, Gallery = photographs.

---

# Gallery

## 22. Add photos to an existing gallery album

Current albums include:

```text
gallery/conferences/
gallery/graduations/
gallery/lab-life/
```

Put the image files directly inside the appropriate album folder.

Example:

```text
gallery/conferences/conference-01.jpg
gallery/conferences/conference-02.jpg
gallery/conferences/conference-03.jpg
```

Then edit:

```text
gallery/conferences/index.qmd
```

Remove:

```markdown
*Photos coming soon.*
```

and add:

```markdown
::: {.photo-grid}
![Presenting our research](conference-01.jpg){group="conferences"}
![EIS Lab students at the conference](conference-02.jpg){group="conferences"}
![Conference venue](conference-03.jpg){group="conferences"}
:::
```

If you do not want a caption:

```markdown
![](conference-03.jpg){group="conferences"}
```

Use the same `group="..."` value for all photos in one album so they open together in the lightbox/slideshow.

### Important gallery convention

For the current site, **gallery album photographs live inside their album folder**. For example:

```text
gallery/conferences/photo.jpg
gallery/graduations/photo.jpg
gallery/lab-life/photo.jpg
```

Do not duplicate those photographs under `assets/img/gallery/` unless the site is deliberately redesigned later.

---

## 23. Add a completely new gallery album

Suppose you want a separate Open Lab Day album.

Create:

```text
gallery/open-lab-2027/
```

Inside it, create:

```text
gallery/open-lab-2027/index.qmd
```

A simple template:

```markdown
---
title: "Open Lab Day 2027"
---

[← Back to gallery](../index.qmd)

::: {.photo-grid}
![Open Lab Day](photo1.jpg){group="open-lab-2027"}
![Lab visitors](photo2.jpg){group="open-lab-2027"}
![](photo3.jpg){group="open-lab-2027"}
:::
```

Put the photos in the same folder:

```text
gallery/open-lab-2027/photo1.jpg
gallery/open-lab-2027/photo2.jpg
gallery/open-lab-2027/photo3.jpg
```

Then edit:

```text
gallery/index.qmd
```

and add a new album card, for example:

```html
<a class="album-card" href="open-lab-2027/index.html">
<div class="album-cover"><i class="bi bi-camera"></i></div>
<div class="album-body">
<h3>Open Lab Day 2027</h3>
<p>Visitors, demonstrations, and activities from Open Lab Day.</p>
</div>
</a>
```

At present, creating a completely new album is one of the few tasks that still requires editing the Gallery landing-page HTML manually.

---

# Funded Projects

## 24. Add a funded project later

Edit:

```text
_data/projects.yml
```

The file is currently empty, so the Research page hides the Projects section automatically.

Example:

```yaml
projects:
  - title: "Project Title"
    funder: "National Research Foundation of Korea"
    program: "Program Name"
    role: "Principal Investigator"
    start: "2027-03"
    end: "2030-02"
    amount:
    url:
```

Fields currently displayed by the generator include:

```text
title
funder
program
role
start / end
amount
url
```

You may also use a single `duration:` field instead of separate `start` and `end` values.

When at least one project exists, the **Funded Projects** section appears automatically.

---

# Occasional Page Edits

## 25. Edit the homepage hero text or image

Edit:

```text
index.qmd
```

The hero text is near the top of the file.

The hero image is inside:

```markdown
::: {.hero-art}
![](assets/img/...){fig-alt="..."}
:::
```

Put the final hero illustration under an appropriate image folder such as:

```text
assets/img/research/
```

or create a dedicated folder such as:

```text
assets/img/hero/
```

and update the image path in `index.qmd`.

---

## 26. Edit the PI section

The PI content is maintained manually in:

```text
people/index.qmd
```

Use this file for the PI portrait, short biography, office/lab information, Google Scholar/GitHub/personal-site links, etc.

Student cards are **not** edited here; they come from `_data/people.yml`.

---

## 27. Edit the Teaching page

Edit:

```text
teaching.qmd
```

---

# Render and Test Locally

## 28. First-time setup

From the website root:

```powershell
pip install -r requirements.txt
```

You normally only need to do this once for a Python environment.

---

## 29. Render the entire website

From the website root:

```powershell
quarto render
```

This does all of the following automatically:

- runs the People generator;
- runs the Research generator;
- runs the manuscript generator;
- runs the publication generator;
- renders all QMD pages;
- writes the final static site to `_site/`.

You do not need to run the Python generator scripts individually during normal maintenance.

---

## 30. Inspect the fully rendered site locally without Quarto re-rendering every page

After `quarto render`, run:

```powershell
python -m http.server 8000 --directory _site
```

Open:

```text
http://localhost:8000
```

Now you can navigate through the already-rendered site instantly.

Keep the server running. When you edit the source:

1. open another terminal;
2. run `quarto render` again;
3. refresh the browser.

This is usually much more convenient than `quarto preview` for checking the entire website.

Stop the local server with:

```text
Ctrl+C
```

---

## 31. If the browser seems to show an old version

First confirm you are rendering the correct project folder:

```powershell
Get-Location
```

Then render:

```powershell
quarto render
```

Check that the rendered homepage was updated:

```powershell
Get-Item .\_site\index.html | Select-Object FullName, LastWriteTime
```

Restart the local server from the same project root if necessary:

```powershell
python -m http.server 8000 --directory "$PWD\_site"
```

Then use a hard browser refresh:

```text
Ctrl+F5
```

---

# Publish to GitHub Pages

## 32. Normal publishing workflow

Once the site looks correct locally:

```powershell
git add .
git commit -m "Update EIS Lab website"
git push
```

The included GitHub Actions workflow:

```text
.github/workflows/publish.yml
```

renders and deploys the complete site automatically after pushes to `main`.

GitHub Pages should be configured once as:

```text
Repository → Settings → Pages → Build and deployment → Source → GitHub Actions
```

After that, you should not manually upload `_site/`.

---

# YAML / BibTeX Safety Notes

## 33. YAML indentation

YAML is indentation-sensitive. Use spaces, not tabs.

Good:

```yaml
topics:
  - XAI
  - Smart Manufacturing
```

Bad:

```yaml
topics:
- XAI
    - Smart Manufacturing
```

When a title or value contains punctuation that may confuse YAML, put it in quotes:

```yaml
title: "TRACE: Agentic Explanation Generation"
```

---

## 34. Empty fields

For optional YAML fields, either of these is acceptable:

```yaml
code:
```

or:

```yaml
code: null
```

The generators treat them as empty and do not render the corresponding element.

Do **not** write placeholder strings such as:

```yaml
code: "None"
```

because the website may display them as real content.

---

# Common Workflows

## 35. Student joins the lab

1. Put portrait in `assets/img/people/`.
2. Add student to `_data/people.yml` with blank `graduated:`.
3. Add new topic labels to `_data/topic_styles.yml` if needed.
4. Optionally create a News item.
5. Run `quarto render`.

---

## 36. Student graduates

1. Add `graduated: "YYYY-MM"` in `_data/people.yml`.
2. Optionally add `thesis:` and `current_position:`.
3. Add a graduation News item.
4. Add photos to `gallery/graduations/` if available.
5. Run `quarto render`.

---

## 37. Paper is submitted

1. Add it under `submitted:` in `_data/manuscripts.yml`.
2. Add preprint/code links if public.
3. Run `quarto render`.

No News post is normally necessary.

---

## 38. Paper is accepted / published

1. Remove it from `_data/manuscripts.yml`.
2. Add final BibTeX record to `publications/references.bib`.
3. Optionally update the corresponding research topic in `_data/research.yml` with DOI/paper/code links.
4. Create a publication News item.
5. Run `quarto render`.

---

## 39. Lab attends a conference

1. Add any published conference paper to `publications/references.bib`.
2. Create a conference News post in `news/`.
3. Put event photos in `gallery/conferences/` and edit `gallery/conferences/index.qmd`.
4. Run `quarto render`.

---

## 40. Start a new research line

1. Add the topic to `_data/research.yml`.
2. Set `public: false` if you want to prepare it privately first.
3. Add a conceptual image under `assets/img/research/`.
4. When ready, switch `public: true`.
5. Add relevant paper/preprint/code/dataset links as they become available.
6. Run `quarto render`.

---

# The main rule

For routine maintenance, think in terms of **content records**, not web layout:

```text
new student      → _data/people.yml
student graduates → _data/people.yml
new research     → _data/research.yml
working/submitted paper → _data/manuscripts.yml
published paper  → publications/references.bib
news             → one new news/*.qmd file
gallery photos   → the relevant gallery/<album>/ folder
funded project   → _data/projects.yml
```

Then:

```powershell
quarto render
```

Check locally, commit, and push.
