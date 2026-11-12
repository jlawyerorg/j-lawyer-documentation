# Historie {#historie}

Der Tab "Historie" zeigt das Änderungsprotokoll der Akte.

## Aktenhistorie

Die Historie protokolliert alle relevanten Änderungen an der Akte:

- Erstellung der Akte
- Änderungen an Stammdaten
- Hinzufügen / Entfernen von Beteiligten
- Dokumentenoperationen (Hinzufügen, Umbenennen, Löschen)
- Kalendereintrag-Änderungen
- Finanzielle Buchungen
- Und weitere Aktionen

## Anzeige

Die Historie zeigt für jeden Eintrag:

| Spalte | Beschreibung |
|--------|--------------|
| **Datum / Zeit** | Zeitpunkt der Änderung |
| **Nutzer** | Wer die Änderung durchgeführt hat |
| **Aktion** | Art der Änderung |
| **Details** | Zusätzliche Informationen zur Änderung |

## Historie exportieren

Die Aktenhistorie kann exportiert werden:

- **Im Browser anzeigen**: Öffnet die Historie in einem Browserfenster mit Such- und Filterfunktionen
- **Als Dokument speichern**: Speichert die Historie als Dokument zur Akte

### Filtern und Suchen im Export

Im Browser-Export stehen Filter- und Suchfunktionen zur Verfügung, um gezielt nach bestimmten Änderungen zu suchen.

## Aktenübergreifende Historie {#aktenuebergreifende-historie}

Neben der Historie einer einzelnen Akte gibt es eine aktenübergreifende Recherche über die Historieneinträge aller Akten, auf die der angemeldete Nutzer zugreifen darf. Damit lässt sich bspw. nachvollziehen, an welchen Akten man selbst oder ein Kollege an einem bestimmten Tag gearbeitet hat, oder in welcher Akte sich ein inzwischen gelöschtes Dokument mit einer bestimmten Belegnummer befunden hat. Die Historie dokumentiert auch Löschvorgänge.

Die Recherche ist über **Auswertungen** → **Aktenhistorie** in der Navigationsleiste erreichbar. Beim Öffnen werden die eigenen Einträge der letzten 7 Tage angezeigt, die neuesten zuerst.

### Filter {#historie-filter}

Die Filterleiste im oberen Bereich bietet folgende Einschränkungen:

| Filter | Beschreibung |
|--------|--------------|
| **Zeitraum** | Vorgaben **Heute**, **Gestern**, **Letzte 7 Tage**, **Letzte 30 Tage**, **Dieser Monat**, **Letzter Monat** und **Dieses Jahr**. Die Auswahl einer Vorgabe setzt die Datumsfelder und startet die Suche sofort. Werden die Felder **von** und **bis** von Hand geändert, wechselt der Zeitraum auf **Benutzerdefiniert**. Das Bis-Datum schließt den ganzen Tag ein. |
| **Nutzer** | **Ich** (Standard), **Alle Nutzer** oder ein bestimmter Nutzer |
| **Akte** | Aktenzeichen oder Rubrum bzw. ein Teil davon |
| **Text** | Suchbegriff in der Änderungsbeschreibung, bspw. eine Belegnummer oder ein Dokumentname |
| **max.** | Höchstzahl der angezeigten Einträge: 100, 500, 1000 (Standard) oder 5000 |

In den Feldern **Akte** und **Text** startet **Enter** oder der Button **Suchen** die Suche. Über das Kreuz im Feld wird der Suchbegriff gelöscht und erneut gesucht.

Zeitraum-Vorgabe, Nutzer und Höchstzahl werden gespeichert und beim nächsten Öffnen wiederhergestellt. Ein benutzerdefinierter Zeitraum wird nicht gespeichert, stattdessen gilt wieder „Letzte 7 Tage“.

