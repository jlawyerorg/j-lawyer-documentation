# j-lawyer.org Dokumentation

[![Deploy Documentation](https://github.com/j-lawyer-org/j-lawyer-documentation/actions/workflows/docs.yml/badge.svg)](https://github.com/j-lawyer-org/j-lawyer-documentation/actions/workflows/docs.yml)

Dokumentationsprojekt für [j-lawyer.org](http://www.j-lawyer.org) - eine kostenfreie Kanzleisoftware.

## Format

Die Dokumentation wird im Markdown-Format gepflegt und mit [MkDocs](https://www.mkdocs.org/) und dem [Material Theme](https://squidfunk.github.io/mkdocs-material/) als statische Website generiert.

## Struktur

```
docs/
├── index.md                    # Startseite
├── benutzerhandbuch/
│   ├── index.md                # Übersicht
│   └── vollstaendig.md         # Vollständiges Handbuch
├── releasenotes/
│   ├── index.md                # Übersicht aller Versionen
│   └── v*.md                   # Release Notes pro Version
└── images/                     # Bilder
mkdocs.yml                      # MkDocs Konfiguration
```

## Lokale Entwicklung

### Voraussetzungen

- Python 3.x
- pip

### Installation

```bash
pip install mkdocs-material
```

### Lokaler Server starten

```bash
mkdocs serve
bzw.
~/.local/bin/mkdocs serve
```

Die Dokumentation ist dann unter http://localhost:8000 erreichbar. Änderungen an Markdown-Dateien werden automatisch neu geladen.

### Build

```bash
mkdocs build
```

Die generierte Website liegt im Verzeichnis `site/`.

## Deployment

Die Dokumentation wird automatisch über GitHub Actions auf GitHub Pages veröffentlicht:

1. Bei jedem Push auf den `master`-Branch (wenn Änderungen in `docs/`, `mkdocs.yml` oder `.github/workflows/docs.yml`)
2. Der Workflow baut die Dokumentation und deployt sie auf GitHub Pages

### GitHub Pages einrichten

1. Repository Settings → Pages
2. Source: "GitHub Actions" auswählen
3. Nach dem ersten erfolgreichen Workflow ist die Dokumentation unter `https://<org>.github.io/j-lawyer-documentation/` erreichbar

## Dokumentation bearbeiten

1. Markdown-Dateien im `docs/` Verzeichnis bearbeiten
2. Lokal testen mit `mkdocs serve`
3. Änderungen committen und pushen
4. GitHub Actions baut und deployt automatisch

### Neue Seite hinzufügen

1. Markdown-Datei unter `docs/` erstellen
2. In `mkdocs.yml` unter `nav:` eintragen

### Bilder hinzufügen

1. Bild in `docs/images/` ablegen
2. In Markdown einbinden: `![Beschreibung](images/bildname.png)`

## Mitwirkende

j-dimension / j-lawyer.org

## Lizenz

GNU AFFERO GENERAL PUBLIC LICENSE (AGPL-3.0)

https://www.gnu.org/licenses/agpl-3.0.txt
