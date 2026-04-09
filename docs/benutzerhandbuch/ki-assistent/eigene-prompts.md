# Eigene Prompts konfigurieren {#eigene-prompts}

Oftmals gibt es den Bedarf, Anfragen an eine KI mehrfach verwenden zu können. Bspw. stellen sich für das Erschließen umfangreicher Verträge immer die selben Fragen. Damit solche Anfragen nicht ständig erneut formuliert werden müssen, lassen Sie sich an zentraler Stelle hinterlegen und dann im jeweiligen Kontext (bspw. einer E-Mail oder per Rechtsklick auf ein Dokument) einfach aufrufen.

Im Menü „Einstellungen" – „Assistent Ingo" – „eigene Prompts" können Anfragen konfiguriert und gespeichert werden. Auf der linken Seite befindet sich die Liste aller eigenen Prompts, auf der rechten Seite die Detailkonfiguration des ausgewählten Prompts.

## Prompt konfigurieren

Nach einem Klick auf „+" wird ein neuer Prompt angelegt. Folgende Felder stehen zur Verfügung:

- **Name**: Der Name der Anfrage – dieser Wert erscheint bspw. in Kontextmenüs und sollte daher bewusst gewählt werden und nicht zu lang sein.

- **Funktion**: Bestimmt, welche Art einer Anfrage mittels des eigenen Prompts ausgeführt werden soll. Mögliche Werte sind:
    - **chat**: für Prompts, die zur Befragung / für iterative Frage-Antwort-Szenarien verwendet werden können
    - **explain**: für Prompts, die zu Recherchezwecken verwendet werden können (bspw. Erläutern von Begriffen oder Sachverhalten in E-Mails)
    - **generate**: für Prompts, die für das Generieren von Texten (bspw. Antworten auf E-Mails oder Generieren von Schriftsätzen) verwendet werden können
    - **summarize**: für Prompts, die zum Zusammenfassen von Texten (E-Mails, Dokumente) verwendet werden können
    - **transcribe**: aktuell nicht unterstützt
    - **translate**: für Prompts, die Texte übersetzen sollen
    - **vision**: für Prompts, welche eine Bildanalyse durchführen sollen – bspw. Extraktion von Text oder Beschreibung von Bildinhalten

- **Modell**: Auswahl des KI-Modells, das für diesen Prompt verwendet werden soll. Die verfügbaren Modelle hängen von der gewählten Funktion ab. Die Option „(Standard)" verwendet das Standardmodell der jeweiligen Funktion. Für das ausgewählte Modell werden folgende Informationen angezeigt:
    - **Token-Verbrauch**: Ob das Modell Ingo-Tokens oder Fremd-Tokens verbraucht
    - **Agentenfähigkeit**: Ob das Modell als Agent eingesetzt werden kann
    - **Modellbeschreibung**: Detailinformationen zum ausgewählten Modell

- **Prompt**: Die Anfrage an das KI-Modell. Auch wenn beliebige Formulierungen oftmals zu guten Ergebnissen führen, so ist es doch ratsam, sich mit den Grundlagen für das Prompting vertraut zu machen. Dazu gibt es eine Vielzahl guter Ressourcen, eine davon ist bspw. <https://www.promptingguide.ai/de>

- **System Prompt**: Optionaler System Prompt, der als übergeordnete Instruktion an das Modell gesendet wird (z.B. Rollendefinition oder Verhaltensregeln). Wird nur übertragen, wenn ein Wert eingetragen ist.

- **Modell-Konfiguration**: Je nach ausgewähltem Modell können zusätzliche modellspezifische Parameter konfiguriert werden (z.B. Temperatur oder andere Steuerungsparameter). Die verfügbaren Parameter werden dynamisch anhand des gewählten Modells angezeigt.

