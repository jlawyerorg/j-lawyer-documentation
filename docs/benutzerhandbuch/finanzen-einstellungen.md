# Einstellungen

### Steuersätze {#steuersaetze}

Steuersätze, die an Rechnungspositionen angegeben werden können, werden im Menü „Einstellungen" – „Finanzen" – „Steuersätze" hinterlegt. 0% und 19% sind voreingestellt. Weitere Steuersätze sollten das Format „x,0" haben, d.h. Komma als Dezimaltrenner und eine Nachkommastelle.

### Währungen

Währungen, die bei Rechnungslegung ausgewählt werden können, werden im Menü „Einstellungen" – „Finanzen" – „Währungen" hinterlegt. Es sollte das Währungskürzel genutzt werden. EUR und CHF sind voreingestellt.

### Belegarten

Belegarten, die bei Erstellung eines Belegs innerhalb einer Akte ausgewählt werden können, werden im Menü „Einstellungen" – „Finanzen" – „Belegarten" konfiguriert. Eine Belegart besteht dabei aus Name, Beschreibung und einer Angabe, ob ein Beleg dieser Art in der „Offene Posten"-Liste erscheinen soll. Die gebräuchlichsten Belegarten sind vorkonfiguriert.

### Belegnummernkreise

Grundsätzlich gilt: jeder Beleg bekommt eine eindeutige Nummer / Bezeichnung, unabhängig vom Status des Belegs. Somit erhalt auch eine Rechnung im Entwurfsstatus bereits eine Belegnummer.

Belegnummern werden automatisch vergeben. Damit die Schemata den eigenen Anforderungen entsprechen, sollten eigene Nummernkreise konfiguriert werden: Menü „Einstellungen" – „Finanzen" – „Belegnummernkreise".

Ein Nummernkreis hat die Attribute
- Anzeigename (zwecks Auswahl bei Belegerstellung)

- Schema (Definition ähnlich Aktenzeichenschema)

- Zahlungsziel (zur automatischen Berechnung des Fälligkeitsdatums)

- Start-Index (laufende Nummer in der Belegnummer beginnt bei diesem Wert)

- USt ausweisen (wird bei Belegerstellung ausgewertet und angewendet)

Nach Erstellung eines neuen Nummernkreises ist dessen Nutzung ggf. über die Nutzerverwaltung zu ermöglichen. An jedem Nutzer ist einstellbar, welche Nummernkreise genutzt werden dürfen. So ist im Falle einer Bürogemeinschaft ein unabhängiges Abrechnen möglich.

### Girocode: Bezahlen per Banking App ermöglichen {#girocode}

Bei Erstellung eines Dokumentes aus einem Beleg (einer Rechnung) kann automatisch ein QR-Code erstellt werden, der vom Rechnungsempfänger mittels Banking-App gescannt wird und die relevanten Informationen direkt in eine Überweisungsmaske übernimmt. Somit werden Fehleingaben vermieden und der Bezahlprozess für Rechnungsempfänger wesentlich vereinfacht.

Um einen Girocode in der Rechnung aufzunehmen, so ist – analog zu anderen Tabellenplatzhaltern – eine 1x1-Tabelle in die Vorlage aufzunehmen, mit dem Platzhalter {{BEL_GIROCODE}}. Die Tabelle kann ggf. als rahmenlos formatiert werden.

Folgende Hinweise gelten für die Nutzung von Girocode:
- Unterstützt werden ausschließlich Rechnungen, die in EUR abgerechnet werden.

- Das Konto, auf welches der Rechnungsempfänger überweisen soll, wird aus dem Absender der Rechnung übernommen.

- Ab j-lawyer.org Version 3.0 kann die Größe der generierten Girocodes über das Menü „Einstellungen" – „Finanzen" – „Girocodes" konfiguriert werden.

- Vor der Nutzung von Girocodes sollte die korrekte Funktionsweise einmal ausprobiert werden: In der Detailansicht eines Belegs findet man im Kopf (links neben der Rechnungsnummer) einen Button zur Anzeige des Girocodes. Diesen kann man mit der eigenen Banking-App scannen (und dann natürlich nicht absenden) und so die Korrektheit der Daten im Kanzleiprofil etc. testen.
