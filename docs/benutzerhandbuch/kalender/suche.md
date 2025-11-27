# Kalendersuche {#kalendersuche}

Die Kalendersuche ermöglicht es, Wiedervorlagen, Fristen und Termine aktenübergreifend zu suchen und zu filtern.

## Zugriff auf die Ansicht

Die Ansicht ist über die Hauptnavigation links unter **Kalender** → **Suchen** erreichbar.

## Suchkriterien

Die Suche bietet verschiedene Filteroptionen, die kombiniert werden können:

### Nach Datum filtern

| Feld | Beschreibung |
|------|--------------|
| **von** | Startdatum des Suchzeitraums |
| **bis** | Enddatum des Suchzeitraums |

Lassen Sie beide Felder leer, um alle Einträge unabhängig vom Datum zu suchen.

### Nach Typ filtern

| Option | Beschreibung |
|--------|--------------|
| **alle** | Zeigt alle Eintragstypen |
| **Fristen** | Zeigt nur Fristen |
| **Wiedervorlagen** | Zeigt nur Wiedervorlagen |
| **Termine** | Zeigt nur Termine |

### Nach Status filtern

| Option | Beschreibung |
|--------|--------------|
| **alle** | Zeigt sowohl offene als auch erledigte Einträge |
| **erledigt** | Zeigt nur erledigte Einträge |
| **offen** | Zeigt nur offene (nicht erledigte) Einträge (Standardeinstellung) |

### Volltextsuche

Im Feld **enthält** kann ein Suchbegriff eingegeben werden. Die Suche durchsucht:

- Aktenzeichen
- Kurzrubrum
- Grund
- Beschreibung

Drücken Sie **Enter** (↵), um die Suche zu starten.

### Filter zurücksetzen

Über den **Zurücksetzen**-Button (⌫) können alle Suchkriterien auf die Standardwerte zurückgesetzt werden.

## Suchergebnisse

Die Ergebnistabelle zeigt folgende Spalten:

| Spalte | Beschreibung |
|--------|--------------|
| **Datum / Zeit** | Datum und Uhrzeit des Kalendereintrags |
| **Typ** | Art des Eintrags (Frist, Wiedervorlage, Termin) |
| **Aktenzeichen** | Das Aktenzeichen der zugehörigen Akte |
| **Kurzrubrum** | Das Kurzrubrum der Akte |
| **Grund** | Der Grund des Kalendereintrags |
| **Beschreibung** | Zusätzliche Beschreibung |
| **erledigt** | Status des Eintrags (erledigt/offen) |
| **Anwalt** | Zuständiger Sachbearbeiter der Akte |
| **verantwortlich** | Verantwortlicher für den Kalendereintrag |
| **Kalender** | Name des Kalenders |

## Bedienung

### Akte öffnen

- **Doppelklick** auf eine Zeile öffnet die zugehörige Akte
- **Rechtsklick** öffnet ein Kontextmenü mit der Option "Akte bearbeiten"

### Werkzeugleiste

| Symbol | Funktion | Beschreibung |
|--------|----------|--------------|
| Export | LibreOffice-Export | Exportiert die Ergebnisliste als CSV-Datei |
| Drucken | Liste drucken | Druckt die aktuelle Ergebnisliste |
| Aktualisieren | Suche wiederholen | Führt die Suche mit den aktuellen Kriterien erneut aus |

## Anwendungsbeispiele

### Alle offenen Fristen dieser Woche

1. Setzen Sie **von** auf den aktuellen Tag
2. Setzen Sie **bis** auf das Ende der Woche
3. Wählen Sie bei Typ: **Fristen**
4. Wählen Sie bei Status: **offen**
5. Klicken Sie auf **Aktualisieren**

### Alle Wiedervorlagen eines bestimmten Mandanten

1. Wählen Sie bei Typ: **Wiedervorlagen**
2. Geben Sie im Feld **enthält** den Namen des Mandanten ein
3. Drücken Sie **Enter**

### Erledigte Termine im letzten Monat

1. Setzen Sie **von** auf den ersten Tag des letzten Monats
2. Setzen Sie **bis** auf den letzten Tag des letzten Monats
3. Wählen Sie bei Typ: **Termine**
4. Wählen Sie bei Status: **erledigt**
5. Klicken Sie auf **Aktualisieren**
