# App koppeln

Um die Mobile App nutzen zu können, muss zunächst ein Verbindungsprofil zu Ihrem j-lawyer Server eingerichtet werden.

## Voraussetzung: Serververbindung

!!! warning "Wichtig"
    Die Mobile App benötigt eine Verbindung zum j-lawyer Server. Stellen Sie sicher, dass der Server von Ihrem mobilen Gerät aus erreichbar ist.

- **j-lawyer.CLOUD**: Keine zusätzliche Konfiguration erforderlich - der Server ist immer erreichbar.
- **Self-Hosting**: Der Server muss von außen erreichbar sein, z.B. durch:
    - VPN-Verbindung in das Kanzleinetzwerk
    - Portweiterleitung im Router
    - Reverse Proxy

## Verbindungsprofil erstellen

Es gibt zwei Möglichkeiten, ein Verbindungsprofil zu erstellen:

### Variante 1: QR-Code scannen (empfohlen)

Die einfachste Methode ist das Scannen eines QR-Codes, der alle Verbindungsdaten enthält.

**So zeigen Sie den QR-Code im Desktop-Client an:**

1. Öffnen Sie den j-lawyer Desktop-Client
2. Wechseln Sie zum Tab **App koppeln** im Login-Dialog
3. Wählen Sie das gewünschte Verbindungsprofil aus
4. Der QR-Code wird automatisch angezeigt

**So scannen Sie den QR-Code in der App:**

1. Öffnen Sie die j-lawyer App
2. Tippen Sie auf das **QR-Code-Symbol** in der Profil-Übersicht
3. Scannen Sie den QR-Code vom Desktop-Bildschirm
4. Die Verbindungsdaten werden automatisch übernommen
5. Vergeben Sie einen Namen für das Profil und speichern Sie

### Variante 2: Manuelle Eingabe

Alternativ können Sie die Verbindungsdaten manuell eingeben:

1. Öffnen Sie die j-lawyer App
2. Tippen Sie auf das **Plus-Symbol** zum Hinzufügen eines neuen Profils
3. Geben Sie folgende Daten ein:

| Feld | Beschreibung |
|------|--------------|
| **Profilname** | Frei wählbarer Name zur Identifikation |
| **Server** | Hostname oder IP-Adresse des j-lawyer Servers |
| **Port** | Server-Port (Standard: 8080) |
| **Sicherheitsmodus** | Standard, SSL oder SSH-Tunnel |

**Bei Verwendung eines SSH-Tunnels** sind zusätzlich erforderlich:

| Feld | Beschreibung |
|------|--------------|
| **SSH-Server** | Hostname des SSH-Servers |
| **SSH-Port** | SSH-Port (Standard: 22) |
| **SSH-Benutzer** | Benutzername für die SSH-Verbindung |
| **SSH-Passwort** | Passwort für die SSH-Verbindung |
| **SSH-Zielport** | Zielport auf dem SSH-Server |

## Anmelden

Nach dem Einrichten des Verbindungsprofils:

1. Wählen Sie das Profil in der Dropdown-Liste aus
2. Geben Sie Ihren **Benutzernamen** und Ihr **Passwort** ein (dieselben Zugangsdaten wie im Desktop-Client)
3. Optional: Aktivieren Sie **Angemeldet bleiben**, um die Zugangsdaten zu speichern
4. Tippen Sie auf **Anmelden**

## Mehrere Profile

Sie können mehrere Verbindungsprofile anlegen, z.B. für verschiedene Server oder Verbindungsarten. Wechseln Sie einfach zwischen den Profilen über die Dropdown-Auswahl im Login-Bereich.
