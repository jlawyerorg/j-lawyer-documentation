# Dokumente {#dokumente}

Der Tab "Dokumente" zeigt alle Dateien, die zur Akte gehören.

## Dokumente in Ordnern organisieren {#ordner}

Grundsätzlich werden alle Dateien einer Akte in einem "Dokumente"-Ordner gespeichert. Soll eine detailliertere Strukturierung genutzt werden, so können:

- Ordner direkt in der Akte hinzugefügt, umbenannt und gelöscht werden
- Vorgefertigte Ordnerstrukturen zu einer Akte hinzugefügt werden

### Ordnervorlagen

Die sogenannten Ordnervorlagen können unter **Einstellungen** → **Modul 'Akten'** → **Dokumentordner** hinterlegt werden.

Innerhalb einer Akte ist das Anwenden der Ordnervorlagen über das Zahnradsymbol direkt über der Ordneranzeige möglich. Dabei werden niemals vorhandene Ordner entfernt, es werden stets nur Ordner hinzugefügt, welche in der Ordnervorlage enthalten, in der Akte jedoch noch nicht vorhanden sind.

!!! tip "Mehrere Ordnervorlagen kombinieren"
    Es ist leicht möglich, mehrere Ordnervorlagen nacheinander auf eine Akte anzuwenden: bspw. einmal eine Vorlage "Finanzen" mit den Ordnern "Rechnungen" und "Angebote", gefolgt von der Übernahme sachgebietsspezifischer Ordnervorlagen.

## Dokumentvorschau {#vorschau}

Innerhalb der Akte wird durch einen einfachen Klick auf das Dokument eine Vorschau angezeigt.

### Unterstützte Formate

| Vorschautyp | Formate |
|-------------|---------|
| **Direkte Anzeige** (Inhalt und Layout) | GIF, JPG, PDF, PNG, TIF |
| **Textanzeige** (Inhalt als Textextrakt) | Alle Dokumente mit Textinformationen |
| **Keine Vorschau** | Alle weiteren Binärformate |

Ein **Doppelklick** öffnet das Dokument im entsprechenden Editor.

![Abbildung 3](../../images/j-lawyer-org-UserGuide-de-009.png)

### Vorschau-Tabs

Die Dokumentvorschau bietet mehrere Tabs:

- **Vorschau**: Grafische Darstellung des Dokuments
- **Text**: Extrahierter Text des Dokuments (nützlich zum schnellen Kopieren in die Zwischenablage)

### Navigation in der Vorschau

- **Blättern**: Mit den Pfeiltasten (links/rechts) können Sie zwischen Seiten blättern
- **Zoomen**: Mit dem Mausrad oder den Zoom-Schaltflächen

## Dokumente hinzufügen

Dokumente können auf verschiedene Wegen zur Akte hinzugefügt werden:

- **Drag & Drop**: Dateien vom Desktop oder aus dem Dateimanager in die Dokumentenliste ziehen
- **Aus Vorlage erstellen**: Über den "Erstellen"-Button ein Dokument aus einer Vorlage generieren
- **Scannen**: Über die Scanner-Integration
- **E-Mail-Anhänge**: Beim Speichern von E-Mails zur Akte

## Dokumentetiketten

Dokumente können – ähnlich wie Akten – mit Etiketten versehen werden. Dies ermöglicht eine zusätzliche Kategorisierung und Filterung.

### Etiketten für mehrere Dokumente setzen

Wählen Sie mehrere Dokumente aus und setzen Sie über das Kontextmenü die Etiketten für alle ausgewählten Dokumente gleichzeitig.

## Volltextsuche innerhalb der Akte

Über das Suchfeld oberhalb der Dokumentenliste kann innerhalb aller Dokumente der Akte gesucht werden. Treffer werden hervorgehoben und die Dokumentenliste wird entsprechend gefiltert.

## PDF-Stapelexport {#stapelexport}

Oberhalb der Dokumentenliste befindet sich ein Button für den PDF-Stapelexport. Mit dieser Funktion können mehrere Dokumente zu einem einzigen PDF-Dokument zusammengeführt werden.

### Vorgehensweise

1. **Dokumente auswählen**: Markieren Sie die gewünschten Dokumente in der Dokumentenliste
2. **Stapelexport starten**: Klicken Sie auf den Export-Button oberhalb der Dokumentenliste

### Schritt 1: PDF-Konvertierung

Im ersten Schritt werden alle ausgewählten Dokumente automatisch in das PDF-Format konvertiert. Der Fortschritt wird angezeigt. Dokumente, die nicht konvertiert werden können (z.B. unbekannte Formate), werden mit einem Warnsymbol gekennzeichnet.

### Schritt 2: Dokumente sortieren

In diesem Schritt können Sie:

- **Reihenfolge festlegen**: Ordnen Sie die Dokumente per Drag & Drop in der gewünschten Reihenfolge an
- **Übersicht nutzen**: Der Button "Übersicht" öffnet eine Kachelansicht für einfacheres Sortieren
- **Reihenfolge umkehren**: Der Button "Umkehren" kehrt die aktuelle Reihenfolge um
- **Inhaltsverzeichnis**: Option zum Hinzufügen eines automatisch generierten Inhaltsverzeichnisses mit Seitenangaben und Lesezeichen
- **Seitenzahlen**: Option zum Hinzufügen von Seitenzahlen im Format "Seite X / Y"

Die Gesamtzahl der Seiten und die Dateigröße werden angezeigt.

### Schritt 3: Zusammenführen und Speichern

Im letzten Schritt werden die Dokumente zusammengeführt:

- Eine **Vorschau** des fertigen PDFs wird angezeigt
- Das Ergebnis kann **lokal gespeichert** werden (Verzeichnisauswahl)
- Das Ergebnis kann **zur Akte gespeichert** werden

