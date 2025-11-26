# Fehlerbehebung

### LibreOffice öffnet Dokumente immer im Hintergrund {#libreoffice-hintergrund}



Sollte beim Öffnen von Dokumenten aus einer Akte heraus die LibreOffice-Anwendung immer im Hintergrund starten, so kann wie folgt erzwungen werden, das Dokument im Vordergrund zu öffnen:
- LibreOffice Writer öffnen
- Menü “Extra” - “Optionen” anklicken
- Eintrag “LibreOffice” - “Erweitert” wählen
- Rechts unten Button "Experteneinstellungen öffnen" klicken
- ins Suchfeld "ForceFocusAndToFront" eingeben und auf suchen klicken
- Eintrag "NewDocumentHandling" markieren und unten auf Bearbeiten klicken
- Der Wert des Eintrages sollte dann von false auf true wechseln

Dann mit OK betätigen und LibreOffice (Writer und Calc) sollten die Dokumente nun auch im Vordergrund öffnen.

### Probleme mit Kopieren und Einfügen unter Mac OS



Unter Mac OS ist mit CMD(“Apfeltaste”)+C ein Kopieren, mit CMD(“Apfeltaste”)+V ein Einfügen möglich.

j-lawyer.org wird plattformübergreifend für Windows, Linux und Mac OS entwickelt und es gibt an dieser Stelle eine Besonderheit für Mac OS-Nutzer zu beachten: die “Schlüsseltest” innerhalb von j-lawyer.org ist Strg / Ctrl. Man verfährt daher wie folgt:

Kopieren aus einer Mac OS-Anwendung nach j-lawyer.org:
- In Mac OS-Anwendung markieren und CMD+C
- In j-lawyer.org anschließend Strg+V

Und für das Kopieren aus j-lawyer.org in eine Mac OS-Anwendung:
- In j-lawyer.org markieren und Strg+C
- In Mac OS-Awendung anschließend CMD+V

### j-lawyer.BOX: Login Administrationsoberfläche schlägt fehl {#box-login}



Ist ein Login in der browserbasierten j-lawyer.BOX-Administrationsoberfläche nicht möglich, so kann das folgende Gründe haben:
- Der Nutzer hat nicht die notwendigen Berechtigungen: in der Nutzerverwaltung prüfen ob “volle Administrationsrechte” vergeben sind.
- Das Passwort des Nutzer enthält Umlaute oder bestimmte Sonderzeichen. Aufgrund eines Fehlers in einer verwendeten Bibliothek ist dies momentan nicht möglich. Es empfiehlt sich die Verwendung von a-z, A-Z, 0-9, -+{[]}<>_.:,;
- Der j-lawyer.org Serverdienst generiert Fehler und muss neu gestartet werden (bspw. über den Reiter “j-lawyer.BOX” im Logindialog des j-lawyer.org Clients)

### j-lawyer.BOX: Login in j-lawyer.org Client schlägt fehl



Ist ein Login im j-lawyer.org Client nicht möglich, so ist in einem ersten Schritte über den Tab “j-lawyer.BOX” im Logindialog ein Neustart des Serverdiensts durchzuführen:
- root-Passwort eingeben: es handelt sich um das Passwort des Betriebssystemnutzers “root” - Sie finden das Passwort auf der mit der j-lawyer.BOX ausgelieferten “Identity Card” (der Teil nach dem Schrägstrich).
- Den mittleren Knopf nutzen (wird die Maus über den Knopf bewegt erscheint der Hinweis “j-lawyer.org Serverdienst neu starten”
- Wird die Meldung durch Ausgabe eines grünen Infotextes quittiert, so ist der Dienstneustart erfolgreich initiiert. Nach ca. zwei Minuten ist ein Login wieder auf üblichem Weg möglich.
- Wird die Meldung durch Ausgabe eines roten Textes quittert, so ist ein Neustart des Serverdienstes fehlgeschlagen. In dem Fall ist ein manuelles Login auf der j-lawyer.BOX notwendig.

Manuelles SSH-Login auf der j-lawyer.BOX:
- Linux und macOS
    - Terminal öffnen
    - Kommando ausführen: ssh root@j-lawyer-box (und ENTER)
    - Es wird ein Passwort abgefragt. Es handelt sich um das Passwort des Betriebssystemnutzers “root” - Sie finden das Passwort auf der mit der j-lawyer.BOX ausgelieferten “Identity Card” (der Teil nach dem Schrägstrich).
    - Nach erfolgreichem Login folgendes Kommando ausführen: 
sudo service j-lawyer-server restart (und ENTER)
    - Die Ausführung dieses Befehl kann mehrere Sekunden in Anspruch nehmen.
    - Die Terminalsitzung mit folgendem Kommando beenden: exit (und ENTER)
    - Nach ca. zwei Minuten ist ein Login über den j-lawyer.org Client wieder auf üblichem Weg möglich.
- Windows:
    - Putty herunterladen – Quelle: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
    - Abbildung 66: SSH-Verbindung zur j-lawyer.BOX mit putty.exe
         
        Nach dem Start von putty.exe bitte folgende Einstellungen vornehmen (in der Regel ist nur der Wert unter “Hostname (or IP address)” zu ändern):
    - Es wird ein Passwort abgefragt. Es handelt sich um das Passwort des Betriebssystemnutzers “root” - Sie finden das Passwort auf der mit der j-lawyer.BOX ausgelieferten “Identity Card” (der Teil nach dem Schrägstrich).
    - Nach erfolgreichem Login folgendes Kommando ausführen: 
sudo service j-lawyer-server restart (und ENTER)
    - Die Ausführung dieses Befehl kann mehrere Sekunden in Anspruch nehmen.
    - Die Terminalsitzung mit folgendem Kommando beenden: exit (und ENTER)
    - Nach ca. zwei Minuten ist ein Login über den j-lawyer.org Client wieder auf üblichem Weg möglich.

### “Unexpected Error” bei Erstellen von Dokumenten



Wird der j-lawyer.org Server auf einem Linuxsystem ohne grafische Oberfläche betrieben, so kann es bei der Erstellung eines Dokuments zu einem Fehler mit Ausgabe „Unexpected Error“ kommen, wenn eine Berechnung aus bspw. einem RVG-Plugin per Platzhalter übernommen werden soll.

Das Problem lässt sich durch Installation der folgenden Pakete beheben:
- xvfb
- libxext6
- libxi6
- libxtst6
- libxrender1
- libongoft2-1.0.0

Anschließend muss die Datei sudo vim /etc/java-8-openjdk/accessibility.properties bearbeitet und die folgende Zeile auskommentiert werden:

assistive_technologies=org.GNOME.Accessibility.AtkWrapper
