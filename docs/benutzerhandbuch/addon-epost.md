# Add-Ons: E-POST (Hybridmail)

### Allgemeines zur E-POST Business API



Die E-POST-Integration ermöglicht den Versand von Schriftstücken mit wenigen Klicks, der Empfänger hingegen erhält eine echte „Papiersendung“. Die Dokumente werden aus der Akte heraus in Druckzentren der Deutschen Post übermittelt, dort gedruckt, kuvertiert, frankiert und verschickt. Die Arbeitsschritte entfallen somit auf Versenderseite.

### E-POST - Einrichtung



Für die Nutzung der E-POST-Integration sind folgende Schritte notwendig:

(1) Registrierung für die Dienstleistung „E-POSTBUSINESS API“: <https://www.deutschepost.de/de/e/epost/geschaeftskunden/partner/business-api.html> Hier ist nicht der Link für Softwarehersteller zu nutzen, sondern jener für Endkunden.

(2) Freischaltung in j-lawyer.org: im Menü „Administration“ – „Nutzer“ – Nutzer wählen – „Sipgate / E-POST“ die „Freischalten“-Funktion nutzen. Die Integration mit den Systemen der Deutschen Post generiert monatliche Kosten bei Softwareherstellern, daher ist die Funktionalität nicht komplett kostenfrei. Jedoch haben wir uns dafür entschieden, kein Abo-Modell einzuführen, sondern einen geringen Einmalbetrag zur Refinanzierung zu nutzen. Für Anwender(innen) der j-lawyer.CLOUD ist der Dienst kostenfrei, es soll jedoch der gleiche Freischaltprozess befolgt werden.

(3) Zugangsdaten aus (1) hinterlegen – ebenfalls in der Nutzerverwaltung

(4) Ggf. Erstellung einer spezifischen Vorlage für die Nutzung mit E-POST. Ob vorhandene Vorlagen „kompatibel“ sind, kann direkt in der Vorlagenverwaltung geprüft werden (Kontextmenü auf eine Vorlage öffnen). Sind im Prüfergebnis rot umrandete Flächen markiert, sollte eine Bearbeitung der Vorlage stattfinden, um diese Bereiche frei zu halten. Beim Druck der Sendung fügt die Deutsche Post dort bspw. QR-Codes ein etc.

### E-POST - Versand {#versand}

Der Versand kann aus der Akte heraus angestoßen werden. In einer Akte werden ein oder mehrere Dokumente markiert und per Rechtsklick der E-POST-Assistent gestartet.

#### Schritt 1: PDF-Konvertierung {#versand-konvertierung}

Alle ausgewählten Dokumente werden automatisch in das PDF-Format konvertiert. Dokumente, die bereits im PDF-Format vorliegen, werden direkt übernommen. Der Konvertierungsstatus wird für jedes Dokument einzeln angezeigt.

#### Schritt 2: Dokumente sortieren {#versand-sortieren}

Die konvertierten PDF-Dokumente können in die gewünschte Reihenfolge gebracht werden:

- **Reihenfolge ändern**: Mit den Pfeiltasten können Dokumente nach oben oder unten verschoben werden
- **Übersicht**: Öffnet eine Drag & Drop-Ansicht zum einfachen Sortieren
- **Umkehren**: Kehrt die Reihenfolge aller Dokumente um
- **Entfernen**: Einzelne PDFs können aus der Liste entfernt werden

Die Gesamtgröße und Seitenzahl werden angezeigt. Die maximale Versandgröße beträgt **20 MB**.

#### Schritt 3: Layout prüfen {#versand-layout}

Das Dokument wird an die E-POST-Schnittstelle übertragen und auf Layoutfehler geprüft. Folgende Optionen stehen zur Verfügung:

**Druckoptionen:**

| Option | Beschreibung |
|--------|--------------|
| Vorderseite | Einseitiger Druck (Simplex) |
| Vorder- und Rückseite | Beidseitiger Druck (Duplex) - Standard |
| farbig | Farbdruck |
| schwarz/weiß | Schwarz-Weiß-Druck - Standard |

**Deckblatt:**

- **Deckblatt generieren**: Erzeugt automatisch ein Deckblatt, das alle Layoutanforderungen der Deutschen Post erfüllt. Die Prüfung erfolgt mit Testdaten für die Empfängeradresse.

**Prüfergebnis:**

Das Prüfergebnis wird als Vorschau angezeigt. Rot markierte Bereiche kennzeichnen Verletzungen der Layout-Anforderungen. Diese Bereiche müssen für den Druck frei bleiben (z.B. für QR-Codes der Deutschen Post).

Optional kann das Prüfergebnis per E-Mail zugestellt werden.

#### Schritt 4: Empfänger und Absender {#versand-adressen}

Hier werden die Adressdaten für Empfänger und Absender eingegeben bzw. aus der Akte übernommen:

**Empfänger:**

- Bis zu 5 Adresszeilen
- PLZ und Ort
- Land (optional, für internationalen Versand)

