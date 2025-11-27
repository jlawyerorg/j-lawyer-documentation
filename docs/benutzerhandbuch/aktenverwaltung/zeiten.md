# Zeiten {#zeiten}

Der Tab "Zeiten" dient der Zeiterfassung innerhalb einer Akte.

## Tab-Farbkodierung

Der Tab "Zeiten" zeigt durch seine Farbe den Status der Zeiterfassung an:

| Farbe | Bedeutung |
|-------|-----------|
| **Schwarz** | Keine Zeiterfassung aktiv |
| **Grün** | Mindestens ein offenes Projekt vorhanden |
| **Rot** | Ein Projekt hat das Zeitlimit überschritten |

## Projekte

Die Zeiterfassung erfolgt projektbasiert. Ein Projekt definiert einen Rahmen für die Zeiterfassung, z.B. "Außergerichtliche Beratung" oder "Gerichtsverfahren".

### Neues Projekt erstellen

1. Klicken Sie auf **Neues Projekt**
2. Geben Sie eine Bezeichnung ein
3. Optional: Definieren Sie ein Zeitlimit
4. Optional: Erstellen Sie eine Wiedervorlage zur Abrechnung

### Projekt bearbeiten

Per Doppelklick oder Rechtsklick → **Bearbeiten** können die Projekteinstellungen angepasst werden.

### Projekt abschließen

Abgeschlossene Projekte können nicht mehr bearbeitet werden. Der Status kann über das Kontextmenü geändert werden.

## Zeiten erfassen

### Neue Zeit buchen

Das Erfassen von Zeiten ist über das Stoppuhrsymbol innerhalb des Aktenkopfes oder über die Fußzeile der Anwendung möglich. Es öffnet sich der Dialog "Zeit erfassen".

#### Dialogaufbau

Der Dialog ist zweigeteilt:

- **Linke Seite**: Liste der offenen Projekte (mit Suchfeld zum Filtern)
- **Rechte Seite**: Aktive Zeitbuchungen

#### Neue Zeitbuchung erstellen

1. Wählen Sie links ein **Projekt** aus der Liste der offenen Projekte
2. Eine neue Zeitbuchung wird rechts angelegt
3. Wählen Sie eine **Positionsvorlage** aus der Dropdown-Liste (z.B. Stundensatz, Tätigkeitsart)
4. Geben Sie optional eine **Beschreibung** der Tätigkeit ein

#### Stoppuhr-Funktion

- Klicken Sie auf den **Play-Button**, um die Zeitmessung zu starten
- Die laufende Zeit wird in Echtzeit angezeigt (rot markiert)
- Klicken Sie auf den **Stop-Button**, um die Zeitmessung zu beenden
- Start- und Endzeit werden automatisch erfasst

!!! info "Parallele Zeiterfassungen"
    Wenn bereits eine Zeiterfassung für dieselbe Akte läuft, werden Sie gefragt, ob diese gestoppt werden soll. Optional kann auch eine Warnung bei parallelen Erfassungen in verschiedenen Akten aktiviert werden.

#### Manuelle Zeiteingabe

Alternativ zur Stoppuhr können Sie Zeit manuell eingeben:

1. Geben Sie die Dauer im Feld neben "oder" ein
2. Bestätigen Sie mit **Enter**

Die manuelle Eingabe unterstützt folgende Formate:

- `2h45m` – 2 Stunden 45 Minuten
- `2h` – 2 Stunden
- `45m` – 45 Minuten
- Reine Zahleneingaben werden je nach Servereinstellung als Minuten oder Stunden interpretiert

#### Zeitraum nachträglich anpassen

Nach dem Stoppen einer Zeiterfassung können Start- und Endzeit manuell angepasst werden (Format: TT.MM.JJ HH:MM). Speichern nicht vergessen!

#### Dialog-Buttons

| Button | Beschreibung |
|--------|--------------|
| **Alle stoppen und schliessen** | Stoppt alle laufenden Zeiterfassungen und schließt den Dialog |
| **Schliessen** | Speichert alle Einträge und schließt den Dialog |

### Zeiteingabe-Format

Die Dauer kann in verschiedenen Formaten eingegeben werden:

- `2h30m` – 2 Stunden 30 Minuten
- `2h` – 2 Stunden (Minutenangabe ist optional)
- `90m` – 90 Minuten
- `0m` – 0 Minuten (z.B. um festzuhalten, dass etwas getan wurde, oder um die Zeit später nachzutragen)

### Zeit bearbeiten

Die Bearbeitung der Zeiten ist innerhalb der Akte im Tab "Zeiten" möglich, bis zum Zeitpunkt der Abrechnung bleiben Zeiten editierbar.

## Zeiten zwischen Projekten transferieren

Zeiten können von einem Projekt in ein anderes verschoben werden: In der Projektübersicht unter "Zeiten" in einer Akte gibt es dazu einen Button direkt am Projekt.
