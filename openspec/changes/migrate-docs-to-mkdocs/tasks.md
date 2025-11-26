# Tasks: Migration der Dokumentation zu MkDocs

## 1. MkDocs-Projekt initialisieren
- [ ] 1.1 `mkdocs.yml` Konfigurationsdatei erstellen
- [ ] 1.2 `docs/` Verzeichnis anlegen
- [ ] 1.3 Material Theme mit deutschen Spracheinstellungen konfigurieren
- [ ] 1.4 Such-Plugin mit deutscher Sprache aktivieren
- [ ] 1.5 Markdown-Extensions konfigurieren (attr_list, toc, tables, admonition)

## 2. Verzeichnisstruktur anlegen
- [ ] 2.1 `docs/index.md` - Startseite erstellen
- [ ] 2.2 `docs/installation/` - Installationsanleitungen
- [ ] 2.3 `docs/benutzerhandbuch/` - Hauptdokumentation
- [ ] 2.4 `docs/administration/` - Admin-Dokumentation
- [ ] 2.5 `docs/images/` - Bildverzeichnis
- [ ] 2.6 `docs/releasenotes.md` - Release Notes

## 3. Bilder extrahieren
- [ ] 3.1 Base64-eingebettete Bilder aus .fodt dekodieren
- [ ] 3.2 Bilder nach `docs/images/` exportieren
- [ ] 3.3 Sinnvolle Dateinamen vergeben
- [ ] 3.4 Bildverzeichnis strukturieren (nach Kapitel oder Funktion)

## 4. Inhalte migrieren
- [ ] 4.1 .fodt zu Markdown konvertieren (pandoc als Hilfsmittel)
- [ ] 4.2 Kapitelstruktur in separate Dateien aufteilen
- [ ] 4.3 Tabellen in Markdown-Format anpassen
- [ ] 4.4 Bildverweise aktualisieren
- [ ] 4.5 Interne Links anpassen
- [ ] 4.6 Release Notes separat migrieren

## 5. Stabile Anker implementieren
- [ ] 5.1 Wichtige Abschnitte mit expliziten `{#id}` Ankern versehen
- [ ] 5.2 Konvention für Anker-IDs festlegen (kebab-case)
- [ ] 5.3 Interne Verlinkungen prüfen und korrigieren
- [ ] 5.4 Liste der stabilen Anker dokumentieren

## 6. Navigation konfigurieren
- [ ] 6.1 `nav:` Sektion in mkdocs.yml aufbauen
- [ ] 6.2 Logische Kapitelreihenfolge festlegen
- [ ] 6.3 Navigation testen

## 7. GitHub Actions einrichten
- [ ] 7.1 Workflow-Datei `.github/workflows/docs.yml` erstellen
- [ ] 7.2 Build-Step für MkDocs konfigurieren
- [ ] 7.3 Deploy-Step für GitHub Pages konfigurieren
- [ ] 7.4 Optional: PDF auf eigenen Server kopieren

## 8. GitHub Pages aktivieren
- [ ] 8.1 Repository-Einstellungen für GitHub Pages konfigurieren
- [ ] 8.2 `gh-pages` Branch als Quelle setzen
- [ ] 8.3 Optional: Custom Domain `docs.j-lawyer.org` einrichten

## 9. PDF-Export konfigurieren
- [ ] 9.1 `mkdocs-with-pdf` Plugin installieren und konfigurieren
- [ ] 9.2 PDF-Styling anpassen (Cover, Header, Footer)
- [ ] 9.3 PDF-Ausgabe testen

## 10. Migration abschließen
- [ ] 10.1 Alle Inhalte auf Vollständigkeit prüfen
- [ ] 10.2 Links und Bilder testen
- [ ] 10.3 Suche testen
- [ ] 10.4 PDF-Export prüfen
- [ ] 10.5 Alte .fodt-Dateien archivieren oder entfernen
- [ ] 10.6 README.md aktualisieren
- [ ] 10.7 CLAUDE.md aktualisieren
