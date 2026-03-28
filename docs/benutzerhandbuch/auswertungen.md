# Auswertungen {#auswertungen}

Über die Hauptnavigation am linken Bildschirmrand gelangt man zum Modul „Auswertungen". Hier stehen verschiedene Reporte zur Verfügung, die nach Kategorien gruppiert sind.

## Berechtigungen {#berechtigungen}

Zum Ausführen von Auswertungen sind Berechtigungen notwendig. Diese können in der Nutzerverwaltung gepflegt werden. Es wird unterschieden zwischen:

- **Allgemeine Auswertungen**: Für alle Nutzer mit Auswertungsberechtigung zugänglich
- **Vertrauliche Auswertungen**: Erfordern eine zusätzliche Berechtigung. Vertrauliche Auswertungen können mitarbeiterbezogene oder umsatzbezogene Daten beinhalten.

In der Reportliste sind vertrauliche Auswertungen mit einem Schloss-Icon gekennzeichnet.

## Bedienung {#bedienung}

### Report ausführen

1. Wählen Sie einen Report aus der Übersicht
2. Klicken Sie auf den **Play-Button**, um den Report zu starten
3. Die Ergebnisse werden als Tabelle und/oder Diagramm angezeigt

### Zeitraum filtern

Die meisten Reporte lassen sich nach einem Zeitraum filtern. Über die Kalender-Buttons können Start- und Enddatum angepasst werden. Die Bezeichnung des Datumsbezugs (z.B. „fällig", „erstellt") wird am jeweiligen Report angezeigt. Nach Änderung des Zeitraums kann der Report über den **Aktualisieren-Button** neu geladen werden.

### Ergebnisse

Die Ergebnisse werden in zwei Bereichen dargestellt:

- **Diagramme**: Grafische Darstellung der Daten als Balkendiagramm
- **Tabellen**: Tabellarische Darstellung mit sortierbaren Spalten. Bei Reporte mit Summenzeilen werden diese am Ende der Tabelle angezeigt.

### Daten exportieren

Tabellen können per Klick auf den **Export-Button** (Tabellensymbol) als Tabellendokument exportiert werden. Je nach konfigurierter Textverarbeitung wird eine XLSX-Datei (Microsoft Office) oder ODS-Datei (LibreOffice) erzeugt. Die Datei wird automatisch geöffnet.

### Zur Akte navigieren

Bei Reporte mit Aktenbezug kann per **Rechtsklick** auf eine Tabellenzeile direkt zur zugehörigen Akte navigiert werden (Kontextmenü → „Zur Akte wechseln").

## Verfügbare Reporte {#reporte}

### Finanzen: Rechnungen {#finanzen-rechnungen}

| Report | Beschreibung | Vertraulich |
|--------|-------------|:-----------:|
| **Offene Rechnungen** | Alle offenen Rechnungen, filterbar nach Fälligkeitsdatum | Nein |
| **Fällige Rechnungen** | Alle überfälligen Rechnungen, filterbar nach Fälligkeitsdatum | Nein |
| **Rechnungsentwürfe** | Alle Rechnungen im Entwurfsstatus, filterbar nach Erstellungsdatum | Nein |
| **Akten ohne Rechnung** | Alle Akten ohne umsatzrelevante Rechnungen, filterbar nach Erstellungsdatum der Akte | Nein |
| **Alle Rechnungen / Belege** | Alle Rechnungen und Belege unabhängig von Belegart, Status oder Erstellungsdatum | Nein |

### Finanzen: Zahlungen {#finanzen-zahlungen}

| Report | Beschreibung | Vertraulich |
|--------|-------------|:-----------:|
| **Alle Zahlungen** | Alle Zahlungen unabhängig von Status oder Erstellungsdatum | Nein |

### Finanzen: Controlling {#finanzen-controlling}

| Report | Beschreibung | Vertraulich |
|--------|-------------|:-----------:|
| **Umsatz pro Kunde / Kundin** | Umsätze pro Kunde/Kundin, basierend auf bezahlten Rechnungen, filterbar nach Fälligkeitsdatum | Ja |
| **Aktenkonto – Buchungen** | Alle Buchungen in Aktenkonten in einem bestimmten Zeitraum, filterbar nach Buchungsdatum | Ja |
| **Akten mit nicht ausgeglichenem Fremdgeld** | Akten mit nicht ausgeglichenem Fremdgeld, filterbar nach Erstellungsdatum der Akte | Nein |
| **Ergebnis pro Akte** | Betriebswirtschaftliches Ergebnis pro Akte basierend auf Aktenkonten, filterbar nach Erstellungsdatum der Akte | Ja |

### Zeiterfassung {#zeiterfassung}

| Report | Beschreibung | Vertraulich |
|--------|-------------|:-----------:|
| **Offene Zeiterfassungsprojekte (Übersicht)** | Alle offenen Zeiterfassungsprojekte, sortiert nach letzter Buchung | Nein |
| **Offene Zeiterfassungsprojekte (Buchungen)** | Alle offenen Zeiterfassungsprojekte mit deren Buchungen, gruppiert nach Projekt | Nein |
| **Gebuchte Zeiten pro Mitarbeiter** | Werte aller gebuchten Zeiten, gruppiert nach Person und Monat/Jahr | Ja |
| **Meine gebuchten Zeiten** | Eigene gebuchte Zeiten, gruppiert nach Monat/Jahr | Nein |
| **Mitarbeiterreport** | Aktenaktivitäten einer Person basierend auf der Aktenhistorie, gestaffelt nach Kalendertagen. Der Report dient zur Orientierung und ersetzt keine detaillierte Mitarbeiter-Zeiterfassung. | Ja |

### Unternehmensentwicklung {#unternehmensentwicklung}

| Report | Beschreibung | Vertraulich |
|--------|-------------|:-----------:|
| **Akten pro Monat** | Aktenaufkommen pro Monat für einen ausgewählten Zeitraum (tabellarisch und grafisch) | Ja |
| **Akten pro Jahr** | Aktenaufkommen pro Jahr (tabellarisch und grafisch) | Nein |

### Systemwartung {#systemwartung}

| Report | Beschreibung | Vertraulich |
|--------|-------------|:-----------:|
| **Akten nach Größe / Speicherbelegung** | Die 500 größten Akten nach Speicherbelegung | Nein |
| **Akten ohne Zugriffsbeschränkungen** | Alle Akten, für die keine Zugriffsbeschränkungen konfiguriert sind | Nein |
