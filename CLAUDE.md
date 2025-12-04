<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the documentation repository for j-lawyer.org, a free case management solution for law firms. Documentation is maintained in **Markdown** format and built with **MkDocs** using the Material theme.

## Build Commands

Requires: Python 3, pip

```bash
# Install dependencies
pip install mkdocs-material mkdocs-with-pdf

# Local development server (auto-reload)
mkdocs serve

# Build static site
mkdocs build

# Build with PDF export
ENABLE_PDF_EXPORT=1 mkdocs build
```

Output:
- `site/` - Static HTML site
- `j-lawyer-dokumentation.pdf` - PDF export (when enabled)

## Repository Structure

```
docs/
├── index.md                    # Landing page
├── benutzerhandbuch/           # User guide (German)
│   ├── index.md
│   ├── installation.md
│   ├── aktenverwaltung.md
│   └── ...
├── releasenotes/               # Release notes by version
│   ├── index.md
│   ├── v3-4.md
│   └── ...
├── images/                     # Screenshots and images
└── overrides/                  # Theme customizations
    └── stylesheets/extra.css
scripts/                        # Helper scripts
├── add_anchors.py              # Add stable anchors to headings
├── extract_images.py           # Extract images from .fodt
└── fodt_to_markdown.py         # Convert .fodt to Markdown
mkdocs.yml                      # MkDocs configuration
.github/workflows/docs.yml      # GitHub Actions for deployment
```

## Working with Documentation

- Edit Markdown files in `docs/`
- Add images to `docs/images/` and reference them with `![Alt](../images/filename.png)`
- Stable anchors use the format `{#anchor-id}` after headings
- Run `mkdocs serve` to preview changes locally at http://localhost:8000
- Push to `master` branch to trigger automatic deployment to GitHub Pages

## Deployment

GitHub Actions automatically builds and deploys to GitHub Pages on push to `master`.

Live site: https://jlawyerorg.github.io/j-lawyer-documentation/

## License

GNU Affero General Public License (AGPL-3.0)
- starte mkdocs serve niemals auf port 8080 oder 8081
- Wenn eine Suche / ein Abgleich mit Code erforderlich ist, suche in /home/jens/dev/j-lawyer-org.