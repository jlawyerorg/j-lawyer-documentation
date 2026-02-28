# Add-Ons: Telefonie mit Softphone

## Allgemeines

j-lawyer.org unterstützt Telefonie mit Hilfe sogenannter Softphones, also verschiedenartiger Telefoniesoftware, die auf dem Rechner installiert ist.

Anrufe können direkt aus j-lawyer.org heraus initiiert werden - z.B. aus der Kontaktansicht, aus der Beteiligtenansicht einer Akte oder aus der E-Mail-Seitenleiste. j-lawyer.org übergibt die Telefonnummer dabei an die konfigurierte Softphone-Anwendung, die den eigentlichen Anruf aufbaut.

!!! info "Hinweis"
    Die Softphone-Funktion wird nur genutzt, wenn kein Sipgate konfiguriert ist. Ist für den angemeldeten Nutzer ein Sipgate-Zugang hinterlegt, hat dieser Vorrang.

!!! info "Hinweis"
    Softphone-Einstellungen werden pro Arbeitsplatz gespeichert, nicht pro Nutzer.

## Konfiguration

Die Softphone-Einstellungen werden über das Menü **Einstellungen** - **Telefonie per Softphone** geöffnet.

Im Dialog „Voice-over-IP - Einstellungen" stehen zwei Modi zur Verfügung:

### Aufruf per Protokollhandler (empfohlen)

Dies ist die Standardeinstellung. j-lawyer.org öffnet die Telefonnummer über einen Protokollhandler (z.B. `tel://`) und überlässt dem Betriebssystem die Zuordnung zur richtigen Anwendung.

Im Feld **Protokoll** kann das gewünschte Protokoll eingetragen werden. Voreingestellt ist `tel://`.

Je nach verwendeter Softphone-Anwendung kann es notwendig sein, ein anderes Protokoll zu verwenden (z.B. `callto://` oder `sip://`). Welches Protokoll die jeweilige Software unterstützt, ist der nachfolgenden Tabelle zu entnehmen.

### Aufruf per Kommandozeilenparameter

Alternativ kann eine Softphone-Anwendung direkt über ihren Dateipfad aufgerufen werden. Dazu werden folgende Felder konfiguriert:

- **Ausführbare Datei**: Pfad zur Softphone-Anwendung (über den „..."-Button auswählbar)
- **Parameter**: Kommandozeilenparameter für den Aufruf. Der Platzhalter `TELNR` wird automatisch durch die anzurufende Telefonnummer ersetzt.

Beispiel: Ist als ausführbare Datei `/usr/bin/linphone` und als Parameter `--call TELNR` konfiguriert, wird beim Anruf der Befehl `/usr/bin/linphone --call 004912345678` ausgeführt.

## Rufnummernformatierung

j-lawyer.org wandelt Telefonnummern vor dem Wählen automatisch in das internationale E.164-Format um. Leerzeichen, Bindestriche, Punkte, Schrägstriche und Klammern werden entfernt. Ist keine Landesvorwahl angegeben, wird +49 (Deutschland) als Standard angenommen.

## Protokollhandler für bekannte VoIP-Software

Die folgende Tabelle zeigt Protokollhandler, die von gängiger VoIP-Software unterstützt werden:

| Software | Plattform | Protokoll | Hinweise |
|---|---|---|---|
| PhonerLite | Windows | `tel://` | In PhonerLite unter „Optionen" - „URL-Protokollhandler" - „tel:" aktivieren |
| MicroSIP | Windows | `tel://`, `sip://`, `callto://` | Registriert sich bei Installation als Protokollhandler |
| 3CX | Windows, macOS | `tel://`, `callto://` | Wird bei Installation als Standard-Telefonanwendung registriert |
| Twinkle | Linux | `tel://` | Keine besonderen Einstellungen notwendig |
| Linphone | Windows, macOS, Linux | `sip://` | Unterstützt primär das SIP-Protokoll |
| Zoiper | Windows, macOS, Linux | `tel://`, `sip://`, `callto://` | In den Einstellungen unter „Automation" die gewünschten Protokolle aktivieren |
| Telefon (64 Characters) | macOS | `tel://` | Empfehlung für macOS, siehe Hinweis unten |
| Softphone.Pro | Windows | `tel://`, `sip://`, `callto://` | Alle drei Protokolle werden unterstützt |
| Microsoft Teams | Windows, macOS, Linux | `tel:`, `callto:` | Neuere Versionen erfordern das Protokoll **ohne** doppelten Slash (also `tel:` statt `tel://` und `callto:` statt `callto://`) |

!!! tip "macOS"
    In den Voreinstellungen von macOS wird beim Initiieren eines Anrufs standardmäßig die Anwendung FaceTime geöffnet. Möchte man eine andere Anwendung nutzen, öffnet man in FaceTime die Einstellungen und ändert die Standardanwendung für Anrufe. Eine Empfehlung ist die App „Telefon" von 64 Characters ([https://www.64characters.com/telephone/](https://www.64characters.com/telephone/)).

### Gängige Protokolle im Überblick

| Protokoll | Beschreibung |
|---|---|
| `tel://` | Standard-Protokoll für Telefonanrufe. Wird von den meisten Softphones und Betriebssystemen unterstützt. Empfohlene Einstellung. |
| `callto://` | Alternatives Protokoll, das von einigen Softphones unterstützt wird. |
| `sip://` | SIP-Protokoll (Session Initiation Protocol). Wird vor allem von reinen SIP-Clients wie Linphone verwendet. |
