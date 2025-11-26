# Deinstallation

### Deinstallation auf Windows-Systemen



Sowohl der j-lawyer.org Server als auch der j-lawyer.org Client werden wie allgemein üblich über die Systemsteuerung entfernt: Startmenü → “Programm ändern oder entfernen” → markieren → “Deinstallieren”. Anschließend folgen Sie den Anweisungen.

Hinweis: Das vom j-lawyer.org Server genutzte MySQL wird nicht automatisch deinstalliert, da nicht sichergestellt werden kann, ob zwischenzeitlich vom Anwender installierte andere Applikationen MySQL nutzen. MySQL kann daher separat auf gleichem Weg wie oben beschrieben deinstalliert werden.

### Deinstallation auf Linux-Systemen



Sowohl der j-lawyer.org Server als auch der j-lawyer.org Client werden mit uninstall-Skripten ausgeliefert, die auf Systemen mit grafischer Oberfläche einen Deinstallations-Assistenten starten, und auf “headless”-Systemen im Konsolenmodus durchlaufen werden. Zum Deinstallieren wechseln Sie in das Installationsverzeichnis (“cd <Ordner>” - bitte für Ihre Gegebenheiten entsprechend anpassen) und führen anschließend folgende Anweisungen aus:

cd /opt/j-lawyer-server

sudo sh uninstall

Hinweis: Die MySQL-Datenbank des j-lawyer.org Servers wird nicht automatisch deinstalliert und kann wie unten aufgeführt gelöscht werden. Es wird das Passwort des MySQL-Nutzers “root” benötigt:

mysql -u root -p

drop database if exists jlawyerdb;

commit;

quit;

### Deinstallation auf Mac OS-Systemen



Zur Deinstallation des j-lawyer.org Servers öffnen Sie die Applikation “Finder” und wechseln in den Ordner “Applications”. Den dort enthaltenen Ordner “j-lawyer-server” öffnen Sie und führen die darin enthaltene Applikation “j-lawyer.org (Server) Uninstaller” aus. Folgen Sie den Anweisungen.

Zur Deinstallation des j-lawyer.org Clients öffnen Sie die Applikation “Finder” und wechseln in den Ordner “Applications”. Die dort vorhandene Applikation “j-lawer.org (Client)” verschieben Sie über ihr Kontextmenü in den Papierkorb.
