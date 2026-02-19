# PDF-Funktionen {#pdf-konvertierung}

## PDF-Konvertierung

j-lawyer.org ist in der Lage, die meisten Dokumentenformate automatisch im Hintergrund nach PDF zu konvertieren, insbesondere bei:

- Versand von Dokumenten via Email
- Versand von Dokumenten über die Drebis-Schnittstelle
- Versand von Dokumenten als Fax via Sipgate

Die Konvertierung wird dabei für den Nutzer nicht direkt sichtbar im Hintergrund durchgeführt.

## Akte / ausgewählte Dokumente als ein PDF exportieren

Mittels eines Buttons oberhalb der Dokumentenliste lassen sich alle ausgewählten Dokumente in ein einzelnes PDF exportieren. Die relevanten Dokumente können mittels Dokumentselektion und Ordnerselektion bestimmt werden.

![Abbildung 18](../../images/j-lawyer-org-UserGuide-de-024.png)

Die Sortierung der Dokumente wird in das PDF übernommen, daher empfiehlt sich das bewusste Sortieren nach dem gewünschten Kriterium, bevor der Exportprozess gestartet wird.

Der Exportprozess läuft wie folgt ab:

1. **Prüfung der Dateiformate**: nicht unterstützte Formate (bspw. können Sprachmemos nicht in PDF konvertiert werden) werden ausgegeben. E-Mails werden samt Ihrer Anlagen konvertiert, sofern der Anlagentyp nach PDF konvertiert werden kann.

2. **Übersicht der Dokumente**: Die einzelnen Dokumente werden in einer Übersicht dargestellt, samt Seitenzahlen und Dateigrößen. Für das zu erstellende Gesamt-PDF werden die Summen für beide Wert ausgegeben. In diesem Schritt können die Dokumente mittels auf-/ab-Tasten in eine abweichende Reihenfolge gebracht werden.

3. **Vorschau und Export**: Im nächsten Schritt werden zwei Seiten generiert: eine mit den Stammdaten der Akte, sowie eine weitere mit einem Inhaltsverzeichnis. Das Ergebnis kann als Vorschau betrachtet werden. In diesem Schritt kann der Export in die Akte, in ein Verzeichnis auf dem Arbeitsplatz, oder beides gewählt werden.

Bei sehr vielen und / oder sehr umfangreichen Dokumenten kann der Export eine Weile in Anspruch nehmen.

Das Gesamt-PDF ist mit Lesezeichen versehen, um schnell zwischen den ehemaligen Einzeldokumenten springen zu können.

## PDFs schwärzen / anonymisieren

Über das Kontextmenü auf ein PDF („PDF und Konvertierung" – „PDF schwärzen") lassen sich PDF-Dokumente anonymisieren, d.h. es werden Inhalte und Metadaten angepasst:

- Anmerkungen können automatisch entfernt werden
- Metadaten, bspw. Autor, Titel, Betreff, Schlüsselwörter, erstellende Anwendung, Erstellungsdatum und Änderungsdatum werden entfernt oder auf einen Standardwert gesetzt
- Wörter werden im PDF geschwärzt und der ursprüngliche Inhalt entfernt. Eine Suche nach diesen Wörtern ist dann nicht mehr möglich.

Zum Entfernen mehrerer Wörter können diese durch Komma separiert angegeben werden. Voreingestellt sind:

- Aktenzeichen
- Beteiligtendaten: Bankverbindung, beA Safe-ID, Geburtsdatum und -name, Anschrift, Unternehmen und Abteilung, Sterbedatum, Kontaktdaten, Versicherungsinformationen, TIN und UstId

Es gibt im Dialog die Möglichkeit, weitere anonymisierungswürdige Terme KI-gestützt extrahieren zu lassen.

Das anonymisierte Dokument kann dann zur Akte gespeichert werden.

!!! warning "Hinweis"
    Die Qualität der Anonymisierung ist bei OCR-erkannten Texten stark abhängig von der Qualität der Texterkennung. Bitte prüfen Sie das Resultat vor einer weiteren Verwendung sorgfältig!

## PDFs bearbeiten mit Foxit Reader

j-lawyer.org öffnet Dokumenttypen in LibreOffice, sofern unterstützt. Alle anderen Dokumenttypen werden mit dem auf dem System installierten "Standardprogramm" geöffnet. Dabei ist es dann vom Verhalten des externen Programmes abhängig, ob Änderugen am Dokument verlässlich in der Akte gespeichert werden.

Am Beispiel von PDFs auf Windows wird hier beschrieben, wie mit der kostenlosen Anwendung "Foxit Reader" (<https://www.foxitsoftware.com/de/pdf-reader/>) in PDF eingefügte Lesezeichen und Kommentare direkt in der Akte gespeichert werden können.

Weitere Informationen zum Konfigurieren externer Programme finden sich unter [Externe Programme](externe-programme.md).

### Einrichtung

1. Zuerst wird die Anwendung heruntergeladen und installiert. Nach dem Öffnen wird über Menü "Datei" und "Einstellungen" in der Kategorie "Dokumente" die oberste Option "Mehrere Instanzen zulassen" aktiviert und anschließend der Einstellungsdialog und die Anwendung beendet.

2. Im j-lawyer.org Client öffnet man das Menü "Einstellungen" - "Modul 'Dokumente'" - "externe Programme". Im Eingabefeld "Dateitypen" gibt man `pdf` ohne führenden Punkt ein und klickt anschließend "Hinzufügen". In der Liste im linken Bereich erscheint nun pdf als Auswahlmöglichkeit. Man wählt den Eintrag aus und klickt dann auf den […]-Knopf hinter "Ausführbare Datei". Navigieren Sie zur Datei "FoxitReader.exe", der Standardpfad ist unten im Bild exemplarisch gezeigt.

![Abbildung 15](../../images/j-lawyer-org-UserGuide-de-021.png)

3. Nach erfolgter Auswahl wird der Dialog mit "Speichern", gefolgt von "Schliessen" beendet. Foxit Reader ist nun als externe Anwendung zur Bearbeitung von PDFs registriert.

### Verwendung

Aus einer Akte heraus öffnet ein Doppelklick auf ein PDF-Dokument nun Foxit Reader. Dort vorgenommene Änderungen werden in der Akte gespeichert.

Unter Umständen kann der j-lawyer.org Client das Schliessen von Dokumenten nicht korrekt erkennen. Wird das selbe Dokument dann erneut geöffnet, so erscheint folgende Meldung:

![Abbildung 16](../../images/j-lawyer-org-UserGuide-de-022.png)

Die Frage kann dann einfach mit "Ja" quittiert werden.

!!! info "Hinweis"
    Die Einstellung ist an jedem Arbeitsplatz durchzuführen. Sie wird im Windows-Nutzerprofil gespeichert.
