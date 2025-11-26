# Add-Ons: Nextcloud-Integration

Nextcloud (https://nextcloud.com) ist eine Open Source Cloudlösung, die sich auch selbst installieren und betreiben lässt. Sie beinhaltet u.a. Dateispeicherung und -freigaben, Kalender, Kontakte, E-Mail, u.v.m.

### Nextcloud-Installation für Dokumentfreigaben nutzen



Die Verbindungs- und Zugangsinformationen werden über die Nutzerverwaltung an den gewünschten Nutzerkonten hinterlegt. Es werden folgende Angaben benötigt:
- Servername: Name des Servers ohne Prokoll (ohne http / https), bspw. www.advobox.com
- Port: 443 wenn der Server https unterstützt, ansonsten in der Regel 80 oder 8080
- Pfad: Unterverzeichnis, in welchem die Nextcloud installiert ist.
- SSL: aktivieren, wenn der Server https unterstützt, ansonsten inaktiv setzen
- Nutzername, Passwort: die Zugangsdaten des Nutzers dieser Nextcloud

Hinweise zur „Pfad“-Angabe: Ist die Nextcloud direkt unter einer Domain abrufbar, bspw. https://cloud.musterkanzlei-12345.de, so bleibt die Pfadangabe leer. Wird die Nextcloud jedoch über  https://www.musterkanzlei-12345.de/meinecloud abgerufen, so ist der Werte „meinecloud“ (ohne Anführungszeichen) als Pfad anzugeben.

Die Verknüpfung mit dem Nutzer der Kanzleisoftware gibt die größtmögliche Flexibilität, bspw. die gemeinsame Nutzung eines Nextcloud-Zugangs für alle Mitarbeiter der Kanzlei, oder die Nutzung separater Nextcloud-Zugänge je Kanzleisoftwarenutzer zwecks Nutzung unterschiedlicher Berechtigungen / Inhalte oder auch die Nutzung völlig unterschiedlicher Nextcloud-Installationen, bspw. in Bürogemeinschaften.

### Freigeben von Dokumenten {#dokumente-freigeben}



Nach erfolgreicher Verknüpfung eines Nextcloud-Zugangs können aus der Akte heraus ein oder mehrere Dokumente selektiert und per Aktionsdropdown freigegeben werden (“Freigabe senden”). Anschließend kann in einem Dialog entweder eine vorhandene Freigabe genutzt und die Dokumente dorthin hochgeladen oder eine neue Freigabe erstellt werden.

![Abbildung 57](../images/j-lawyer-org-UserGuide-de-057.png)


Der Empfänger der Freigabe als auch das Aktenzeichen können automatisch als Ordner verwendet werden, auch in Kombination.

Die Berechtigungen können so definiert werden, dass der Beteiligte auch Dokumente editieren oder neue hinzuladen darf.

Optional kann die Freigabe mit einem Passwortschutz versehen werden. Die Freigabelinks in Nextcloud sind jedoch willkürliche Ziffer-Buchstaben-Kombinationen die nicht zu “erraten” sind, insofern ist auch eine Freigabe ohne Passwort akzeptabel, wenn der Freigabelink auf sicherem Weg übertragen wird (bspw. per verschlüsselter E-Mail oder Messengern wie Signal oder WhatsApp).

Nach Erstellen der Freigabe lässt sich der Freigabelink wahlweise in die Zwischenablage kopieren oder es öffnet sich ein E-Mail-Versandfenster, in welchem der Link voreingetragen ist. Soll für den Versand per E-Mail eine E-Mail-Vorlage verwendet werden, so ist der Freigabelink als Platzhalter {{CLOUD_LINK}} einbindbar.

Die voreingestellte Gültigkeitsdauer für Freigaben beträgt 30 Tage.

### Synchronisieren des Adressbuchs (Nextcloud, mobile Geräte) {#adressbuch-sync}



Adressen einer j-lawyer.org Installation können in eine Nextcloud synchronisiert werden. Dabei werden all jene Adressbucheinträge synchronisiert, die in mindestens einer Akte als Beteiligte geführt sind.

Vorbereitend sollte in der Oberfläche der Nextcloud ein separates Adressbuch angelegt werden, welches ausschließlich in Verbindung mit j-lawyer.org verwendet wird. So kann das Adressbuch bei Bedarf vollständig neu synchronisiert oder neu aufgebaut werden, ohne andere Adressdaten zu beeinflussen.

Anschließend wird über das Menü „Einstellungen“ – „Adressen“ – „Synchronisation konfigurieren“ die Verbindung zur Nextcloud-Installation hergestellt. An dieser Stelle sollte das gewünschte Zieladressbuch ausgewählt werden. Optional lässt sich das Synchronisieren von Geburtsdaten deaktiveren, sodass bspw. an mobilen Geräten keine überflüssigen Geburtstagsbenachrichtigungen ausgelöst werden. Über das Menü „Einstellungen“ – „Adressen“ – „Synchronisation ausführen“ wird eine Erstsynchronisation durchgeführt. Alle weiteren Datenänderungen werden ab sofort automatisch im Hintergrund in die Nextcloud übertragen.

Bzgl. des Anbindens mobiler Geräte und Mailprogrammen, um die Adressdaten auch dort im Zugriff zu haben, bitte die Nextcloud-Dokumentation konsultieren: https://docs.nextcloud.com/server/19/benutzerhandbuch/contents.html

## Synchronisieren der Kalender (Nextcloud, mobile Geräte) {#kalender-sync}



Termine, Wiedervorlagen und Fristen einer j-lawyer.org Installation können in eine Nextcloud synchronisiert werden. Dabei werden alle offenen / nocht nicht erledigten Einträge synchronisiert, erledigte Einträge werden aus Nextcloud entfernt.

Vorbereitend sollten in der Oberfläche der Nextcloud separate Kalender angelegt werden, welche ausschließlich in Verbindung mit j-lawyer.org verwendet wird. So können diese Kalender bei Bedarf vollständig neu synchronisiert oder neu aufgebaut werden, ohne andere Kalenderdaten zu beeinflussen.

Es ist möglich, für jeden Kalender der Kanzleisoftware einen Nextcloud-Kalender anzubinden, ebenso können mehrere Kanzleisoftwarekalender in den selben Nextcloud-Kalender synchronisiert werden.

Über das Menü „Einstellungen“ – „Kalender“ – „Kalender und Synchronisation konfigurieren“ verknüpft man nun die gewünschten Kalender. Über das Menü „Einstellungen“ – „Kalender“ – „Synchronisation ausführen“ wird eine Erstsynchronisation durchgeführt. Alle weiteren Datenänderungen werden ab sofort automatisch im Hintergrund in die Nextcloud übertragen.

Das „erledigt“-Setzen von Kalendereinträgen führt zum Löschen des dazugehörigen Eintrages im Nextcloud-Kalender. Ist dieses Verhalten nicht erwünscht, so kann in den Einstellungen des Kalenders die Option „erledigte Termine aus Nextcloud löschen“ deaktiviert werden.

Bzgl. des Anbindens mobiler Geräte und Mailprogrammen, um die Adressdaten auch dort im Zugriff zu haben, bitte die Nextcloud-Dokumentation konsultieren: https://docs.nextcloud.com/server/19/benutzerhandbuch/contents.html
