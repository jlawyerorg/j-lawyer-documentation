#!/usr/bin/env python3
"""
Formatiert Script-Beispiele und andere Code-ähnliche Inhalte in Markdown-Dateien
als Code-Blöcke.
"""

import os
import re

def fix_code_blocks_in_file(filepath):
    """Formatiert Code-Beispiele in der Datei."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Muster 1: Zeilen die mit [[SCRIPT: beginnen und noch nicht in Code-Block sind
    # Prüfen ob vorherige Zeile ``` ist
    lines = content.split('\n')
    new_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Prüfe ob Zeile ein Script-Beispiel ist und nicht bereits in Code-Block
        if '[[SCRIPT:' in line and line.strip().startswith('[[SCRIPT:'):
            # Prüfe ob vorherige Zeile bereits ``` ist
            if new_lines and new_lines[-1].strip() == '```':
                new_lines.append(line)
            else:
                # Füge Code-Block hinzu
                new_lines.append('```')
                new_lines.append(line)
                # Prüfe ob nächste Zeile auch ein Script ist oder leer
                if i + 1 < len(lines) and not lines[i + 1].strip().startswith('[[SCRIPT:'):
                    new_lines.append('```')
                elif i + 1 >= len(lines):
                    new_lines.append('```')
        elif line.strip() == '```' and new_lines:
            # Bereits existierender Code-Block-Marker
            new_lines.append(line)
        else:
            # Prüfe ob wir gerade einen Code-Block beenden müssen
            # (vorherige Zeile war Script und diese nicht)
            if (new_lines and
                len(new_lines) >= 2 and
                '[[SCRIPT:' in new_lines[-1] and
                new_lines[-2].strip() == '```' and
                not line.strip().startswith('[[SCRIPT:')):
                new_lines.append('```')
            new_lines.append(line)

        i += 1

    new_content = '\n'.join(new_lines)

    # Bereinige doppelte Code-Block-Marker
    new_content = re.sub(r'```\n\n```', '', new_content)
    new_content = re.sub(r'```\n```', '```', new_content)

    if new_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    filepath = '/home/jens/dev/j-lawyer-documentation/docs/benutzerhandbuch/dokumentenmanagement.md'

    if fix_code_blocks_in_file(filepath):
        print(f"Korrigiert: {filepath}")
    else:
        print("Keine Änderungen notwendig")

if __name__ == '__main__':
    main()
