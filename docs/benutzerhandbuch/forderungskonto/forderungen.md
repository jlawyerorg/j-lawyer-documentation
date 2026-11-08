# Forderungen & Zinsen

Eine Forderung setzt sich aus einzelnen **Positionen** zusammen, bspw. der Hauptforderung aus einer Rechnung, vorgerichtlichen Mahnkosten und der vorgerichtlichen Anwaltsvergütung. Jede Position hat einen Typ, einen Betrag und optional Zinsregeln. Die Positionen werden im Reiter **Positionen** des Forderungskontos gepflegt.

## Positionen {#positionen}

Die Tabelle zeigt die Spalten **Betrag**, **Typ**, **Name** und **Beschreibung**. Über die Buttons am Rand werden Positionen hinzugefügt, bearbeitet und entfernt.

Beim Hinzufügen einer Position bucht j-lawyer.org automatisch eine **Initialbuchung** über den Betrag der Position. Ihr Datum ist der Beginn der ersten Zinsregel, bei unverzinslichen Positionen das aktuelle Datum. Der Kommentar der Buchung beschreibt die Verzinsung, bspw. „Kaufpreis, initiale Buchung, verzinst mit 5% Zinsen über dem Basiszinssatz“.

!!! info "Positionen löschen"
    Forderungs- und Kostenbuchungen können im Reiter *Buchungen* nicht direkt gelöscht werden. Soll eine Forderung entfernt werden, wird die zugehörige Position im Reiter *Positionen* gelöscht.

### Typen von Positionen {#positionstypen}

**Forderungen und Kosten**

| Typ | Verwendung |
|---|---|
| Hauptforderung | Die eigentliche Forderung, bspw. aus Kaufvertrag, Werkvertrag oder Rechnung |
| laufende monatliche Hauptforderung | Wiederkehrende Forderungen, bspw. Miete oder Pacht |
| Kosten (verzinslich) | Nebenforderungen, die verzinst werden |
| Kosten (unverzinslich) | Nebenforderungen ohne Verzinsung |
| festgesetzte Kosten | Kosten aus einem Kostenfestsetzungsbeschluss (verzinslich nach § 104 Abs. 1 S. 2 ZPO) |
| Zinsrückstand | Bereits ausgerechnete, rückständige Zinsen als eigener Betrag |

**Vorgerichtliche Nebenforderungen**

Diese Typen entsprechen den Feldern für Nebenforderungen im Mahnbescheidsantrag und werden dort jeweils an der richtigen Stelle übertragen:

| Typ |
|---|
| Auslagen des Gläubigers |
| Mahnkosten |
| Auskunftskosten |
| Bankrücklastkosten |
| Inkassokosten |
| vorgerichtliche Anwaltsvergütung (Nr. 2300 VV RVG) |
| andere Nebenforderung |

