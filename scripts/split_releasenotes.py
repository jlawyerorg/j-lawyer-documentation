#!/usr/bin/env python3
"""
Teilt die Release Notes in separate Dateien pro Version auf.
"""

import re
from pathlib import Path

def split_releasenotes():
    docs_dir = Path(__file__).parent.parent / 'docs'
    releasenotes_file = docs_dir / 'releasenotes.md'
    output_dir = docs_dir / 'releasenotes'
    output_dir.mkdir(exist_ok=True)

    with open(releasenotes_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Finde alle Versionsabschnitte
    # Pattern: ### j-lawyer.org X.Y oder ### j-lawyer.org X.Y.Z
    pattern = r'(### j-lawyer\.org (\d+\.\d+(?:\.\d+)?).*?)(?=### j-lawyer\.org \d|$)'
    matches = re.findall(pattern, content, re.DOTALL)

    versions = []
    for match in matches:
        section_content = match[0].strip()
        version = match[1]

        # Erstelle Dateiname
        filename = f"v{version.replace('.', '-')}.md"
        filepath = output_dir / filename

        # Schreibe Datei mit korrigierter Überschrift (# statt ###)
        section_content = re.sub(r'^### ', '# ', section_content, count=1)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(section_content + '\n')

        versions.append((version, filename))
        print(f"Erstellt: {filename}")

    # Erstelle Index-Datei
    index_content = """# Release Notes

Übersicht aller Versionen von j-lawyer.org.

## Aktuelle Versionen

"""
    # Sortiere Versionen (neueste zuerst)
    def version_key(v):
        parts = v[0].split('.')
        return tuple(int(p) for p in parts)

    versions_sorted = sorted(versions, key=version_key, reverse=True)

    for version, filename in versions_sorted:
        index_content += f"- [Version {version}]({filename})\n"

    index_file = output_dir / 'index.md'
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"\nErstellt: index.md")
    print(f"\nInsgesamt {len(versions)} Versionen extrahiert.")

    return versions_sorted

if __name__ == '__main__':
    split_releasenotes()