!!! tip "Metadaten im PDF"
    Das exportierte PDF enthält automatisch Metadaten wie Aktenzeichen, Kurzrubrum, Sachgebiet, Anwalt und Erstellungsdatum. Diese erscheinen auch auf der ersten Seite, wenn ein Inhaltsverzeichnis erstellt wird.

!!! info "Verschlüsselte PDFs"
    Verschlüsselte oder fehlerhafte PDFs können nicht zusammengeführt werden. Diese werden übersprungen und am Ende des Vorgangs aufgelistet.

## Kontextmenü {#kontextmenue}

Per Rechtsklick auf ein oder mehrere Dokumente öffnet sich das Kontextmenü mit zahlreichen Aktionen.

### Grundlegende Aktionen

| Aktion | Beschreibung |
|--------|--------------|
| **öffnen** | Öffnet das Dokument im Standardprogramm |
| **öffnen mit...** | Öffnet das Dokument mit einem wählbaren Programm |
| **umbenennen** | Ändert den Dateinamen des Dokuments |
| **Erstellungsdatum anpassen** | Ändert das Erstellungsdatum des Dokuments |
| **löschen** | Verschiebt das Dokument in den Papierkorb |

### Kopieren und Verschieben

| Aktion | Beschreibung |
|--------|--------------|
| **in Zwischenablage kopieren** | Kopiert die ausgewählten Dateien in die Zwischenablage |
| **lokal speichern** | Speichert die ausgewählten Dokumente auf dem lokalen Rechner |
| **duplizieren** | Erstellt eine Kopie des Dokuments in der gleichen Akte |
| **in andere Akte kopieren** | Kopiert das Dokument in eine andere Akte |
| **in andere Akte verschieben** | Verschiebt das Dokument in eine andere Akte |

### Organisation und Kennzeichnung

| Aktion | Beschreibung |
|--------|--------------|
| **farblich hervorheben** | Hebt das Dokument farblich hervor (zwei Farben verfügbar) |
| **Favoritendokument an/aus** | Markiert das Dokument als Favorit für schnellen Zugriff |
| **Nachricht senden** | Sendet eine interne Nachricht zu diesem Dokument an Kollegen |

### PDF und Konvertierung {#pdf-konvertierung}

Das Untermenü **PDF und Konvertierung** enthält Funktionen zur PDF-Bearbeitung:

| Aktion | Beschreibung |
|--------|--------------|
| **Texterkennung (OCR)** | Führt eine Texterkennung für die ausgewählten Dokumente durch |
| **als PDF zusammenführen** | Exportiert alle ausgewählten Dokumente in ein einziges PDF |
| **PDF aufteilen** | Teilt ein PDF anhand von Seitenzahlen auf |
| **als PDF lokal speichern** | Speichert das Dokument als PDF auf dem lokalen Rechner |
| **PDF Seiten umsortieren** | Ermöglicht das Umsortieren der Seiten innerhalb eines PDFs |
| **PDF verkleinern** | Reduziert die Dateigröße eines PDFs |
| **verschlüsseltes PDF exportieren** | Exportiert das Dokument als passwortgeschütztes PDF |
| **ablegen als ...** | Speichert das Dokument in einem anderen Format zur Akte |
| **PDF schwärzen** | Schwärzt vertrauliche Inhalte in einem PDF |
| **PDF stempeln** | Fügt einen Stempel (z.B. "Kopie", Datum) zum PDF hinzu |

!!! info "Hinweis"
    Weitere Details zu PDF-Funktionen finden Sie unter [PDF-Funktionen](../dokumentenmanagement/pdf.md).

### Versand per E-Mail

| Aktion | Beschreibung |
|--------|--------------|
| **senden** | Sendet das Dokument per E-Mail über den integrierten Mailclient |
| **als PDF senden** | Konvertiert das Dokument zu PDF und sendet es per E-Mail |
| **im externen Mailprogramm öffnen** | Öffnet eine neue E-Mail im externen Mailprogramm mit dem Dokument als Anhang |

### Versand per beA

| Aktion | Beschreibung |
|--------|--------------|
| **senden** | Sendet das Dokument über das besondere elektronische Anwaltspostfach (beA) |
| **als PDF senden** | Konvertiert das Dokument zu PDF und sendet es per beA |

!!! info "Hinweis"
    Weitere Details zur beA-Integration finden Sie unter [beA (Anwaltspostfach)](../addon-bea.md).

### Weitere Versandoptionen

| Aktion | Beschreibung |
|--------|--------------|
| **als Fax senden** | Sendet das Dokument als Fax (erfordert Sipgate-Integration) |
| **drucken (Standarddrucker)** | Druckt das Dokument direkt auf dem Standarddrucker |
| **per E-POST versenden** | Sendet das Dokument als Hybridbrief über E-POST |
| **Freigabe senden** | Teilt das Dokument über Nextcloud mit externen Empfängern |

!!! info "Hinweis"
    Für E-POST siehe [Add-On: E-POST](../addon-epost.md), für Nextcloud siehe [Add-On: Nextcloud](../addon-nextcloud.md).

### KI-Assistent

| Aktion | Beschreibung |
|--------|--------------|
| **Assistent Ingo** | Öffnet den KI-Assistenten zur Analyse des Dokuments |

!!! info "Hinweis"
    Weitere Details zum KI-Assistenten finden Sie unter [KI-Assistent](../ki-assistent.md).

### Vorlagen

| Aktion | Beschreibung |
|--------|--------------|
| **als Vorlage speichern** | Speichert das Dokument als Vorlage für die spätere Wiederverwendung |
| **als PDF zur Akte speichern** | Konvertiert das Dokument zu PDF und speichert es zusätzlich zur Akte |
