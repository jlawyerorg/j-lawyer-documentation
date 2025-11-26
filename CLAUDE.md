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

This is the documentation repository for j-lawyer.org, a free case management solution for law firms. Documentation is maintained in **.fodt** (Flat OpenDocument Text) format - a plain-text XML format compatible with LibreOffice/OpenOffice that works well with version control.

## Build Commands

Requires: LibreOffice, unoconv, Ant, Java 8+

```bash
# Convert .fodt files to PDF
ant convertToPdf

# Convert .fodt files to HTML
ant convertToHtml

# Build and publish (requires remote server credentials as env vars)
ant publish
```

Output directories:
- `build/pdf/` - PDF exports
- `build/html/` - HTML exports

## Repository Structure

```
src/
├── j-lawyer.org-UserGuide-de.fodt      # German user guide (main doc)
├── j-lawyer.org-UserGuide-en.fodt      # English user guide
├── j-lawyer.org-ReleaseNotes-de.fodt   # German release notes
├── j-lawyer.org-ReleaseNotes-en.fodt   # English release notes
├── j-lawyer.BOX-QuickStart-de.fodp     # German quickstart (presentation)
└── j-lawyer.BOX-IdentityCard-de.fodp   # German identity card docs
```

## Working with .fodt Files

- .fodt files are XML-based and can be edited directly, but LibreOffice/OpenOffice is recommended for formatting
- The German documentation (`*-de.fodt`) is the primary/most current version
- Changes to .fodt files trigger CI builds that convert to PDF/HTML and publish to the server

## License

GNU Affero General Public License (AGPL-3.0)
