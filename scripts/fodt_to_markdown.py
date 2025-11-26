#!/usr/bin/env python3
"""
Konvertiert .fodt-Dateien (LibreOffice Flat XML) zu Markdown.
Extrahiert Text und Struktur, ersetzt Bildverweise.
"""

import re
import xml.etree.ElementTree as ET
from pathlib import Path
from html import unescape
import sys

# Namespaces in fodt
NS = {
    'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0',
    'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
    'table': 'urn:oasis:names:tc:opendocument:xmlns:table:1.0',
    'draw': 'urn:oasis:names:tc:opendocument:xmlns:drawing:1.0',
    'style': 'urn:oasis:names:tc:opendocument:xmlns:style:1.0',
    'xlink': 'http://www.w3.org/1999/xlink',
}

# Tags die übersprungen werden sollen (binäre Daten)
SKIP_TAGS = {
    f'{{{NS["office"]}}}binary-data',
    f'{{{NS["draw"]}}}image',
}

class FodtToMarkdown:
    def __init__(self, fodt_path, image_prefix):
        self.fodt_path = Path(fodt_path)
        self.image_prefix = image_prefix
        self.image_counter = 0
        self.output = []
        self.in_list = False
        self.list_level = 0

    def get_text(self, element):
        """Extrahiert allen Text aus einem Element rekursiv."""
        # Überspringe binäre Daten und Bilder
        if element.tag in SKIP_TAGS:
            return ''

        text = element.text or ''

        # Prüfe ob Text wie Base64 aussieht (lang und nur bestimmte Zeichen)
        if len(text) > 100 and re.match(r'^[A-Za-z0-9+/=\s]+$', text):
            text = ''

        for child in element:
            # Überspringe binäre Daten
            if child.tag in SKIP_TAGS:
                text += child.tail or ''
                continue

            # Zeilenumbruch
            if child.tag == f'{{{NS["text"]}}}line-break':
                text += '\n'
            # Tab
            elif child.tag == f'{{{NS["text"]}}}tab':
                text += '\t'
            # Leerzeichen
            elif child.tag == f'{{{NS["text"]}}}s':
                count = int(child.get(f'{{{NS["text"]}}}c', 1))
                text += ' ' * count
            # Span oder andere Textelemente
            else:
                text += self.get_text(child)
            text += child.tail or ''
        return text

    def process_paragraph(self, elem, style_name=''):
        """Verarbeitet einen Absatz."""
        # Prüfe auf eingebettete Frames/Bilder
        frames = elem.findall(f'.//{{{NS["draw"]}}}frame')
        for frame in frames:
            self.process_frame(frame)

        text = self.get_text(elem).strip()
        if not text:
            return

        # Prüfe auf Überschriften-Style
        if style_name:
            style_lower = style_name.lower()
            if 'heading' in style_lower or 'überschrift' in style_lower:
                # Extrahiere Level aus Style-Name
                match = re.search(r'(\d+)', style_name)
                level = int(match.group(1)) if match else 1
                level = min(level, 6)
                self.output.append(f"\n{'#' * level} {text}\n")
                return

        # Normaler Absatz
        self.output.append(f"\n{text}\n")

    def process_heading(self, elem):
        """Verarbeitet eine Überschrift."""
        text = self.get_text(elem).strip()
        if not text:
            return

        level = int(elem.get(f'{{{NS["text"]}}}outline-level', 1))
        level = min(level, 6)
        self.output.append(f"\n{'#' * level} {text}\n")

    def process_list_item(self, elem, level=0):
        """Verarbeitet ein Listenelement."""
        indent = '    ' * level
        for child in elem:
            if child.tag == f'{{{NS["text"]}}}p':
                text = self.get_text(child).strip()
                if text:
                    self.output.append(f"{indent}- {text}\n")
            elif child.tag == f'{{{NS["text"]}}}list':
                self.process_list(child, level + 1)

    def process_list(self, elem, level=0):
        """Verarbeitet eine Liste."""
        for item in elem.findall(f'{{{NS["text"]}}}list-item'):
            self.process_list_item(item, level)

    def process_table(self, elem):
        """Verarbeitet eine Tabelle."""
        rows = elem.findall(f'.//{{{NS["table"]}}}table-row')
        if not rows:
            return

        table_data = []
        for row in rows:
            cells = row.findall(f'{{{NS["table"]}}}table-cell')
            row_data = []
            for cell in cells:
                # Anzahl der überspannten Spalten
                repeat = int(cell.get(f'{{{NS["table"]}}}number-columns-repeated', 1))
                cell_text = ''
                for p in cell.findall(f'.//{{{NS["text"]}}}p'):
                    cell_text += self.get_text(p).strip() + ' '
                cell_text = cell_text.strip().replace('|', '\\|')
                for _ in range(repeat):
                    row_data.append(cell_text)
            if row_data:
                table_data.append(row_data)

        if not table_data:
            return

        # Finde maximale Spaltenanzahl
        max_cols = max(len(row) for row in table_data)

        # Normalisiere Zeilen
        for row in table_data:
            while len(row) < max_cols:
                row.append('')

        # Ausgabe als Markdown-Tabelle
        self.output.append('\n')

        # Header
        header = table_data[0] if table_data else [''] * max_cols
        self.output.append('| ' + ' | '.join(header) + ' |\n')
        self.output.append('| ' + ' | '.join(['---'] * max_cols) + ' |\n')

        # Body
        for row in table_data[1:]:
            self.output.append('| ' + ' | '.join(row) + ' |\n')

        self.output.append('\n')

    def process_frame(self, elem):
        """Verarbeitet einen Frame (nur wenn er direkt ein Bild enthält)."""
        # Prüfe ob Frame direkt ein Bild enthält (nicht in Kind-Frame)
        # Suche draw:image als direktes oder nahes Kind
        image_elem = elem.find(f'{{{NS["draw"]}}}image')
        if image_elem is None:
            # Versuche auch in draw:frame zu suchen (verschachtelt)
            return

        # Prüfe ob das Image binary-data enthält
        binary_data = image_elem.find(f'{{{NS["office"]}}}binary-data')
        if binary_data is None:
            return

        self.image_counter += 1
        image_name = f"{self.image_prefix}-{self.image_counter:03d}.png"
        self.output.append(f"\n![Abbildung {self.image_counter}](../images/{image_name})\n")

    def process_element(self, elem):
        """Verarbeitet ein Element rekursiv."""
        tag = elem.tag

        if tag == f'{{{NS["text"]}}}p':
            style = elem.get(f'{{{NS["text"]}}}style-name', '')
            self.process_paragraph(elem, style)

        elif tag == f'{{{NS["text"]}}}h':
            self.process_heading(elem)

        elif tag == f'{{{NS["text"]}}}list':
            self.process_list(elem)

        elif tag == f'{{{NS["table"]}}}table':
            self.process_table(elem)

        elif tag == f'{{{NS["draw"]}}}frame':
            self.process_frame(elem)

        else:
            # Rekursiv verarbeiten
            for child in elem:
                self.process_element(child)

    def convert(self):
        """Führt die Konvertierung durch."""
        print(f"Lese {self.fodt_path}...")

        # Parse XML
        tree = ET.parse(self.fodt_path)
        root = tree.getroot()

        # Finde office:body/office:text
        body = root.find(f'.//{{{NS["office"]}}}body')
        if body is None:
            print("Fehler: Kein office:body gefunden")
            return ""

        text_content = body.find(f'{{{NS["office"]}}}text')
        if text_content is None:
            print("Fehler: Kein office:text gefunden")
            return ""

        # Verarbeite alle Elemente
        for child in text_content:
            self.process_element(child)

        # Bereinige Output
        markdown = ''.join(self.output)

        # Entferne übermäßige Leerzeilen
        markdown = re.sub(r'\n{4,}', '\n\n\n', markdown)

        return markdown


def main():
    src_dir = Path(__file__).parent.parent / 'src'
    docs_dir = Path(__file__).parent.parent / 'docs'

    # UserGuide-de
    userguide_de = src_dir / 'j-lawyer.org-UserGuide-de.fodt'
    if userguide_de.exists():
        converter = FodtToMarkdown(userguide_de, 'j-lawyer-org-UserGuide-de')
        markdown = converter.convert()

        output_file = docs_dir / 'benutzerhandbuch' / 'vollstaendig.md'
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"Geschrieben: {output_file} ({len(markdown):,} Zeichen)")

    # ReleaseNotes-de
    releasenotes_de = src_dir / 'j-lawyer.org-ReleaseNotes-de.fodt'
    if releasenotes_de.exists():
        converter = FodtToMarkdown(releasenotes_de, 'j-lawyer-org-ReleaseNotes-de')
        markdown = converter.convert()

        output_file = docs_dir / 'releasenotes.md'

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"Geschrieben: {output_file} ({len(markdown):,} Zeichen)")


if __name__ == '__main__':
    main()
