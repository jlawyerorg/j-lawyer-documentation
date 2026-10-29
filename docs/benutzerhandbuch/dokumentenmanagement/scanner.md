# Scanner-Integration {#scanner}

## Zentraler Scanordner

j-lawyer bietet eine einfache Möglichkeit, gescannte oder andere bereits vorhandene Dokumente halbautomatisch zu Akten zuzuordnen. Dazu überwacht die Anwendung einen Ordner auf dem Server und zeigt an den Arbeitsplätzen die Dokumente in diesem Ordner an, sowie eine Liste möglicher Aktionen: Dokument löschen, Dokument einer Akte zuordnen oder Suchen einer Akte mit anschließender Zuordnung.

### Aktenvorschläge {#aktenvorschlaege}

Beim Auswählen eines Dokuments im Scaneingang werden automatisch passende Akten vorgeschlagen. Die Vorschläge werden in folgender Reihenfolge ermittelt:

1. **Textbasierte Suche im Dokumentinhalt**: Der Inhalt des gescannten Dokuments wird per Texterkennung analysiert. Der erkannte Text wird nach eigenen Aktenzeichen und nach Fremdaktenzeichen (Aktenzeichen von Beteiligten) durchsucht. Werden Treffer gefunden, werden die zugehörigen Akten vorgeschlagen.
2. **Dateinamenbasierte Suche**: Der Dateiname wird mit Aktenzeichen und Kurzrubren abgeglichen. Heißt das Dokument bspw. „387.pdf", so wird das Zuordnen zu einer Akte 00387/12 vorgeschlagen; heißt das Dokument „meier.pdf", würde bspw. die Akte „Schulze ./. Meier" vorgeschlagen.
3. **Zuletzt geänderte Akten**: Werden keine textbasierten oder dateinamenbasierten Treffer gefunden, werden die zuletzt geänderten Akten als Vorschläge angeboten.

Konfigurieren Sie Ihren Scanner so, daß alle Scans automatisch in diesem Ordner abgelegt werden, haben Sie so eine komfortable Möglichkeit, direkt im j-lawyer auf die Dokumente zuzugreifen.

