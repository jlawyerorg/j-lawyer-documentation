# Aufbau der Programmoberfläche

### Übersicht {#uebersicht}

Der Desktop ist die zentrale Anlaufstelle nach dem Start von j-lawyer.org. Er zeigt auf einen Blick alle wichtigen Informationen zu Ihrer täglichen Arbeit und ermöglicht die schnelle Navigation zu den jeweiligen Bereichen der Anwendung.

Der Desktop gliedert sich in drei Hauptbereiche:

- **Kopfzeile**: Nachrichten- und Statusindikatoren, Datum, Benutzerprofil und Schnellzugriff
- **Hauptbereich**: Drei konfigurierbare Panels — „Zuletzt geändert", „Fällig" und „Nach Etikett"
- **Fußzeile**: Systeminformationen und Statistiken

![Abbildung 4](../images/j-lawyer-org-UserGuide-de-008.png)

### Nachrichten und Status {#nachrichten-status}

Am oberen linken Rand des Desktops zeigen Statusindikatoren den aktuellen Zustand verschiedener Kommunikationskanäle und Systembereiche. Jeder Indikator ist anklickbar und öffnet den jeweiligen Bereich direkt.

| Indikator | Beschreibung |
|-----------|-------------|
| **E-Mails** | Anzahl ungelesener Nachrichten im Posteingang. Klick öffnet den Posteingang. |
| **Scans** | Anzahl eingescannter Dokumente im Scaneingang. Klick öffnet den Scaneingang. |
| **Versandstatus** | Status der Fax-/Briefwarteschlange. Bei fehlgeschlagenen Faxen wird der Indikator rot dargestellt. |
| **beA-Nachrichten** | Anzahl ungelesener Nachrichten des besonderen elektronischen Anwaltspostfachs. Klick öffnet den beA-Posteingang. |
| **Sofortnachrichten** | Unbearbeitete Erwähnungen im Nachrichtencenter. Klick öffnet das Nachrichtencenter. |
| **Update-Status** | Zeigt verfügbare Anwendungsupdates an. |
| **Formular-Plugin-Updates** | Zeigt verfügbare Aktualisierungen für Formular-Plugins an. |
| **Neuigkeiten** | Aktuelle Neuigkeiten rund um j-lawyer.org. |

### Systeminformationen {#systeminformationen}

In der Fußzeile des Desktops werden allgemeine Systeminformationen angezeigt:

| Information | Beschreibung |
|-------------|-------------|
| **Akten** | Gesamtanzahl der vorhandenen Akten |
| **Archivierte Akten** | Anzahl der Akten im Archiv |
| **Adressen** | Anzahl der Adressbucheinträge |
| **Dokumente** | Gesamtanzahl der gespeicherten Dokumente |
| **Fax-/Druckguthaben** | Aktuelles Guthaben in EUR für den Fax- und Briefversand |
| **KI-Assistent** | Status des KI-Assistenten |

### Benutzerprofil und Schnellzugriff {#benutzerprofil}

Am oberen rechten Rand des Desktops befinden sich Benutzerprofil und Schnellzugriffe:

