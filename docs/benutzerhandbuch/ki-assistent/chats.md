# Gespeicherte Chats {#gespeicherte-chats}

Chats mit Assistent Ingo werden automatisch gespeichert – nach jeder Anfrage inklusive aller Antworten und Werkzeugaufrufe. Ein Chat kann so jederzeit nachgelesen und später fortgesetzt werden, auch nachdem das Chat-Fenster geschlossen wurde.

## Chats mit und ohne Aktenbezug {#aktenbezug}

| | Chat mit Aktenbezug | Chat ohne Aktenbezug |
|---|---|---|
| **Entsteht** | wenn der Chat aus einer Akte heraus gestartet wird (bspw. aus der Akte, aus einem Dokument oder einem [Falldatenblatt](../aktenverwaltung/falldaten.md#falldaten-ingo-chat)) | bspw. vom Desktop oder aus dem Modul **AI** |
| **Zu finden** | in der Akte im Tab **AI** | im Navigationsbereich unter **Recherche** → **AI** |
| **Sichtbar für** | alle Nutzer mit Zugriff auf die Akte | nur den eigenen Nutzer |
| **Gelöscht** | zusammen mit der Akte | zusammen mit dem Nutzer |

!!! info "Gemeinsame Nutzung"
    Chats mit Aktenbezug sind Teil der Akte. Kolleginnen und Kollegen mit Zugriff auf die Akte können sie lesen und fortsetzen. Bei Aktenchats zeigt ein Icon in der Liste, wer den Chat gestartet hat (Name per Tooltip).

## Ansicht der Chats {#ansicht}

Der Tab **AI** in der Akte und das Modul **AI** sind gleich aufgebaut:

- **Links** die Liste der Chats, sortiert nach letzter Aktivität. Je Chat werden Titel, Zeitpunkt der letzten Aktivität und Wortanzahl angezeigt.
- **Rechts** der Verlauf des ausgewählten Chats.

Folgende Aktionen stehen über die Schaltflächen und per Rechtsklick zur Verfügung:

| Aktion | Beschreibung |
|--------|--------------|
| **Fortsetzen** | Öffnet den Chat im Chat-Fenster und setzt ihn fort (auch per Doppelklick) |
| **Umbenennen** | Ändert den Titel. Bleibt das Feld leer, wird der Titel wieder aus der ersten Nachricht gebildet. |
| **Akte zuordnen** | Ordnet einen Chat ohne Aktenbezug nachträglich einer Akte zu. Der Chat ist danach für alle Nutzer mit Zugriff auf die Akte sichtbar. Die Zuordnung kann nicht rückgängig gemacht werden. |
| **Löschen** | Löscht die ausgewählten Chats (Mehrfachauswahl möglich) |
| **Aktualisieren** | Lädt die Liste neu |

Im Modul **AI** kann über **neuen Chat beginnen** im Kopfbereich direkt ein neuer Chat ohne Aktenbezug gestartet werden. Angeboten werden dabei Prompts mit [agentenfähigem Modell](agenten.md).

!!! note "Berechtigungen"
    Umbenennen und Löschen von Chats mit Aktenbezug erfordert Schreibrechte für Akten.

## Chats fortsetzen {#fortsetzen}

Beim Fortsetzen werden Modell, System Prompt und Einstellungen des ursprünglichen Chats verwendet – auch dann, wenn der zugrundeliegende eigene Prompt inzwischen umbenannt oder gelöscht wurde.

Wird derselbe Chat gleichzeitig an zwei Stellen fortgesetzt (bspw. von zwei Kolleginnen), wird nichts überschrieben: Der später gespeicherte Verlauf wird als neuer Chat abgelegt, worauf ein Hinweis aufmerksam macht.

!!! tip "Länge im Blick behalten"
    Das Chat-Fenster zeigt die Wortanzahl des gesamten Chats. Bei jeder weiteren Anfrage wird der komplette bisherige Verlauf erneut an das Modell gesendet. Lange Chats verbrauchen daher mehr Tokens und können die Grenzen des Modells erreichen – für ein neues Thema ist ein neuer Chat oft die bessere Wahl.
