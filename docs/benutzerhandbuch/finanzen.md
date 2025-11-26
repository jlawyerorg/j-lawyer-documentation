# Rechnungen



### Steuersätze {#steuersaetze}



Steuersätze, die an Rechnungspositionen angegeben werden können, werden im Menü „Einstellungen“ – „Finanzen“ – „Steuersätze“ hinterlegt. 0% und 19% sind voreingestellt. Weitere Steuersätze sollten das Format „x,0“ haben, d.h. Komma als Dezimaltrenner und eine Nachkommastelle.

### Währungen



Währungen, die bei Rechnungslegung ausgewählt werden können, werden im Menü „Einstellungen“ – „Finanzen“ – „Währungen“ hinterlegt. Es sollte das Währungskürzel genutzt werden. EUR und CHF sind voreingestellt.

### Belegarten



Belegarten, die bei Erstellung eines Belegs innerhalb einer Akte ausgewählt werden können, werden im Menü „Einstellungen“ – „Finanzen“ – „Belegarten“ konfiguriert. Eine Belegart besteht dabei aus Name, Beschreibung und einer Angabe, ob ein Beleg dieser Art in der „Offene Posten“-Liste erscheinen soll. Die gebräuchlichsten Belegarten sind vorkonfiguriert.

### Belegnummernkreise



Grundsätzlich gilt: jeder Beleg bekommt eine eindeutige Nummer / Bezeichnung, unabhängig vom Status des Belegs. Somit erhalt auch eine Rechnung im Entwurfsstatus bereits eine Belegnummer.

Belegnummern werden automatisch vergeben. Damit die Schemata den eigenen Anforderungen entsprechen, sollten eigene Nummernkreise konfiguriert werden: Menü „Einstellungen“ – „Finanzen“ – „Belegnummernkreise“.

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

- Ab j-lawyer.org Version 3.0 kann die Größe der generierten Girocodes über das Menü „Einstellungen“ – „Finanzen“ – „Girocodes“ konfiguriert werden.

- Vor der Nutzung von Girocodes sollte die korrekte Funktionsweise einmal ausprobiert werden: In der Detailansicht eines Belegs findet man im Kopf (links neben der Rechnungsnummer) einen Button zur Anzeige des Girocodes. Diesen kann man mit der eigenen Banking-App scannen (und dann natürlich nicht absenden) und so die Korrektheit der Daten im Kanzleiprofil etc. testen.

### Rechnungen / Belege erstellen {#rechnungen}



Rechnungen (oder Belege im Allgemeinen) können im Tab „Finanzen“ einer Akte erstellt werden („+“-Button im Sub-Tab „Belege“). Nach einer Bestätigung der Belegart und des Nummernkreises (Button hinter „Typ“) sind auch alle weiteren Kopfinformationen für eine Bearbeitung freigegeben.

In einem nächsten Schritt ist der Beleg mit Positionen zu befüllen. Es gibt folgende Möglichkeiten, um Positionen hinzuzufügen:

#### Beleg vorbereiten
- Gehe in einer Akte auf den Reiter oben „Finanzen“.

- Gehe dort auf den Menüpunkt links „Belege“.

- Klicke nun auf das Pluszeichen.

- Wähle den Typ aus (z.B. „Rechnung“ für die Erstellung einer Rechnung).

- Wähle den verwendeten Nummernkreis aus. Beachte dabei, dass Rechnungsnummern nur einmalig verwendet werden können und automatisch erstellt werden. Bei einer Testrechnung solltest du also den „Testnummernkreis“ anwählen, für eine „echte Rechnung“ den „Standardnummernkreis“.

- Zur automatischen Vergabe der Rechnungsnummer und Eröffnung der Möglichkeit, weitere Felder auszufüllen, klicke nun auf den Haken neben dem „Typ“ der „Rechnung“.

#### Position hinzufügen: manuell / vollständige händische Eingabe
- Im Reiter „Positionen“ fügt man eine Rechnungsposition hinzu, indem man über das Pluszeichen eine frei eintragbare Position erstellt. Die Menge und der Preis können noch manuell angepasst werden.

#### Position hinzufügen: erfasste Zeiten abrechnen

