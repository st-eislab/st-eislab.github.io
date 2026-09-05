# EIS Lab Website (Quarto)

Website of the Explainable Intelligent Systems Lab @ SeoulTech. The site is intentionally data-driven so routine updates require editing YAML/BibTeX/Markdown rather than page layout.

## Requirements

- Quarto 1.4+
- Python 3

```bash
pip install -r requirements.txt
```

## Render the complete site and inspect it locally

```bash
quarto render
python -m http.server 8000 --directory _site
```

Open <http://localhost:8000>. Navigation uses the already-rendered HTML, so clicking between pages does not trigger Quarto rendering. After an edit, run `quarto render` again and refresh the browser.

## Main maintenance files

- `_data/people.yml` — current students and alumni
- `_data/topic_styles.yml` — consistent research-topic badge styles
- `_data/research.yml` — research directions and active/emerging topics
- `_data/manuscripts.yml` — working and submitted/under-review manuscripts
- `_data/projects.yml` — funded projects; an empty file means no Projects section is shown
- `publications/references.bib` — published scholarly outputs
- `news/` — one `.qmd` per news item
- `gallery/` — event photo albums

See `_docs/MAINTENANCE.md` for the detailed workflow.

## Publish

The included GitHub Actions workflow renders and deploys the site after pushes to `main`. Set the GitHub repository's Pages source to **GitHub Actions** once.
