# Kontoauszugimport {#kontoauszugimport}

Der Kontoauszugimport ermöglicht es, Banktransaktionen aus CSV-Dateien zu importieren und direkt mit Akten, Belegen und Zahlungen zu verknüpfen. Dies erleichtert die Buchhaltung erheblich, da Zahlungseingänge automatisch erkannt und zugeordnet werden können.

## Sinn und Zweck {#sinn-und-zweck}

Der Kontoauszugimport bietet folgende Vorteile:

- **Automatische Zuordnung**: Transaktionen werden automatisch den passenden Akten und Belegen zugeordnet
- **Zeitersparnis**: Keine manuelle Suche nach zugehörigen Rechnungen oder Zahlungen
- **Duplikatschutz**: Bereits verarbeitete Transaktionen werden erkannt und nicht doppelt gebucht
- **Flexible Buchungsoptionen**: Zahlungseingänge können als Einnahmen, Auslagen oder Fremdgeld verbucht werden
- **Belegstatus-Aktualisierung**: Rechnungen können direkt als bezahlt markiert werden

## Bedienung {#bedienung}

### Import starten {#import-starten}

Der Kontoauszugimport wird über das Menü **Finanzen** gestartet.

1. **CSV-Konfiguration wählen**: Wählen Sie die passende CSV-Konfiguration für Ihre Bank aus der Dropdown-Liste
2. **Kontoauszug laden**: Klicken Sie auf "Kontoauszug laden" und wählen Sie die CSV-Datei Ihrer Bank

### Transaktionen durcharbeiten {#transaktionen-durcharbeiten}

Nach dem Laden der CSV-Datei werden die Transaktionen einzeln angezeigt. Mit den Pfeil-Buttons können Sie zwischen den Transaktionen navigieren.

Für jede Transaktion werden folgende Informationen angezeigt:

- Datum der Buchung
- Name des Absenders/Empfängers
- IBAN
- Verwendungszweck
- Betrag und Währung
- Buchungsart

### Automatische Zuordnung {#automatische-zuordnung}

Das System versucht automatisch, jede Transaktion einer Akte und einem Beleg zuzuordnen. Die Zuordnung erfolgt in folgender Reihenfolge – sobald ein Treffer gefunden wird, werden die nachfolgenden Schritte übersprungen:

#### 1. Suche nach Rechnungsnummer im Verwendungszweck

Das System durchsucht den Verwendungszweck nach Rechnungsnummern offener Belege (Status: offen, Mahnstufen 1-3, neu). Dabei werden zwei Methoden angewandt:

- **Exakte Übereinstimmung**: Die Rechnungsnummer ist vollständig im Verwendungszweck enthalten
- **Ähnlichkeitssuche (Jaro-Winkler)**: Wird keine exakte Übereinstimmung gefunden, wird eine Ähnlichkeitsanalyse durchgeführt. Eine Übereinstimmung von über 90% führt zur Zuordnung. Bei mehreren Treffern wird der mit der höchsten Ähnlichkeit gewählt.

#### 2. Suche nach Zahlungsnummer im Verwendungszweck

Analog zur Rechnungsnummer wird der Verwendungszweck nach Zahlungsnummern offener ausgehender Zahlungen durchsucht (Status: neu, genehmigt, initiiert). Auch hier wird zunächst exakt und dann per Ähnlichkeitssuche geprüft.

#### 3. Suche nach Aktenzeichen im Verwendungszweck

Falls weder eine Rechnungs- noch eine Zahlungsnummer gefunden wird, durchsucht das System den Verwendungszweck nach Aktenzeichen. Die Suche erfolgt ohne Berücksichtigung der Groß-/Kleinschreibung. Längere Aktenzeichen werden bevorzugt geprüft, um Fehlzuordnungen bei kurzen Nummern zu vermeiden.

#### 4. Suche nach IBAN

Falls keiner der vorherigen Schritte erfolgreich war, prüft das System die IBAN des Absenders:

- Die IBAN wird normalisiert (Leerzeichen und Bindestriche entfernt) und ohne Berücksichtigung der Groß-/Kleinschreibung mit den in Kontakten hinterlegten IBANs abgeglichen
- Ist der Kontakt **eindeutig einer aktiven Akte** zugeordnet, wird diese Akte vorgeschlagen
- Bei mehreren aktiven Akten zum selben Kontakt erfolgt keine automatische Zuordnung

!!! info "Hinweis"
    Archivierte Akten werden bei der automatischen Zuordnung nicht berücksichtigt – weder bei der Aktenzeichen-Suche noch bei der IBAN-Zuordnung. Rechnungen und Zahlungen archivierter Akten können jedoch über ihre Beleg- oder Zahlungsnummer zugeordnet werden.

### Verfügbare Aktionen {#verfuegbare-aktionen}

Je nach Zuordnung und Transaktionsrichtung stehen verschiedene Aktionen zur Verfügung:

#### Rechnung als bezahlt markieren

Bei Zahlungseingängen (positive Beträge) kann die zugeordnete Rechnung direkt als bezahlt markiert werden.

#### Zahlung als ausgeführt markieren

Bei Zahlungsausgängen (negative Beträge) kann eine zugehörige ausgehende Zahlung als ausgeführt markiert werden.

