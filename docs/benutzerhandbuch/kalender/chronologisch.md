# Übersicht {#chronologisch}

Die Übersicht zeigt alle offenen Kalendereinträge (Termine, Wiedervorlagen und Fristen) chronologisch sortiert an – unabhängig davon, zu welcher Akte sie gehören.

## Zugriff auf die Ansicht

Die Ansicht ist über die Hauptnavigation links unter **Kalender** → **Übersicht** erreichbar.

## Darstellungsformen

Die Ansicht bietet drei Reiter:

| Reiter | Beschreibung |
|--------|--------------|
| **Liste** | Tabellarische Übersicht aller Kalendereinträge |
| **Kalenderblatt** | Grafische Kalenderdarstellung mit Tages-, Wochen- und Monatsansicht |
| **suchen** | Aktenübergreifende Suche nach offenen und erledigten Kalendereinträgen (siehe [Kalendersuche](suche.md)) |

!!! tip "Standard-Ansicht merken"
    j-lawyer.org merkt sich, welchen Reiter Sie zuletzt verwendet haben, und öffnet diesen beim nächsten Aufruf automatisch.

## Listenansicht {#listenansicht}

Die Listenansicht zeigt alle Kalendereinträge in einer tabellarischen Übersicht.

### Angezeigte Spalten

| Spalte | Beschreibung |
|--------|--------------|
| **Datum / Zeit** | Fälligkeitsdatum und Uhrzeit des Eintrags |
| **Typ** | Art des Eintrags (Frist, Wiedervorlage, Termin) |
| **Aktenzeichen** | Das Aktenzeichen der zugehörigen Akte |
| **Kurzrubrum** | Das Kurzrubrum der Akte |
| **Grund** | Der Grund des Kalendereintrags |
| **Beschreibung** | Zusätzliche Beschreibung |
| **Anwalt** | Zuständiger Sachbearbeiter der Akte |
| **verantwortlich** | Verantwortlicher für den Kalendereintrag |
| **erstellt von** | Nutzer, der den Kalendereintrag angelegt hat |
| **Kalender** | Name des Kalenders |

### Bedienung der Listenansicht

#### Akte öffnen

- **Doppelklick** auf einen Eintrag öffnet die zugehörige Akte und springt direkt zum ausgewählten Kalendereintrag
- **Rechtsklick** öffnet ein Kontextmenü mit der Option "Akte bearbeiten"

#### Werkzeugleiste

| Symbol | Funktion | Beschreibung |
|--------|----------|--------------|
| Export | LibreOffice-Export | Exportiert die Liste als CSV-Datei |
| Aktualisieren | Daten neu laden | Lädt die Kalendereinträge neu |

Neben den Schaltflächen zeigt eine Statusanzeige den Stand der Daten. Kann die Liste nicht aktualisiert werden, weist die Anzeige darauf hin; j-lawyer.org versucht es dann automatisch weiter.

## Kalenderblatt {#kalenderblatt}

Das Kalenderblatt bietet eine grafische Darstellung der Kalendereinträge in verschiedenen Ansichten.

### Ansichten wechseln

Das Kalenderblatt unterstützt drei verschiedene Ansichten:

| Ansicht | Beschreibung |
|---------|--------------|
| **Tagesansicht** | Detaillierte Ansicht eines einzelnen Tages mit Zeitraster |
| **Wochenansicht** | Übersicht über eine Woche mit allen Tagen nebeneinander |
| **Monatsansicht** | Übersicht über einen Monat mit allen Tagen im Raster |

Die Ansichten können über die Schaltflächen in der oberen Leiste des Kalenderblatts gewechselt werden. Über die Schaltfläche **Kalenderblatt aktualisieren** werden die Einträge neu geladen.

### Navigation im Kalenderblatt

- **Vor / Zurück**: Mit den Pfeiltasten in der Kopfleiste navigieren Sie zum vorherigen oder nächsten Tag / Woche / Monat (je nach aktiver Ansicht)
- **Heute**: Springt zum aktuellen Datum
- **Datum auswählen**: Klicken Sie auf einen Tag in der Monatsansicht, um zur Tagesansicht dieses Tages zu wechseln

### Kalendereinträge filtern

#### Nach Verantwortlichem filtern

Über das Personensymbol in der Werkzeugleiste können Sie die angezeigten Kalendereinträge nach verantwortlichen Nutzern filtern:

1. Klicken Sie auf das Personensymbol
2. Aktivieren oder deaktivieren Sie die gewünschten Nutzer im Dropdown-Menü
3. Die Ansicht wird automatisch aktualisiert

Die Zahl neben dem Symbol zeigt an, wie viele Nutzer aktuell ausgewählt sind.

!!! info "Einträge ohne Verantwortlichen"
    Kalendereinträge, denen kein Verantwortlicher zugewiesen ist, werden unabhängig von der Filtereinstellung immer angezeigt.

#### Nach Kalender filtern