**Absender:**

- Absenderzeile
- Straße
- PLZ und Ort

#### Schritt 5: Versandoptionen {#versand-optionen}

**Einschreiben-Optionen:**

- Standardbrief (kein Einschreiben)
- Einschreiben
- Einschreiben Einwurf
- Einschreiben Rückschein

#### Schritt 6: Versand {#versand-absenden}

Das Dokument wird an die E-POST-Schnittstelle übertragen. Der Versandstatus wird im Assistenten angezeigt.

Nach Versand ist der Status der Sendung jederzeit im Modul **Brief / Fax** in der Hauptnavigation nachzuvollziehen.

### E-POST - Sendungsstatus {#sendungsstatus}

Der Sendungsstatus aller E-POST-Sendungen kann im Modul **Brief / Fax** in der Hauptnavigation eingesehen werden. Das Modul zeigt sowohl E-POST- als auch Fax-Sendungen in einer gemeinsamen Übersicht.

#### Übersichtstabelle {#sendungsstatus-tabelle}

Die Tabelle zeigt alle Sendungen mit folgenden Informationen:

| Spalte | Beschreibung |
|--------|--------------|
| Gesendet | Datum und Uhrzeit des Versands |
| von | Nutzer, der die Sendung veranlasst hat |
| an | Empfängeradresse |
| Datei | Name des versendeten Dokuments |
| aktueller Status | Aktueller Bearbeitungsstand |
| Akte | Verknüpfte Akte (Aktenzeichen und Name) |

Die Liste wird automatisch alle 30 Sekunden aktualisiert.

#### Detailbereich {#sendungsstatus-details}

Bei Auswahl einer Sendung werden im Detailbereich weitere Informationen angezeigt:

- **Status**: Aktueller Status mit Ampel-Anzeige
  - Grün: Erfolgreich zugestellt
  - Gelb: In Bearbeitung
  - Rot: Fehler aufgetreten
- **Statusdetails**: Detaillierte Beschreibung des aktuellen Status
- **Sendungs-ID**: Eindeutige Kennung der Sendung
- **Sendedatum**: Datum, Uhrzeit und Absender
- **Empfänger**: Vollständige Empfängeradresse
- **Akte**: Verknüpfte Akte

#### Verfügbare Aktionen {#sendungsstatus-aktionen}

| Aktion | Beschreibung |
|--------|--------------|
| Aktualisieren | Liste manuell neu laden |
| Alle auswählen | Alle Einträge in der Liste selektieren |
| Bestätigen | Statuseintrag aus der Liste entfernen (nach Bestätigungsdialog) |
| Bericht speichern | E-POST-Bericht als Dokument in der verknüpften Akte speichern |
| Zur Akte | Direkt zur verknüpften Akte navigieren |
| Bericht anzeigen | Detaillierten E-POST-Sendungsstatus in einem Dialog anzeigen |

#### Dialog "Bericht anzeigen" {#sendungsstatus-bericht}

Der Button **Bericht anzeigen** ist nur für E-POST-Sendungen verfügbar und öffnet einen Dialog mit detaillierten Sendungsinformationen:

**Allgemeine Informationen:**

| Feld | Beschreibung |
|------|--------------|
| Dateiname | Name des versendeten Dokuments |
| letzter Status | Aktueller Bearbeitungsstatus der Sendung |
| Anzahl Seiten | Seitenzahl des versendeten Dokuments |
| Sendungsnummer | Eindeutige ID der E-POST-Sendung |
| Sendungsart | Art der Sendung (Standardbrief, Einschreiben etc.) |
| Empfänger | Vollständige Empfängeradresse |
| Gesendet von Nutzer | Nutzer, der den Versand veranlasst hat |
| Akte | Verknüpftes Aktenzeichen |

**Zeitstempel:**

| Feld | Beschreibung |
|------|--------------|
| erstellt | Zeitpunkt der Erstellung in j-lawyer.org |
| Verarbeitungs-Zeitpunkt | Zeitpunkt der Verarbeitung durch E-POST |
| Einlieferungs-Zeitpunkt in das Druckzentrum | Zeitpunkt der Übergabe an das Druckzentrum |
| Verarbeitungs-Rückmeldung des Druckzentrums | Zeitpunkt der Bestätigung durch das Druckzentrum |

**Details zum Einschreiben** (nur bei Einschreiben-Sendungen):

Bei Einschreiben werden zusätzlich angezeigt:

- **Sendungsnummer**: Die offizielle Sendungsnummer der Deutschen Post
- **letzter Status**: Aktueller Zustellstatus mit Datum, z.B.:
  - "Die Sendung wurde eingeliefert."
  - "Die Sendung befindet sich in der Zustellung."
  - "Die Sendung wurde zugestellt."
  - "Der Empfänger konnte nicht angetroffen werden und wurde vom Zusteller benachrichtigt."
  - "Die Sendung geht an den Absender zurück."
- **Sendungsverfolgung**: Link zur Sendungsverfolgung auf deutschepost.de
