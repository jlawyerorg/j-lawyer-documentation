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
