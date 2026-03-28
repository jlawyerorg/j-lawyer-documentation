# Kalender {#kalender-akte}

Der Tab "Kalender" zeigt alle Termine, Wiedervorlagen und Fristen, die zu dieser Akte gehören.

## Eintragstypen

| Typ | Beschreibung |
|-----|--------------|
| **Termin** | Gerichtstermine, Besprechungen, etc. mit konkretem Datum und Uhrzeit |
| **Wiedervorlage** | Erinnerung zur erneuten Bearbeitung der Akte |
| **Frist** | Rechtliche Fristen mit Fälligkeitsdatum |

## Neuen Eintrag erstellen

1. Klicken Sie auf das **+**-Symbol oder den entsprechenden Button
2. Wählen Sie den Eintragstyp (Termin, Wiedervorlage, Frist)
3. Geben Sie Beginn- und Enddatum, Uhrzeit und Grund ein
4. Optional: Beschreibung, Ort (nur bei Terminen) und verantwortliche Person
5. Speichern Sie den Eintrag

### Schnellauswahlen für Datum

Bei der Datumseingabe stehen Schnellauswahlen zur Verfügung:

- **1T**: In einem Tag
- **2T**: In zwei Tagen
- **1W**: In einer Woche
- **2W**: In zwei Wochen
- **3W**: In drei Wochen
- **4W**: In vier Wochen
- **1M**: In einem Monat
- **3M**: In drei Monaten
- **6M**: In sechs Monaten
- **1J**: In einem Jahr

### Automatische Verschiebung bei Feiertagen

Fällt ein gewähltes Datum auf einen Wochenendtag oder Feiertag, erscheint ein Dialog mit folgenden Optionen:

- **Ausgewählten Tag**: Das Datum unverändert übernehmen
- **Nächstmöglichen Werktag**: Auf den nächsten Werktag verschieben
- **Vorhergehenden Werktag**: Auf den vorhergehenden Werktag verschieben
- **Abbrechen**: Datumsauswahl abbrechen

## Kalendereinträge verwalten

### Eintrag bearbeiten

- **Doppelklick** auf einen Eintrag öffnet den Bearbeitungsdialog
- Alternativ: Rechtsklick → **Bearbeiten**

### Eintrag als erledigt markieren

- Aktivieren Sie das Kontrollkästchen in der Spalte "erledigt"
- Oder: Rechtsklick → **Als erledigt markieren**

!!! warning "Warnung bei letztem offenen Eintrag"
    Beim Schließen des letzten offenen Kalendereintrags einer Akte wird eine Warnung angezeigt. Dies dient der Vermeidung von Haftungsrisiken, da Akten ohne offene Kalendereinträge leicht in Vergessenheit geraten können.

### Eintrag löschen

- Rechtsklick auf den Eintrag → **Löschen**
- Bestätigen Sie die Löschung

## Terminkonflikte

Terminkonflikte werden direkt in der Akte angezeigt. Ein Konflikt besteht, wenn zwei Termine zur gleichen Zeit stattfinden.

## Verantwortlichkeit

Jedem Kalendereintrag kann eine verantwortliche Person zugewiesen werden. Standardmäßig wird bei Fristen der Anwalt der Akte als Verantwortlicher eingetragen.

## Kalenderzuordnung

Bei mehreren konfigurierten Kalendern kann beim Erstellen eines Eintrags der Zielkalender ausgewählt werden. Die Zuordnung bestimmt:

- In welchem Kalender der Eintrag erscheint
- Die farbliche Darstellung im Kalenderblatt
- Welche Nutzer den Eintrag sehen können (bei Kalender-Synchronisation)

## Erinnerungen {#erinnerungen}

Für Termine (nicht für Wiedervorlagen oder Fristen) können Erinnerungen konfiguriert werden. Eine Erinnerung benachrichtigt den verantwortlichen Nutzer vor Beginn des Termins direkt in j-lawyer.org.

### Erinnerung konfigurieren

Beim Erstellen oder Bearbeiten eines Termins steht ein Glocken-Button zur Verfügung:

- **Blaue Glocke**: Keine Erinnerung aktiv
- **Grüne Glocke**: Erinnerung aktiv

Per Klick auf die Glocke öffnet sich ein Menü mit folgenden Vorlaufzeiten:

| Option | Vorlaufzeit |
|--------|-------------|
| Bei Beginn | Zum Zeitpunkt des Termins |
| 5 Min. | 5 Minuten vorher |
| 10 Min. | 10 Minuten vorher |
| 15 Min. | 15 Minuten vorher |
| 30 Min. | 30 Minuten vorher |
| 1 Std. | 1 Stunde vorher |
| 2 Std. | 2 Stunden vorher |
| 1 Tag | 1 Tag vorher |
| Keine Erinnerung | Erinnerung deaktivieren |

!!! info "Hinweis"
    Der Glocken-Button ist nur bei Terminen verfügbar. Bei Wiedervorlagen und Fristen ist er deaktiviert.

### Benachrichtigung

Wenn eine Erinnerung fällig wird, erscheint ein Benachrichtigungsfenster am unteren rechten Bildschirmrand. Dieses zeigt:

- **Zusammenfassung** des Termins
- **Beginn** mit Datum und Uhrzeit
- **Ort** (sofern angegeben)
- **Aktenzeichen** als klickbarer Link – ein Klick öffnet die zugehörige Akte

Über den Bestätigen-Button kann jede Erinnerung einzeln quittiert werden. Alternativ werden alle angezeigten Erinnerungen über „Alle bestätigen" auf einmal quittiert.

!!! info "Hinweis"
    Erinnerungen werden nur angezeigt, wenn der j-lawyer Client geöffnet ist. Quittierte Erinnerungen erscheinen in derselben Sitzung nicht erneut, können aber nach einem Neustart des Clients wieder angezeigt werden.

### Erinnerungen und Nextcloud-Synchronisation

Ist eine Nextcloud-Kalender-Synchronisation konfiguriert, werden Erinnerungen automatisch als Kalender-Alarme (VALARM) an Nextcloud übertragen. Dadurch können auch Nextcloud-kompatible Kalender-Apps (z.B. auf dem Smartphone) die Erinnerungen anzeigen.