Der Typ bestimmt auch, in welcher Reihenfolge Zahlungen auf die Positionen angerechnet werden (siehe [Zahlungsverteilung](buchungen.md#zahlungsverteilung)).

### Position bearbeiten {#position-bearbeiten}

| Feld | Bedeutung |
|---|---|
| Name | Bezeichnung der Position, bspw. „Rechnung 2026-0815“ |
| Beschreibung | Freitext |
| Typ | Typ der Position (siehe oben) |
| Betrag | Ursprünglicher Betrag |

### Angaben für den Mahnbescheid {#angaben-mahnbescheid}

Soll die Forderung im [gerichtlichen Mahnverfahren](mahnverfahren.md) geltend gemacht werden, verlangen die Mahngerichte eine genaue Bezeichnung des Anspruchs. Diese Angaben werden bereits an der Position erfasst:

| Feld | Bedeutung |
|---|---|
| Anspruchsart | Die Katalognummer aus der Liste der Mahngerichte, bspw. Kaufvertrag oder Werkvertrag. Andere Angaben nimmt der Antrag nicht an. Für Ansprüche außerhalb des Katalogs gibt es „sonstiger Anspruch“, die Begründung steht dann im Feld *Name*. |
| Vertragsart | Nur bei Katalog-Nr. 28: die von den Mahngerichten zugelassene Vertragsart |
| Anspruchsbegründung | Worauf der Anspruch beruht, wird im Mahnbescheid gedruckt: Schreiben, Rechnung, Mahnung, Kontoauszug, Aufstellung, Vertrag, Stromrechnung, Gasrechnung oder andere |
| Nummer/Beleg | Nummer des Belegs, auf dem der Anspruch beruht, bspw. die Rechnungsnummer. Höchstens 35 Zeichen. |
| vom | Der Tag, an dem der Anspruch entstanden ist, also das Datum der Rechnung, des Vertrages oder der Abrechnung |
| bis | Nur bei Forderungen über einen Zeitraum (Miete, Pacht, wiederkehrende Beträge), sonst leer |

Fehlende oder unzulässige Angaben werden spätestens bei der [Prüfung des Mahnantrags](mahnverfahren.md#antrag-pruefen) gemeldet.

## Zinsregeln {#zinsregeln}

Eine Position ist verzinslich, sobald mindestens eine Zinsregel für sie hinterlegt ist. Zinsregeln sind zeitlich gestaffelt: Jede Regel gilt ab ihrem Datum bis zum Beginn der nächsten. So lassen sich bspw. ein vertraglicher Zins bis zum Verzugseintritt und danach Verzugszinsen abbilden.

Zinsregeln werden im Dialog der Position im Bereich **Zinsregeln** gepflegt:

1. Bei **gültig ab** den Beginn der Verzinsung eintragen, bspw. den Tag nach Eintritt des Verzugs.
2. Das **Zinsmodell** wählen:
    - **fester Zinssatz:** ein fester Prozentsatz pro Jahr
    - **Basiszinssatz + Aufschlag:** der jeweils gültige Basiszinssatz zuzüglich eines Aufschlags in Prozentpunkten
3. Mit **Hinzufügen** die Regel übernehmen.

Für die gesetzlichen Verzugszinsen stehen Vorlagen zur Verfügung:

| Vorlage | Zinssatz | Rechtsgrundlage |
|---|---|---|
| Verzugszinsen Verbrauchergeschäft | Basiszins + 5 Prozentpunkte | § 288 Abs. 1 BGB |
| Verzugszinsen Handelsgeschäft | Basiszins + 9 Prozentpunkte | § 288 Abs. 2 BGB |
| Verzugszinsen Verbraucher bis 28.07.2014 | Basiszins + 8 Prozentpunkte | § 288 Abs. 2 BGB a. F. |
| Allgemeine gesetzliche Zinsen | Basiszins + 5 Prozentpunkte | z. B. Prozesszinsen, § 291 BGB |

### Wie Zinsen berechnet werden {#zinsberechnung}

Zinsen werden **taggenau** berechnet (Zinstage / 365), für jede Position getrennt und unter Berücksichtigung von Zahlungen. Ändert sich der Basiszinssatz oder die Zinsregel, beginnt ein neuer Zinszeitraum. Bei basiszinsbezogener Verzinsung gilt:

> effektiver Zinssatz = Basiszinssatz + Aufschlag
>
> Beispiel: Basiszinssatz 2,27 % + 5 Prozentpunkte = 7,27 % Verzugszinsen

Bis zum [Stichtag](aufstellung.md#stichtag) aufgelaufene Zinsen werden in Summen und Aufstellung **dynamisch** ausgewiesen, ohne dass sie gebucht werden müssen. Sollen Zinsen dauerhaft festgehalten werden, etwa zum Stichtag eines Mahnantrags, wird eine [Zinsbuchung](buchungen.md#zinsen-buchen) erfasst.

## Basiszinsen {#basiszins}

Der Reiter **Basiszinsen** zeigt die hinterlegten Basiszinssätze der Deutschen Bundesbank mit den Spalten **Gültig ab**, **Basiszinssatz** und **Quelle**. Der Basiszinssatz ändert sich jeweils zum 1. Januar und 1. Juli.

Mit **Aktualisieren** prüft j-lawyer.org online, ob neue Basiszinssätze veröffentlicht wurden, und übernimmt sie. Die Basiszinssätze gelten für alle Forderungskonten.

!!! tip "Tipp"
    Nach dem 1. Januar und dem 1. Juli einmal auf **Aktualisieren** klicken, damit Zinsen ab dem neuen Halbjahr mit dem richtigen Satz berechnet werden.
