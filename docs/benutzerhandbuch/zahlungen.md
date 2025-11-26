# Ausgehende Zahlungen

Mit der Funktion für ausgehende Zahlungen können Überweisungen innerhalb einer Akte vorbereitet und als SEPA-XML-Datei exportiert werden. Diese Datei kann dann im Onlinebanking importiert werden, um die Überweisungen auszuführen.

## Übersicht {#uebersicht}

Das Zahlungsmodul ermöglicht:

- Erfassung von Zahlungen direkt in der Akte
- Zentrale Verwaltung aller Zahlungen über alle Akten hinweg
- Export als SEPA-XML für den Import im Onlinebanking
- Statusverfolgung von der Erstellung bis zur Ausführung

## Zahlungen in der Akte erstellen {#zahlung-erstellen}

### Zugang zur Zahlungsverwaltung in der Akte

Öffnen Sie eine Akte und wechseln Sie zum Tab **Finanzen**. Dort finden Sie den Bereich für ausgehende Zahlungen.

### Neue Zahlung anlegen

Klicken Sie auf den Plus-Button, um eine neue Zahlung anzulegen. Es öffnet sich ein Dialog zur Eingabe der Zahlungsdaten.

### Zahlungsfelder

| Feld | Beschreibung |
|------|--------------|
| Zahlungsnummer | Wird automatisch vergeben |
| Bezeichnung | Name/Titel der Zahlung (z.B. "Honorar Sachverständiger") |
| Beschreibung | Optionale ausführliche Beschreibung |
| Verwendungszweck | Text, der auf dem Kontoauszug erscheint |
| Betrag | Zahlbetrag |
| Währung | Standardmäßig EUR |
| Empfänger | Aus den Aktenbeteiligten auswählen |
| Sender | Benutzer der Kanzleisoftware mit hinterlegter Bankverbindung |
| Zahlungsart | SEPA-Überweisung oder Sonstige |
| Zieldatum | Geplantes Ausführungsdatum |
| Status | Aktueller Bearbeitungsstand |

### Empfänger auswählen

Der Empfänger wird aus den Aktenbeteiligten ausgewählt. Damit eine SEPA-Überweisung möglich ist, muss beim Empfänger eine gültige IBAN hinterlegt sein. Die IBAN kann in der Adressverwaltung gepflegt werden.

### Sender auswählen

Als Sender stehen die Benutzer der Kanzleisoftware zur Verfügung, bei denen IBAN und BIC hinterlegt sind. Die Bankverbindung wird in den Benutzereinstellungen unter **Administration** → **Nutzerverwaltung** beim jeweiligen Benutzer konfiguriert. Nur Benutzer mit vollständig hinterlegter Bankverbindung (IBAN und BIC) können als Sender für SEPA-Überweisungen ausgewählt werden.

## Status einer Zahlung {#status}

Jede Zahlung durchläuft verschiedene Status:

| Status | Bedeutung |
|--------|-----------|
| Entwurf | Zahlung ist in Bearbeitung, kann noch geändert werden |
| freigegeben | Zahlung ist bereit für den SEPA-Export |
| veranlasst | SEPA-XML wurde exportiert, Zahlung wurde an die Bank übergeben |
| ausgeführt | Zahlung wurde von der Bank durchgeführt |
| fehlgeschlagen | Zahlung konnte nicht durchgeführt werden |
| storniert | Zahlung wurde abgebrochen |

Eine Zahlung muss auf den Status **freigegeben** gesetzt werden, bevor sie für den SEPA-Export berücksichtigt wird.

## Zentrale Zahlungsübersicht {#zahlungsuebersicht}

### Zugang

Über das Menü **Finanzen** → **Zahlungen verwalten** öffnet sich die zentrale Übersicht aller Zahlungen.

### Funktionen

In der zentralen Übersicht können Sie:

- Alle Zahlungen aus allen Akten einsehen
- Nach Status filtern (z.B. nur freigegebene Zahlungen)
- Zahlungen bearbeiten oder deren Status ändern
- Den SEPA-Export durchführen

## SEPA-Export {#sepa-export}

### Voraussetzungen

Für einen erfolgreichen SEPA-Export müssen folgende Bedingungen erfüllt sein:

- Die Zahlung hat den Status **freigegeben**
- Beim Empfänger ist eine gültige IBAN hinterlegt
- Beim Sender (Benutzer) sind IBAN und BIC hinterlegt
- Die Zahlungsart ist **SEPA-Überweisung**

### Validierung

Vor dem Export können Sie die Zahlungen prüfen lassen. Die Validierung überprüft:

- Gültigkeit der IBAN von Sender und Empfänger
- Vollständigkeit der Pflichtfelder
- Korrekte Formatierung des Verwendungszwecks

### Export durchführen

1. Öffnen Sie die zentrale Zahlungsübersicht
2. Filtern Sie nach Status **freigegeben**
3. Klicken Sie auf **Prüfen**, um die Zahlungen zu validieren
4. Nach erfolgreicher Prüfung klicken Sie auf **SEPA-Datei(en) generieren**
5. Wählen Sie einen Speicherort für die XML-Datei(en)

### Gruppierung nach Bankkonto

Falls mehrere Senderprofile mit unterschiedlichen Bankverbindungen verwendet werden, wird für jedes Bankkonto eine separate SEPA-XML-Datei erstellt. So können die Dateien im jeweiligen Onlinebanking importiert werden.

### Nach dem Export

Nach erfolgreichem Export wechselt der Status der betroffenen Zahlungen automatisch auf **veranlasst**. Sobald die Überweisung im Onlinebanking ausgeführt wurde, kann der Status manuell auf **ausgeführt** gesetzt werden.

Alternativ kann der Status automatisch auf **ausgeführt** gesetzt werden, wenn ein Kontoauszug importiert wird, in dem die Zahlung erkannt wird. Dies erfordert die Nutzung der Kontoauszugs-Import-Funktion.

## Import im Onlinebanking {#onlinebanking-import}

Die exportierte SEPA-XML-Datei entspricht dem Format **SEPA Credit Transfer (pain.001)** und kann in den meisten Onlinebanking-Portalen importiert werden:

1. Melden Sie sich im Onlinebanking an
2. Navigieren Sie zum Bereich für SEPA-Überweisungen oder Datei-Import
3. Wählen Sie die exportierte XML-Datei aus
4. Prüfen und bestätigen Sie die Überweisungen
5. Autorisieren Sie die Transaktion (z.B. per TAN)

Die genaue Vorgehensweise kann je nach Bank variieren.
