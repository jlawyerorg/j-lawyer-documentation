#!/usr/bin/env python3
"""
Konvertiert nackte URLs in Markdown-Links.
URLs die bereits in Markdown-Link-Syntax sind, werden nicht verändert.
"""

import os
import re

def fix_urls_in_file(filepath):
    """Konvertiert nackte URLs zu Markdown-Links."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Muster für URLs die NICHT bereits in Markdown-Link-Syntax sind
    # Nicht matchen: (https://...) oder <https://...> oder [text](https://...)
    # Matchen: https://... am Ende eines Satzes oder alleinstehend

    # Regex für nackte URLs (nicht in Klammern oder bereits als Link)
    # Negative lookbehind für ( und <
    # URL endet bei Whitespace, ), ], > oder Zeilenende
    url_pattern = r'(?<!\(|<|\[)(?<!\]\()https?://[^\s\)\]>\"\'\,]+[^\s\)\]>\"\'\,\.]'

    def replace_url(match):
        url = match.group(0)
        # Prüfen ob URL mit Satzzeichen endet und diese entfernen
        while url and url[-1] in '.,;:':
            url = url[:-1]
        return f'<{url}>'

    # Zeilenweise verarbeiten um Kontext besser zu verstehen
    lines = content.split('\n')
    new_lines = []

    for line in lines:
        # Überspringen wenn Zeile bereits einen Markdown-Link enthält mit dieser URL
        # oder wenn URL in Klammern steht

        # Finde alle URLs in der Zeile
        urls_in_line = re.findall(r'https?://[^\s\)\]>\"\']+', line)

        for url in urls_in_line:
            # Bereinige URL von trailing Satzzeichen
            clean_url = url.rstrip('.,;:')

            # Prüfe ob URL bereits in Link-Syntax ist
            if f']({clean_url})' in line:
                continue
            if f'<{clean_url}>' in line:
                continue
            if f'({clean_url})' in line and f']({clean_url})' not in line:
                # URL ist in Klammern aber kein Markdown-Link - könnte Beispiel-URL sein
                continue

            # Ersetze nackte URL mit Auto-Link Syntax
            # Suche nach der URL mit möglichem trailing Satzzeichen
            pattern = re.escape(clean_url) + r'[.,;:]*'

            # Prüfe dass URL nicht schon in <> oder []() ist
            # Finde Position der URL
            match = re.search(pattern, line)
            if match:
                start = match.start()
                # Prüfe Zeichen davor
                if start > 0:
                    char_before = line[start-1]
                    if char_before in '(<[':
                        continue
                    # Prüfe auf ](
                    if start > 1 and line[start-2:start] == '](':
                        continue

                # Ersetze URL
                line = line[:match.start()] + f'<{clean_url}>' + line[match.end():]

        new_lines.append(line)

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
            if fix_urls_in_file(filepath):
                modified_files.append(filename)
                print(f"Korrigiert: {filename}")

    print(f"\n{len(modified_files)} Dateien wurden korrigiert.")

if __name__ == '__main__':
    main()
