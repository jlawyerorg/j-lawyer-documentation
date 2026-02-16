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
- **beA Softwarezertifikat**: Das Softwarezertifikat ist nicht zum Signieren von Schriftsätzen gedacht, es ersetzt vielmehr das Hantieren mit Smartcard und Kartenleser zwecks Anmeldung am beA. Es kann zu einem Jahrespreis von 4,90 EUR unter der Bezeichnung "beA-Softwarezertifikat" bei der Bundesnotarkammer bezogen werden: <https://zertifizierungsstelle.bnotk.de/bestellen/beaprodukte/bea-produkte-softwarezertifikat> Der Erstellprozess ist hier detailliert beschrieben: <https://onlinehilfe.bnotk.de/einrichtungen/zertifizierungsstelle/bea/bea-softwarezertifikate-tauschprozess/erstellen-herunterladen-eines-bea-softwarezertifikates.html> Bitte unbedingt das beim Generieren des Zertifikats verwendete Passwort notieren. Eine Videoanleitung ist ebenfalls verfügbar: <https://onlinehilfe.bnotk.de/einrichtungen/zertifizierungsstelle/bea/bea-softwarezertifikate-tauschprozess/erklaerfilm-tausch-bea-softwarezertifikat.html>
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

## Versand von beA-Nachrichten {#versand}

Der Versand von beA-Nachrichten kann aus verschiedenen Bereichen der Anwendung heraus initiiert werden. In allen Fällen öffnet sich der Versanddialog, in dem die Nachricht zusammengestellt und abgesendet wird.

### Nachricht erstellen {#nachricht-erstellen}

#### Über die Beteiligten einer Akte

Im Tab **Beteiligte** einer Akte steht über den Aktionsknopf eines Beteiligten die Funktion **"Nachricht verfassen"** zur Verfügung. Der Versanddialog wird mit dem Empfänger, dem Aktenzeichen und allen Beteiligten der Akte vorbelegt.

!!! info "Voraussetzung"
    Beim Kontakt muss eine beA Safe-ID hinterlegt sein. Ist keine Safe-ID vorhanden, wird eine entsprechende Fehlermeldung angezeigt.

#### Über die Dokumentenliste einer Akte

In der Dokumentenliste einer Akte können über das Kontextmenü (Rechtsklick) ausgewählte Dokumente direkt als beA-Nachricht versendet werden:

- **"senden"**: Übernimmt die ausgewählten Dokumente als Anhänge in den Versanddialog
- **"als PDF senden"**: Konvertiert die ausgewählten Dokumente vor dem Versand in das PDF-Format

Die Beteiligten der Akte werden als Empfänger-Kandidaten im Dialog bereitgestellt.

!!! warning "Geöffnete Dokumente"
    Sind ausgewählte Dokumente aktuell zur Bearbeitung geöffnet, erscheint eine Warnung, da das Risiko fehlender oder inkonsistenter Inhalte besteht.

#### Über den beA-Posteingang

Im beA-Posteingang stehen in der Werkzeugleiste folgende Funktionen zum Versand bereit:

- **Neue Nachricht**: Öffnet einen leeren Versanddialog
- **Antworten**: Erstellt eine Antwort an den Absender der ausgewählten Nachricht (Betreff wird mit "Re: " vorangestellt)
- **Allen antworten**: Erstellt eine Antwort an den Absender und alle Empfänger der ausgewählten Nachricht
- **Weiterleiten**: Leitet die ausgewählte Nachricht weiter (Betreff wird mit "Fw: " vorangestellt, Anhänge werden übernommen)

### Der Versanddialog {#versanddialog}

Der Versanddialog gliedert sich in einen linken Hauptbereich (Kopfdaten, Nachrichtentext, Anhänge) und eine rechte Seitenleiste (Speicheroptionen, Optionen, Vorlagen, Wiedervorlage/Frist).

#### Kopfdaten

| Feld | Beschreibung |
|------|--------------|
| **Von** | Auswahl des Absender-Postfachs. Das zuletzt verwendete Postfach wird vorgemerkt. |
| **An** | Liste der Empfänger. Empfänger werden über den Suchen-Knopf hinzugefügt (siehe unten). Per Rechtsklick auf einen Empfänger kann dieser wieder entfernt werden. |
| **Betreff** | Freitextfeld für den Betreff der Nachricht |

Zum Hinzufügen von Empfängern stehen drei Wege zur Verfügung:

- **Beteiligte der Akte**: Werden als Einträge im Empfänger-Menü angeboten (nur Beteiligte mit hinterlegter beA Safe-ID)
- **"suchen (Adressbuch)"**: Suche im lokalen Adressbuch von j-lawyer.org
- **"suchen (beA-Verzeichnis)"**: Suche im beA-Verzeichnisdienst

