#!/usr/bin/env python3
"""
Fügt explizite Anker zu wichtigen Abschnitten hinzu.
Format: ## Überschrift {#anker-id}
"""

import re
from pathlib import Path

# Mapping: (Datei, Überschrift-Pattern) -> Anker-ID
ANCHORS = {
    # Installation
    ("installation.md", "Installation auf Windows-Systemen"): "windows",
    ("installation.md", "Installation auf macOS-Systemen"): "macos",
    ("installation.md", "Installation auf Linux-Systemen"): "linux",
    ("installation.md", "Start der Anwendung"): "start",
    ("installation.md", "Start und Stoppen des j-lawyer.org Servers"): "server-start",
    ("installation.md", "Start des j-lawyer.org Clients"): "client-start",

    # Systemvoraussetzungen
    ("systemvoraussetzungen.md", "Unterstützte Betriebssysteme"): "betriebssysteme",
    ("systemvoraussetzungen.md", "Server"): "server",
    ("systemvoraussetzungen.md", "Client / Arbeitsplatz"): "client",

    # Erste Schritte
    ("erste-schritte.md", "Kanzleiprofil ausfüllen"): "kanzleiprofil",
    ("erste-schritte.md", "Datensicherungen konfigurieren"): "datensicherung",
    ("erste-schritte.md", "Import der deutschen Banken- und Ortschaftenverzeichnisse"): "banken-import",
    ("erste-schritte.md", "Ändern des Administratorpasswortes"): "admin-passwort",
    ("erste-schritte.md", "Optional: Anlegen zusätzlicher Nutzer"): "nutzer-anlegen",

    # Aktenverwaltung
    ("aktenverwaltung.md", "Akten suchen"): "suchen",
    ("aktenverwaltung.md", "Aktenanlage"): "anlegen",
    ("aktenverwaltung.md", "Aktenzeichen"): "aktenzeichen",
    ("aktenverwaltung.md", "Dokumente in Ordnern organisieren"): "ordner",
    ("aktenverwaltung.md", "Aktenhistorie"): "historie",
    ("aktenverwaltung.md", "Aktenablage / Archivierung"): "archivierung",
    ("aktenverwaltung.md", "Zugriff auf Akten beschränken"): "berechtigungen",
    ("aktenverwaltung.md", "Akten löschen"): "loeschen",

    # Adressen
    ("adressen.md", "Adressen suchen"): "suchen",
    ("adressen.md", "Adresse importieren"): "import",
    ("adressen.md", "Beteiligtentypen konfigurieren"): "beteiligtentypen",

    # Dokumentenmanagement
    ("dokumentenmanagement.md", "Auswahl der Textverarbeitung"): "textverarbeitung",
    ("dokumentenmanagement.md", "Dokumentvorlagen"): "vorlagen",
    ("dokumentenmanagement.md", "Platzhalter"): "platzhalter",
    ("dokumentenmanagement.md", "Dokument aus einer Vorlage erstellen"): "dokument-erstellen",
    ("dokumentenmanagement.md", "Volltextsuche"): "volltextsuche",
    ("dokumentenmanagement.md", "Scanner integrieren"): "scanner",
    ("dokumentenmanagement.md", "PDF-Konvertierung"): "pdf-konvertierung",

    # Kalender
    ("kalender.md", "Kalender: Termine, Wiedervorlagen und Fristen"): "uebersicht",

    # Finanzen
    ("finanzen.md", "Rechnungen"): "rechnungen",
    ("finanzen.md", "Steuersätze"): "steuersaetze",
    ("finanzen.md", "Zeiterfassung"): "zeiterfassung",
    ("finanzen.md", "Girocode"): "girocode",
    ("finanzen.md", "Elektronische Rechnungen"): "e-rechnung",

    # E-Mail
    ("email.md", "Anbindung von Postfächern mit Azure AD"): "azure-ad",
    ("email.md", "Anbindung von Google Mail"): "google-mail",
    ("email.md", "Bei Verbindungsproblemen: Mailserver als vertrauenswürdig deklarieren"): "mailserver-vertrauen",

    # KI-Assistent
    ("ki-assistent.md", "Transkription / Diktieren"): "transkription",
    ("ki-assistent.md", "Übersetzung"): "uebersetzung",
    ("ki-assistent.md", "Zusammenfassen"): "zusammenfassen",
    ("ki-assistent.md", "Dokument befragen"): "chat",
    ("ki-assistent.md", "Konfigurieren eigener Prompts"): "eigene-prompts",

    # Add-Ons
    ("addon-bea.md", "Voraussetzungen"): "voraussetzungen",
    ("addon-bea.md", "Inbetriebnahme"): "inbetriebnahme",
    ("addon-nextcloud.md", "Freigeben von Dokumenten"): "dokumente-freigeben",
    ("addon-nextcloud.md", "Synchronisieren des Adressbuchs"): "adressbuch-sync",
    ("addon-nextcloud.md", "Synchronisieren der Kalender"): "kalender-sync",

    # Administration
    ("administration.md", "Aktenzeichen bearbeiten"): "aktenzeichen-bearbeiten",
    ("administration.md", "Passwortkomplexität"): "passwortkomplexitaet",
    ("administration.md", "Datensicherung"): "datensicherung",
    ("administration.md", "Monitoring"): "monitoring",
    ("administration.md", "Logdateien"): "logdateien",

    # Schnittstellen
    ("schnittstellen.md", "REST API"): "rest-api",
    ("schnittstellen.md", "Web Hooks"): "webhooks",

    # Fehlerbehebung
    ("fehlerbehebung.md", "LibreOffice öffnet Dokumente immer im Hintergrund"): "libreoffice-hintergrund",
    ("fehlerbehebung.md", "j-lawyer.BOX: Login"): "box-login",

    # j-lawyer.BOX
    ("jlawyer-box.md", "Verbindung mit einer j-lawyer.BOX"): "verbindung",
    ("jlawyer-box.md", "Aktualisierung"): "updates",
    ("jlawyer-box.md", "Synchronisation zweier j-lawyer.BOXen"): "synchronisation",
}