Beim Zuordnen eines Dokuments zu einer Akte greift die [Etiketten-Automatik](../etiketten.md#etiketten-automatik): Anhand des Dateinamens können Dokument-Etiketten automatisch vergeben werden, etwa um den unbearbeiteten Posteingang zu kennzeichnen.

Um diese Funktionalität zu nutzen, bearbeiten Sie die Einstellung direkt im j-lawyer Client unter „Einstellungen" – „Modul ‚Dokumente'" – „Scannerintegration", bspw. für Linux:

```
/home/<Nutzer>/<Verzeichnis>
```

(Nutzer und Verzeichnis entsprechend ersetzen, bspw. `/home/j-lawyer/j-lawyer-server/scans`)

Oder für Windows:

```
<Laufwerk>:/<Verzeichnis>
```

(Laufwerk und Verzeichnis entsprechend ersetzen, bspw. `C:/j-lawyer-server/scans`)

Im „Scans"-Dialog im j-lawyer Client klicken Sie dann auf das gewünschte Dokument (Doppelklick öffnet es), und klicken Sie doppelt auf einen Aktionsvorschlag um ihn auszuführen.

### Neue Akte aus einem Scan anlegen {#akte-anlegen}

Gehört ein gescanntes Dokument zu einem neuen Mandat, kann über die Aktion **neue Akte erstellen** (Tooltip „neue Akte aus diesem Scan anlegen") direkt eine Akte angelegt werden. Es startet derselbe Assistent wie im [E-Mail-Posteingang](../email.md#akte-anlegen): Kopfdaten der Akte, Beteiligte mit Rolle und Zeichen – aus dem Adressbuch oder per Assistent Ingo aus dem erkannten Text des Dokuments extrahiert (**Weitere Beteiligte aus Dokument extrahieren**) – und optional eine Wiedervorlage. Das Feld „wegen" wird mit dem Dateinamen des Scans vorbelegt.

## Lokaler Scanordner

Zusätzlich zu einem zentralen Scanordner lässt sich an jedem Arbeitsplatz ein Verzeichnis überwachen. Die Einstellung ist direkt im Scaneingang zu aktivieren. Die Einstellung wird für den Arbeitsplatz gespeichert. Wechselt der Nutzer an ein anderes Gerät, ist dort die Konfiguration eines anderen Ordners auf diesem Gerät möglich.

Das Verhalten des lokalen Scanordners ist wie folgt:

- das Verzeichnis wird zyklisch auf neue Dokumente überwacht
- alle Dokumente in diesem Ordner werden anschließend in den zentralen Scanordner transferiert
- und aus dem lokalen Verzeichnis gelöscht

Somit sind verschiedene Anwendungsszenarien abbildbar, bspw. ein Arbeiten aller Mitarbeiter im Home Office, bei gleichzeitiger zentraler Abarbeitung der Dokumente durch eine definierte Person.

## Automatische Texterkennung / OCR {#ocr}

Dokumente im zentralen Scaneingang können automatisch eine Texterkennung durchlaufen.

Für die OCR-Funktionalität wird ein externes Programm aufgerufen. Der Aufruf kann unter Einstellungen - Dokumente - Scannerintegration konfiguriert werden. Für Linux-basierte Server kann bspw. "ocrmypdf" installiert und dann mittels folgendem Aufruf genutzt werden:

```bash
/usr/bin/ocrmypdf --skip-text DATEIEIN DATEIAUS
```

Die beiden letzten Parameter müssen zwingend im Aufruf enthalten sein, auch wenn eine andere OCR-Software genutzt wird. j-lawyer.org wird die Platzhalter bei Aufruf ersetzen.

- `DATEIEIN` ist der volle Pfad zu einer Datei, für welche die Texterkennung ausgeführt werden soll
- `DATEIAUS` ist der volle Pfad zur Ergebnisdatei / zu erstellenden Datei

Der Texterkennungsstatus wird im Scaneingang in der Spalte „OCR" angezeigt:

| Status | Bedeutung |
|--------|-----------|
| gelb | OCR läuft |
| grün | OCR ist erfolgreich abgeschlossen |
| rot | OCR nicht möglich, fehlgeschlagen, oder nicht konfiguriert |

Ist der Status rot, so kann per Klick im Aktionsmenü erneut eine Texterkennung für das Dokument angefordert werden (bspw. weil zum Zeitpunkt der Texterkennung eine fehlende Konfiguration bestand).

## Dropscan-Integration {#dropscan}

[Dropscan](https://www.dropscan.de) ist ein digitaler Briefkasten-Dienst: Physische Post wird an eine Dropscan-Adresse gesendet, dort empfangen und auf Anforderung digitalisiert. j-lawyer.org integriert sich mit Dropscan, sodass eingehende Post direkt aus dem Scaneingang heraus digitalisiert und Akten zugeordnet werden kann.

### Einrichtung

Die Dropscan-Integration wird pro Nutzer in der Nutzerverwaltung konfiguriert:

1. Öffnen Sie die Nutzerverwaltung und wählen Sie den gewünschten Nutzer aus
2. Wechseln Sie zum Tab „Sipgate / E-POST / Dropscan"
3. Geben Sie den persönlichen Dropscan-API-Token in das Token-Feld ein
4. Klicken Sie auf „Test / Scanboxen ermitteln"
5. Bei erfolgreicher Verbindung werden die verfügbaren Scanboxen mit Nummer und ID angezeigt. Die IDs aller Scanboxen werden zugleich in das Feld „Scanboxen (komma-separiert)" eingetragen.
6. Speichern Sie die Einstellungen. Änderungen in diesem Tab werden erst nach einem Neustart des Clients wirksam.

!!! info "Hinweis"
    Jeder Nutzer konfiguriert seinen eigenen API-Token. Der Token wird verschlüsselt in der Datenbank gespeichert.

#### Zugriff auf einzelne Scanboxen beschränken {#dropscan-scanboxen}

Sind über einen Dropscan-Zugang mehrere Scanboxen erreichbar – bspw. für verschiedene Standorte oder Anwälte –, kann je Nutzer festgelegt werden, welche davon er sieht. Dazu werden im Feld **Scanboxen (komma-separiert)** die IDs der freigegebenen Scanboxen eingetragen, bspw. `12345,12346`.

- **Feld leer**: Der Nutzer sieht alle Scanboxen seines Dropscan-Zugangs.
- **IDs eingetragen**: Der Nutzer sieht im Scaneingang nur Sendungen dieser Scanboxen. Andere Scanboxen erscheinen weder im Scanbox-Filter noch in der Sendungsliste.

!!! warning "Test überschreibt die Auswahl"
    „Test / Scanboxen ermitteln" trägt stets **alle** Scanboxen in das Feld ein und überschreibt eine bestehende Einschränkung. Nach einem Test die nicht freizugebenden IDs wieder entfernen, bevor gespeichert wird.

### Scaneingang: Dropscan-Bereich

Im Scaneingang steht ein eigener Bereich für Dropscan-Sendungen zur Verfügung. Dieser ist in drei Bereiche gegliedert:

**Filter und Aktualisierung**

- **Scanbox-Filter:** Auswahl zwischen „Alle" und einzelnen Scanboxen
- **Status-Filter:** Einschränkung auf einen bestimmten Status (Alle, Empfangen, Gescannt, Scan angefordert, Vernichtet, Weitergeleitet)
- **Aktualisieren:** Manuelle Aktualisierung der Sendungsliste
- **Nach Zuordnung vernichten:** Ist diese Option aktiviert, wird die physische Sendung bei Dropscan automatisch nach dem Import in eine Akte zur Vernichtung freigegeben

**Sendungsliste und Vorschau**

Die Sendungsliste zeigt alle Sendungen in einer Tabelle mit folgenden Spalten:

| Spalte | Inhalt |
|--------|--------|
| Scanbox | Nummer der Scanbox |
| Datum | Eingangsdatum |
| Status | Aktueller Bearbeitungsstatus |
| Zustellweg | Art des Eingangs (Briefeingang, Weiterleitung oder Upload) |

Unterhalb der Tabelle wird eine Vorschau angezeigt: Bei noch nicht gescannten Sendungen ein Bild des Umschlags, bei bereits gescannten Sendungen das PDF-Dokument. Über die Aktionsbuttons „Scannen" und „Vernichten" können Aktionen für die ausgewählte Sendung ausgelöst werden.

**Aktenzuordnung**

Im rechten Bereich werden Vorschläge für passende Akten angezeigt. Die Vorschläge basieren auf dem per OCR erkannten Text der gescannten Dokumente – dabei werden Aktenzeichen und Kurzrubren abgeglichen. Zusätzlich werden die zuletzt geänderten Akten als Vorschläge angeboten. Per Klick auf einen Vorschlag werden die Dokumente der Sendung in die gewählte Akte importiert.

### Typischer Arbeitsablauf

1. Post geht bei Dropscan ein – die Sendung erscheint im Scaneingang mit Status „Empfangen"
2. Wählen Sie die Sendung aus und klicken Sie auf „Scannen", um die Digitalisierung anzufordern – Status wechselt auf „Scan angefordert"
3. Dropscan digitalisiert die Sendung – Status wechselt auf „Gescannt"
4. Wählen Sie die gescannte Sendung aus: In der Vorschau wird das PDF angezeigt, rechts erscheinen Vorschläge für passende Akten
5. Klicken Sie auf den passenden Aktenvorschlag – die Dokumente werden heruntergeladen und über den Import-Dialog in die Akte übernommen
6. Ist die Option „nach Zuordnung vernichten" aktiviert, wird die physische Sendung bei Dropscan automatisch zur Vernichtung freigegeben

!!! warning "Achtung"
    Die Vernichtung einer Sendung bei Dropscan ist unwiderruflich. Stellen Sie sicher, dass die Dokumente korrekt importiert wurden, bevor Sie eine Sendung vernichten.

### Status-Übersicht

| Status | Bedeutung |
|--------|-----------|
| Empfangen | Sendung ist bei Dropscan eingegangen |
| Scan angefordert | Digitalisierung wurde angefordert und wird verarbeitet |
| Gescannt | Dokument wurde digitalisiert und steht als PDF bereit |
| Vernichtung angefordert | Vernichtung der physischen Sendung wurde angefordert |
| Vernichtet | Sendung wurde physisch vernichtet |
| Weiterleitung angefordert | Physische Weiterleitung der Sendung wurde angefordert |
| Weitergeleitet | Sendung wurde physisch weitergeleitet |
