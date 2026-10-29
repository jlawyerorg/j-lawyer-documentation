# Ingo als MCP-Server {#mcp-server}

Die Werkzeuge der [agentischen KI](agenten.md) stehen nicht nur im j-lawyer.org-Client zur Verfügung, sondern auch in externen KI-Anwendungen wie Claude oder Mistral Le Chat. Grundlage ist das Model Context Protocol (MCP), ein offener Standard, über den KI-Anwendungen auf die Daten und Funktionen anderer Systeme zugreifen. So lassen sich bspw. in Claude Akten durchsuchen, Dokumente lesen, Termine anlegen oder Zeiten erfassen – mit denselben Werkzeugen, die Assistent Ingo im Client nutzt.

!!! info "Nur für j-lawyer.CLOUD"
    Der MCP-Server ist ausschließlich für j-lawyer.CLOUD verfügbar und wird auf Anfrage durch die Administration der j-lawyer.CLOUD aktiviert. Nach der Aktivierung erhält die Kanzlei die Adresse des MCP-Servers, bspw. `https://kanzlei.example.de/j-lawyer-mcp/mcp`.

## Voraussetzungen {#voraussetzungen}

- die Adresse des MCP-Servers der Kanzlei
- die eigenen j-lawyer.org-Zugangsdaten
- das Recht **KI-Agentenfunktionen** in der [Nutzerverwaltung](../nutzerverwaltung.md#berechtigungen-integrationen) – fehlt es, weist die Anmeldeseite darauf hin

Jede Person richtet die Verbindung selbst ein und meldet sich mit dem eigenen Konto an. Einen gemeinsamen Zugang gibt es nicht.

## Einrichtung in Claude {#claude}

1. In Claude (Web oder Desktop-App) unter **Customize** → **Connectors** auf **+** klicken und **Add custom connector** wählen.
2. Einen Namen (bspw. „j-lawyer.org“) und die Adresse des MCP-Servers eintragen. Die Felder für OAuth Client ID und Client Secret unter **Advanced settings** bleiben leer – der Server richtet sich selbst ein.
3. Mit **Add** bestätigen und anschließend **Connect** wählen.
4. Es öffnet sich die Anmeldeseite von j-lawyer.org. Mit dem eigenen Benutzer anmelden, die gewünschten [Berechtigungen](#berechtigungen) wählen und auf **Erlauben** klicken.

Im Chat lässt sich der Connector anschließend über das **+**-Menü je Unterhaltung ein- und ausschalten.

!!! note "Claude Team und Enterprise"
    In Team- und Enterprise-Organisationen muss der Connector zunächst von einer Person mit Owner-Rolle für die Organisation hinzugefügt werden. Die Mitglieder finden ihn danach in ihrer Connector-Liste und verbinden sich über **Connect** jeweils mit dem eigenen j-lawyer.org-Konto.

## Einrichtung in Mistral Le Chat {#mistral}

1. In Le Chat im Seitenmenü **Intelligence** → **Connectors** öffnen und **Add Connector** wählen.
2. Den Reiter **Custom MCP Connector** wählen, einen Namen (bspw. „j-lawyer.org“) und die Adresse des MCP-Servers eintragen.
3. Die Authentifizierung wird anhand der Adresse erkannt; als Methode OAuth verwenden, ohne Client ID.
4. Mit **Connect** bestätigen. Es öffnet sich die Anmeldeseite von j-lawyer.org: mit dem eigenen Benutzer anmelden, die gewünschten [Berechtigungen](#berechtigungen) wählen und auf **Erlauben** klicken.

Das Hinzufügen eines Connectors erfordert in Le Chat ggf. Administrationsrechte im Mistral-Workspace. Die Mitglieder melden sich danach jeweils mit dem eigenen j-lawyer.org-Konto an.

## Andere KI-Anwendungen {#andere}

Andere KI-Anwendungen, die MCP-Server mit OAuth-Anmeldung unterstützen, werden auf ähnliche Weise eingerichtet: Adresse des MCP-Servers eintragen, Client ID und Secret leer lassen, auf der j-lawyer.org-Seite anmelden und Berechtigungen erteilen. Die genauen Schritte sind der Dokumentation der jeweiligen KI-Anwendung zu entnehmen.

!!! tip "Bezeichnungen können sich ändern"
    Die Menübezeichnungen in Claude und Le Chat ändern sich gelegentlich. Weicht die Oberfläche von der Beschreibung ab, hilft die Dokumentation des Anbieters zum Thema „Custom Connector“ bzw. „Remote MCP“ weiter.

## Berechtigungen {#berechtigungen}

Bei der Anmeldung wird festgelegt, was die KI-Anwendung tun darf:

| Berechtigung | Bedeutung | Werkzeuge mit Risikostufe |
|---|---|---|
| **Lesen** | Akten, Dokumente, Kontakte, Termine, Rechnungen und Zeiterfassung lesen | Niedrig |
| **Anlegen und ändern** | zusätzlich Akten, Kontakte, Termine, Notizen, Dokumente und Rechnungen anlegen und ändern | Mittel |
| **Löschen und verschieben** | zusätzlich Dokumente löschen und in andere Akten verschieben | Hoch |

Voreingestellt ist nur **Lesen**. Werkzeuge, für die keine Berechtigung erteilt wurde, werden der KI-Anwendung gar nicht erst angeboten. Welches Werkzeug welche Risikostufe hat, zeigt die [Werkzeugübersicht](agenten.md#werkzeuge). Um Berechtigungen nachträglich zu erweitern, die Verbindung in der KI-Anwendung entfernen und neu einrichten.

## Was gilt {#was-gilt}

- **Eigene Rechte, nicht mehr:** Die KI-Anwendung sieht genau die Akten, die der angemeldete Benutzer selbst sehen darf. Gruppenzugehörigkeiten und Aktenrechte gelten unverändert.
- **Änderungen unter eigenem Namen:** Jede Änderung wird wie gewohnt in der Aktenhistorie vermerkt – mit dem Benutzer, der die Verbindung eingerichtet hat.
- **Keine Genehmigungsdialoge von j-lawyer.org:** Anders als im Client fragt j-lawyer.org nicht vor jedem schreibenden Aufruf nach. Die Grenze ziehen die bei der Anmeldung erteilten Berechtigungen sowie die Bestätigungseinstellungen der KI-Anwendung selbst.
- **Kein Webzugriff:** Die Werkzeuge für Websuche und Abruf von Webseiten werden nicht angeboten – dafür haben die KI-Anwendungen eigene Mittel.
- **Eigene Modelle und Prompts:** Es arbeitet das Modell der KI-Anwendung. Die in j-lawyer.org konfigurierten Modelle und [eigenen Prompts](eigene-prompts.md) gelten hier nicht.

!!! warning "Datenschutz und Berufsgeheimnis"
    Über den MCP-Server abgerufene Akteninhalte werden an den Anbieter der KI-Anwendung übermittelt und dort verarbeitet. Vor der Nutzung sollte geprüft werden, ob mit dem Anbieter eine Vereinbarung zur Auftragsverarbeitung besteht und die Anforderungen an die Verschwiegenheit (§ 43e BRAO, § 203 StGB) erfüllt sind.

## Verbindung beenden {#beenden}

In der KI-Anwendung den Connector entfernen. Zusätzlich kann die Verbindung auf Anfrage serverseitig durch die Administration der j-lawyer.CLOUD widerrufen werden; das wirkt sofort. Wird einem Benutzer das Recht **KI-Agentenfunktionen** entzogen, kann er den MCP-Server nicht mehr nutzen.

## Fehlerbehebung {#fehlerbehebung}

| Beobachtung | Ursache / Lösung |
|---|---|
| Der Server ist nicht erreichbar | Adresse prüfen. Ist sie korrekt, ist der MCP-Server ggf. noch nicht aktiviert – an die Administration der j-lawyer.CLOUD wenden. |
| „Benutzername oder Passwort ist falsch“ | Dieselben Zugangsdaten wie im j-lawyer.org-Client verwenden. |
| „Der Benutzer … besitzt die Rolle 'aiAgentRole' nicht“ | Das Recht **KI-Agentenfunktionen** muss in der Nutzerverwaltung erteilt werden. |
| Die KI-Anwendung findet keine Werkzeuge | Die Verbindung wurde widerrufen oder ist abgelaufen. Connector entfernen und neu einrichten. |
| Die KI-Anwendung meldet eine fehlende Berechtigung | Bei der Anmeldung wurde die nötige [Berechtigung](#berechtigungen) nicht erteilt. Connector entfernen und mit weiteren Berechtigungen neu einrichten. |
