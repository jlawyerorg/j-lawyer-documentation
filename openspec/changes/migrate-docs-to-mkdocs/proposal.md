# Change: Migration der Dokumentation zu MkDocs

## Why

Die bestehende .fodt-basierte Dokumentation (LibreOffice Flat XML) ist schwer zu bearbeiten, hat keine eingebaute Suche und erfordert einen komplexen Build-Prozess mit LibreOffice/unoconv. Ein modernes Markdown-basiertes System mit MkDocs ermöglicht einfachere Bearbeitung, bessere Versionskontrolle und eine zeitgemäße Web-Präsentation mit Volltextsuche.

## What Changes

- **BREAKING**: Umstellung von .fodt auf Markdown-Format
- Einführung von MkDocs mit Material Theme als Dokumentations-Framework
- Neue Verzeichnisstruktur unter `docs/`
- GitHub Actions Workflow für automatischen Build und Deploy
- GitHub Pages als Hosting-Plattform
- PDF-Export über `mkdocs-with-pdf` Plugin
- Entfernung des alten Ant-basierten Build-Systems

## Impact

- Affected specs: documentation (neu)
- Affected code:
  - `src/*.fodt` - zu entfernen/archivieren
  - `src/*.fodp` - zu entfernen/archivieren
  - `build.xml` - zu entfernen
  - `nbproject/` - zu entfernen
  - `README.md` - zu aktualisieren
  - `CLAUDE.md` - zu aktualisieren
- Neue Dateien:
  - `mkdocs.yml` - MkDocs Konfiguration
  - `docs/**/*.md` - Markdown-Dokumentation
  - `docs/images/*` - extrahierte Bilder
  - `.github/workflows/docs.yml` - CI/CD Workflow
