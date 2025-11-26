#!/usr/bin/env python3
"""
Teilt das Benutzerhandbuch in separate Kapitel-Dateien auf.
"""

import re
from pathlib import Path

# Mapping von H2-Überschriften zu Dateinamen und Kapiteltiteln
CHAPTER_MAPPING = {
    "Autoren / Mitwirkende": ("autoren", "Autoren"),
    "Änderungshistorie": ("aenderungshistorie", "Änderungshistorie"),
    "Systemvoraussetzungen": ("systemvoraussetzungen", "Systemvoraussetzungen"),
    "Installation": ("installation", "Installation"),
    "Start der Anwendung": ("installation", None),  # Anhängen an Installation
    "Aufbau der Programmoberfläche": ("oberflaeche", "Programmoberfläche"),
    "Erste Schritte": ("erste-schritte", "Erste Schritte"),
    "Aktenverwaltung": ("aktenverwaltung", "Aktenverwaltung"),
    "Kontakte / Adressen": ("adressen", "Kontakte / Adressen"),
    "Dokumentenmanagement": ("dokumentenmanagement", "Dokumentenmanagement"),
    "Kalender: Termine, Wiedervorlagen und Fristen": ("kalender", "Kalender"),
    "Rechnungen": ("finanzen", "Finanzen"),
    "Zeiterfassung": ("finanzen", None),  # Anhängen an Finanzen
    "E-Mail-Integration": ("email", "E-Mail-Integration"),
    "KI-Assistenzfunktionen (\"Assistent Ingo\")": ("ki-assistent", "KI-Assistent"),
    "Auswertungen": ("auswertungen", "Auswertungen"),
    "Postvorlagen (E-Mail, beA)": ("postvorlagen", "Postvorlagen"),
    "Instant Messaging / Nachrichtencenter": ("messaging", "Instant Messaging"),
    "Add-Ons: besonderes elektronisches Anwaltspostfach beA": ("addon-bea", "Add-On: beA"),
    "Add-Ons: E-POST (Hybridmail)": ("addon-epost", "Add-On: E-POST"),
    "Add-Ons: Drebis": ("addon-drebis", "Add-On: Drebis"),
    "Add-Ons: Sipgate": ("addon-sipgate", "Add-On: Sipgate"),
    "Add-Ons: Telefonie mit Softphone": ("addon-softphone", "Add-On: Softphone"),
    "Add-Ons: Nextcloud-Integration": ("addon-nextcloud", "Add-On: Nextcloud"),
    "Synchronisieren der Kalender (Nextcloud, mobile Geräte)": ("addon-nextcloud", None),  # Anhängen
    "Add-Ons: Gravity Forms-Anbindung": ("addon-gravityforms", "Add-On: Gravity Forms"),
    "Add-Ons: XJustiz-Viewer": ("addon-xjustiz", "Add-On: XJustiz"),
    "Systemadministration": ("administration", "Systemadministration"),
    "Schnittstellen und Integration": ("schnittstellen", "Schnittstellen"),
    "Deinstallation": ("deinstallation", "Deinstallation"),
    "Fehlerbehebung": ("fehlerbehebung", "Fehlerbehebung"),
    "j-lawyer.BOX": ("jlawyer-box", "j-lawyer.BOX"),
}

def split_handbook():
    docs_dir = Path(__file__).parent.parent / 'docs' / 'benutzerhandbuch'
    input_file = docs_dir / 'vollstaendig.md'

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Finde alle H2-Abschnitte
    # Pattern: ## Überschrift bis zum nächsten ## oder Ende
    pattern = r'^(## .+?)(?=^## |\Z)'
    sections = re.findall(pattern, content, re.MULTILINE | re.DOTALL)

    # Extrahiere auch den Header (vor erstem ##)
    header_match = re.match(r'^(# Benutzerhandbuch.*?)(?=^## )', content, re.MULTILINE | re.DOTALL)
    header = header_match.group(1).strip() if header_match else ""

    # Sammle Kapitel
    chapters = {}  # filename -> content

    for section in sections:
        # Extrahiere Überschrift
        title_match = re.match(r'^## (.+)$', section, re.MULTILINE)
        if not title_match:
            continue

        title = title_match.group(1).strip()

        if title not in CHAPTER_MAPPING:
            print(f"Warnung: Keine Zuordnung für '{title}'")
            continue

        filename, chapter_title = CHAPTER_MAPPING[title]

        if chapter_title is None:
            # Anhängen an existierendes Kapitel
            if filename in chapters:
                chapters[filename] += "\n\n" + section.strip()
            else:
                chapters[filename] = section.strip()
        else:
            # Neues Kapitel
            # Ändere ## zu # für Kapiteltitel
            section_content = re.sub(r'^## ', '# ', section, count=1, flags=re.MULTILINE)

            if filename in chapters:
                chapters[filename] += "\n\n" + section_content.strip()
            else:
                chapters[filename] = section_content.strip()

    # Schreibe Kapitel-Dateien
    nav_entries = []

    for filename, content in chapters.items():
        filepath = docs_dir / f"{filename}.md"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content + "\n")

        # Extrahiere Titel für Navigation
        title_match = re.match(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else filename

        nav_entries.append((filename, title))
        print(f"Erstellt: {filename}.md")

    # Erstelle Index-Datei
    index_content = """# Benutzerhandbuch

Dies ist das Benutzerhandbuch für j-lawyer.org - der freien Kanzleisoftware.

## Kapitelübersicht

"""

    # Ordnung der Kapitel
    chapter_order = [
        "systemvoraussetzungen",
        "installation",
        "oberflaeche",
        "erste-schritte",
        "aktenverwaltung",
        "adressen",
        "dokumentenmanagement",
        "kalender",
        "finanzen",
        "email",
        "ki-assistent",
        "auswertungen",
        "postvorlagen",
        "messaging",
        "addon-bea",
        "addon-epost",
        "addon-drebis",
        "addon-sipgate",
        "addon-softphone",
        "addon-nextcloud",
        "addon-gravityforms",
        "addon-xjustiz",
        "administration",
        "schnittstellen",
        "deinstallation",
        "fehlerbehebung",
        "jlawyer-box",
        "autoren",
        "aenderungshistorie",
    ]

    for filename in chapter_order:
        if filename in chapters:
            title_match = re.match(r'^# (.+)$', chapters[filename], re.MULTILINE)
            title = title_match.group(1) if title_match else filename
            index_content += f"- [{title}]({filename}.md)\n"

    index_file = docs_dir / 'index.md'
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"\nErstellt: index.md")
    print(f"\nInsgesamt {len(chapters)} Kapitel erstellt.")

    # Generiere nav-Einträge für mkdocs.yml
    print("\n--- Navigation für mkdocs.yml ---\n")
    print("  - Benutzerhandbuch:")
    print("    - Übersicht: benutzerhandbuch/index.md")
    for filename in chapter_order:
        if filename in chapters:
            title_match = re.match(r'^# (.+)$', chapters[filename], re.MULTILINE)
            title = title_match.group(1) if title_match else filename
            print(f"    - {title}: benutzerhandbuch/{filename}.md")

if __name__ == '__main__':
    split_handbook()
