# Scanner-Integration {#scanner}

## Zentraler Scanordner

j-lawyer bietet eine einfache Möglichkeit, gescannte oder andere bereits vorhandene Dokumente halbautomatisch zu Akten zuzuordnen. Dazu überwacht die Anwendung einen Ordner auf dem Server und zeigt an den Arbeitsplätzen die Dokumente in diesem Ordner an, sowie eine Liste möglicher Aktionen: Dokument löschen, Dokument einer der zuletzt geänderten Akten zuordnen, Dokument einer Akte zuordnen, deren Aktennummer oder Kurzrubrum Ähnlichkeit mit dem Dokumentnamen hat, oder Suchen einer Akte mit anschließender Zuordnung. Heißt das Dokument bspw. „387.pdf", so wird bspw. das Zuordnen zu einer Akte 00387/12 vorgeschlagen; heißt das Dokument „meier.pdf", würde bspw. die Akte „Schulze ./. Meier" vorgeschlagen werden.

Konfigurieren Sie Ihren Scanner so, daß alle Scans automatisch in diesem Ordner abgelegt werden, haben Sie so eine komfortable Möglichkeit, direkt im j-lawyer auf die Dokumente zuzugreifen.

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
