# E-Mail-Integration



E-Mail-Postfächer können im Menü „Einstellungen“ – „E-Mail – Postfächer“ konfiguriert werden. Die Zugangs- und Verbindungsdaten werden dort an zentraler Stelle hinterlegt.

Über die Nutzerverwaltung („Einstellungen" – „Nutzer") kann einem oder mehreren Nutzern Zugriff auf eines oder mehrere zentral konfigurierte Postfächer gewährt werden.

### Anbindung von IMAP-Postfächern {#imap-postfaecher}

Für die Anbindung eines Standard-IMAP- oder POP3-Postfachs (z. B. bei IONOS, Strato, All-Inkl oder einem eigenen Mailserver) benötigen Sie lediglich die Zugangsdaten Ihres E-Mail-Anbieters. Die Einrichtung erfolgt im Menü **Einstellungen** → **E-Mail – Postfächer**.

#### Übersicht des Dialogs

Der Konfigurationsdialog ist zweigeteilt:

- **Linke Seite**: Liste aller konfigurierten Postfächer mit den Schaltflächen **+** (neues Postfach anlegen), **Entfernen** und **Duplizieren**.
- **Rechte Seite**: Tabs mit den Einstellungen des ausgewählten Postfachs.

#### Schritt 1: Neues Postfach anlegen

Klicken Sie auf **+**, um ein neues Postfach anzulegen. Wechseln Sie anschließend zum Tab **Postfach** und füllen Sie die folgenden Felder aus:

| Feld | Beschreibung |
|------|-------------|
| Postfachname | Anzeigename des Postfachs in der Postfachliste |
| E-Mail-Adresse | Die E-Mail-Adresse des Postfachs (Pflichtfeld) |
| Absendername | Name, der beim Empfänger als Absender angezeigt wird |

#### Schritt 2: Verbindungsdaten konfigurieren

Wechseln Sie zum Tab **Verbindung**. Hier konfigurieren Sie die Server für den Posteingang und den Postausgang.

**Posteingang**

| Feld | Beschreibung |
|------|-------------|
| Eingangsserver | Hostname des IMAP- oder POP3-Servers (Pflichtfeld) |
| Nutzername | Benutzername für die Anmeldung am Eingangsserver (Pflichtfeld) |
| Kontentyp | Protokoll des Eingangsservers: `imap` oder `pop3`. IMAP ist die bevorzugte Variante. |
| Passwort | Passwort für die Anmeldung am Eingangsserver (Pflichtfeld) |
| SSL/TLS | Verschlüsselte Verbindung verwenden (Standard: aktiv) |

**Postausgang**

| Feld | Beschreibung |
|------|-------------|
| Ausgangsserver | Hostname des SMTP-Servers |
| Nutzername | Benutzername für die Anmeldung am Ausgangsserver |
| Port (optional) | SMTP-Port, falls vom Standard abweichend |
| Passwort | Passwort für die Anmeldung am Ausgangsserver |
| StartTLS | StartTLS-Verschlüsselung verwenden |
| SSL/TLS | SSL/TLS-Verschlüsselung verwenden (Standard: aktiv) |

!!! note "Office 365"
    Für die Anbindung von Office 365-Postfächern nutzen Sie die Felder im Bereich „Office 365" desselben Tabs. Die ausführliche Anleitung finden Sie im Abschnitt [Anbindung von Postfächern mit Azure AD](#azure-ad).

Über die Schaltfläche **Einstellungen testen** können Sie die eingegebenen Verbindungsdaten prüfen. j-lawyer.org versucht dabei, eine Verbindung zum Eingangs- und Ausgangsserver aufzubauen und meldet Erfolg oder Fehler.

#### Schritt 3: Signaturen einrichten (optional)

Im Tab **Signatur (HTML)** können Sie eine HTML-formatierte Signatur erstellen, die beim Verfassen neuer E-Mails automatisch angefügt wird. Der integrierte Editor bietet grundlegende Formatierungsmöglichkeiten.

Alternativ oder ergänzend können Sie im Tab **Signatur (Text)** eine reine Textsignatur hinterlegen, die in reinen Textnachrichten verwendet wird.

#### Schritt 4: Erweiterte Einstellungen (optional)

Der Tab **Erweitert** bietet jeweils einen Bereich für **Posteingang** und **Postausgang**, in dem benutzerdefinierte Konfigurationsparameter im Java-Properties-Format hinterlegt werden können. Dies ist nur in Ausnahmefällen notwendig, z. B. bei ungewöhnlichen Serverkonfigurationen.

