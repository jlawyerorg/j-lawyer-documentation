# Kontoauszugimport {#kontoauszugimport}

Der Kontoauszugimport ermöglicht es, Banktransaktionen aus CSV-Dateien zu importieren und direkt mit Akten, Belegen und Zahlungen zu verknüpfen. Dies erleichtert die Buchhaltung erheblich, da Zahlungseingänge automatisch erkannt und zugeordnet werden können.

## Sinn und Zweck {#sinn-und-zweck}

Der Kontoauszugimport bietet folgende Vorteile:

- **Automatische Zuordnung**: Transaktionen werden automatisch den passenden Akten und Belegen zugeordnet
- **Zeitersparnis**: Keine manuelle Suche nach zugehörigen Rechnungen oder Zahlungen
- **Duplikatschutz**: Bereits verarbeitete Transaktionen werden erkannt und nicht doppelt gebucht
- **Flexible Buchungsoptionen**: Zahlungseingänge können als Einnahmen, Auslagen oder Fremdgeld verbucht werden
- **Belegstatus-Aktualisierung**: Rechnungen können direkt als bezahlt markiert werden
- **Überblick vor dem Buchen**: Alle Transaktionen werden als Liste geprüft und angepasst und dann gesammelt gebucht

## Bedienung {#bedienung}

### Import starten {#import-starten}

Der Kontoauszugimport wird über das Menü **Finanzen** gestartet.

1. **CSV-Konfiguration wählen**: Wählen Sie die passende CSV-Konfiguration für Ihre Bank aus der Dropdown-Liste
2. **Kontoauszug laden**: Klicken Sie auf "Kontoauszug laden" und wählen Sie die CSV-Datei Ihrer Bank

### Transaktionen prüfen {#transaktionen-durcharbeiten}

