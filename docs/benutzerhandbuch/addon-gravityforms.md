# Add-Ons: Gravity Forms-Anbindung

### Wordpress-Formulare mit der Kanzleisoftware integrieren



Oftmals ist die Kanzlei-Website der erste Anlaufpunkt für Mandanten (bspw. in der Form einer Online-Mandatsannahme), oder es gibt den Bedarf, umfangreichere Informationen von externen Parteien über die eigene Website zu erheben. Sind diese Daten einmal erfasst, müssen Sie häufig von Hand in die eigene Aktenverwaltung überführt, um später weiterverarbeitet und genutzt zu werden. Das Übertragen der Daten aus den Onlineformularen in die Akten ist ein hoher manueller Aufwand.

Um diesen manuellen Aufwand zu automatisieren, gibt es in j-lawyer.org ein eigenes Falldatenblatt „Gravity Forms“ (Menü „Einstellungen“ – „Akten“ – „Falldatenblätter“). Gravity Forms ist ein Online-Formulareditor für Wordpress-Websites, der ohne Programmierkenntnisse verwendet werden kann. Ist ein solches Formulare einmal erstellt, ist der Arbeitsfluss wie folgt:
- externe Partei füllt Formular aus
- Kanzlei erhält eine E-Mail-Benachrichtigung
- Kanzlei öffnet die relevante Akte und fügt ein Gravity-Forms-Falldatenblatt hinzu
- Über das Falldatenblatt wird das ausgefüllte Formular mit wenigen Klicks in die Kanzleisoftware importiert
- Über das Vorlagensystem stehen alle Eingabefelder des Formulars für eine automatische Dokumenterstellung zur Verfügung.

### Voraussetzungen



Um Onlineformulare anbinden zu können, benötigt man eine Wordpress-Website mit installiertem Gravity Forms-Plugin.
- Option 1: eigene Wordpress-Installation betreiben

Hat man bereits eine eigene Wordpress-Installation und plant die intensive Nutzung der Formulare, so ist es sinnvoll Gravity Forms als Plugin hinzuzufügen. Ein Download ist hier möglich: https://rocketgenius.pxf.io/0JBoXO (*)
- Option 2: fertige Wordpress-Installation samt Gravity Forms nutzen

Hat man keine Wordpress-Installation oder plant nur sporadisch Formulareingaben von externen Parteien zu verarbeiten, so kann man eine fertige Installation nutzen. Dazu erhält man einen an den eigenen Unternehmensnamen angelehnten Bereich unter einer repräsentativen Domain. Mehr Informationen: https://www.j-dimension.com/angebote/j-lawyer-org/

Damit die Kanzleisoftware auf die Formulardaten zugreifen kann, müssen Zugangsschlüssel erstellt werden. Im Wordpress-Dashboard zu „Formulare“ – „Einstellungen“ navigieren. Dort zur Ansicht „REST API“ wechseln und per „Add Key“ einen neuen Schlüssel erzeugen.

![Abbildung 58](../images/j-lawyer-org-UserGuide-de-064.png)


Im Rahmen der Schlüsselerstellung erhält mein zwei Werte, einer ist vergleichbar mit einem Nutzernamen und beginnt mit dem Präfix „ck_“, der andere ist der eigentliche Schlüssel (vergleichbar mit einem Passwort). Diese Werte sind zu notieren / kopieren.

Anschließend ist ein separates Falldatenblatt für die Anbindung von Gravity Forms zu installieren: Menü „Einstellungen“ – „Akten“ – „Falldatenblätter“. Nach erfolgreicher Installation ist der Einstellungen-Knopf am Falldatenblatt aktiv. Über diesen können die API-Schlüssel hinterlegt werden. Es können bis zu fünf verschiedene Websites / Wordpress-Installationen angebunden werden.
- Bezeichung Website: frei wählbar
- API-Endpunkt: hier ist in der Regel ausschließlich der Domainname anzupassen, der Rest bleibt unverändert
- Nutzer / API-Key: den mit „ck_“ beginnenden Wert eintragen, den man bei der Schlüsselerstellung in Wordpress erhalten hat
- Passwort: den mit „cs_“ beginnenden Wert eintragen, den man bei der Schlüsselerstellung in Wordpress erhalten hat

