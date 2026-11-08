# Einrichtung

Für das Erfassen von Forderungen, Buchungen und Zinsen ist keine Einrichtung nötig. Mahnwesen, Mahnverfahren und Zwangsvollstreckung greifen dagegen auf kanzleiweite Einstellungen zurück. Diese werden unter **Einstellungen → Finanzen** sowie in der [Nutzerverwaltung](../nutzerverwaltung.md) gepflegt.

| Einstellung | Menü | Benötigt für |
|---|---|---|
| [Mahnstufen](#mahnstufen) | Einstellungen → Finanzen → Mahnstufen | Vorgerichtliche Mahnung |
| [Gerichte](#gerichte) | Einstellungen → Finanzen → Gerichte | Mahnverfahren, Zwangsvollstreckung, Prozessgericht |
| [Mahngerichts-Zuordnung](#mahngerichts-zuordnung) | Einstellungen → Finanzen → Mahngerichts-Zuordnung | Mahnverfahren |
| [Vollstreckungsformulare](#vollstreckungsformulare) | Einstellungen → Finanzen → Vollstreckungsformulare | Zwangsvollstreckung |
| [Kennziffer und EDA-Kürzel](#nutzer) | Nutzerverwaltung → Reiter *Finanzen* | Mahnverfahren |

## Mahnstufen {#mahnstufen}

Die Mahnstufen gelten kanzleiweit und werden in der angezeigten Reihenfolge versandt. Die Tabelle zeigt **Bezeichnung**, **Zahlungsfrist**, **Mahngebühr**, **Setzt in Verzug**, **Vorlage** und **Aktiv**.

| Button | Funktion |
|---|---|
| nach oben / nach unten | Ändert die Reihenfolge der Stufen |
| Stufe anlegen | Legt eine neue Mahnstufe an |
| Bearbeiten | Ändert die markierte Stufe |
| Entfernen | Entfernt die markierte Stufe; bereits versandte Mahnungen bleiben erhalten |

Eine Mahnstufe hat folgende Angaben:

| Feld | Bedeutung |
|---|---|
| Bezeichnung | Name der Stufe, bspw. „1. Mahnung“; erscheint im Dokumentnamen und in der Wiedervorlage |
| Zahlungsfrist (Tage) | Frist ab dem Versanddatum |
| Mahngebühr (EUR) | Wird beim Versand als Mahnkosten gebucht; 0,00 bucht nichts. Die Mahngebühr darf nur die tatsächlich entstandenen Kosten abdecken. |
| Vorlagenordner / Vorlage | Die [Dokumentvorlage](../dokumentenmanagement/vorlagen.md) für das Mahnschreiben. Ohne Vorlage wird die Stufe nur vermerkt. |
| Beschreibung | Interne Beschreibung |
| setzt den Schuldner in Verzug (§ 286 Abs. 1 BGB) | Ab dem Versanddatum dieser Stufe laufen Verzugszinsen. In aller Regel gilt das nur für die erste förmliche Mahnung, denn eine zweite Mahnung beginnt den Verzug nicht neu. |
| aktiv | Inaktive Stufen werden beim Versenden übersprungen |

!!! tip "Stufe deaktivieren statt löschen"
    Soll eine Stufe nur nicht mehr angeboten werden, genügt es, sie auf inaktiv zu setzen.

Nach der Installation sind vier Stufen vorhanden (Zahlungserinnerung, 1. Mahnung, 2. Mahnung, Letzte Mahnung vor gerichtlichen Schritten), siehe [Vorgerichtliche Mahnung](mahnungen.md#mahnstufen). Ihnen ist noch keine Vorlage zugeordnet.

## Gerichte {#gerichte}

Gerichte werden zentral gepflegt und von Mahnverfahren, Zwangsvollstreckung und der Angabe des Prozessgerichts verwendet. Die Tabelle zeigt **Bezeichnung**, **Zusatz**, **Ort**, **XJustiz-Kennung**, **Zuständigkeiten** und **aktiv**.

| Button | Funktion |
|---|---|
| Gericht anlegen / Bearbeiten | Gericht erfassen oder ändern |
| Deaktivieren / Aktivieren | Gericht nicht mehr bzw. wieder zur Auswahl anbieten; bestehende Vorgänge behalten es |
| Entfernen | Gericht löschen |

!!! warning "Deaktivieren statt löschen"
    Ein Gericht, das bereits verwendet wurde, sollte deaktiviert und nicht gelöscht werden. Vorgänge, die auf ein gelöschtes Gericht verweisen, können es nicht mehr auflösen.

Ein Gericht hat folgende Angaben:

- Bezeichnung, Zusatzbezeichnung und XJustiz-Kennung
- Postanschrift und Hausanschrift
- Telefon, Fax, E-Mail, Internet und EGVP-/beA-SAFE-ID
- Bankverbindung (Kontoinhaber, IBAN, BIC)
- **Zuständigkeiten:** Mahngericht, Vollstreckungsgericht, Prozessgericht, Insolvenzgericht, Grundbuchamt, Arbeitsgericht. Sie steuern, wo das Gericht zur Auswahl angeboten wird.
- für neue Vorgänge anbieten, Notiz

!!! info "Mahngerichte: Hausanschrift"
    Ein Mahngericht wird im EDA-Antrag allein über Postleitzahl und Ort adressiert. Maßgeblich ist die Zustellbezirks-PLZ der **Hausanschrift**, nicht eine Großempfänger-PLZ der Postanschrift. Ohne diese Angaben kann für das Gericht kein Mahnantrag erzeugt werden.

Nach der Installation sind die zwölf zentralen Mahngerichte hinterlegt. Weitere Gerichte, bspw. Vollstreckungsgerichte, werden von Hand angelegt oder über **Datei → Import: Gerichtsadressen** aus dem beA-Verzeichnis übernommen.

## Mahngerichts-Zuordnung {#mahngerichts-zuordnung}

Die Mahngerichts-Zuordnung bestimmt, welches Mahngericht für einen Antragsteller vorgeschlagen wird: nach § 689 Abs. 2 ZPO das Gericht am allgemeinen Gerichtsstand, für Antragsteller ohne inländischen Gerichtsstand das dafür bestimmte Gericht. Sie wird beim [Ermitteln des Mahngerichts](mahnverfahren.md#mahnsache-anlegen) verwendet.

Die Tabelle zeigt **Bundesland**, **Einschränkung**, **PLZ von**, **PLZ bis**, **Mahngericht** und **aktiv**. Mit **nach oben** und **nach unten** wird die Reihenfolge innerhalb desselben Bundeslands geändert.

| Feld | Bedeutung |
|---|---|
| Mahngericht | Das zuständige Mahngericht; es muss als Gericht mit der Zuständigkeit *Mahngericht* angelegt sein |
| Bundesland | Bundesland des Antragstellers |
| Antragsteller ohne inländischen Gerichtsstand | Die Regel gilt für Antragsteller ohne Gerichtsstand in Deutschland (§ 689 Abs. 2 S. 2 ZPO) |
| Einschränkung (z. B. OLG-Bezirk) | Freitext, falls ein Bundesland auf mehrere Gerichte aufgeteilt ist |
| PLZ von / PLZ bis | Optionaler Postleitzahlenbereich; leer lassen, wenn die Regel für das ganze Bundesland gilt |
| Einreichungswege (mit ; getrennt) | Vom Gericht angenommene Einreichungswege |
| eigene Kennziffer erforderlich | Ob das Gericht eine eigene Kennziffer verlangt |
| Lastschrift bundesweit anzumelden | Hinweis zum Kosteneinzug |
| Reihenfolge | Reihenfolge der Prüfung |
| Regel anwenden | Regel aktiv oder inaktiv |
| Notiz | Interne Notiz |

Nach der Installation ist die Zuordnung für alle Bundesländer hinterlegt. Ist ein Bundesland auf mehrere Mahngerichte aufgeteilt (Nordrhein-Westfalen nach dem OLG-Bezirk Köln), werden beide zur Auswahl angeboten, denn die Aufteilung lässt sich aus dem Bundesland allein nicht bestimmen. Wer die Aufteilung nach Postleitzahlen kennt, kann sie als eigene Regel ergänzen.

!!! info "Ohne Zuordnung"
    Ist keine Zuordnung hinterlegt oder greift keine Regel, schlägt j-lawyer.org kein Mahngericht vor. Es muss dann bei jedem Antrag von Hand gewählt werden.

## Vollstreckungsformulare {#vollstreckungsformulare}

Für die [Zwangsvollstreckung](zwangsvollstreckung.md#formulare) füllt j-lawyer.org die acht amtlichen Anlagen der Zwangsvollstreckungsformular-Verordnung (ZVFV) aus:

| Anlage | Formular |
|---|---|
| 1 | Vollstreckungsauftrag an Gerichtsvollzieher |
| 2 | Antrag auf Erlass einer richterlichen Durchsuchungsanordnung |
| 3 | Entwurf der Durchsuchungsanordnung |
| 4 | Antrag auf Erlass eines Pfändungs- und Überweisungsbeschlusses |
| 5 | Entwurf des Pfändungs- und Überweisungsbeschlusses |
| 6 | Forderungsaufstellung zum Vollstreckungsauftrag |
| 7 | Forderungsaufstellung zum Pfändungs- und Überweisungsbeschluss |
| 8 | Forderungsaufstellung bei Unterhalt |

Die Formulare werden einmalig mit **Standardpaket importieren** übernommen. Das Standardpaket enthält die mit der Software ausgelieferten Fassungen samt Feldzuordnung; vorhandene Vorlagen bleiben dabei unverändert. Ohne Formularvorlagen lassen sich keine Vollstreckungsformulare erzeugen.

Die obere Tabelle **Formularvorlagen** zeigt **Anlage**, **Bezeichnung**, **Fassung**, **gültig ab** und **gültig bis**. Die untere Tabelle **Felder der gewählten Vorlage** zeigt die Formularfelder mit **Seite**, **Feldname**, **Art** und **Werte**.

| Button | Funktion |
|---|---|
| Standardpaket importieren | Übernimmt die acht mitgelieferten Anlagen |
| Fassung hinzufügen | Hinterlegt eine neue Fassung eines Formulars als PDF, mit Anlage, Fassungsdatum und Gültigkeitsbeginn |
| Von Fassung übernehmen | Übernimmt die Feldzuordnung einer anderen Fassung desselben Formulars. Felder, die es nicht mehr gibt oder die ihre Bedeutung geändert haben, werden genannt. |
| Zuordnung übernehmen | Übernimmt die mitgelieferte Feldzuordnung für die gewählte Vorlage; eine angepasste Zuordnung geht dabei verloren |
| Gültigkeit beenden | Setzt das Gültigkeitsende der gewählten Fassung, ohne sie zu löschen |

### Neue Formularfassungen {#neue-fassung}

Wird ein Formular neu gefasst, wird die alte Fassung nicht ersetzt. Sie erhält ein Gültigkeitsende, die neue Fassung wird daneben hinterlegt. Maßnahmen, die mit der alten Fassung erzeugt wurden, behalten den Vermerk ihrer Fassung, denn sie waren zu ihrer Zeit richtig und müssen nachvollziehbar bleiben. Für neue Maßnahmen verwendet j-lawyer.org die Fassung, die am Datum der Maßnahme gilt.

!!! warning "ZVFV-Fassung ab 01.10.2026"
    Die Fassung der Formulare vom 01.09.2024 gilt bis zum 30.09.2026. Ab dem 01.10.2026 ist die neue Fassung zu verwenden. Sie ist im Standardpaket enthalten. Wurden die Formulare vor dem Update importiert, wird die neue Fassung mit **Standardpaket importieren** ergänzt.

## Kennziffer und EDA-Kürzel {#nutzer}

Für das gerichtliche Mahnverfahren benötigt jeder einreichende Rechtsanwalt eine **Kennziffer**, die das zentrale Mahngericht auf Antrag zuteilt, sowie das zugehörige **EDA-Kürzel**. Beides wird in der [Nutzerverwaltung](../nutzerverwaltung.md) beim jeweiligen Anwalt im Reiter **Finanzen**, Abschnitt **Mahnverfahren**, eingetragen.

| Feld | Bedeutung |
|---|---|
| Kennziffer | Die vom Mahngericht zugeteilte Kennziffer des Prozessbevollmächtigten |
| EDA-Kürzel | Dreistelliges Buchstabenkürzel, das das Mahngericht zusammen mit der Kennziffer zuteilt. Die EDA-Datei wird aus dem Kürzel und einer fortlaufenden Nummer benannt. |

Im [Mahnverfahren](mahnverfahren.md#mahnsache-anlegen) stehen bei der Kennziffer alle Anwältinnen und Anwälte zur Auswahl, für die eine Kennziffer hinterlegt ist.