Nach dem Laden der CSV-Datei werden alle Transaktionen des Kontoauszugs in einer Liste angezeigt, ein Eintrag pro Transaktion. Die [automatische Zuordnung](#automatische-zuordnung) läuft im Hintergrund, der Fortschritt wird unten im Fenster angezeigt („Zuordnung x / y“). Die Einträge erscheinen nach und nach, und die Liste kann bereits bedient werden, während die Zuordnung noch läuft.

Jeder Eintrag zeigt in der Kopfzeile:

- Datum, Name und IBAN des Absenders bzw. Empfängers sowie den Betrag
- Buchungsart und Verwendungszweck
- die zugeordnete Akte und in Klammern den Grund der Zuordnung, bspw. „(Rechnungsnummer RE-2026-0042 im Verwendungszweck)“. Der Tooltip der Akte zeigt weitere Angaben zur Akte, u.a. den Anwalt.
- eine Zusammenfassung der vorgesehenen Aktionen, bspw. „Rechnung RE-2026-0042 bezahlt · Aktenkonto: Einnahme 595,00 (RE-2026-0042)“
- ggf. einen Status, bspw. „keine Rechnung, Zahlung oder Akte gefunden“, „Wurde bereits gebucht“, „erledigt“ oder „Fehler: …“

Über das Kontrollkästchen am Anfang des Eintrags wird festgelegt, ob die Aktionen dieser Transaktion beim Buchen ausgeführt werden. Transaktionen mit Zuordnung und vorgeschlagenen Aktionen sind automatisch markiert. Transaktionen ohne Akte lassen sich erst markieren, nachdem eine Akte zugeordnet wurde.

!!! info "Bis zum Buchen wird nichts gespeichert"
    Alle Änderungen in der Liste, auch an Aktenetiketten, sind zunächst nur vorgemerkt. Am Server ändert sich erst etwas, wenn Sie **Alle Buchungen ausführen** wählen. Wird das Fenster geschlossen oder ein neuer Kontoauszug geladen, während noch markierte Buchungen offen sind, erscheint eine Rückfrage.

### Eintrag bearbeiten {#eintrag-bearbeiten}

Über den Button **Aktionen bearbeiten** wird ein Eintrag aufgeklappt. Dort lassen sich die vorgeschlagenen [Aktionen](#verfuegbare-aktionen) anpassen:

- **Akte**: über **Akte suchen und zuordnen** eine andere Akte wählen (siehe [Manuelle Zuordnung](#manuelle-zuordnung))
- **Rechnung als bezahlt markieren**, mit Auswahl der Rechnung
- **Zahlung als ausgeführt markieren**, mit Auswahl der Zahlung
- **Buchung im Aktenkonto erstellen**: Buchungsart, Beleg zur Buchung, Buchungskontakt (aus den Beteiligten der Akte) und Buchungstext
- **Aktenetiketten**: Etiketten der Akte vormerken, die beim Buchen gesetzt bzw. entfernt werden

Die Zusammenfassung in der Kopfzeile wird bei jeder Änderung aktualisiert.

### Abweichende Beträge {#betragsabweichung}

Weicht der Betrag der Transaktion vom Bruttobetrag der zugeordneten bzw. ausgewählten Rechnung ab, wird der Eintrag deutlich gekennzeichnet:

- eine rote Warnzeile, bspw. „Betrag 500,00 weicht vom Rechnungsbetrag ab: Rechnung RE-2026-0042 über 595,00 (Differenz -95,00)“
- ein roter Balken am linken Rand des Eintrags
- in den Details der Rechnungsbetrag mit Differenz in Rot. Passt der Betrag, wird der Rechnungsbetrag grün angezeigt.

So fallen Teilzahlungen oder falsch zugeordnete Rechnungen vor dem Buchen auf.

### Filter und Markierung {#filter}

Über **Anzeigen** lässt sich die Liste einschränken:

| Filter | Angezeigte Transaktionen |
|--------|--------------------------|
| alle Transaktionen | alle Transaktionen des Kontoauszugs |
| zum Buchen markiert | markierte Transaktionen mit Aktionen, die noch nicht ausgeführt wurden |
| ohne Zuordnung | Transaktionen ohne zugeordnete Akte |
| bereits gebucht | Transaktionen, die bereits bei einem früheren Import gebucht wurden (siehe [Duplikaterkennung](#duplikaterkennung)) |
| fehlgeschlagen | Transaktionen, deren Buchung fehlgeschlagen ist |
| erledigt | in diesem Durchgang erfolgreich gebuchte Transaktionen |

Mit **alle markieren** bzw. **keine markieren** werden alle aktuell angezeigten Transaktionen mit Aktionen markiert bzw. die Markierung aufgehoben. Eine Statuszeile fasst den Stand zusammen, bspw. „48 Transaktionen · 31 zum Buchen markiert · 5 bereits gebucht · 12 ohne Zuordnung“.

### Buchungen ausführen {#buchungen-ausfuehren}

Mit **Alle Buchungen ausführen** werden die Aktionen aller markierten Transaktionen verarbeitet:

1. **Prüfung**: Gibt es Abweichungen zwischen Transaktions- und Rechnungsbetrag oder wird dieselbe Rechnung bzw. Zahlung mehrfach als bezahlt bzw. ausgeführt markiert, werden diese Punkte aufgelistet. Sie können dann abbrechen oder trotzdem fortfahren.
2. **Bestätigung**: Eine Rückfrage zeigt, wie viele Rechnungen als bezahlt markiert, Zahlungen als ausgeführt markiert, Aktenkonto-Buchungen erstellt und Akten mit geänderten Etiketten betroffen sind.
3. **Verarbeitung**: Die Transaktionen werden nacheinander gebucht, der Fortschritt wird angezeigt („Buchung x / y“). Schlägt eine Transaktion fehl, etwa weil die Akte zwischenzeitlich gelöscht wurde oder Berechtigungen fehlen, laufen die übrigen Buchungen weiter.
4. **Abschlussbericht**: Zum Schluss wird angezeigt, wie viele Transaktionen erfolgreich gebucht wurden und welche mit welchem Fehler fehlgeschlagen sind.

Erfolgreich gebuchte Transaktionen erhalten den Status **erledigt** und können nicht mehr bearbeitet werden. Fehlgeschlagene Transaktionen bleiben markiert und können nach einer Korrektur erneut ausgeführt werden. Bereits erfolgreich ausgeführte Teilaktionen werden dabei nicht wiederholt.

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

Je nach Zuordnung und Transaktionsrichtung werden folgende Aktionen vorgeschlagen. Sie können im aufgeklappten Eintrag angepasst werden (siehe [Eintrag bearbeiten](#eintrag-bearbeiten)) und werden erst beim [Buchen](#buchungen-ausfuehren) ausgeführt.

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

Zusätzlich können [Aktenetiketten](etiketten.md) zum Setzen oder Entfernen vorgemerkt werden, z.B. um den Zahlungsstatus der Akte zu dokumentieren. Die Etiketten werden erst beim Buchen geändert.

### Manuelle Zuordnung {#manuelle-zuordnung}

Falls die automatische Zuordnung nicht erfolgreich war oder eine andere Akte gewünscht ist, kann über den Button **Akte suchen und zuordnen** manuell eine Akte ausgewählt werden. Nach Auswahl der Akte werden die zugehörigen Belege, Zahlungen und Beteiligten geladen, passende Aktionen vorgeschlagen und der Eintrag zum Buchen markiert. Als Grund der Zuordnung wird „manuell zugeordnet“ angezeigt.

### Duplikaterkennung {#duplikaterkennung}

Das System führt eine Duplikatprüfung durch. Wurde eine Transaktion bereits verarbeitet, erscheint sie ausgegraut mit dem Status „Wurde bereits gebucht“ sowie dem Namen des Nutzers und dem Datum der Verarbeitung, bspw. „Wurde bereits gebucht (mustermann am 03.11.2026 14:12)“.

Solche Transaktionen sind nicht markiert und können weder bearbeitet noch erneut gebucht werden, um versehentliche Doppelbuchungen zu vermeiden. Wird derselbe Kontoauszug erneut geladen, erscheinen alle bereits gebuchten Transaktionen in diesem Zustand.

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
