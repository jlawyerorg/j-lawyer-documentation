# Installation

### Installation auf Windows-Systemen {#windows}

Die Installation auf Windowssystemen ist hier beschrieben: http://www.j-lawyer.org/?page_id=100

### Installation auf macOS-Systemen {#macos}

Die Installation auf macOS-Systemen ist hier beschrieben: http://www.j-lawyer.org/?page_id=355

### Installation auf Linux-Systemen {#linux}

Die Installation auf Windowssystemen ist hier beschrieben: http://www.j-lawyer.org/?page_id=93

## Start der Anwendung {#start}

### Start und Stoppen des j-lawyer.org Servers {#server-start}



Windows:
- im Startmenü nach “Dienste” suchen und diese Anwendung starten, es erscheint eine Liste von installierten Diensten
- Scrollen zum Dienst “j-lawyer.org-Server”
- via Rechtsklick auf den Dienst kann dieser beendet / gestartet werden

Linux:
- Terminal öffnen
- Kommando zum Starten des Dienstes: sudo service j-lawyer-server start
- Kommando zum Stoppen des Dienstes: sudo service j-lawyer-server stop
- Kommando zum Neustarten des Dienstes: sudo service j-lawyer-server restart
- Kommando zum Ermitteln des Dienststatus: sudo service j-lawyer-server status

macOS:
- Terminal öffnen
- Kommando zum Starten des Dienstes:

cd /Library/LaunchDaemons

sudo launchctl start j-lawyer-server
- Kommando zum Stoppen des Dienstes:

cd /Library/LaunchDaemons

sudo launchctl unload /Library/LaunchDaemons/j-lawyer-server.plist

### Start des j-lawyer.org Clients {#client-start}



Nach dem Start des j-lawyer.org Clients ist zwingend eine Anmeldung mit gültigen Nutzerdaten notwendig. Handelt es sich um eine Neuinstallation, so gibt es folgende voreingestellte Nutzer:
- Nutzer “user”, Passwort “u” - Nutzer mit eingeschränkten Rechten
- Nutzer “admin”, Passwort “a” - Nutzer mit vollen administrativen Rechten

![Abbildung 1](../images/j-lawyer-org-UserGuide-de-001.png)


Vor einer Anmeldung ist im Falle einer ersten Nutzung unter “Verbindung” der Name oder die IP des Servers einzutragen (bzw. “localhost”, wenn j-lawyer.org Server und j-lawyer.org Client auf dem selben Gerät genutzt werden) sowie der zu verwendende Netzwerkport (in der Regel 8080).

![Abbildung 2](../images/j-lawyer-org-UserGuide-de-002.png)


Folgende Verbindungsarten sind verfügbar:
- Standard: die Daten zwischen j-lawyer.org Client und Server werden unverschlüsselt übertragen. Diese Option ist innerhalb eines lokalen Unternehmensnetzwerkes in der Regel akzeptabel.
- SSL: der j-lawyer.org Server selbst wurde mit einem SSL-Verschlüsselungszertifikat ausgestattet oder befindet sich hinter einem sogenannten Reverse Proxy, welcher Verschlüsselung beherrscht. Diese Option nutzt Transportverschlüsselung und bietet eine hohe Sicherheit, auch wenn die Daten über öffentliche Netze (wie das Internet) übertragen werden. Diese Variante erfordert zusätzliche Konfigurationen auf Serverseite.
- SSH-Tunnel: der j-lawyer.org Client verbindet sich über eine verschlüsselte SSH-Verbindung mit dem j-lawyer.org Server. Auf dem Gerät, auf welchem der j-lawyer.org Server installiert ist, muss ein SSH-Dienst laufen, was bspw. auf Linuxservern gegeben ist. Diese Option nutzt Transportverschlüsselung und bietet eine hohe Sicherheit, auch wenn die Daten über öffentliche Netze (wie das Internet) übertragen werden. Es ist in der Regel keine besondere Konfiguration notwendig. Es empfiehlt sich, einen dedizierten Nutzer für den Aufbau des SSH-Tunnels zu verwenden, der außer einer SSH-Verbindung keine Berechtigungen auf dem Server hat. Gerät der Nutzer in fremde Hände, ist das Risiko beschränkt. Ein solcher Nutzer lässt sich unter Debian oder Ubuntu-Derivaten bspw. per

sudo adduser -r -s /bin/nologin jlawyer oder 
sudo adduser jlawyer --shell=/bin/false –no-create-home

erstellen. Die Verbindungsparameter für den SSH-Tunnel lauten wie folgt:
    - Host, Port: Servername und Port des SSH-Dienstes (in der Regel 22)
    - Nutzer, Passwort: Nutzername und Passwort des SSH-berechtigten Nutzers auf dem Server
    - Server lauscht auf Port: der Netzwerkport auf dem Server, auf welchem der j-lawyer.org Server lauscht – in der Regel 8080.

Anschließend verbindet man sich per Server und Port nicht zum Server selbst,

sondern auf localhost. Die Portangabe unterhalb des Server ist der „Startport“, ab

welchem automatisch ein freier lokaler Port ausgewählt wird. So können mehrere

Clients auf dem selben Gerät über jeweils eigene SSH-Tunnel zum Server

verbinden.

### Direktstart des j-lawyer.org Clients in die Desktopansicht



Der Login-Dialog des j-lawyer.org Clients kann optional übersprungen werden – so ist ein direkter Start bis zur “Mein Desktop”-Ansicht möglich. Dazu müssen beim Start folgende Kommandozeilenparameter übergeben werden:

Option 1: direkte Verbindung (Sicherheit „Standard“)
- Server
- Port
- Nutzername
- Passwort

also bspw. “localhost 8080 admin a”

Option 2: SSL-verschlüsselte Verbindung (Sicherheit „SSL“)
- Server
- Port
- Nutzername
- Passwort
- „ssl“ als Verbindungsmodus

also bspw. “localhost 443 admin a ssl”

Option 3: Verbindung per SSH (Sicherheit „SSH-Tunnel“)
- in der Regel „localhost“
- Port
- Nutzername
- Passwort
- „ssh“ als Verbindungsmodus
- IP oder Name des Servers
- Port des Servers, auf welchem der SSH-Dienst verfügbar ist
- Nutzername des SSH-Nutzers
- Passwort des SSH-Nutzers
- Port auf dem Server, auf welchem der j-lawyer.org Server lauscht

also bspw. “localhost 8080 admin a ssh 84.2.3.4 22 root rootpasswort 8080”

Insbesondere in Umgebungen in denen der Client regelmäßig für verschiedene j-lawyer.org-User oder -Server gestartet wird, kann diese Funktionalität Zeit sparen.

Hinweis: Um die Sicherheit Ihrer Installation zu gewährleisten, stellen Sie sicher dass die Funktionalität nur in kontrollierten und entsprechend abgesicherten Umgebungen genutzt wird. Insbesondere wenn Nutzername und  Passwort in Skripten verwendet werden, so ist sicherzustellen dass kein anderer Nutzer des Betriebssystems das Skript lesen und somit Kenntnis des Passwortes erhalten kann.

### Abbildung 3: Login-Dialog, j-lawyer.BOX-Integration