def add_anchors():
    docs_dir = Path(__file__).parent.parent / 'docs' / 'benutzerhandbuch'

    modified_files = 0
    added_anchors = 0

    for (filename, heading_text), anchor_id in ANCHORS.items():
        filepath = docs_dir / filename

        if not filepath.exists():
            print(f"Warnung: {filename} nicht gefunden")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Suche Überschrift (##, ###, ####) mit dem Text
        # Escape special regex chars in heading_text
        escaped_heading = re.escape(heading_text)
        pattern = r'^(#{2,4}) (' + escaped_heading + r'[^\n]*?)$'

        # Prüfe ob Anker bereits existiert
        if f'{{#{anchor_id}}}' in content:
            continue

        match = re.search(pattern, content, re.MULTILINE)
        if match:
            old_heading = match.group(0)
            hashes = match.group(1)
            title = match.group(2).rstrip()

            # Entferne evtl. existierenden Anker
            title = re.sub(r'\s*\{#[^}]+\}\s*$', '', title)

            new_heading = f"{hashes} {title} {{#{anchor_id}}}"

            content = content.replace(old_heading, new_heading, 1)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            added_anchors += 1
            print(f"  {filename}: #{anchor_id}")
        else:
            # Versuche Teilübereinstimmung
            partial_pattern = r'^(#{2,4}) ([^\n]*' + re.escape(heading_text[:20]) + r'[^\n]*)$'
            match = re.search(partial_pattern, content, re.MULTILINE)
            if match:
                print(f"  Hinweis: '{heading_text}' nicht exakt gefunden in {filename}")
                print(f"    Gefunden: '{match.group(2)}'")

    print(f"\n{added_anchors} Anker hinzugefügt")

if __name__ == '__main__':
    add_anchors()