Ein Prompt kann beliebige Platzhalter enthalten, welche auch über das Vorlagensystem genutzt werden können (siehe Abschnitt „[Verwendung von Platzhaltern in Prompts](#platzhalter-in-prompts)").

!!! info "Hinweis"
    Aktenbezogene Platzhalter (bspw. `{{AKTE_ZEICHEN}}`) werden nur dann ersetzt, wenn der Prompt aus einer Akte heraus verwendet wird.

## Sichtbarkeit eigener Prompts

Je nach gewählter Funktion wird ein eigener Prompt an unterschiedlichen Stellen in der Anwendung angeboten. Die folgende Übersicht zeigt, wo Prompts welcher Funktion zur Verfügung stehen:

| Funktion | Verfügbar in |
|----------|-------------|
| **chat** | Aktenansicht (Kopfbereich und Dokumentenliste), E-Mail senden, E-Mail lesen, Desktop (eigenständiger Chat) |
| **generate** | Aktenansicht (Kopfbereich und Dokumentenliste), E-Mail senden, E-Mail lesen |
| **summarize** | Aktenansicht (Dokumentenliste), E-Mail senden, E-Mail lesen |
| **explain** | E-Mail senden, E-Mail lesen |
| **translate** | E-Mail senden, E-Mail lesen |
| **extract** | Aktenansicht (Dokumentenliste), Formulare (automatisches Befüllen), Adresserfassung aus Zwischenablage oder E-Mail, PDF-Anonymisierung |
| **vision** | Aktenansicht (Bildanalyse von Dokumenten) |
| **transcribe** | Audioplayer (Transkription von Audiodateien) |

!!! tip "Tipp"
    Der Name des eigenen Prompts erscheint direkt in den jeweiligen Kontextmenüs. Wählen Sie daher kurze, aussagekräftige Namen, damit die Menüs übersichtlich bleiben.

## Prompts verwalten

Neben dem Anlegen und Bearbeiten von Prompts stehen weitere Funktionen zur Verfügung:

- **Duplizieren**: Erstellt eine Kopie des ausgewählten Prompts (mit dem Suffix „(Kopie)")
- **Per E-Mail teilen**: Exportiert den Prompt als JSON-Datei und öffnet eine neue E-Mail zum Versand. Enthaltene API-Schlüssel werden dabei automatisch entfernt.
- **JSON importieren**: Importiert einen Prompt aus einer JSON-Datei, bspw. einen von einem Kollegen erhaltenen Prompt.

## Verfügbare Modelle {#modelle}

Bei der Konfiguration eigener Prompts kann ein spezifisches Modell ausgewählt werden. Die verfügbaren Modelle unterscheiden sich in Leistungsfähigkeit, Geschwindigkeit, Kosten und Funktionsumfang. Sie sind in zwei Kategorien unterteilt:

### j-lawyer.CLOUD-Modelle (Ingo-Tokens) {#cloud-modelle}

Diese Modelle werden lokal in der j-lawyer.CLOUD-Infrastruktur betrieben und über Ingo-Tokens abgerechnet. Sie sind kostenlos im Rahmen des Token-Kontingents nutzbar.

| Modell | Beschreibung | Agentenfähig |
|--------|-------------|:------------:|
| **Ingo Occiglot** | Lokales 7B-Modell, spezialisiert auf Deutsch und Englisch. Gut für einfache Zusammenfassungen und Übersetzungen. Begrenzte Leistung bei komplexen Aufgaben. | Nein |
| **Ingo Gemma2** | Google Gemma 2 mit 9B Parametern. Solide Textqualität und gutes Sprachverständnis. Schwächer als größere Modelle bei komplexem Reasoning. | Nein |
| **Ingo Gemma3** | Google Gemma 3 mit 12B Parametern. Sehr gute Textqualität, multilingual. Deutlich besser als Gemma 2 bei Reasoning und Instruktionsbefolgung. Für die Größe sehr leistungsfähig. | Nein |
| **Ingo Qwen3.5** | Alibaba Qwen 3.5 mit 4B Parametern. Gute Mehrsprachigkeit. Für die Größe starkes Reasoning. Bei langen Texten und komplexen Analysen limitiert. | Ja |
| **Ingo Llama3.1-uncensored** | Meta Llama 3.1 ohne Sicherheitsfilter. Gutes Reasoning. Keine Inhaltsverweigerungen – geeignet für juristische Texte ohne Zensurprobleme. | Ja |
| **Ingo Llama3.1-abliterated** | Meta Llama 3.1 8B mit entfernten Sicherheitssperren. Ähnlich wie Uncensored-Variante, aber per Abliteration optimiert. Kompakt und schnell. | Ja |
| **Ingo Ministral-3 Small** | Mistral Ministral 3B. Extrem schnell und ressourcenschonend. Optimiert für einfache Aufgaben wie Klassifikation und Extraktion. Für komplexe Texte nicht geeignet. | Ja |
| **Ingo Ministral-3** | Mistral Ministral 3. Optimiert für Aufgaben wie Klassifikation und Extraktion. | Ja |
| **Ingo Llama3.2** | Meta Llama 3.2 mit 3B Parametern. Sehr schnell. Gut für Extraktion und einfache Aufgaben. Begrenzte Qualität bei anspruchsvoller Textgenerierung. | Ja |
| **Ingo Llama3.2-uncensored** | Meta Llama 3.2 ohne Sicherheitsfilter. Schnell, keine Inhaltsverweigerungen. Ideal für Extraktion ohne Zensurprobleme. | Ja |

### Externe Modelle (Fremd-Tokens) {#externe-modelle}

Diese Modelle werden über externe Anbieter bereitgestellt. Die Nutzung wird separat abgerechnet und verbraucht keine Ingo-Tokens. Daten werden an den jeweiligen Anbieter übertragen.

| Modell | Anbieter | Beschreibung | Agentenfähig |
|--------|----------|-------------|:------------:|
| **Sonnet 4** | Anthropic | Leistungsstarkes Cloud-Modell. Mittlere Kosten. Exzellentes Reasoning, Coding und Textverständnis. Sehr gute Balance aus Qualität und Geschwindigkeit. Ideal für anspruchsvolle juristische Aufgaben. | Ja |
| **Haiku 3.5** | Anthropic | Schnellstes und günstigstes Anthropic-Modell. Sehr schnelle Antwortzeiten. Gut für einfache Aufgaben, Klassifikation und Extraktion. | Ja |
| **Opus 4** | Anthropic | Leistungsfähigstes Anthropic-Modell. Hohe Kosten. Bestes Reasoning, Analyse und Textgenerierung. Ideal für komplexeste juristische Analysen. Langsamer und deutlich teurer als Sonnet. | Ja |
| **Deepseek** | DeepSeek | DeepSeek V3. Sehr günstig. Starkes Reasoning und gute Mehrsprachigkeit. Gutes Preis-Leistungs-Verhältnis. Gelegentlich weniger zuverlässig bei Instruktionsbefolgung. | Ja |
| **Mistral Large** | Mistral | Größtes Mistral-Modell. Mittlere Kosten. Starkes Reasoning, sehr gute europäische Sprachunterstützung. Besonders gut für mehrsprachige juristische Texte. | Ja |
| **Mistral Medium** | Mistral | Mittelgroßes Mistral-Modell. Günstiger als Large. Gute europäische Sprachunterstützung. Schneller als Large. Für Standardaufgaben ausreichend. | Ja |
| **Mistral Small** | Mistral | Kleines Mistral-Modell. Günstiger als Medium. Gute europäische Sprachunterstützung. Sehr schnell. Sehr großes Kontextfenster von 256.000 Tokens. | Ja |
| **Google Gemini 2 Flash** | Google | Schnelles Modell mit großem Kontextfenster (1M Tokens). Ideal für lange Dokumente. Bei Präzision und Nuancen schwächer als Claude oder Mistral Large. | Ja |

!!! tip "Empfehlung"
    Für einfache Extraktionen und Klassifikationen sind die j-lawyer.CLOUD-Modelle wie **Ingo Occiglot** oder **Ingo Llama3.2** ausreichend. Für [agentische KI](agenten.md) sollte ein agentenfähiges Modell gewählt werden - bspw. **Ingo Qwen3.5**.

!!! warning "Datenschutz bei externen Modellen"
    Bei der Nutzung externer Modelle werden Daten an den jeweiligen Anbieter übertragen. Achten Sie darauf, dass dies mit den Datenschutzanforderungen Ihrer Kanzlei vereinbar ist.

### Modellempfehlung: Mistral {#modellempfehlung-mistral}

Für beste Performance und ein gutes Preis-/Leistungsverhältnis bei externen Modellen ist **Mistral Small** ein sehr gutes Modell. Mistral bietet starke europäische Sprachunterstützung und ist besonders für mehrsprachige juristische Texte geeignet.

Aus Datenschutzsicht sind die Modelle von Mistral besonders interessant: Mistral schließt vertraglich aus, dass übermittelte Daten für das Training von Modellen verwendet werden, und bietet einen DSGVO-konformen Auftragsverarbeitungsvertrag (AVV) an.

#### Mistral AI Studio aufladen

Um die Mistral-Modelle in j-lawyer nutzen zu können, wird ein Guthaben im [Mistral AI Studio](https://admin.mistral.ai/subscriptions?subscription-tab=ai-studio) benötigt. Dieses kann mit wenigen Euro aufgeladen werden – es ist kein klassisches Abonnement, das Guthaben wird nach tatsächlichem Verbrauch abgerechnet.

Zum Aufladen im AI Studio unter „Workspace" – „Billing" eine Zahlungsmethode hinterlegen und Guthaben aufladen.

#### API Key bei Mistral erstellen

1. Im [Mistral AI Studio](https://admin.mistral.ai/organization/api-keys) anmelden bzw. ein Konto erstellen.
2. Im Menü links auf „API Keys" klicken.
3. Auf „Create new key" klicken.
4. Einen Namen für den Key vergeben (bspw. „j-lawyer") und bestätigen.
5. Den angezeigten Key kopieren und sicher aufbewahren – er wird nur einmal angezeigt.

#### API Key in j-lawyer hinterlegen

1. Im j-lawyer Client unter „Einstellungen" – „Assistent Ingo" – „eigene Prompts" einen Prompt anlegen oder bearbeiten.
2. Als Modell eines der Mistral-Modelle auswählen (bspw. **Mistral Small**).
3. In den daraufhin angezeigten Konfigurationsfeldern den kopierten API Key im Feld `api-key` eintragen.
4. Den Prompt speichern.

Der API Key wird pro Prompt hinterlegt. Beim Teilen von Prompts per E-Mail wird der API Key automatisch entfernt.

## Verwendung von Platzhaltern in Prompts {#platzhalter-in-prompts}

Die Ergebnisse einer KI-Anfrage ist maßgeblich abhängig von der Qualität der Eingangsdaten als auch von der Formulierung der Anfrage selbst (des sogenannten Prompts). Je besser der Prompt, umso weniger „Nacharbeiten" ist notwendig und umso treffender wird die Ergebnismenge sein. Daher kann es sinnvoll sein, möglichst viele relevante Informationen in einen Prompt aufzunehmen – das können bspw. Informationen zur Akte, zu Beteiligten oder fachliche Informationen zum Fall selbst sein.

Anbei ein Beispiel-Prompt zur Anwendung in verkehrsrechtlichen Angelegenheiten:

Du bist {{USER_FKT}} {{USER_AN}}. Generiere aus der untenstehenden Unfallanzeige einen Klageschriftsatz. Gehe dabei wie folgt vor:

1. Ermittle aus der Unfallanzeige die Beteiligten. Dein Mandant ist {{MANDANT_VORNAME}} {{MANDANT_NAME}}. Dieser ist in dem Klageschreiben der "Kläger". Benenne diesen mit vollständigem Namen und Adresse und nimm die Informationen als Absatz in den Klageschriftsatz auf.

2. Ermittle aus dem Text den Gegner, sein Name ist {{GEGNER_VORNAME}} {{GEGNER_NAME}}, und die Versicherung seines Fahrzeugs. Benenne diese als "Beklagte zu 1.", "Beklagte zu 2." und nimm die Informationen als Absatz in den Klageschriftsatz auf.

3. Formuliere Klageanträge, in denen die Beklagten gesamtschuldnerisch zur Zahlung des offenen Schadensersatzes i.H.v. {{VRKHR_SCHADENSUMME}} EUR verurteilt werden zuzüglich Zinsen in Höhe des Basiszinssatzes seit dem Verzugszeitpunkt. Nimm die Klageanträge in den Klageschriftsatz auf.

4. Begründe die Klage. Beginne hierbei zunächst mit den Statusangaben und nenne dabei den Mandanten Kläger, die Fahrerin des anderen Fahrzeugs Beklagte  zu 1., den Halter des anderen Fahrzeugs  Beklagter zu 2. und die Kfz-Haftpflichtversicherung des anderen Fahrzeugs Beklagte zu 3. Teile mit ob der Unfall polizeilich aufgenommen wurde und wenn ja benenne das Polizeirevier und die polizeiliche Tagebuchnummer. Nimm die Begründung in den Klageschriftsatz auf.

5. Übernehme den dargestellten Unfallhergang und benenne den Mandanten Kläger und den Fahrer des anderen Fahrzeuges Beklagter zu 1. und nimm diese Informationen in den Klageschriftsatz auf.

6. Übernehme die Darstellung des Schadens, die dort verwendeten Formulierungen und Tabelle. Nimm diese Informationen in den Klageschriftsatz auf.

7. Übernehme die Formulierung der rechtlichen Ausführungen. Ersetze dabei Mandant oder Mandantschaft als Kläger und nimm diese Informationen in den Klageschriftsatz auf.

Hier der Text der Unfallanzeige:

Wird der Prompt genutzt, so findet vorab automatisch eine Ersetzung der Platzhalter statt.
