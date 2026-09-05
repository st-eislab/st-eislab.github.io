# EIS Lab website — maintenance guide

The site is intentionally data-driven. In routine maintenance you should almost never edit HTML or CSS.

## Local full-site inspection (fast navigation)

From the website root:

```bash
pip install -r requirements.txt
quarto render
```

Then serve the already-rendered `_site` folder:

```bash
python -m http.server 8000 --directory _site
```

Open <http://localhost:8000>. Navigation is instant because Quarto is no longer rendering pages on demand. Keep the server running; after edits, run `quarto render` again in another terminal and refresh the browser.

## Add a student

Edit `_data/people.yml`, copy a student record, and fill the fields you have. Empty optional fields are hidden.

To graduate a student, set for example:

```yaml
graduated: "2026-08"
thesis: "Optional thesis title"
current_position: "Optional current position"
```

That automatically moves the person from Current Members to Alumni.

Portraits should normally be placed in `assets/img/people/`.

## Image organization

Keep images in their purpose-specific folders:

- `assets/img/people/` — PI/student portraits
- `assets/img/research/` — research-topic and homepage research visuals
- `assets/img/news/` — representative images for news posts
- `assets/img/gallery/` — event photo albums

Do not keep duplicate portraits in `assets/img/` itself. Legacy slider assets have been removed; any image reused from the old slider now lives under `assets/img/research/`.

## Student research-topic badges

People records contain simple labels under `topics`. Their visual family is controlled centrally in `_data/topic_styles.yml`. Reusing the same label automatically gives the same visual style across people.

## Add or edit research

Edit `_data/research.yml`.

- `directions` = stable lab-level research directions.
- `topics` = concrete active research topics.
- Optional `paper`, `doi`, `preprint`, `code`, `dataset`, and `project_url` fields render only when populated.
- Set `public: false` to keep a research topic in the YAML without publishing it. Change it to `true` when you are ready to disclose it.

A topic's `image` is just a path, so you can replace a conceptual image with a published paper figure later without touching the page layout.

## Working / submitted manuscripts

Edit `_data/manuscripts.yml`.

- `working`: title is enough.
- `submitted`: title is required; venue, submission date, preprint, code, and quartile are optional.

The section "Submitted / Under Review" is generated automatically. Empty categories do not appear.

## Published papers

Edit `publications/references.bib`. Published outputs are generated automatically from BibTeX.

The publication generator separates journal articles, international conference papers, book chapters, domestic conference papers, and domestic journal articles. Add the optional custom field `scope = {domestic}` to a published BibTeX entry when it should be placed in a domestic category.

## Funded projects

`_data/projects.yml` is currently empty, so no Projects section appears. When you want to publish a funded project, add a record there and the Research page will show it automatically.

## News

Use News as the public timeline of meaningful lab milestones: student graduations/defenses, paper acceptances, conference participation, awards, releases, invited talks, grants, and major lab events. Create a new `.qmd` item using the existing News structure; Quarto listings sort items automatically.

For events with many photos, use both: a short News item with one representative image, and a Gallery album containing the full photo set.

## Gallery

Put event images under `assets/img/gallery/` and update the appropriate gallery `.qmd` page. This part remains intentionally manual because each event usually benefits from a selected cover image and captions.

## Publish

The included `.github/workflows/publish.yml` renders and deploys the complete site after a push to `main`. In GitHub, set **Settings → Pages → Build and deployment → Source** to **GitHub Actions** once.
