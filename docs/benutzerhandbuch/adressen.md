# Kontakte / Adressen

### Adressen suchen {#suchen}

Im Navigationsbaum am linken Bildschirmrand unter "bearbeiten" bzw. "einsehen" können Sie Adressen über eine Schnellsuche finden.

#### Durchsuchte Felder {#suchen-felder}

Folgende Felder werden bei der Suche berücksichtigt:

- Name
- Vorname
- Geburtsname
- Unternehmen / Firma
- Abteilung
- E-Mail (alle drei Adressen: primär, privat, sonstige)
- Telefon
- Mobilnummer
- Ort / Stadt
- Postleitzahl
- beA-SafeId
- Eigene Felder 1-3

#### Suche mit mehreren Begriffen {#suchen-mehrere-begriffe}

Mehrere Suchbegriffe können durch **Leerzeichen** oder **Kommas** getrennt eingegeben werden. Alle Begriffe müssen zutreffen (UND-Verknüpfung).

**Beispiele:**

| Sucheingabe | Findet |
|-------------|--------|
| `Müller` | Alle Adressen mit "Müller" in einem der Suchfelder |
| `Müller Berlin` | Adressen mit "Müller" UND "Berlin" |
| `Schmidt, 10115` | Adressen mit "Schmidt" UND Postleitzahl "10115" |

#### Suchverhalten {#suchen-verhalten}

- **Teilbegriffe:** Es werden auch Teilübereinstimmungen gefunden. Die Suche nach `Mül` findet auch "Müller".
- **Groß-/Kleinschreibung:** Wird ignoriert. `müller` findet auch "MÜLLER" oder "Müller".
- **Umlaute:** Deutsche Umlaute (ä, ö, ü, ß) werden korrekt verarbeitet.

#### Kombination mit Etiketten {#suchen-tags}

Zusätzlich zur Textsuche ist eine Einschränkung über [Etiketten](etiketten.md) möglich. Beide Filter werden kombiniert - es werden nur Adressen angezeigt, die sowohl den Suchbegriffen als auch den gewählten Etiketten entsprechen.

### E-Mail-Adressen {#email-adressen}

Für jeden Kontakt können bis zu drei E-Mail-Adressen hinterlegt werden:

| Feld | Verwendung |
|------|------------|
| **E-Mail (primär)** | Hauptadresse des Kontakts – wird bevorzugt verwendet |
| **E-Mail (privat)** | optionale private Adresse |
| **E-Mail (sonstige)** | optionale weitere Adresse |

Die Adressen werden wie folgt genutzt:

- **Suche**: Ein Kontakt wird über jede seiner E-Mail-Adressen gefunden.
- **E-Mail-Versand**: In der Empfängerauswahl steht jede hinterlegte Adresse eines Beteiligten als eigener Eintrag für An, CC und BCC zur Verfügung. Ist keine primäre Adresse hinterlegt, wird beim Versand an einen Kontakt automatisch die erste vorhandene weitere Adresse verwendet.
- **Dokumentvorlagen**: Der Platzhalter `{{…_EMAIL}}` (bspw. `{{MANDANT_EMAIL}}`) enthält die erste vorhandene Adresse in der Reihenfolge primär, privat, sonstige.
- **Nextcloud**: Beim [Abgleich des Adressbuchs](addon-nextcloud.md#adressbuch-sync) werden alle Adressen übertragen; die primäre Adresse wird als bevorzugte markiert.

### Dokumente an Kontakten {#dokumente}

Manche Dokumente gehören nicht zu einer einzelnen Akte, sondern zu einem Kontakt – bspw. eine Vollmacht für mehrere Mandate, eine Ausweiskopie, eine Einwilligungserklärung oder eine Honorarvereinbarung. Solche Dokumente werden im Tab **Dokumente** der Adresse abgelegt.

Die Dokumente werden in einer Liste mit Name, Datum und Größe angezeigt; ein Doppelklick öffnet ein Dokument. Neue Dokumente kommen wie folgt hinzu:

- **Hinzufügen**: Dateien vom Arbeitsplatz auswählen
- **Erstellen**: ein Dokument aus einer [Dokumentvorlage](dokumentenmanagement/vorlagen.md) erzeugen
- **Drag & Drop**: Dateien in die Liste ziehen
- aus einer Akte heraus über **kopieren oder verschieben** (siehe [Dokumente – Kontextmenü](aktenverwaltung/dokumente.md#kopieren-und-verschieben))

Per Rechtsklick auf ein Dokument stehen **als PDF zum Kontakt speichern**, **umbenennen** und **Löschen** zur Verfügung. Gelöschte Dokumente landen im [Papierkorb](dokumentenmanagement/papierkorb.md).

Beim Versand von E-Mails und beA-Nachrichten aus einer Akte stehen die Dokumente der Beteiligten bei der Auswahl von Anhängen in einem eigenen Reiter je Beteiligtem zur Verfügung.

!!! info "Hinweise"
    - Dokumente an Kontakten werden als einfache Liste geführt – Ordner, Etiketten, Favoriten und Farbmarkierungen stehen hier nicht zur Verfügung.
    - Wird ein Kontakt gelöscht, werden auch seine Dokumente gelöscht.

### Adresse importieren {#import}

Adressen im vCard-Format können importiert werden. Dabei werden in der Datenbank existierende Kontakte weder geändert noch gelöscht, es werden ausschließlich neue Adressen angelegt. Nach Auswahl einer Importdatei bekommen Sie eine Übersicht der darin enhaltenen Kontakte und können über ein Auswahlfeld exakt bestimmen welche Adressen sie importieren / nicht importieren wollen.

Enthält ein Kontakt in der vCard mehrere E-Mail-Adressen, werden bis zu drei davon übernommen und auf die Felder [E-Mail (primär), (privat) und (sonstige)](#email-adressen) verteilt – die bevorzugte bzw. geschäftliche Adresse wird zur primären.

### Beteiligtentypen konfigurieren {#beteiligtentypen}

Je nach Anwendungsgebiet der Software ergibt sich der Bedarf nach spezifischen Beteiligtentypen – bspw. “Gericht”, “Mandant”, “Gegner” oder “Mieter”, “Vermieter” etc. Unter “Einstellungen” - “Modul ‘Adressen’” - “Beteiligtentypen” lassen sich diese Rollen erstellen und konfigurieren. 

Jeder Typ verfügt über

- Bezeichnung: ein “sprechender” Name, der an verschiedenen Stellen der Anwendung angezeigt wird, bspw. bei der Erstellung von Dokumenten oder dem Versenden von E-Mails und beA-Nachrichten.
- Platzhalter: der Präfix für die in Dokumenten verwendbaren Platzhalter. Vergibt man bspw. für einen Beteiligtentyp “Hausverwalter” den Platzhalter “HV”, so sind dessen Informationen in Dokumenten über {{HV_NAME}} etc. nutzbar. Es ist daher empfohlen, den Platzhalter kurz zu halten und ausschließlich Großbuchstaben zu verwenden.
- Markieren in: eine Farbe, welche für die Darstellung der Beteiligten verwendet wird. So lassen sich bei vielen Beteiligten auf einen Blick verschiedene Typen erkennen.

Da keine Beziehungen zwischen Beteiligtentypen konfiguriert werden, ist eine Prüfung auf Interessenkonflikte nicht einfach umsetzbar. Die Anwendung wird daher informieren, sobald eine Beteiligte / Adresse in verschiedenen Rollen verwendet wird.

Um einen neuen Beteiligtentypus hinzuzufügen, wird der "+"-Knopf genutzt und eine Bezeichnung eingegeben und bestätigt. Anschließend den neuen Eintrag in der Liste selektieren und Platzhalter und Farbe definieren, danach "Übernehmen".
Zum Bearbeiten eines bestehenden Eintrages wird dieser in der Liste selektiert, wie gewünscht verändert und per "Übernehmen" gespeichert.