!!! info "Zugriffsrechte und Höchstzahl"
    Einträge zu Akten, auf die der Nutzer keinen Zugriff hat, werden nicht angezeigt. Die Höchstzahl bezieht sich nur auf die sichtbaren Einträge. Wird sie erreicht, weist die Statuszeile darauf hin („Limit erreicht, ältere Einträge werden nicht angezeigt“). In diesem Fall sollten Zeitraum oder Filter eingegrenzt werden.

### Kategorien {#historie-kategorien}

Jeder Eintrag wird anhand seiner Änderungsbeschreibung einer Kategorie zugeordnet und in der Tabelle mit einem farbigen Symbol gekennzeichnet:

| Kategorie | Beispiele |
|-----------|-----------|
| **Dokumente** | Dokument hinzugefügt, umbenannt, gelöscht |
| **Termine / Fristen** | Wiedervorlagen, Fristen, Termine, Kalendereinträge |
| **Beteiligte** | Beteiligte hinzugefügt, geändert, entfernt |
| **Nachrichten** | E-Mail, beA, E-POST, Fax |
| **Etiketten** | Akten- und Dokument-Etiketten |
| **Finanzen** | Rechnungen bzw. Belege, Zahlungen, Aktenkonto, Forderungskonto, Zeiterfassung |
| **Akte** | Änderungen an der Akte selbst und an Falldaten |
| **Sonstiges** | alle übrigen Einträge |

Unter der Filterleiste wird jede Kategorie als Schaltfläche mit der Anzahl ihrer Einträge angezeigt. Durch Anklicken einer oder mehrerer Kategorien werden nur deren Einträge angezeigt. **Alle** hebt die Auswahl wieder auf. Der Kategoriefilter wirkt auf die bereits geladenen Einträge, es wird also nicht neu gesucht.

### Kennzahlen und Aktivitätsdiagramm {#historie-kennzahlen}

Neben der Filterleiste werden Kennzahlen zu den angezeigten Einträgen eingeblendet:

- Anzahl der **Einträge**, der **Akten** und der **Nutzer**
- die **meistbearbeitete Akte**. Ein Klick darauf öffnet die Akte.

Das Diagramm zeigt die **Aktivität pro Tag**, bei Zeiträumen von mehr als 62 Tagen die **Aktivität pro Woche**. Ein Klick auf einen Balken springt in der Tabelle zu den Einträgen dieses Tages bzw. dieser Woche. Kennzahlen und Diagramm berücksichtigen einen gesetzten Kategoriefilter.

### Ergebnistabelle {#historie-tabelle}

Die Tabelle enthält die Spalten **Zeit**, **Nutzer**, **Aktenzeichen**, **Rubrum** und **Änderung**. Bei Sortierung nach Zeit sind die Einträge nach Tagen gruppiert, jeweils mit einer Trennzeile wie „Heute · Mi, 05.11.2026 · 23 Einträge“. Ein Klick auf einen Spaltenkopf sortiert nach dieser Spalte. Die Trennzeilen entfallen dann.

Die Suchbegriffe aus **Akte** und **Text** werden in der Tabelle und in der Detailansicht hervorgehoben.

Unterhalb der Tabelle zeigt eine Detailansicht den ausgewählten Eintrag mit Kategorie, Zeitpunkt, Nutzer und Akte sowie dem vollständigen Änderungstext. Längere Texte lassen sich dort scrollen.

### Akte öffnen, kopieren und exportieren {#historie-aktionen}

- **Akte öffnen**: per Doppelklick oder **Enter** auf einem Eintrag, über den Button **Akte öffnen**, über das Kontextmenü oder per Klick auf die Akte in der Detailansicht. Mit der Zurück-Navigation gelangt man wieder zur Aktenhistorie.
- **Änderungstext kopieren**: über das Kontextmenü (Rechtsklick) wird der Änderungstext eines Eintrags in die Zwischenablage kopiert.
- **Export**: Die aktuell angezeigten Einträge werden als Tabellendokument exportiert und geöffnet, ohne Trennzeilen und mit zusätzlicher Spalte für die Kategorie. Ein gesetzter Kategoriefilter wird berücksichtigt.