- **Benutzername und -icon**: Zeigt den angemeldeten Nutzer. Klick öffnet den Profildialog, über den Sie z.B. Ihr Profilbild anpassen können.
- **Aktuelles Datum**: Das heutige Datum mit Wochentag wird in der Mitte der Kopfzeile angezeigt.
- **Globale Suche**: Über die Lupe oder die Tastenkombination **Strg+K** (macOS: **Cmd+K**) öffnen Sie die globale Suche, mit der Sie aktenübergreifend nach Inhalten suchen können.
- **Desktop anpassen**: Über den Layout-Button können Sie das Layout des Desktops nach Ihren Wünschen anpassen (siehe Abschnitt [Layout anpassen](#layout-anpassen)).

### Bereich "Zuletzt geändert" {#zuletzt-geaendert}

Dieser Bereich zeigt die zuletzt bearbeiteten Akten in chronologischer Reihenfolge. Für jede Akte werden folgende Informationen dargestellt:

- **Aktenzeichen und Name** der Akte
- **Grund** der letzten Änderung
- **Verantwortlicher Anwalt** (mit Profilbild)
- **Sachbearbeiter** (mit Profilbild)
- **Etiketten** der Akte

Ein Verweilen mit der Maus über einem Eintrag blendet weitere Details ein. Per Klick auf einen Eintrag navigieren Sie direkt zur jeweiligen Akte.

Über die Schaltflächen in der Kopfleiste des Bereichs stehen folgende Funktionen zur Verfügung:

- **Aktualisieren**: Manuelles Neuladen der Anzeige
- **Benutzerfilter**: Filtert die Anzeige nach verantwortlichen Nutzern. Über ein Auswahlmenü können Sie gezielt einzelne Nutzer ein- oder ausblenden.

### Bereich "Fällig" {#faellig}

Der Bereich „Fällig" zeigt fällige und überfällige Fristen, Wiedervorlagen und Termine, gruppiert nach Akten und sortiert nach Fälligkeitsdatum.

#### Farbliche Kennzeichnung {#faellig-farben}

| Formatierung | Bedeutung |
|--------------|-----------|
| schwarze/weiße Beschriftung | heute fällig |
| rote Beschriftung | überfällige Frist |
| orangefarbene Beschriftung | überfällige Wiedervorlage oder überfälliger Termin |

#### Icons nach Ereignistyp {#faellig-icons}

Die Einträge werden nach Ereignistyp gruppiert und durch farbige Abschnittsüberschriften getrennt:

| Icon/Farbe | Bedeutung |
|------------|-----------|
| Rot | Fristen |
| Blau | Termine |
| Grün | Wiedervorlagen |

Innerhalb jeder Gruppe werden die Einträge nach Akte und Tag zusammengefasst. Jede Aktengruppe zeigt Aktenzeichen, Name, Grund und zugeordnete Etiketten.

#### Tabs nach Ereignistyp {#faellig-tabs}

Am unteren Rand des Bereichs befinden sich Tabs zur Filterung:

- **alle**: Zeigt alle Ereignistypen
- Weitere Tabs werden dynamisch pro Ereignistyp (Fristen, Wiedervorlagen, Termine) angezeigt

#### Funktionen {#faellig-funktionen}

Über die Schaltflächen in der Kopfleiste stehen folgende Funktionen zur Verfügung:

- **Aktualisieren**: Manuelles Neuladen der Anzeige
- **Suchfeld**: Echtzeit-Filterung der Einträge (mindestens 2 Zeichen eingeben). Durchsucht werden Aktenzeichen, Aktenname, Grund und verantwortliche Person.
- **Kompaktansicht**: Blendet Etiketten und den Aktengrund in den Gruppenüberschriften ein oder aus, um eine platzsparendere Darstellung zu ermöglichen.
- **Zeitraumfilter**: Über das Kalender-Symbol legen Sie fest, wie viele Tage in die Vergangenheit und in die Zukunft angezeigt werden sollen.
- **Benutzerfilter**: Filtert die Anzeige nach verantwortlichen Nutzern.

#### Aktionen auf Einträgen {#faellig-aktionen}

- **Doppelklick** auf einen Eintrag öffnet die zugehörige Akte.
- **Erledigt-Checkbox**: Markiert eine Frist oder Wiedervorlage als erledigt. Bei Fristen wird eine Sicherheitsabfrage angezeigt. Der Eintrag verschwindet beim nächsten Laden aus dem Arbeitsvorrat.
- **Verschieben**: Über das Kalender-Symbol an einem Eintrag kann der Termin auf ein späteres Datum verschoben werden (nicht verfügbar für Fristen).
- Ein Verweilen mit der Maus über einem Eintrag blendet weitere Informationen ein (Fälligkeitsdatum, Beschreibung, zugehörige Akte, verantwortliche Person).

### Bereich "Nach Etikett" {#nach-etikett}

Dieser Bereich zeigt Akten und Dokumente gefiltert nach Etiketten. So können Sie bestimmte Arbeitsvorgänge im Blick behalten, indem Sie die relevanten Etiketten abonnieren.

Am unteren Rand des Bereichs befinden sich Tabs:

- **alle**: Zeigt alle Einträge unabhängig vom Etikett
- Weitere Tabs werden dynamisch pro Etikett angezeigt

Über die Schaltflächen in der Kopfleiste stehen folgende Filter zur Verfügung:

- **Akten-Etiketten**: Filtert nach Etiketten, die Akten zugeordnet sind
- **Dokument-Etiketten**: Filtert nach Etiketten, die Dokumenten zugeordnet sind
- **Benutzerfilter**: Filtert die Anzeige nach verantwortlichen Nutzern. Ist gar kein Nutzer ausgewählt, werden alle Elemente angezeigt.

!!! info "Hinweis zum Benutzerfilter"
    Ein Element wird angezeigt, wenn:

    - der Anwalt der Akte in der Auswahl enthalten ist, ODER
    - der Sachbearbeiter der Akte in der Auswahl enthalten ist, ODER
    - die Akte weder Anwalt noch Sachbearbeiter zugewiesen hat (beide leer)

### Layout anpassen {#layout-anpassen}

Über den Layout-Button in der Kopfzeile des Desktops können Sie das Erscheinungsbild des Hauptbereichs anpassen. Es stehen vier Layout-Vorlagen zur Auswahl:

| Vorlage | Beschreibung |
|---------|-------------|
| **Klassisch** | „Zuletzt geändert" und „Nach Etikett" links, „Fällig" rechts (2x2-Raster) |
| **Horizontal** | Alle drei Bereiche nebeneinander |
| **Vertikal** | Alle drei Bereiche übereinander gestapelt |
| **Kompakt (Tabs)** | Alle Bereiche als Tabs dargestellt — nur ein Bereich gleichzeitig sichtbar |

Zusätzlich können Sie unter „Bereiche anzeigen" die Sichtbarkeit der einzelnen Panels ein- und ausschalten. Mindestens ein Bereich muss sichtbar bleiben.

!!! warning "Hinweis"
    Die Layout-Einstellungen werden pro Benutzer gespeichert und stehen nach erneutem Anmelden wieder zur Verfügung.

### Automatische Aktualisierung {#automatische-aktualisierung}

Alle Bereiche des Desktops werden automatisch im Hintergrund aktualisiert, sodass Sie stets aktuelle Informationen sehen. Darüber hinaus kann jeder Bereich jederzeit über seinen Aktualisieren-Button manuell neu geladen werden.

Bestimmte Ereignisse lösen zusätzlich eine sofortige Aktualisierung aus — beispielsweise wird der Bereich „Fällig" automatisch aktualisiert, wenn eine Frist oder Wiedervorlage angelegt oder geändert wird.