Bevor eine Rechnung erstellt wird, erstellt man zunächst ein Zeiterfassungsprojekt und erfasst Zeiten (siehe Kapitel „Zeiterfassung“).
- Im Reiter „Positionen“ fügt man eine Rechnungsposition hinzu, indem man über das den Stoppuhr-Buton die zu übernehmenden Zeiten auswählt und auf „in Rechnung übernehmen“ klickt. Pro Stundensatz werden Zeiten zu einer gemeinsamen Rechnungsposition zusammengefasst. Im Leistungsnachweis (der automatisch in das Rechnungsdokument aufgenommen werden kann) wird trotzdem ein detaillierter Nachweis der einzelnen Zeiten ersichtlich.

#### Position hinzufügen: aus Gebührenrechner / Plugin
- Im Reiter „Positionen“ oben auf das Symbol für „Positionen aus Rechnungsplugin übernehmen“ klicken und einen Berechner auswählen, bspw. „Rechnung RVG Wertgebühren“.

- Relevante Gebühreneingaben tätigen

- Button ganz unten nutzen: „als Rechnung“. Daraufhin werden die Gebührenpositionen in den Beleg aufgenommen.

#### Belegdokument erstellen
- Im Reiter Dokumente klickt man auf „erstellen“, „elektronische Rechnung“ und wähle die gewünschte Rechnungsvorlage aus und gehe auf „erstellen und öffnen“. Hinweis: Bei der Auswahl des E-Rechnungs-Formates sollte „Elektronische Rechnung (an Unternehmen)“ ausgewählt werden, wenn die Rechnung an Unternehmen oder Verbraucher gestellt wird.

- Im nun geöffneten Rechnungsdokument kann jetzt das Layout angepasst werden. Inhaltliche Angaben, die auch im maschinenlesbaren Format enthalten sind (wie Rechnungssumme oder Rechnungsempfänger), sollten nicht mehr verändert werden.

- Nach einem speichern und schließen des Dokuments speichert man im j-lawyer das Popup des Rechnungsfensters und geht in der Akte auf Dokumente. Dort klickt man mit der rechten Maustaste auf das Rechnungsdokument und wählt aus „als pdf zur Akte speichern“. Nun ist das Rechnungsdokument als pdf in der Akte.

- Auf das Rechnungsdokument als pdf klickt man nun mit einem Rechtsklick und wählt aus „@ als pdf versenden“, um die Rechnung per E-Mail an den Mandanten zu senden.

### Elektronische Rechnungen (“E-Rechnung”) {#e-rechnung}



j-lawyer.org kann Rechnungen sowohl im ZUGFeRD-Standard („Zentraler User Guide des Forums elektronische Rechnung Deutschland“) als auch als Xrechnung erstellen und lesen.

ZUGFeRD kommt primär zwischen Unternehmen zum Einsatz und beinhaltet die Erstellung von PDF-Dokumenten mit einem eingebetteten „Datenschnipsel“, welcher die Rechnung maschinell lesbar macht.

XRechnung wird primär für die Rechnungsstellung eines Unternehmens an einen öffentlichen Auftraggeber genutzt. Es handelt sich um ein XML-Dokument, das nur maschinell lesbar ist. In der Adressverwaltung sollte in diesen Fällen am Rechnungsempfänger eine sogenannte „Leitweg-ID“ hinterlegt werden, welche den Rechnungsempfänger eindeutig kennzeichnet und ein automatisches „Routing“ innerhalb der Behörden ermöglicht.

Die Rechnungserstellung findet – wie auch in den Version vor j-lawyer.org 3.0 – in der Akte im Tab „Finanzen“, dort unter „Belege“ statt. Nach Befüllen des Belegs wird ein Dokument generiert. Mit diesem letzten Schritt muss auch eine Entscheidung für eines der beiden obenstehenden Formate getroffen werden. Im Falle einer XRechnung wird direkt das XML-Dokument erstellt, im Fall von ZUGFeRD wird zunächst ein Dokument über das Vorlagensystem erstellt. Erst bei Konvertierung in ein PDF wird j-lawyer.org eine echte elektronische Rechnung in das PDF einbetten.

Die Struktur einer elektronischen Rechnung ist streng formalisiert. Insbesondere sind eigene Spaltenlayouts – bspw. den RVG-Faktor in separater Spalte – in den Standards nicht abbildbar.