#### Nachrichtentext und Vorlagen

Im mittleren Bereich des Dialogs befindet sich das Textfeld für den Nachrichteninhalt. In der rechten Seitenleiste kann unter **Vorlagedaten** eine Vorlage ausgewählt werden. Vorlagen können Platzhalter enthalten, die beim Anwenden automatisch mit Daten der Akte, der Beteiligten sowie des Anwalts oder Sachbearbeiters befüllt werden. Über das Beteiligte-Panel unterhalb der Vorlagenauswahl wird festgelegt, welche Beteiligten in die Platzhalter eingesetzt werden.

#### Anhänge {#versand-anhaenge}

Unterhalb des Nachrichtentextes befindet sich die Anhangstabelle mit folgenden Spalten:

| Spalte | Beschreibung |
|--------|--------------|
| **Schriftsatz** | Kennzeichnet den Anhang als Schriftsatz (gegenseitig exklusiv mit "Anlage") |
| **Anlage** | Kennzeichnet den Anhang als Anlage (gegenseitig exklusiv mit "Schriftsatz") |
| **AZ Sender** | Fügt das Aktenzeichen des Senders in den Alias des Dokuments ein |
| **AZ Empfänger** | Fügt das Aktenzeichen des Empfängers in den Alias des Dokuments ein |
| **Alias** | Automatisch generierter Anzeigename (z.B. "01_Schriftsatz_Dateiname.pdf"), kann manuell angepasst werden |
| **Dateiname** | Ursprünglicher Dateiname (nicht editierbar) |

Anhänge können auf drei Wegen hinzugefügt werden:

- **Datei anhängen** (Knopf in der Werkzeugleiste): Öffnet einen Dialog zur Dateiauswahl
- **Drag & Drop**: Dateien können direkt auf die Anhangstabelle gezogen werden
- **Vorbelegung**: Bei Aufruf über die Dokumentenliste oder Weiterleitung werden Anhänge automatisch übernommen

Die Reihenfolge der Anhänge kann über die **Pfeil-Buttons** (auf/ab) rechts neben der Tabelle geändert werden. Per Rechtsklick können Anhänge wieder entfernt werden.

!!! info "Anlagen-Limits"
    Die Statuszeile unterhalb der Tabelle zeigt die aktuelle Anzahl und voraussichtliche Größe der Anhänge an. Es gelten folgende Grenzen: maximal **1000 Anhänge** und maximal **200 MB** Gesamtgröße. Bei Überschreitung von 50 Anhängen oder 60 MB wird die Anzeige zur Warnung rot eingefärbt.

#### Optionen {#versand-optionen}

Im Bereich **Optionen** der rechten Seitenleiste stehen folgende Einstellungen zur Verfügung:

- **Priorität**: Auswahl der Nachrichtenpriorität
- **Nachrichtentyp**: Auswahl zwischen "Allgemeine Nachricht", "Mahnantrag" und "Testnachricht"
- **Zustellung gegen Empfangsbekenntnis**: Fordert ein elektronisches Empfangsbekenntnis (eEB) an

!!! warning "eEB-Voraussetzung"
    Ein eEB kann nur für Nachrichten angefordert werden, die mindestens einen Anhang enthalten.

#### Aktenzeichen

Neben der Werkzeugleiste befinden sich die Felder **AZ Sender** und **AZ Empfänger** zur Angabe der jeweiligen Aktenzeichen. Das Empfänger-Aktenzeichen ist als editierbare Dropdown-Liste umgesetzt und kann bei Aufruf über die Beteiligten mit dem dort hinterlegten Aktenzeichen vorbelegt sein.

#### Speicheroptionen

- **als Dokument speichern**: Speichert die gesendete Nachricht als Dokument zur Akte (standardmäßig aktiviert). Ist keine Akte zugeordnet, wird vor dem Versand ein Dialog zur Aktenauswahl angezeigt.
- **Etikett**: Optional kann ein Dokumenten-Etikett für das gespeicherte Dokument vergeben werden.
- **Wiedervorlage / Frist**: Ermöglicht das Erstellen eines Kalendereintrags (Wiedervorlage oder Frist) beim Versand. Es können Grund, verantwortliche Person und Datum angegeben werden.

### Nachricht absenden {#absenden}

Die Werkzeugleiste des Versanddialogs bietet zwei Aktionen:

- **Absenden**: Sendet die Nachricht sofort. Vor dem Versand wird die Auswahl einer Kammer / eines Gerichts als Absenderautorität abgefragt.
- **In "Entwürfe" speichern**: Speichert die Nachricht als Entwurf im beA-Postfach, um sie später zu signieren und zu senden.

!!! tip "Hinweis"
    Es muss mindestens ein Empfänger angegeben sein, um eine Nachricht abzusenden oder als Entwurf zu speichern.

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
