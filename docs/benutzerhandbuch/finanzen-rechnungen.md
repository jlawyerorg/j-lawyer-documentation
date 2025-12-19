# Rechnungen erstellen

### Rechnungen / Belege erstellen {#rechnungen}

Rechnungen (oder Belege im Allgemeinen) können im Tab „Finanzen" einer Akte erstellt werden („+"-Button im Sub-Tab „Belege"). Nach einer Bestätigung der Belegart und des Nummernkreises (Button hinter „Typ") sind auch alle weiteren Kopfinformationen für eine Bearbeitung freigegeben.

In einem nächsten Schritt ist der Beleg mit Positionen zu befüllen. Es gibt folgende Möglichkeiten, um Positionen hinzuzufügen:

#### Beleg vorbereiten
- Gehe in einer Akte auf den Reiter oben „Finanzen".

- Gehe dort auf den Menüpunkt links „Belege".

- Klicke nun auf das Pluszeichen.

- Wähle den Typ aus (z.B. „Rechnung" für die Erstellung einer Rechnung).

- Wähle den verwendeten Nummernkreis aus. Beachte dabei, dass Rechnungsnummern nur einmalig verwendet werden können und automatisch erstellt werden. Bei einer Testrechnung solltest du also den „Testnummernkreis" anwählen, für eine „echte Rechnung" den „Standardnummernkreis".

- Zur automatischen Vergabe der Rechnungsnummer und Eröffnung der Möglichkeit, weitere Felder auszufüllen, klicke nun auf den Haken neben dem „Typ" der „Rechnung".

#### Position hinzufügen: manuell / vollständige händische Eingabe
- Im Reiter „Positionen" fügt man eine Rechnungsposition hinzu, indem man über das Pluszeichen eine frei eintragbare Position erstellt. Die Menge und der Preis können noch manuell angepasst werden.

#### Position hinzufügen: erfasste Zeiten abrechnen

Bevor eine Rechnung erstellt wird, erstellt man zunächst ein Zeiterfassungsprojekt und erfasst Zeiten (siehe Kapitel „Zeiterfassung").
- Im Reiter „Positionen" fügt man eine Rechnungsposition hinzu, indem man über das den Stoppuhr-Buton die zu übernehmenden Zeiten auswählt und auf „in Rechnung übernehmen" klickt. Pro Stundensatz werden Zeiten zu einer gemeinsamen Rechnungsposition zusammengefasst. Im Leistungsnachweis (der automatisch in das Rechnungsdokument aufgenommen werden kann) wird trotzdem ein detaillierter Nachweis der einzelnen Zeiten ersichtlich.

#### Position hinzufügen: aus Gebührenrechner / Plugin
- Im Reiter „Positionen" oben auf das Symbol für „Positionen aus Rechnungsplugin übernehmen" klicken und einen Berechner auswählen, bspw. „Rechnung RVG Wertgebühren".

- Relevante Gebühreneingaben tätigen

- Button ganz unten nutzen: „als Rechnung". Daraufhin werden die Gebührenpositionen in den Beleg aufgenommen.

#### Belegdokument erstellen

Die verfügbaren Platzhalter für Belegvorlagen sind unter [Platzhalter für Belege / Rechnungen](dokumentenmanagement/vorlagen.md#platzhalter-fur-belege-rechnungen) dokumentiert.

- Im Reiter Dokumente klickt man auf „erstellen", „elektronische Rechnung" und wähle die gewünschte Rechnungsvorlage aus und gehe auf „erstellen und öffnen". Hinweis: Bei der Auswahl des E-Rechnungs-Formates sollte „Elektronische Rechnung (an Unternehmen)" ausgewählt werden, wenn die Rechnung an Unternehmen oder Verbraucher gestellt wird.

- Im nun geöffneten Rechnungsdokument kann jetzt das Layout angepasst werden. Inhaltliche Angaben, die auch im maschinenlesbaren Format enthalten sind (wie Rechnungssumme oder Rechnungsempfänger), sollten nicht mehr verändert werden.

- Nach einem speichern und schließen des Dokuments speichert man im j-lawyer das Popup des Rechnungsfensters und geht in der Akte auf Dokumente. Dort klickt man mit der rechten Maustaste auf das Rechnungsdokument und wählt aus „als pdf zur Akte speichern". Nun ist das Rechnungsdokument als pdf in der Akte.

- Auf das Rechnungsdokument als pdf klickt man nun mit einem Rechtsklick und wählt aus „@ als pdf versenden", um die Rechnung per E-Mail an den Mandanten zu senden.

### Elektronische Rechnungen ("E-Rechnung") {#e-rechnung}

j-lawyer.org kann Rechnungen sowohl im ZUGFeRD-Standard („Zentraler User Guide des Forums elektronische Rechnung Deutschland") als auch als Xrechnung erstellen und lesen.

ZUGFeRD kommt primär zwischen Unternehmen zum Einsatz und beinhaltet die Erstellung von PDF-Dokumenten mit einem eingebetteten „Datenschnipsel", welcher die Rechnung maschinell lesbar macht.

XRechnung wird primär für die Rechnungsstellung eines Unternehmens an einen öffentlichen Auftraggeber genutzt. Es handelt sich um ein XML-Dokument, das nur maschinell lesbar ist. In der Adressverwaltung sollte in diesen Fällen am Rechnungsempfänger eine sogenannte „Leitweg-ID" hinterlegt werden, welche den Rechnungsempfänger eindeutig kennzeichnet und ein automatisches „Routing" innerhalb der Behörden ermöglicht.

Die Rechnungserstellung findet – wie auch in den Version vor j-lawyer.org 3.0 – in der Akte im Tab „Finanzen", dort unter „Belege" statt. Nach Befüllen des Belegs wird ein Dokument generiert. Mit diesem letzten Schritt muss auch eine Entscheidung für eines der beiden obenstehenden Formate getroffen werden. Im Falle einer XRechnung wird direkt das XML-Dokument erstellt, im Fall von ZUGFeRD wird zunächst ein Dokument über das Vorlagensystem erstellt. Erst bei Konvertierung in ein PDF wird j-lawyer.org eine echte elektronische Rechnung in das PDF einbetten.

Die Struktur einer elektronischen Rechnung ist streng formalisiert. Insbesondere sind eigene Spaltenlayouts – bspw. den RVG-Faktor in separater Spalte – in den Standards nicht abbildbar.

Rechnungen, die durch j-lawyer.org generiert oder von außen empfangen und als Dokument zur Akte gespeichert worden sind, können entsprechend visualisiert werden. Im Dokumente-Tab der Akte wurden dazu verschiedene Viewer entwickelt und erweitert. So hat zum Beispiel der PDF-Viewer zusätzliche Tabs erhalten, welche einen Einblick in die Rohform der elektronischen Rechnung sowie deren Darstellung als HTML ermöglichen. Eine Rechnungskontrolle sollte niemals ausschließlich anhand eines PDFs durchgeführt werden, sondern immer die elektronische Rechnung mit einschließen. Technisch ist es möglich, dass beide – im selben Dokument vorhandenen – Daten abweichende Informationen enthalten. Eine solche Rechnung wäre zu hinterfragen.

![Abbildung 22](../images/j-lawyer-org-UserGuide-de-028.png)