Rechnungen, die durch j-lawyer.org generiert oder von außen empfangen und als Dokument zur Akte gespeichert worden sind, können entsprechend visualisiert werden. Im Dokumente-Tab der Akte wurden dazu verschiedene Viewer entwickelt und erweitert. So hat zum Beispiel der PDF-Viewer zusätzliche Tabs erhalten, welche einen Einblick in die Rohform der elektronischen Rechnung sowie deren Darstellung als HTML ermöglichen. Eine Rechnungskontrolle sollte niemals ausschließlich anhand eines PDFs durchgeführt werden, sondern immer die elektronische Rechnung mit einschließen. Technisch ist es möglich, dass beide – im selben Dokument vorhandenen – Daten abweichende Informationen enthalten. Eine solche Rechnung wäre zu hinterfragen.

![Abbildung 22](../images/j-lawyer-org-UserGuide-de-028.png)


## Zeiterfassung {#zeiterfassung}



Die Konfiguration und das Buchen von Zeiten sind als Videotutorial in der j-lawyer.ACADEMY verfügbar: <https://j-lawyer.cloud/j-lawyer-academy/>

### Projekt- / aktenbezogene Stundensätze



Alle relevanten Stundensätze lassen sich im Menü unter „Einstellungen“ – „Zeiterfassung“ – „Zeiterfassungspositionen“ verwalten. Die dort hinterlegten Positionen oder Stundensätze lassen sich dann bei Buchung einer Zeit auswählen.

In manchen Fällen kann es sinnvoll sein, die Menge der auswählbaren Positionen für ein Projekt zu beschränken – bspw. weil man ausschließen möchte, versehentlich einen Stundensatz zu wählen, der mit dem Auftraggeber nicht vereinbart wurde. Dazu kann direkt im Zeiterfassungsprojekt (Akte öffnen, Tab „Finanzen“, Sub-Tab „Zeiterfassung“, dort ein vorhandenes Projekt öffnen) eine entsprechende Beschränkung konfiguriert werden:

![Abbildung 23](../images/j-lawyer-org-UserGuide-de-030.png)


### Projektumfang/-leistung beschränken



Sofern benötigt, lässt sich die Leistung / lassen sich die Kosten eines Zeiterfassungsprojektes beschränken, bspw. weil ein Auftraggeber nur ein Kontingent von x Euro in Auftrag gegeben hat.

Dazu wird direkt im Projekt ein Netto-Limit hinterlegt. Es spielt also keine Rolle, mit welchen (auch unterschiedlichen) Stundensätzen gebucht wird – die Anwendung wird dabei unterstützen, dass nicht mehr geleistet als bestellt wurde.

![Abbildung 25](../images/j-lawyer-org-UserGuide-de-031.png)


Nach Aktivierung eines Limits werden sowohl in der Akte als auch beim Buchen von Zeiten Hinweise in Form kleiner Diagramme mit Farbgebung angezeigt, bspw. wie folgt:

![Abbildung 26](../images/j-lawyer-org-UserGuide-de-032.png)


Verweilt man mit dem Mauszeiger auf dem Diagramm, werden weitere Informationen eingeblendet, bspw. die prozentuale Abarbeitung und das absolute Limit.

Wird ein Limit erreicht oder überschritten, so wird der „Finanzen“-Tab der Akte rot eingefärbt.

### Zeiten erfassen



Zeiten können erfasst werden, indem in der Akte oben rechts auf die Stoppuhr oder – unabhängig von der aktuellen Ansicht – in der Fußzeile der Anwendung auf das Stoppuhrsymbol geklickt wird. Danach im Popup links das zu verwendende Zeiterfassungsprojekt durch Klick auf das Playzeichen in die rechte Spalte zur Bearbeitung hinzufügen. Dort kann etwa durch Klick auf das große grüne Playzeichen die Zeit gestartet, später gestoppt und auch noch verändert werden durch Klick in das Datums- und Uhrzeitenfeld, um ordnungsgemäße Korrekturen vorzunehmen. Der korrekte Stundensatz kann ausgewählt werden und darunter eine Beschreibung hinzugefügt werden, die in das Rechnungsdokument übernommen werden kann (der Mandant also ggf. sieht). Mit einem Klick auf die Diskette rechts vom Eintrag speichert man diesen.

Soll keine Erfassung durch Stoppuhr genutzt, sondern die Zeit manuell angegeben werden, so gibt es die Möglichkeit, oberhalb der Beschreibung einer zu erfassenden Zeit eine Eingabe in der Form 2h45m (Beispiel für 2 Stunden und 45 Minuten) zu tätigen und mit Enter zu bestätigen.
