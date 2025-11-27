# Aktenverwaltung

Die Aktenverwaltung ist das zentrale Modul in j-lawyer.org. Hier werden alle Informationen zu einem Fall erfasst und verwaltet.

## Übersicht der Funktionen

| Bereich | Beschreibung |
|---------|--------------|
| [Allgemeine Daten](allgemeine-daten.md) | Aktenzeichen, Kurzrubrum, Sachgebiet, Etiketten, Notizen, Archivierung |
| [Beteiligte](beteiligte.md) | Mandanten, Gegner und weitere Beteiligte einer Akte |
| [Dokumente](dokumente.md) | Dokumentenverwaltung, Ordnerstruktur, Vorschau |
| [Kalender](kalender-akte.md) | Termine, Wiedervorlagen und Fristen zur Akte |
| [Zeiten](zeiten.md) | Zeiterfassung und Projekte |
| [Eigene Felder](eigene-felder.md) | Benutzerdefinierte Felder |
| [Falldaten](falldaten.md) | Strukturierte Falldatenblätter |
| [Historie](historie.md) | Änderungsprotokoll der Akte |

## Akten suchen {#suchen}

Im Navigationsbaum am linken Bildschirmrand unter "suchen" können Sie Akten über eine Schnellsuche finden. Durchsucht werden:

- Aktenzeichen
- Kurzrubrum
- wegen
- eigene Felder (alle)

Zusätzlich ist eine Einschränkung über Etiketten möglich.

Voreingestellt ist eine Suche ohne archivierte Akten – soll das Archiv mit durchsucht werden, so ist die Option "Archivsuche" zu aktivieren.

## Aktenanlage {#anlegen}

Eine Aktenanlage ist im linken Navigationsbereich unter **Akten** → **neu** möglich. Es ist sinnvoll, vorab zu prüfen ob alle Beteiligten in der Adressverwaltung existieren. Innerhalb der Akte unter dem Reiter "Beteiligte" ist ggf. auch eine Schnellerfassung noch nicht vorhandener Kontakte möglich. In diesem Fall sollten die Adressdaten nach Schnellerfassung weiter verfeinert werden, der Arbeitsfluss wird so jedoch nicht unterbrochen.

## Aktenzeichen {#aktenzeichen}

j-lawyer vergibt automatisch Aktenzeichen im Format „fünfstellige lfd. Nummer + / + zweistellige Jahreszahl", also bspw. 00123/12. Für Umsteiger kann es hilfreich sein, das „Start-Aktenzeichen" einstellen zu können.

Über Menü **Einstellungen** → **Akten** → **Aktenzeichen-Schema** kann definiert werden, wie Aktenzeichen automatisch gebildet werden.

Es sind folgende Werte nutzbar:

| Zeichen | Bedeutung |
|---------|-----------|
| C | Zufälliger Buchstabe |
| R | Zufallsziffer |
| N | Unabhängig laufende Nummer |
| n | Innerhalb anderer Kriterien laufende Nummer |
| Y/YY/YYYY | Jahr (1-, 2- oder 4-stellig) |
| M/MM | Monat (1- oder 2-stellig) |
| D/DD | Tag (1- oder 2-stellig) |

### Beispiele für Aktenzeichen-Schemata

- `nnnnn/YY` – 5-stellige laufende Nummer innerhalb eines Jahres, gefolgt von fixem Schrägstrich, gefolgt von 2-stelliger Jahreszahl
- `YY-CCCCC` – 2-stellige Jahreszahl, gefolgt von fixem Bindestrich, gefolgt von 5 zufälligen Buchstaben
- `NNNNN/YYYYMMDD` – 5-stellige unabhängig laufende Nummer, gefolgt von fixem Schrägstrich, gefolgt von Datum

!!! info "Eindeutigkeit"
    In jedem Fall wird j-lawyer.org die Eindeutigkeit des Aktenzeichens forcieren.

### Erweiterte Aktenzeichen

Über das Menü **Einstellungen** → **Akten** → **Aktenzeichen-Schema** lassen sich auch erweiterte Aktenzeichen aktivieren. Die Aktenzeichenerweiterung wird grundsätzlich als Suffix ans Ende des Aktenzeichens angefügt.

Folgende Werte können in die Erweiterungsangabe aufgenommen werden:

- Eine beliebige feste Angabe am Beginn der Aktenzeichenerweiterung
- Das Kürzel des Anwalts, der als Eigentümer einer Akte angegeben wird
- Das Kürzel der Gruppe, welche als Eigentümergruppe einer Akte angegeben wird
- Eine beliebige feste Angabe am Ende der Aktenzeichenerweiterung

Es ist möglich, die Trennzeichen (zwischen Aktenzeichen und Erweiterung, sowie zwischen den einzelnen Angaben innerhalb der Erweiterung) zu definieren.

!!! warning "Wichtig"
    Das Aktenzeichen ist dafür verantwortlich, die Akte eindeutig zu identifizieren – es ist ohne Erweiterung immer einmalig. Die Erweiterungen gelten als zusätzliche Informationen. Werden die erweiterten Aktenzeichen genutzt, so sind ab diesem Zeitpunkt die gewählten Angaben verpflichtend.

## Akten löschen {#loeschen}

Im Navigationsbaum am linken Bildschirmrand unter "suchen" können Sie die zu löschende(n) Akte(n) über eine Schnellsuche finden. In der Ergebnisliste werden anschließend eine oder mehrere Akten markiert und per Rechtsklick und Menüpunkt „löschen" unwiderruflich entfernt.
