# Besonderes elektronisches Anwaltspostfach (beA) {#bea}

## Allgemeines zur beA-Integration {#allgemeines}

j-lawyer.org ermöglicht eine grundsätzliche Arbeit mit einem oder mehreren beA-Postfächern direkt aus der Anwendung heraus:

- Zugriff auf ein oder mehrere Postfächer
- Empfangen von Nachrichten
- Export von Nachrichten in eine Akte
- Senden von Nachrichten
- Anfordern, Abgeben oder Zurückweisen von elektronischen Empfangsbekenntnissen (eEB)
- Zugriff auf das beA-Adressverzeichnis
- Import von Gerichtsadressen
- Übernahme von Safe-IDs in vorhandene Adressen

!!! warning "Hinweis"
    j-lawyer.org-Anwender nutzen die Integration auf eigenes Risiko. Das bedingt dass bspw. der korrekte Versand und Empfang nach Bedarf über die beA-Weboberfläche kontrolliert werden.

## Voraussetzungen {#voraussetzungen}

Aktuell ist für den Zugang zum beA ein Softwarezertifikat notwendig. Es ersetzt in der Nutzung weitgehend die beA Smartcards, und ist im Allgemeinen komfortabler anzuwenden. Bei der Nutzung in j-lawyer.org werden die Zertifikate nutzerspezifisch hinterlegt und weder Zertifikat noch Passwort gelangen in den Besitz der Nutzer der Kanzleisoftware.

Weitere Voraussetzungen im Überblick:

- **Vollständig in Betrieb genommenes beA-Postfach** (hier nicht weiter ausgeführt, da bereits eine passive Nutzungspflicht besteht ("Empfangsbereitschaft")).
- **beA Softwarezertifikat**: Das Softwarezertifikat ist nicht zum Signieren von Schriftsätzen gedacht, es ersetzt vielmehr das Hantieren mit Smartcard und Kartenleser zwecks Anmeldung am beA. Es kann zu einem Jahrespreis von 4,90 EUR unter der Bezeichnung "beA-Softwarezertifikat" bei der Bundesnotarkammer bezogen werden: <https://zertifizierungsstelle.bnotk.de/bestellen/beaprodukte/bea-produkte-softwarezertifikat> Der Erstellprozess ist hier detailliert beschrieben: <https://onlinehilfe.bnotk.de/einrichtungen/zertifizierungsstelle/bea/bea-softwarezertifikate-tauschprozess/erstellen-herunterladen-eines-bea-softwarezertifikates.html> Bitte unbedingt das beim Generieren des Zertifikats verwendete Passwort notieren.
- **Einrichtung des Softwarezertifikats** als zusätzlicher Sicherheitstoken für ein Postfach: <https://www.brak.de/zur-rechtspolitik/newsletter/bea-newsletter/2016/ausgabe-2-2016-v-14122016.news.html#hl75740>

Sind alle Voraussetzungen erfüllt, so kann mit der Inbetriebnahme im j-lawyer.org Client fortgefahren werden.

## Inbetriebnahme in j-lawyer.org {#inbetriebnahme}

Im Folgenden werden die Schritte zur vollständigen Inbetriebnahme der beA-Integration beschrieben:

1. Starten Sie den j-lawyer.org Client mit einem Nutzer der über administrative Berechtigungen verfügt.
2. Öffnen Sie die globalen beA-Einstellungen über das Menü **Einstellungen** → **beA (Anwaltspostfach)**. Stellen Sie die beA-Integration dort auf "an".
3. Öffnen Sie die Nutzerverwaltung: Menü **Einstellungen** → **Nutzerverwaltung**.
4. Markieren Sie den Nutzer, welcher mit einem oder mehreren beA-Postfächern arbeiten soll.
5. Im Tab **beA** kann nun über den "..."-Knopf ("Zertifikat uploaden") das Softwarezertifikat samt PIN/Passwort hinterlegt werden. Ist der Upload erfolgreich, so werden Seriennummer und weitere Informationen angezeigt.

![Abbildung 56](../images/j-lawyer-org-UserGuide-de-062.png)

6. Abschließend aktivieren Sie die **automatische** oder **manuelle Anmeldung**:
    - **Automatische Anmeldung**: Das beA-Postfach wird bereits beim Start des j-lawyer.org Clients geöffnet und auf neu eingegangene Nachrichten geprüft.
    - **Manuelle Anmeldung**: Das Postfach muss explizit geöffnet werden (durch Navigation zur Posteingangssicht im linken Navigationsbaum). In diesem Fall findet eine Nachfrage statt, ob mit dem hinterlegten Softwarezertifikat oder der Smartcard angemeldet werden soll.

## Der beA-Posteingang {#posteingang}

Der beA-Posteingang ist über die Navigation links erreichbar und zeigt alle verfügbaren beA-Postfächer an.

### Aufbau der Oberfläche

Die Oberfläche gliedert sich in drei Bereiche:

- **Ordnerstruktur** (links): Zeigt alle beA-Postfächer mit ihren Ordnern (Posteingang, Gesendet, Papierkorb und benutzerdefinierte Ordner)
- **Nachrichtenliste** (oben rechts): Zeigt die Nachrichten des ausgewählten Ordners mit Betreff, Absender, Empfänger, Datum und Aktenzeichen
- **Nachrichteninhalt** (unten rechts): Zeigt den Inhalt der ausgewählten Nachricht mit Anhängen

### Werkzeugleiste

Die Werkzeugleiste bietet folgende Funktionen:

| Symbol | Funktion | Beschreibung |
|--------|----------|--------------|
| Aktualisieren | Postfächer neu laden | Lädt die Ordnerstruktur und Nachrichten neu |
| Ausloggen | Abmelden | Meldet vom beA ab, z.B. um mit anderem Token neu anzumelden |
| Neue Nachricht | Nachricht verfassen | Öffnet den Dialog zum Erstellen einer neuen beA-Nachricht |
| Antworten | Beantworten | Beantwortet die ausgewählte Nachricht |
| Allen antworten | Allen Empfängern antworten | Beantwortet an alle Empfänger |
| Weiterleiten | Nachricht weiterleiten | Leitet die ausgewählte Nachricht weiter |
| Löschen | Nachricht löschen | Verschiebt die Nachricht in den Papierkorb |

### Ordnerverwaltung {#ordnerverwaltung}

Per Rechtsklick auf einen Ordner stehen folgende Funktionen zur Verfügung:

- **Neuer Ordner**: Erstellt einen Unterordner im ausgewählten Ordner
- **Ordner löschen**: Löscht benutzerdefinierte Ordner (Systemordner wie Posteingang, Gesendet und Papierkorb können nicht gelöscht werden)
- **Papierkorb leeren**: Leert den Papierkorb (nur bei Papierkorb verfügbar)

### Nachrichten verwalten {#nachrichten-verwalten}

#### Nachrichten anzeigen

- **Einfacher Klick**: Zeigt die Nachricht im unteren Bereich an
- **Doppelklick**: Öffnet die Nachricht in einem separaten Fenster mit vollständiger Ansicht

#### Nachrichten in Akte speichern

Über das Kontextmenü (Rechtsklick auf eine Nachricht) oder die Seitenleiste können Nachrichten zur Akte gespeichert werden:

- **In Akte speichern**: Speichert die Nachricht samt aller Anhänge zur Akte
- **In Akte speichern (ohne Anhänge)**: Speichert nur die Nachricht ohne Anhänge
- **In Akte speichern (nur Anhänge)**: Speichert nur die Anhänge zur Akte

!!! tip "Automatisches Verschieben"
    Mit der Option **"in 'importiert' verschieben"** wird die Nachricht nach erfolgreicher Zuordnung zu einer Akte automatisch in einen Ordner "in Akte importiert" verschoben. Dies hilft dabei, bereits bearbeitete Nachrichten von neuen zu unterscheiden.

#### Nachrichten per Drag & Drop verschieben

Nachrichten können per Drag & Drop zwischen Ordnern verschoben werden. Ziehen Sie eine Nachricht einfach auf den gewünschten Zielordner.

#### Nachrichten aus dem Papierkorb wiederherstellen

Nachrichten im Papierkorb können über das Kontextmenü (Rechtsklick → **Wiederherstellen**) in den Posteingang zurückverschoben werden.

### Nachrichtenanzeige beschränken

Über die Dropdown-Liste oben rechts kann die Anzahl der angezeigten Nachrichten beschränkt werden. Dies ist nützlich bei Ordnern mit vielen Nachrichten, um die Ladezeit zu verkürzen.

## Anzeige des Übermittlungsstatus {#uebermittlungsstatus}

Im Kopf einer angezeigten beA-Nachricht wird im rechten Teil der Übermittlungsstatus angezeigt. Der Status wird durch eine Farbe angezeigt. Details zum angezeigten Status sind als Mouse-Over-Text des Icons verfügbar.

Die Anzeige folgt folgenden Regeln:

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| Empfangene Nachricht | Neutral | Keine besondere Kennzeichnung |
| Versendete Nachricht mit gutem Journal an Nicht-EGVP | Grün | Erfolgreich zugestellt |
| Versendete Nachricht mit schlechtem Journal an Nicht-EGVP | Rot | Zustellung fehlgeschlagen |
| Versendete Nachricht mit gutem Journal und gutem Laufzettel an EGVP | Grün | Erfolgreich zugestellt |
| Versendete Nachricht mit gutem Journal und fehlendem Laufzettel an EGVP | Orange | Zustellung unklar |
| Versendete Nachricht mit schlechtem Journal oder schlechtem Laufzettel an EGVP | Rot | Zustellung fehlgeschlagen |

!!! info "EGVP-Laufzettel"
    EGVP-Laufzettel sind in der Regel nur in der gesendeten beA-Nachricht, welche zur Akte gespeichert wurde, verfügbar. Die Anzeige der Nachricht im „Gesendet"-Ordner des beA-Posteingangs hat keinen Zugriff auf die Laufzettel.

## Beschränkungen bei Nutzung der beA-Integration {#beschraenkungen}

Die Nutzung von beA-Postfächern in j-lawyer.org unterliegt folgenden Beschränkungen:

- Der Status "gelesen" / "ungelesen" bezieht sich ausschließlich auf das Abrufen / Lesen der Nachrichten über die beA-Weboberfläche. Ein Abruf von Nachrichten über die von der BRAK zur Verfügung gestellte Schnittstelle wird nicht als Lesevorgang gewertet. Außerdem ist ein explizites Setzen des "gelesen" / "ungelesen"-Status über die Schnittstelle nicht möglich. Es handelt sich hier um Beschränkungen der von der BRAK bereitgestellten Schnittstelle – j-lawyer.org kann diesbezüglich keine Verbesserung implementieren.

## Hinweise zu temporären Dateien {#temporaere-dateien}

Bei der Arbeit mit beA-Nachrichten werden temporäre Dateien im System abgelegt. Bei intensiver Nutzung kann sich eine große Anzahl von temporären Ordnern ansammeln. Falls dies zu Geschwindigkeitseinbußen führt, wird eine Warnung angezeigt ("Hinweis: temporäre Dateien"). In diesem Fall sollte das angegebene Verzeichnis manuell bereinigt werden.