![Abbildung 59](../images/j-lawyer-org-UserGuide-de-065.png)


Fertig- Ihre Onlineformulare sind nun angebunden.

(*) Die mit Sternchen (*) gekennzeichneten Links sind sogenannte Affiliate-Links. Wenn Sie auf so einen Affiliate-Link klicken und über diesen Link einkaufen, bekomme ich von dem betreffenden Online-Shop oder Anbieter eine Provision. Für Sie verändert sich der Preis nicht.

Einnahmen kommen zu 100% dem kostenfreien Open Source-Projekt „j-lawyer.org“ (Kanzleisoftware) zugute.

### Übernehmen von Formulardaten



Füllt eine externe Partei ein Formular aus, erhält man in der Regel eine E-Mail-Benachrichtigung. Diese kann zum Anlass genommen werden, in einer relevanten Akte ein Falldatenblatt vom Typ „Gravity Forms“ zu erstellen. Über den Tab „Wordpress-Import“ des Falldatenblattes gelangen die Formulardaten in die Akte.

Der „?“-Knopf zeigt die Platzhalternamen für jedes Formularfeld an. Die Platzhalter lassen sich – wie die üblichen Akten- und Adressenplatzhalter – automatisch in Dokumente übernehmen.

### Platzhalternamen definieren



Ohne weiteres Zutun vergibt Gravity Forms numerische Platzhalternamen. Diese haben einen geringen „Wiedererkennungswert“ und können das Erstellen von Vorlagen erschweren. Aus diesem Grund wertet das Falldatenblatt zusätzlich das sogenannten „Admin-Etikett“ aus.

Im Formulareditor von Gravity Forms hat jedes Oberflächenelement im Abschnitt „Erweitert“ ein Attribut „Admin-Etikett“. Dies kann vom Anwender frei verwendet werden. Vergibt man für ein Feld das Admin-Etikett „WUNSCHTERMIN“, so lautet der Platzhalter für Vorlagen „{{FORM_WUNSCHTERMIN}}“

![Abbildung 60](../images/j-lawyer-org-UserGuide-de-066.png)


### Adressbucheinträge aus Formulardaten erstellen



Das Gravity Forms-Falldatenblatt bietet die Möglichkeit, aus Formulardaten neue Einträge im Adressbuch der Kanzleisoftware zu generieren. Dabei wird ein Dialog geöffnet, der eine Zuordnung der Formularfelder zu Adressfeldern erlaubt. Um diesen Vorgang weitestgehend zu automatisieren, können im Formular die Felder (deren „Admin-Feld-Etiketten“) so benannt werden, dass j-lawyer eine automatische Zuordnung anwenden kann:
- E-Mail: Admin-Feld-Etikett sollte „EMAIL“ enthalten (bpsw. MANDANT_EMAIL oder EMAIL_ANFRAGENDE – „EMAIL“ muss also lediglich enthalten sein)
- Telefonnummer:  Admin-Feld-Etikett sollte „TELEFON“ enthalten
- Mobilnummer:  Admin-Feld-Etikett sollte „MOBIL“ enthalten
- Faxnummer:  Admin-Feld-Etikett sollte „FAX“ enthalten
- PLZ:  Admin-Feld-Etikett sollte „PLZ“ enthalten
- Ort:  Admin-Feld-Etikett sollte „ORT“ enthalten
- Land:  Admin-Feld-Etikett sollte „LAND“ enthalten
- Strasse:  Admin-Feld-Etikett sollte „STRASSE“ enthalten
- Hausnummer:  Admin-Feld-Etikett sollte „HAUSNR“ enthalten
- Vorname: Admin-Feld-Etikett sollte „VORNAME“ enthalten
- Name: Admin-Feld-Etikett sollte „NAME“ enthalten
- Unternehmensname: Admin-Feld-Etikett sollte „UNTERNEHMEN“ enthalten
- Beruf: Admin-Feld-Etikett sollte „BERUF“ enthalten
- Funktion: Admin-Feld-Etikett sollte „FUNKTION“ enthalten
- Abteilung: Admin-Feld-Etikett sollte „ABTEILUNG“ enthalten