#### Schritt 5: Speichern und Zugriff freigeben

Klicken Sie auf **Übernehmen**, um die Einstellungen zu speichern. Damit andere Nutzer auf das Postfach zugreifen können, muss der Zugriff anschließend in der Nutzerverwaltung (**Einstellungen** → **Nutzer**) freigegeben werden.

#### Typische Servereinstellungen

Die folgende Tabelle listet die Serveradressen gängiger deutscher E-Mail-Anbieter auf:

| Anbieter | Eingangsserver (IMAP) | Ausgangsserver (SMTP) |
|----------|----------------------|----------------------|
| IONOS (1&1) | imap.ionos.de | smtp.ionos.de |
| Strato | imap.strato.de | smtp.strato.de |
| All-Inkl | imap.all-inkl.com | smtp.all-inkl.com |
| T-Online | secureimap.t-online.de | securesmtp.t-online.de |

Bei allen Anbietern sollte **SSL/TLS** aktiviert sein. Benutzername und Passwort entsprechen in der Regel den Zugangsdaten, die Sie von Ihrem Anbieter erhalten haben.

### Anbindung von Postfächern mit Azure AD (Office 365) {#azure-ad}

j-lawyer.org bindet Office 365-Postfächer über die **Microsoft Graph API** mit dem **Client Credentials Flow** (OAuth 2.0) an. Die Anwendung greift dabei als App (nicht im Namen eines Benutzers) auf die Postfächer zu. Dafür muss in Azure eine App-Registrierung erstellt und konfiguriert werden.

Eine separate Aktivierung von IMAP oder SMTP im Microsoft 365 Admin Center ist **nicht** erforderlich – der Zugriff erfolgt ausschließlich über die Graph API.

!!! note "Update von j-lawyer.org Version 3.4 → 3.5"
    Ist die App-Registrierung aus der Vorversion bereits vorhanden, muss sie nicht neu angelegt werden. Es genügt:

    1. In der bestehenden App-Registrierung in Azure unter **API-Berechtigungen** → **Berechtigung hinzufügen** → **Microsoft Graph** → **Anwendungsberechtigungen** die beiden Berechtigungen **Mail.ReadWrite** und **Mail.Send** hinzufügen und anschließend **Administratorzustimmung erteilen** (vgl. Schritt 2).
    2. Im j-lawyer.org Client im Tab **Postfach** neben dem Feld **Client-ID** den Button **Authentifizierung zurücksetzen** klicken, damit das zwischengespeicherte Token aus der alten Anbindung verworfen und beim nächsten Zugriff per Client Credentials Flow neu geholt wird.

    Tenant-ID, Client-ID und Client-Secret bleiben unverändert. Die in der Vorversion konfigurierten delegierten Berechtigungen (IMAP, SMTP.Send, openid …) können in der App-Registrierung verbleiben, werden aber nicht mehr verwendet.

#### Schritt 1: App-Registrierung erstellen