Für jeden Kalender (z.B. "Fristen Anwalt Müller", "Termine Kanzlei") wird automatisch ein farbiger Toggle-Button in der Werkzeugleiste angezeigt. Damit können einzelne Kalender ein- oder ausgeblendet werden:

- **Klick auf den Kalender-Button**: Blendet diesen Kalender aus (Symbol wechselt zu "durchgestrichenem Auge")
- **Erneuter Klick**: Blendet den Kalender wieder ein

Die Farbe des Buttons entspricht der konfigurierten Kalenderfarbe.

#### Erledigte Einträge einblenden {#erledigte-einblenden}

Standardmäßig zeigt das Kalenderblatt nur offene Einträge. Über die Umschaltfläche mit dem Häkchen-Symbol in der Werkzeugleiste können zusätzlich die erledigten Einträge des sichtbaren Zeitraums eingeblendet werden – bspw. um nachzuvollziehen, welche Termine in der vergangenen Woche stattgefunden haben.

Erledigte Einträge werden abgeschwächt und mit einem Häkchen (✓) dargestellt. Beim Blättern in einen anderen Zeitraum werden die erledigten Einträge dieses Zeitraums nachgeladen. Ein erneuter Klick auf die Umschaltfläche blendet sie wieder aus.

!!! info "Hinweis"
    Die Einstellung wird nicht gespeichert – beim nächsten Öffnen zeigt das Kalenderblatt wieder nur offene Einträge.

### Kalendereinträge bearbeiten {#eintraege-bearbeiten}

Im Kalenderblatt können Kalendereinträge direkt bearbeitet werden, ohne die zugehörige Akte öffnen zu müssen.

#### Kontextmenü

Per Rechtsklick auf einen Kalendereintrag öffnet sich ein Kontextmenü mit folgenden Optionen:

| Option | Beschreibung |
|--------|--------------|
| **Akte bearbeiten** | Öffnet die zugehörige Akte |
| **Eintrag bearbeiten** | Öffnet den Dialog zum Bearbeiten des Kalendereintrags (Datum, Zeit, Grund, Beschreibung etc.) |
| **erledigt** | Markiert den Kalendereintrag als erledigt (nach Bestätigung) |

#### Eintrag als erledigt markieren

Beim Markieren als "erledigt" erscheint eine Sicherheitsabfrage. Nach Bestätigung wird der Eintrag im System als erledigt gekennzeichnet und aus dem Kalenderblatt entfernt – bzw. bei [eingeblendeten erledigten Einträgen](#erledigte-einblenden) sofort als erledigt dargestellt.

### Neue Einträge erstellen {#neue-eintraege}

Im Kalenderblatt können neue Termine direkt durch Ziehen erstellt werden:

1. Klicken und halten Sie an der gewünschten Startzeit
2. Ziehen Sie bis zur gewünschten Endzeit
3. Es öffnet sich ein Dialog zur Aktenauswahl
4. Wählen Sie die Akte, zu der der Termin gehören soll
5. Im folgenden Dialog können Sie die Details des neuen Termins eingeben

!!! info "Mehrtägige Termine"
    In der Monatsansicht können mehrtägige Termine durch Ziehen im Kopfbereich (Tagesangabe) der relevanten Tage erstellt werden.

### Darstellung von mehrtägigen Terminen

Termine, die über mehrere Tage gehen, werden im Kalenderblatt auf die einzelnen Tage aufgeteilt dargestellt:

- Am **ersten Tag**: Vom Startzeitpunkt bis Mitternacht
- An **Zwischentagen**: Ganztägig (00:00 bis 23:59)
- Am **letzten Tag**: Von Mitternacht bis zum Endzeitpunkt

## Anwendungsbeispiele

### Tagesplanung

Nutzen Sie die aktenübergreifende Ansicht, um Ihren Arbeitstag zu planen:

1. Öffnen Sie die Ansicht "Chronologisch"
2. Wechseln Sie zum Reiter "Kalenderblatt"
3. Wählen Sie die Tagesansicht
4. Sie sehen alle anstehenden Termine, Fristen und Wiedervorlagen für den Tag

### Wochenübersicht erstellen

Für eine Übersicht der anstehenden Aufgaben der Woche:

1. Öffnen Sie die Ansicht "Chronologisch"
2. Wechseln Sie zum Reiter "Kalenderblatt"
3. Wählen Sie die Wochenansicht
4. Optional: Exportieren Sie die Liste für Besprechungen oder zur Dokumentation

### Termine für bestimmte Mitarbeiter anzeigen

Um nur die Termine eines bestimmten Mitarbeiters zu sehen:

1. Öffnen Sie die Ansicht "Chronologisch"
2. Klicken Sie auf das Personensymbol in der Werkzeugleiste
3. Deaktivieren Sie alle Nutzer außer dem gewünschten Mitarbeiter
4. Das Kalenderblatt zeigt nun nur dessen Einträge
