# Postvorlagen (E-Mail, beA)

Postvorlagen ermöglichen das automatische Erstellen von E-Mails und beA-Nachrichten auf Basis vordefinierter Texte. Sie können Betreff, Empfänger und Nachrichteninhalt vorbelegen und mit Platzhaltern personalisieren.

## Vorlagen verwalten

Die Vorlagenverwaltung erreichen Sie über die Navigationsleiste ganz unten unter **Vorlagen** > **Post: Vorlagen**.

### Übersicht der Oberfläche

Die Vorlagenverwaltung ist in drei Bereiche unterteilt:

- **Vorlagenliste (oben):** Zeigt alle verfügbaren Vorlagen an
- **Vorlageneditor (unten links):** Bearbeitung der ausgewählten Vorlage
- **Platzhalter-Panel (unten rechts):** Einfügen von Platzhaltern

### Aktionen für Vorlagen

Unterhalb der Vorlagenliste stehen folgende Aktionen zur Verfügung:

| Schaltfläche | Beschreibung |
|--------------|--------------|
| **Neu** | Erstellt eine neue, leere Vorlage |
| **Duplizieren** | Kopiert die ausgewählte Vorlage unter einem neuen Namen |
| **Umbenennen** | Ändert den Namen der ausgewählten Vorlage |
| **Speichern** | Speichert Änderungen an der ausgewählten Vorlage |
| **Löschen** | Entfernt die ausgewählte Vorlage |
| **Aktualisieren** | Lädt die Vorlagenliste neu |

## Vorlage erstellen und bearbeiten

Wählen Sie eine Vorlage aus der Liste aus oder erstellen Sie eine neue Vorlage mit **Neu**. Der Vorlageneditor zeigt dann die folgenden Felder:

### Empfängerfelder

- **An:** Standard-Empfänger der Nachricht
- **CC:** Kopie-Empfänger
- **BCC:** Blindkopie-Empfänger

In den Empfängerfeldern können ebenfalls Platzhalter verwendet werden, um Empfänger dynamisch aus Aktenbeteiligten zu beziehen.

### Betreff

Das Betreff-Feld enthält den vordefinierten Betreff der E-Mail oder beA-Nachricht. Platzhalter werden beim Anwenden der Vorlage automatisch ersetzt.

### Format

Wählen Sie das gewünschte Nachrichtenformat:

- **text/plain:** Reiner Text ohne Formatierung
- **text/html:** HTML-formatierter Text mit Formatierungsmöglichkeiten

Der Editor passt sich dem gewählten Format an:

- Bei **text/plain** wird ein einfacher Texteditor angezeigt
- Bei **text/html** wird ein HTML-Editor mit Formatierungsoptionen angezeigt

### Inhalt

Im Inhaltsbereich geben Sie den Nachrichtentext ein. Je nach gewähltem Format steht Ihnen ein entsprechender Editor zur Verfügung.

## Platzhalter verwenden

Platzhalter ermöglichen das automatische Einfügen von aktenspezifischen Daten in die Vorlage.

### Platzhalter-Panel

Das Platzhalter-Panel auf der rechten Seite enthält:

1. **Zielauswahl:** Dropdown-Menü mit den Optionen "in Betreff" oder "in Inhalt"
2. **Platzhalter-Liste:** Alle verfügbaren Platzhalter
3. **Einfügen-Button:** Fügt die ausgewählten Platzhalter an der Cursorposition ein

### Platzhalter einfügen

1. Positionieren Sie den Cursor im Betreff- oder Inhaltsfeld
2. Wählen Sie im Dropdown das Ziel ("in Betreff" oder "in Inhalt")
3. Wählen Sie einen oder mehrere Platzhalter aus der Liste
4. Klicken Sie auf den Einfügen-Button (Pfeil-Symbol)

### Spezielle Platzhalter

| Platzhalter | Beschreibung |
|-------------|--------------|
| `{{CURSOR}}` | Positioniert den Cursor nach Anwendung der Vorlage an dieser Stelle. Nur für text/plain-Vorlagen verfügbar. |
| `{{CLOUD_LINK}}` | Wird durch einen Cloud-Link ersetzt, falls Cloud-Freigaben verwendet werden. |

## Vorlagen beim Verfassen anwenden

Beim Verfassen einer E-Mail oder beA-Nachricht können Sie eine Vorlage anwenden.

### Vorlagenauswahl

Im Bereich **Vorlagedaten** des E-Mail-Dialogs finden Sie:

- **Suchfeld:** Filtern Sie die Vorlagenliste durch Eingabe eines Suchbegriffs
- **Vorlagen-Dropdown:** Wählen Sie die gewünschte Vorlage aus

### Anwendung der Vorlage

Sobald Sie eine Vorlage auswählen:

1. Der Betreff wird aus der Vorlage übernommen
2. Die Empfängerfelder (An, CC, BCC) werden gefüllt, falls in der Vorlage hinterlegt
3. Der Nachrichteninhalt wird eingefügt
4. Alle Platzhalter werden durch die aktuellen Aktendaten ersetzt
5. Das Nachrichtenformat wird entsprechend der Vorlage angepasst
6. Bei text/plain-Vorlagen mit `{{CURSOR}}` wird der Cursor automatisch positioniert

### Letzte Vorlage merken

Die zuletzt verwendete Vorlage wird automatisch gespeichert. Beim nächsten Verfassen einer neuen E-Mail (nicht beim Antworten oder Weiterleiten) wird diese Vorlage vorausgewählt.

### Vorlagen bei Antworten und Weiterleitungen

Beim Antworten auf oder Weiterleiten von E-Mails wird die Vorlagenauswahl nicht automatisch angewendet, um den zitierten Originalinhalt nicht zu überschreiben. Sie können jedoch manuell eine Vorlage auswählen, die dann mit dem bestehenden Inhalt kombiniert wird.