1. Im [Azure Portal](https://portal.azure.com) anmelden
2. Zu **Microsoft Entra ID** (ehemals Azure Active Directory) navigieren
3. Im linken Menü **App-Registrierungen** auswählen
4. **Neue Registrierung** klicken
5. Konfiguration:
    - **Name**: z. B. „j-lawyer Mailzugriff"
    - **Unterstützte Kontotypen**: *Nur Konten in diesem Organisationsverzeichnis* (Single Tenant)
    - **Umleitungs-URI**: kann leer bleiben (wird nicht benötigt)
6. **Registrieren** klicken

![App-Registrierung in Microsoft Entra ID](../images/azure-app-registrierung.png)

#### Schritt 2: API-Berechtigungen konfigurieren

1. In der erstellten App-Registrierung auf **API-Berechtigungen** klicken
2. **Berechtigung hinzufügen** → **Microsoft Graph** → **Anwendungsberechtigungen** (nicht „Delegierte Berechtigungen"!)
3. Folgende Berechtigungen hinzufügen:
    - **Mail.ReadWrite** – Lesen, Verschieben, Löschen und Aktualisieren von E-Mails und Ordnern
    - **Mail.Send** – Versenden von E-Mails
4. **Administratorzustimmung erteilen** klicken (erfordert Global Admin oder Privileged Role Admin)

!!! warning "Wichtig"
    Es müssen **Anwendungsberechtigungen** (Application Permissions) sein, keine delegierten Berechtigungen. j-lawyer.org authentifiziert sich per Client Credentials, nicht im Namen eines Benutzers.

![Auswahl Anwendungsberechtigungen](../images/azure-anwendungsberechtigungen.png)

![API-Berechtigungen mit Mail.ReadWrite und Mail.Send](../images/azure-api-berechtigungen.png)

#### Schritt 3: Client Secret erstellen

1. Im linken Menü **Zertifikate & Geheimnisse** auswählen
2. **Neuer geheimer Clientschlüssel** klicken
3. Beschreibung eingeben (z. B. „j-lawyer") und Ablaufdatum wählen
4. **Hinzufügen** klicken
5. Den **Wert** des Geheimnisses sofort kopieren – er wird nur einmal angezeigt! Relevant ist der „Wert", nicht die „Geheime ID".
6. Das Ablaufdatum notieren – nach Ablauf muss ein neues Secret erstellt und in j-lawyer.org hinterlegt werden.

!!! tip "Ablauf im Blick behalten"
    Wer Aufwand sparen möchte, nutzt die maximal möglichen 24 Monate und trägt sich einen Kalendertermin einige Wochen vor Ablauf ein („Azure AD Client Secret erneuern"). j-lawyer.org warnt anhand des im Client hinterlegten Ablaufdatums rechtzeitig vor dem Auslaufen.

![Neuer Clientschlüssel mit Wert](../images/azure-client-secret.png)

#### Schritt 4: IDs ermitteln

Auf der Übersicht der App-Registrierung finden sich die benötigten Werte:

| Azure-Portal | Feld in j-lawyer.org |
|---|---|
| Anwendungs-ID (Client-ID) | Client-ID |
| Verzeichnis-ID (Mandanten-ID) | Mandanten-ID |
| Geheimer Clientschlüssel (Wert aus Schritt 3) | Client-Secret |
| Ablaufdatum des Secrets (aus Schritt 3) | Ablaufdatum |

![Anwendungs-ID und Verzeichnis-ID in der App-Übersicht](../images/azure-ids.png)

#### Schritt 5: In j-lawyer.org eintragen

Im Client unter **Einstellungen** → **E-Mail – Postfächer** wird über den **+**-Knopf ein neues Postfach angelegt. Im Tab **Postfach** folgende Felder ausfüllen:

- **E-Mail-Adresse**: die vollständige Adresse des Office 365-Postfachs (z. B. `anwalt@kanzlei.de`)
- Checkbox **Office 365** aktivieren
- **Mandanten-ID**: Verzeichnis-ID (Mandanten-ID) aus Azure
- **Client-ID**: Anwendungs-ID (Client-ID) aus Azure
- **Client-Secret**: der geheime Clientschlüssel (Wert) aus Schritt 3
- **Ablaufdatum**: das in Schritt 3 gewählte Ablaufdatum des Client Secrets

![Postfachkonfiguration in j-lawyer.org mit aktiviertem Office 365](../images/jlawyer-postfach-office365.png)

#### Schritt 6: Verbindung testen

Nach dem Speichern der Konfiguration ("Übernehmen") und der ersten Authentifizierung (Button hinter der Client-ID) kann über die Schaltfläche **Einstellungen testen** die Verbindung geprüft werden.

Anschließend kann das Postfach über die Nutzerverwaltung (**Einstellungen** → **Nutzer**) für die gewünschten j-lawyer.org-Nutzer freigegeben und nach Neustart des Clients genutzt werden.

### Anbindung von Google Mail-Postfächern {#google-mail}



Google Mail-Postfächer können mittels eines sogenannten App-Passworts angebunden werden. Bedingung ist, dass für den Account eine 2-Faktor-Authentifizierung (2FA) aktiv ist.

2FA aktivieren
- Zu den Kontoeinstellungen wechseln: <https://myaccount.google.com/>

- Wählen Sie „Sicherheit“ aus

- Wählen Sie unter „Bei Google anmelden“ die Option für 2-Faktor-Authentifizierung aus

Ist die Einstellung bei Google Workspace-Konten nicht zu finden, so muss sie vorab vom Administrator aktiviert / freigegeben werden (<https://admin.google.com/ac/security/2sv>).

App-Passwort erstellen
- Öffnen Sie die Seite zur Erstellung von App-Passwörtern: <https://myaccount.google.com/apppasswords>

- Nutzen Sie einen leicht identifizierbaren Namen für das App-Passwort. Es sollte den Zweck widerspiegeln, bspw. „j-lawyer-mail“.

- Nach Klick auf „Erstellen“ wird das App-Passwort angezeigt. Es besteht aus 4 Gruppen mit je 4 Zeichen, getrennt durch Leerzeichen und sollte in die Zwischenablage übernommen oder anderweitig gespeichert werden.

- Abschließend nutzen Sie dieses App-Passwort anstelle des Google-Account-Passworts in den Einstellen des E-Mail-Postfaches im j-lawyer.org Client.

### Bei Verbindungsproblemen: Mailserver als vertrauenswürdig deklarieren {#mailserver-vertrauen}



Unter Windows gibt es verschiedene Hersteller von „Sicherheitssoftware", deren Produkte verschlüsselte Verbindungen aufbrechen um darin nach Viren etc. zu suchen. Der j-lawyer.org Client vertraut den dabei untergeschobenen SSL-Zertifikaten nicht und verwehrt eine Verbindung.

Ist man sich sicher, dass eine Verbindung zu einem Mailserver vertrauenswürdig ist, kann man über eine Konfiguration den jeweiligen Server whitelisten: Menü „Administration" – „Administrator-Konsole". Dort folgenden Befehl eingeben:

```bash
setsetting mail.imaps.ssl.trust NAMEDESMAILSERVERS
```

NAMEDESMAILSERVERS durch den Namen des SMTP / IMAP-Servers ersetzen, bspw.

```bash
setsetting mail.imaps.ssl.trust mail.your-server.de
```

Es können – durch Komma getrennt – mehrere Server angegeben werden.

### Automatische Veraktung {#automatische-veraktung}

j-lawyer.org kann E-Mails automatisch zur passenden Akte speichern. Der Server prüft regelmäßig die konfigurierten Postfächer und ordnet eingehende E-Mails anhand verschiedener Kriterien der richtigen Akte zu.

#### Einstellungen in der Postfachkonfiguration

Die automatische Veraktung wird pro Postfach im Menü **Einstellungen** → **E-Mail – Postfächer** konfiguriert. Wählen Sie ein Postfach aus und wechseln Sie zum Tab **Automation**.

| Einstellung | Beschreibung |
|-------------|--------------|
| Posteingang scannen | Aktiviert die automatische Veraktung für dieses Postfach |
| Zeitraum (Tage) | Nur E-Mails der letzten X Tage werden geprüft (Standard: 2 Tage) |
| Dokumenten-Etiketten | Etiketten, die automatisch gespeicherten Dokumenten zugewiesen werden |
| Blacklist Dateitypen | Anhang-Dateitypen, die nicht gespeichert werden sollen (z.B. exe, bat) |
| Ausschlussliste | E-Mail-Adressen, die vom Scan ausgeschlossen werden (Absender oder Empfänger) |
| Mindestgröße Anhänge | Anhänge unterhalb dieser Größe werden ignoriert |
| Inline-Anhänge ignorieren | Eingebettete Bilder in der E-Mail nicht als separate Dokumente speichern |
| Standard-Akte | Fallback-Akte für E-Mails, die keiner Akte zugeordnet werden können |

#### Wie die Aktenzuordnung funktioniert

Der Server versucht, eingehende E-Mails automatisch einer Akte zuzuordnen. Dabei werden folgende Kriterien in dieser Reihenfolge geprüft:

1. **Aktenzeichen im Betreff**: Enthält der Betreff ein bekanntes Aktenzeichen, wird die E-Mail dieser Akte zugeordnet.

2. **Aktenzeichen im Text**: Enthält der E-Mail-Text ein bekanntes Aktenzeichen, wird die E-Mail dieser Akte zugeordnet.

3. **Absender (FROM)**: Ist die Absender-Adresse eindeutig einem Kontakt zugeordnet, der nur in einer aktiven Akte beteiligt ist, wird die E-Mail dieser Akte zugeordnet.

4. **CC-Empfänger**: Ist eine CC-Adresse eindeutig einem Kontakt zugeordnet, der nur in einer aktiven Akte beteiligt ist, wird die E-Mail dieser Akte zugeordnet.

5. **TO-Empfänger**: Ist eine Empfänger-Adresse eindeutig einem Kontakt zugeordnet, der nur in einer aktiven Akte beteiligt ist, wird die E-Mail dieser Akte zugeordnet.

6. **Standard-Akte**: Kann keine Zuordnung gefunden werden und ist eine Standard-Akte konfiguriert, wird die E-Mail dort gespeichert.

Archivierte Akten werden bei der Zuordnung nicht berücksichtigt.

#### Verarbeitung und Ablage

Nach erfolgreicher Zuordnung wird die E-Mail:

- Als .eml-Datei in der Akte gespeichert
- Mit den konfigurierten Dokumenten-Etiketten versehen
- Anhänge werden als separate Dokumente gespeichert (sofern nicht auf der Blacklist oder zu klein)
- Im Postfach in den Unterordner **in Akte importiert** verschoben

#### Tipps für die Praxis

- Bitten Sie Mandanten und Gegner, das Aktenzeichen im Betreff anzugeben – dies ermöglicht die zuverlässigste Zuordnung
- Nutzen Sie die Ausschlussliste für Newsletter oder Systembenachrichtigungen
- Konfigurieren Sie passende Dokumenten-Etiketten wie „E-Mail" oder „Eingang", um importierte E-Mails schnell zu erkennen
- Prüfen Sie regelmäßig den Ordner „in Akte importiert" im Postfach, um die korrekte Zuordnung zu kontrollieren

## Termineinladungen aus E-Mails übernehmen {#termineinladungen}

Enthält eine E-Mail eine Termineinladung (ICS-Datei als Anhang), wird diese automatisch erkannt und oberhalb des E-Mail-Inhalts als Hinweisleiste angezeigt. Die Leiste zeigt:

- **Zusammenfassung** des Termins
- **Datum und Uhrzeit** (Beginn und Ende)
- **Ort** (sofern angegeben)

Per Klick auf „als Kalendereintrag übernehmen" wird der Termin als neuer Kalendereintrag angelegt. Dabei werden Zusammenfassung, Beschreibung, Ort sowie Beginn und Ende aus der Einladung übernommen. Wurde die E-Mail bereits einer Akte zugeordnet, wird der Termin direkt in dieser Akte erstellt. Andernfalls öffnet sich ein Suchedialog zur Auswahl der Zielakte.

## Thunderbird-Erweiterung {#thunderbird}

Für den E-Mail-Client Thunderbird steht eine Erweiterung zur Verfügung, die eine direkte Integration mit j-lawyer.org ermöglicht. Mit dieser Erweiterung können E-Mails direkt aus Thunderbird an den j-lawyer.org Server gesendet und dort in Akten gespeichert werden.

### Funktionen

- **E-Mail-Veraktung**: Komplette Nachricht inkl. Anhänge, nur Nachricht oder nur Anhänge in eine Akte hochladen
- **Mehrfachauswahl**: Mehrere markierte Nachrichten per Rechtsklick an eine Akte senden
- **Bildverarbeitung**: Bilder zuschneiden, Reihenfolge festlegen, umbenennen und als ein PDF zusammenfassen
- **Automatische Tags**: Gespeicherte Nachrichten werden automatisch mit dem Tag „veraktet" versehen
- **Zielordner-Auswahl**: Dokumente können in bestimmte Ordner innerhalb der Aktenstruktur abgelegt werden
- **Kalenderintegration** (ab j-lawyer.org 2.6): Termine, Fristen und Wiedervorlagen direkt aus Thunderbird erstellen
- **Vorlagen im Verfassen-Modus**: Beim Schreiben von E-Mails Vorlagen mit Platzhaltern einfügen und Dokumente aus der Akte als Anhang hinzufügen
- **Automatische Aktenzeichen-Erkennung**: Aktenzeichen in der Betreffzeile werden automatisch erkannt
- **Datensynchronisation**: Automatischer täglicher Datenabgleich mit dem j-lawyer.org Server
- **Optionales Aufräumen**: E-Mails nach dem Upload automatisch verschieben oder löschen

### Installation

Die Erweiterung ist im offiziellen Thunderbird Add-ons-Verzeichnis verfügbar:

<https://services.addons.thunderbird.net/de/thunderbird/addon/j-lawyer-org-tb-extension/>

**Systemvoraussetzungen:** Thunderbird 125.0 oder neuer

### Quellcode

Der Quellcode der Erweiterung ist öffentlich auf GitHub verfügbar:

<https://github.com/jlawyerorg/j-lawyer-tbaddon>