#### Buchung im Aktenkonto erstellen

Für jede Transaktion kann eine Buchung im Aktenkonto erstellt werden. Dabei sind folgende Buchungsarten verfügbar:

| Buchungsart | Beschreibung | Verfügbar bei |
|-------------|--------------|---------------|
| Einnahme | Reguläre Einnahme (z.B. Honorar) | Zahlungseingang |
| Ausgabe | Reguläre Ausgabe | Zahlungsausgang |
| Auslage ein | Erstattung einer verauslagten Summe | Zahlungseingang |
| Auslage aus | Verauslagung für den Mandanten | Zahlungsausgang |
| Fremdgeld ein | Eingang von Fremdgeldern | Zahlungseingang |
| Fremdgeld aus | Auszahlung von Fremdgeldern | Zahlungsausgang |

Die Buchung enthält automatisch:

- Datum der Banktransaktion
- Betrag
- Beschreibung (zusammengesetzt aus Name, IBAN und Verwendungszweck)
- Optional: Verknüpfung mit einem Beleg
- Optional: Buchungskontakt (aus den Beteiligten der Akte wählbar)

#### Aktenetiketten setzen

Zusätzlich können direkt Aktenetiketten gesetzt oder entfernt werden, z.B. um den Zahlungsstatus der Akte zu dokumentieren.

### Manuelle Zuordnung {#manuelle-zuordnung}

Falls die automatische Zuordnung nicht erfolgreich war, kann über den Such-Button manuell eine Akte ausgewählt werden. Nach Auswahl der Akte werden alle zugehörigen Belege und Zahlungen geladen.

### Duplikaterkennung {#duplikaterkennung}

Das System führt eine Duplikatprüfung durch. Wurde eine Transaktion bereits verarbeitet, wird dies angezeigt:

- Der Name des Nutzers, der die Transaktion verarbeitet hat
- Das Datum der Verarbeitung

In diesem Fall ist die Aktensuche deaktiviert, um versehentliche Doppelbuchungen zu vermeiden.

## CSV-Konfiguration {#csv-konfiguration}

Da jede Bank ein eigenes CSV-Format verwendet, müssen entsprechende Konfigurationen angelegt werden.

### Konfiguration erstellen {#konfiguration-erstellen}

Die CSV-Konfigurationen werden über **Einstellungen** verwaltet. Eine Konfiguration enthält:

| Einstellung | Beschreibung |
|-------------|--------------|
| Name | Bezeichnung der Konfiguration (z.B. "Sparkasse", "Postbank") |
| Kopfzeilen | Anzahl der zu überspringenden Zeilen am Dateianfang |
| Fußzeilen | Anzahl der zu ignorierenden Zeilen am Dateiende |
| Trennzeichen | Das Feldtrennzeichen (z.B. ";" oder ",") |
| Zahlenformat | Format der Beträge (z.B. "#,##0.00") |
| Locale | Ländereinstellung für Zahlenformate (DE oder EN) |
| Dezimaltrenner | Zeichen für Dezimaltrennung (z.B. "," für deutsch) |
| Tausendertrennzeichen | Zeichen für Tausendergruppierung (optional) |

### Spaltenzuordnung {#spaltenzuordnung}

Für jede Konfiguration muss angegeben werden, in welcher Spalte (beginnend bei 0) sich die jeweilige Information befindet:

| Spalte | Beschreibung | Pflicht |
|--------|--------------|---------|
| Datum | Datum der Buchung | Ja |
| von / an | Name des Absenders/Empfängers | Ja |
| IBAN | IBAN des Absenders/Empfängers | Nein (-1 wenn nicht vorhanden) |
| Verwendungszweck | Buchungstext / Verwendungszweck | Ja |
| Betrag | Transaktionsbetrag | Ja |
| Währung | Währungskürzel | Nein (-1 wenn nicht vorhanden, Standard: EUR) |
| Buchungsart | Art der Buchung | Nein (-1 wenn nicht vorhanden) |

!!! tip "Tipp"
    Für nicht vorhandene Spalten wählen Sie "-1". Das System verwendet dann Standardwerte (z.B. EUR für Währung).

### Beispielkonfiguration {#beispielkonfiguration}

Für eine typische deutsche Bankdatei mit Semikolon-Trennung:

| Einstellung | Wert |
|-------------|------|
| Trennzeichen | ; |
| Kopfzeilen | 1 |
| Fußzeilen | 0 |
| Zahlenformat | #,##0.00 |
| Locale | DE |
| Dezimaltrenner | , |
| Tausendertrennzeichen | . |

## Workflow-Empfehlung {#workflow-empfehlung}

1. **Regelmäßiger Import**: Importieren Sie Kontoauszüge regelmäßig (z.B. wöchentlich)
2. **Belegnummern verwenden**: Tragen Sie bei Rechnungserstellung eine aussagekräftige Belegnummer ein, die im Verwendungszweck erscheint
3. **IBANs pflegen**: Hinterlegen Sie bei wichtigen Kontakten die IBAN für bessere automatische Zuordnung
4. **Etiketten nutzen**: Verwenden Sie Aktenetiketten wie "Zahlung offen" oder "Bezahlt", um den Überblick zu behalten
