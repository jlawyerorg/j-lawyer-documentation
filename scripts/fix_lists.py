#!/usr/bin/env python3
"""
Fügt Leerzeilen zwischen aufeinanderfolgenden Listenpunkten ein,
damit MkDocs sie als separate Listen-Items rendert.
"""

import os
import re
import sys

def fix_lists_in_file(filepath):
    """Fügt Leerzeilen zwischen Listenpunkten ein."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Muster: Zeile die mit "- " beginnt, gefolgt von Zeile die mit "- " beginnt
    # Ersetzen durch: erste Zeile, Leerzeile, zweite Zeile
    # Wir müssen das iterativ machen, da sich Muster überlappen können

    lines = content.split('\n')
    new_lines = []

    for i, line in enumerate(lines):
        new_lines.append(line)

        # Prüfen ob aktuelle Zeile ein Listenpunkt ist und nächste auch
        if i < len(lines) - 1:
            current_is_list = line.strip().startswith('- ') and not line.startswith('    ')
            next_is_list = lines[i + 1].strip().startswith('- ') and not lines[i + 1].startswith('    ')

            # Auch nummerierte Listen berücksichtigen
            current_is_numbered = re.match(r'^\d+\.\s', line.strip()) and not line.startswith('    ')
            next_is_numbered = re.match(r'^\d+\.\s', lines[i + 1].strip()) and not lines[i + 1].startswith('    ')

            if (current_is_list and next_is_list) or (current_is_numbered and next_is_numbered):
                new_lines.append('')  # Leerzeile einfügen

    new_content = '\n'.join(new_lines)

    if new_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    docs_dir = '/home/jens/dev/j-lawyer-documentation/docs/benutzerhandbuch'

    modified_files = []

    for filename in os.listdir(docs_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(docs_dir, filename)
            if fix_lists_in_file(filepath):
                modified_files.append(filename)
                print(f"Korrigiert: {filename}")

    print(f"\n{len(modified_files)} Dateien wurden korrigiert.")

if __name__ == '__main__':
    main()
