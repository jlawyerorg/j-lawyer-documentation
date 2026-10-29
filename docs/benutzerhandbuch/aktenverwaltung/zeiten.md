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

### Stundensatz nachträglich ändern

In der Projektübersicht können Stundensätze nachträglich für eine bestimmte Person geändert werden:

1. Öffnen Sie das Projekt per Doppelklick
2. Klicken Sie auf den Button **Stundensatz für Person ändern** (Timer-Icon)
3. Wählen Sie die gewünschte **Person** aus der Liste
4. Geben Sie den neuen **Stundensatz** ein
5. Alle Positionen dieser Person werden aktualisiert und die Gesamtbeträge neu berechnet

Bereits abgerechnete Positionen bleiben unverändert.

### Projekt abschließen

Abgeschlossene Projekte können nicht mehr bearbeitet werden. Der Status kann über das Kontextmenü geändert werden.

## Zeiten erfassen

### Neue Zeit buchen

Das Erfassen von Zeiten ist über das Stoppuhrsymbol innerhalb des Aktenkopfes oder über die Fußzeile der Anwendung möglich. Es öffnet sich der Dialog "Zeit erfassen".

#### Dialogaufbau

Der Dialog ist zweigeteilt:

- **Linke Seite**: Liste der offenen Projekte (mit Suchfeld zum Filtern)
- **Rechte Seite**: Aktive Zeitbuchungen

Jede Zeitbuchung zeigt ihren aktuellen Status durch einen farbigen Rand auf der linken Seite an:

| Farbe | Bedeutung |
|-------|-----------|
| **Grau** | Neu angelegt, noch nicht gestartet |
| **Rot** | Stoppuhr läuft |
| **Grün** | Gestoppt und gespeichert |
| **Blau** | Wird bearbeitet (ungespeicherte Änderungen) |

#### Neue Zeitbuchung erstellen

1. Wählen Sie links ein **Projekt** aus der Liste der offenen Projekte
2. Eine neue Zeitbuchung wird rechts angelegt
3. Wählen Sie einen **Stundensatz** aus der Dropdown-Liste
4. Geben Sie optional eine **Beschreibung** der Tätigkeit ein – oder fügen Sie eine vordefinierte [Tätigkeit](#taetigkeiten) ein

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

#### Beginn und Ende manuell erfassen {#beginn-ende-manuell}

Als dritte Möglichkeit neben Stoppuhr und Eingabe einer Dauer kann eine Zeit direkt mit Beginn und Ende erfasst werden, etwa für einen Termin, der nachträglich eingetragen werden soll:

1. Klicken Sie auf den Button **Zeit manuell mit Beginn und Ende erfassen** (rechts neben dem Eingabefeld für die Dauer). Beginn und Ende werden mit der aktuellen Uhrzeit vorbelegt.
2. Passen Sie [Beginn und Ende](#beginn-ende-bearbeiten) an, wählen Sie den Stundensatz und geben Sie eine Beschreibung ein
3. Klicken Sie auf **Speichern** – erst dann wird die Zeit angelegt

Wird der Button an einer bereits erfassten Zeit verwendet, entsteht ein neuer Eintrag, der Stundensatz, Beschreibung, Bearbeiter und Steuersatz der vorhandenen Zeit übernimmt. Die vorhandene Zeit bleibt unverändert.

!!! info "Hinweis"
    Ein manuell begonnener Eintrag, der nicht gespeichert wurde, wird beim Schließen des Dialogs verworfen. So entstehen keine Einträge mit 0 Minuten.

#### Zeitraum nachträglich anpassen

Nach dem Stoppen und Speichern einer Zeiterfassung sind alle Felder zunächst gesperrt. Um Start- und Endzeit nachträglich anzupassen:

1. Klicken Sie auf den **Bearbeiten-Button** (Stift-Icon) – die Felder werden freigeschaltet
2. Passen Sie [Beginn und/oder Ende](#beginn-ende-bearbeiten) an
3. Klicken Sie auf **Speichern**

#### Beginn und Ende bearbeiten {#beginn-ende-bearbeiten}

Beginn und Ende einer Zeit bestehen jeweils aus einem Datumsfeld mit Kalenderauswahl sowie getrennten Feldern für Stunde und Minute. Stunde und Minute lassen sich mit den Pfeilen hoch- und herunterzählen; wird dabei über 59 Minuten bzw. 23 Uhr hinaus gezählt, werden Stunde bzw. Tag automatisch mitgezählt.

Beim Speichern werden die Angaben geprüft: Ein ungültiges Datum oder ein Ende, das nicht nach dem Beginn liegt, wird gemeldet, und die Zeit wird erst nach der Korrektur gespeichert.

#### Tätigkeiten einfügen {#taetigkeiten}

Für die Beschreibung einer Zeit steht eine Liste vordefinierter Tätigkeiten zur Verfügung (bspw. „Aktenstudium", „Telefonat mit Mandant", „Schriftsatz erstellt"). Eine Tätigkeit lässt sich auf zwei Wegen einfügen:

- über den Button **Tätigkeit in Beschreibung einfügen** rechts neben der Auswahl des Stundensatzes
- per Rechtsklick in das Beschreibungsfeld

Ist die Beschreibung leer, wird sie durch die Tätigkeit ersetzt. Andernfalls wird die Tätigkeit an der Cursorposition eingefügt und – je nach vorangehendem Text – mit einem Semikolon oder Leerzeichen abgetrennt. So lassen sich mehrere Tätigkeiten kombinieren, bspw. „Aktenstudium; Telefonat mit Mandant".

Die Liste der Tätigkeiten wird von Administratoren [in den Einstellungen gepflegt](../zeiterfassung.md#taetigkeiten-verwalten).

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

Die Bearbeitung der Zeiten ist innerhalb der Akte im Tab "Zeiten" möglich, bis zum Zeitpunkt der Abrechnung bleiben Zeiten editierbar. [Beginn und Ende](#beginn-ende-bearbeiten) werden dort wie im Dialog "Zeit erfassen" bearbeitet, und auch dort lassen sich [Tätigkeiten](#taetigkeiten) in die Beschreibung einfügen.

## Zeiten zwischen Projekten transferieren

Zeiten können von einem Projekt in ein anderes verschoben werden: In der Projektübersicht unter "Zeiten" in einer Akte gibt es dazu einen Button direkt am Projekt.
