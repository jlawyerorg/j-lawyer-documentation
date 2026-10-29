# Eigene Prompts konfigurieren {#eigene-prompts}

Oftmals gibt es den Bedarf, Anfragen an eine KI mehrfach verwenden zu können. Bspw. stellen sich für das Erschließen umfangreicher Verträge immer die selben Fragen. Damit solche Anfragen nicht ständig erneut formuliert werden müssen, lassen Sie sich an zentraler Stelle hinterlegen und dann im jeweiligen Kontext (bspw. einer E-Mail oder per Rechtsklick auf ein Dokument) einfach aufrufen.

Im Menü „Einstellungen" – „Assistent Ingo" – „eigene Prompts" können Anfragen konfiguriert und gespeichert werden. Auf der linken Seite befindet sich die Liste aller eigenen Prompts, auf der rechten Seite die Detailkonfiguration des ausgewählten Prompts.

## Prompt konfigurieren

Nach einem Klick auf „+" wird ein neuer Prompt angelegt. Folgende Felder stehen zur Verfügung:

- **Name**: Der Name der Anfrage – dieser Wert erscheint bspw. in Kontextmenüs und sollte daher bewusst gewählt werden und nicht zu lang sein.

- **Untermenü**: Optional. Ordnet den Prompt in den Kontextmenüs von Assistent Ingo einem Untermenü zu (siehe [Prompts in Untermenüs gruppieren](#untermenues)). Bleibt das Feld leer, erscheint der Prompt auf der obersten Ebene.

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
| **chat** | Aktenansicht (Kopfbereich und Dokumentenliste), Falldatenblätter (nur agentenfähige Modelle), Vorschläge für Bezeichnung und Schlagworte von Dokumenten, E-Mail senden, E-Mail lesen, Desktop (eigenständiger Chat) |
| **generate** | Aktenansicht (Kopfbereich und Dokumentenliste), E-Mail senden, E-Mail lesen |
| **summarize** | Aktenansicht (Dokumentenliste), E-Mail senden, E-Mail lesen |
| **explain** | E-Mail senden, E-Mail lesen |
| **translate** | E-Mail senden, E-Mail lesen |
| **extract** | Aktenansicht (Dokumentenliste), Vorschläge für Bezeichnung und Schlagworte von Dokumenten, Formulare (automatisches Befüllen), Adresserfassung aus Zwischenablage oder E-Mail, PDF-Anonymisierung |
| **vision** | Aktenansicht (Bildanalyse von Dokumenten) |
| **transcribe** | Audioplayer (Transkription von Audiodateien) |

!!! tip "Tipp"
    Der Name des eigenen Prompts erscheint direkt in den jeweiligen Kontextmenüs. Wählen Sie daher kurze, aussagekräftige Namen, damit die Menüs übersichtlich bleiben.

## Prompts in Untermenüs gruppieren {#untermenues}

Mit wachsender Zahl eigener Prompts werden die Kontextmenüs von Assistent Ingo schnell unübersichtlich. Über das Feld **Untermenü** lassen sich Prompts deshalb nach eigenen Kriterien gruppieren – bspw. nach Rechtsgebiet („Arbeitsrecht", „Mietrecht") oder nach Tätigkeit („Mahnwesen", „Schriftsätze").

- **Bestehendes Untermenü wählen oder neues anlegen**: Die Auswahlliste schlägt alle bereits verwendeten Untermenüs vor. Für ein neues Untermenü wird einfach ein neuer Name eingetippt.
- **Mehrere Untermenüs**: Soll ein Prompt in mehreren Untermenüs erscheinen, werden die Namen durch Semikolon getrennt, bspw. `Klage;Vorlagen`. Der Prompt muss dafür nicht dupliziert werden.
- **Eine Ebene**: Untermenüs können nicht weiter verschachtelt werden.

Im Menü erscheinen zuerst die Prompts ohne Untermenü, danach die Untermenüs in alphabetischer Reihenfolge. Ein Untermenü wird nur einmal angezeigt, auch wenn darin Prompts unterschiedlicher Funktionen (bspw. **chat** und **generate**) enthalten sind.

Die Gruppierung wirkt überall, wo eigene Prompts angeboten werden – in den Kontextmenüs von Dokumenten und E-Mails ebenso wie in der Prompt-Auswahl der Chat- und Generieren-Dialoge.

!!! example "Beispiel"
    | Prompt | Untermenü |
    |--------|-----------|
    | Vertrag zusammenfassen | *(leer)* |
    | Kündigung prüfen | Arbeitsrecht |
    | Abmahnung entwerfen | Arbeitsrecht;Schriftsätze |
    | Mieterhöhung prüfen | Mietrecht |

    Im Kontextmenü erscheint „Vertrag zusammenfassen" direkt, darunter die Untermenüs „Arbeitsrecht", „Mietrecht" und „Schriftsätze". „Abmahnung entwerfen" ist sowohl unter „Arbeitsrecht" als auch unter „Schriftsätze" zu finden.

!!! note "Hinweis"
    Das Untermenü kann derzeit nur im Desktop-Client gepflegt werden.

## Prompts verwalten

Neben dem Anlegen und Bearbeiten von Prompts stehen weitere Funktionen zur Verfügung:

- **Duplizieren**: Erstellt eine Kopie des ausgewählten Prompts (mit dem Suffix „(Kopie)")
- **Per E-Mail teilen**: Exportiert den Prompt als JSON-Datei und öffnet eine neue E-Mail zum Versand. Enthaltene API-Schlüssel werden dabei automatisch entfernt. Das Untermenü wird mit exportiert.
- **JSON importieren**: Importiert einen Prompt aus einer JSON-Datei, bspw. einen von einem Kollegen erhaltenen Prompt.

## Verfügbare Modelle {#modelle}

Bei der Konfiguration eigener Prompts kann ein spezifisches Modell ausgewählt werden. Die verfügbaren Modelle unterscheiden sich in Leistungsfähigkeit, Geschwindigkeit, Kosten und Funktionsumfang. Die Spalte **Funktionen** zeigt, für welche [Funktionen](#prompt-konfigurieren) ein Modell ausgewählt werden kann; **Agentenfähig** kennzeichnet Modelle mit Unterstützung für Werkzeugaufrufe (siehe [Agentische KI](agenten.md)). Die Modelle sind in zwei Kategorien unterteilt:

### j-lawyer.CLOUD-Modelle (Ingo-Tokens) {#cloud-modelle}

Diese Modelle werden lokal in der j-lawyer.CLOUD-Infrastruktur betrieben und über Ingo-Tokens abgerechnet. Sie sind kostenlos im Rahmen des Token-Kontingents nutzbar.

| Modell | Beschreibung | Funktionen | Agentenfähig |
|--------|-------------|------------|:------------:|
| **j-lawyer.CLOUD: Ingo Qwen3.8 Large** | Alibaba Qwen 3.8 mit 27B Parametern. Größtes lokales Modell mit sehr guter Mehrsprachigkeit und starkem Reasoning. Gut geeignet für lange Texte und anspruchsvolle Analysen. Langsamer als die kleineren Modelle. | summarize, explain, generate, chat, extract | Ja |
| **j-lawyer.CLOUD: Ingo Qwen3.5** | Alibaba Qwen 3.5 mit 9B Parametern. Sehr gute Mehrsprachigkeit, gutes Reasoning. Deutlich schneller als Qwen 3.8 Large. Gut für Zusammenfassungen, Extraktion und Chat; bei sehr komplexen Analysen schwächer. | summarize, explain, generate, chat, extract | Ja |
| **j-lawyer.CLOUD: Ingo Granite4.1** | IBM Granite 4.1 mit 8B Parametern. Nativ mehrsprachig, sehr großes Kontextfenster. Schnell, **ohne Denkmodus** und mit planbaren Antwortzeiten. Gut für Zusammenfassungen, Extraktion und Werkzeugaufrufe; bei komplexem Reasoning schwächer als größere Modelle. | summarize, explain, generate, chat, extract | Ja |
| **j-lawyer.CLOUD: Ingo Gemma3** | Google Gemma 3 mit 12B Parametern. Sehr gute Textqualität, multilingual. Für die Größe sehr leistungsfähig. | summarize, explain, generate, chat, extract, translate | Nein |
| **j-lawyer.CLOUD: Ingo Gemma4** | Google Gemma 4 E2B (2,3B effektive Parameter). Multimodal, über 140 Sprachen. Sehr kompakt und schnell; für komplexe Analysen und lange Texte limitiert. | summarize, explain, generate, chat, extract, vision | Nein |
| **j-lawyer.CLOUD: Ingo Llama3.1-uncensored** | Meta Llama 3.1 ohne Sicherheitsfilter. Gutes Reasoning, keine Inhaltsverweigerungen – geeignet für juristische Texte ohne Zensurprobleme. | summarize, explain, generate, chat, translate | Nein |
| **j-lawyer.CLOUD: Ingo Llama3.1-abliterated** | Meta Llama 3.1 8B mit entfernten Sicherheitssperren, per Abliteration optimiert. Kompakt und schnell, aber weniger präzise als größere Modelle. | summarize, explain, generate, chat | Nein |
| **j-lawyer.CLOUD: Ingo Llama3.2** | Meta Llama 3.2 mit 3B Parametern. Sehr schnell, gut für Extraktion und einfache Aufgaben. | extract | Nein |
| **j-lawyer.CLOUD: Ingo Llama3.2-uncensored** | Meta Llama 3.2 ohne Sicherheitsfilter. Schnell, keine Inhaltsverweigerungen. Für Extraktion ohne Zensurprobleme. | extract | Nein |
| **j-lawyer.CLOUD: Ingo Qwen3-VL** | Alibaba Qwen 3 VL mit 8B Parametern. Bildanalyse, Dokumentverständnis und Texterkennung in Bildern (32 Sprachen), robust bei schrägen oder schlecht belichteten Aufnahmen. | vision | Ja |
| **j-lawyer.CLOUD: Ingo Qwen3-VL small** | Alibaba Qwen 3 VL mit 4B Parametern. Wie Qwen3-VL, kleiner und schneller. | vision | Ja |
| **j-lawyer.CLOUD: Ingo Ministral-3** | Mistral Ministral 3 mit 14B Parametern. Gute Bild- und Texterkennung, geeignet für Bildbeschreibungen und die Extraktion von Text aus Bildern und Scans. | vision | Ja |
| **j-lawyer.CLOUD: Ingo Ministral-3 Small** | Mistral Ministral 3B. Extrem schnell und ressourcenschonend, für einfache Bildanalysen. | vision | Ja |

### Externe Modelle (Fremd-Tokens) {#externe-modelle}

Diese Modelle werden über externe Anbieter bereitgestellt. Die Nutzung wird separat abgerechnet und verbraucht keine Ingo-Tokens. Daten werden an den jeweiligen Anbieter übertragen.

| Modell | Anbieter | Beschreibung | Funktionen | Agentenfähig |
|--------|----------|-------------|------------|:------------:|
| **Anthropic: Sonnet 4.6** | Anthropic | Leistungsstark und kosteneffizient, günstigstes der drei Anthropic-Modelle. Exzellentes Reasoning und Textverständnis, adaptives Thinking, 1M-Token-Kontextfenster. Ideal für anspruchsvolle juristische Standardaufgaben. | summarize, explain, generate, chat, extract | Ja |
| **Anthropic: Opus 4.8** | Anthropic | Sehr leistungsfähiges Spitzenmodell. Teurer als Sonnet, günstiger als Fable 5. Herausragend bei Analyse, Textgenerierung und langen Aufgaben; adaptives Thinking, 1M-Token-Kontextfenster. Langsamer als Sonnet. | summarize, explain, generate, chat, extract | Ja |
| **Anthropic: Fable 5** | Anthropic | Neuestes und leistungsfähigstes Anthropic-Modell, teurer als Opus. Stärkstes Reasoning, Thinking ist immer aktiv. Erfordert 30 Tage Datenaufbewahrung beim Anbieter (nicht mit Zero-Data-Retention verfügbar). | summarize, explain, generate, chat, extract | Ja |
| **OpenAI: GPT-4o** | OpenAI | Flaggschiff-Modell von OpenAI. Mittlere Kosten. Starkes Reasoning, multimodal, 128k Kontextfenster. Sehr gute Textqualität und Instruktionsbefolgung. | summarize, explain, generate, chat, extract | Ja |
| **OpenAI: GPT-4o mini** | OpenAI | Kompakt und günstig, sehr schnell, 128k Kontextfenster. Gut für einfachere Aufgaben wie Zusammenfassungen und Extraktion. | summarize, explain, generate, chat, extract | Ja |
| **OpenAI: o3-mini** | OpenAI | Reasoning-Modell für logisches Denken und komplexe Problemlösung. Langsamere Antworten durch erweiterten Denkprozess. | summarize, explain, generate, chat, extract | Ja |
| **LangDock: GPT-5.6 Sol** | LangDock | Aktuelles OpenAI-Flaggschiff via LangDock, DSGVO-konform und EU-gehostet. Stärkstes Reasoning, exzellente Instruktionsbefolgung. | summarize, explain, generate, chat, extract | Ja |
| **LangDock: GPT-5.2** | LangDock | Sehr starkes Allzweckmodell via LangDock mit guter Balance aus Intelligenz und Kosten. | summarize, explain, generate, chat, extract | Ja |
| **LangDock: GPT-5.1** | LangDock | Ausgereiftes Allzweckmodell via LangDock mit sehr guter Textqualität. Gut für Schriftsatzentwürfe und Analysen. | summarize, explain, generate, chat, extract | Ja |
| **LangDock: GPT-5** | LangDock | Solides Allzweckmodell der GPT-5-Generation via LangDock. | summarize, explain, generate, chat, extract | Ja |
| **LangDock: GPT-5 mini** | LangDock | Kompakte, günstige und schnelle Variante via LangDock. Gut für Zusammenfassungen und Extraktion. | summarize, explain, generate, chat, extract | Ja |
| **LangDock: o3** | LangDock | OpenAI-Reasoning-Modell via LangDock. Langsamere Antworten durch erweiterten Denkprozess. | summarize, explain, generate, chat, extract | Ja |
| **LangDock: o4-mini** | LangDock | Kompaktes Reasoning-Modell via LangDock, schnell und kosteneffizient. | summarize, explain, generate, chat, extract | Ja |
| **Mistral: Large** | Mistral | Größtes Mistral-Modell. Mittlere Kosten, starkes Reasoning, sehr gute europäische Sprachunterstützung, 256.000 Tokens Kontextfenster. | summarize, explain, generate, chat, extract | Ja |
| **Mistral: Medium** | Mistral | Günstiger und schneller als Large, 128.000 Tokens Kontextfenster. Für Standardaufgaben ausreichend. | summarize, explain, generate, chat, extract | Ja |
| **Mistral: Small** | Mistral | Günstiger als Medium, sehr schnell, 256.000 Tokens Kontextfenster. | summarize, explain, generate, chat, extract | Ja |
| **Google: Gemini 3 Flash** | Google | Schnelles Modell mit 1M-Token-Kontext und Bildanalyse. Reasoning-Modell mit spürbarer Latenz durch interne Denkschritte. Derzeit im Preview-Status. | summarize, explain, generate, chat, extract, vision | Ja |
| **Deepseek** | DeepSeek | DeepSeek V3. Sehr günstig, starkes Reasoning, gute Mehrsprachigkeit. Gelegentlich weniger zuverlässig bei Instruktionsbefolgung. | summarize, explain, generate, chat | Ja |

!!! tip "Empfehlung"
    Für einfache Extraktionen und kurze, klar umrissene Aufgaben sind schnelle Modelle ohne Denkmodus wie **j-lawyer.CLOUD: Ingo Granite4.1** oder **j-lawyer.CLOUD: Ingo Llama3.2** gut geeignet. Für [agentische KI](agenten.md) sollte ein agentenfähiges Modell gewählt werden – bspw. **j-lawyer.CLOUD: Ingo Qwen3.5**, für anspruchsvolle Analysen **j-lawyer.CLOUD: Ingo Qwen3.8 Large**. Für die [Bildanalyse](bildanalyse.md) stehen eigene Modelle mit der Funktion **vision** zur Verfügung.

!!! warning "Datenschutz bei externen Modellen"
    Bei der Nutzung externer Modelle werden Daten an den jeweiligen Anbieter übertragen. Achten Sie darauf, dass dies mit den Datenschutzanforderungen Ihrer Kanzlei vereinbar ist.

### Modellempfehlung: Mistral {#modellempfehlung-mistral}

Für beste Performance und ein gutes Preis-/Leistungsverhältnis bei externen Modellen ist **Mistral: Small** ein sehr gutes Modell. Mistral bietet starke europäische Sprachunterstützung und ist besonders für mehrsprachige juristische Texte geeignet.

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
2. Als Modell eines der Mistral-Modelle auswählen (bspw. **Mistral: Small**).
3. In den daraufhin angezeigten Konfigurationsfeldern den kopierten API Key im Feld `api-key` eintragen.
4. Den Prompt speichern.

Der API Key wird pro Prompt hinterlegt. Beim Teilen von Prompts per E-Mail wird der API Key automatisch entfernt.

### Modellempfehlung: LangDock {#modellempfehlung-langdock}

[LangDock](https://www.langdock.com) ist eine deutsche KI-Plattform mit Sitz in Berlin, die Zugang zu führenden KI-Modellen verschiedener Anbieter über eine einheitliche, DSGVO-konforme Schnittstelle bietet. Alle Anfragen werden ausschließlich über Server in der EU verarbeitet.

Über LangDock stehen in j-lawyer Modelle von OpenAI zur Verfügung (GPT-5.6 Sol, GPT-5.2, GPT-5.1, GPT-5, GPT-5 mini, o3, o4-mini) – ohne dass ein separates Konto beim Anbieter erforderlich ist. Ein einziger LangDock API Key genügt für alle Modelle.

#### Vorteile in Sachen Datenschutz

- **EU-Datenverarbeitung**: Alle Daten werden ausschließlich auf Servern innerhalb der EU verarbeitet und gespeichert – es findet keine Übertragung in Drittländer statt.
- **DSGVO-Konformität**: LangDock bietet einen Auftragsverarbeitungsvertrag (AVV) nach Art. 28 DSGVO an.
- **Kein Training mit Nutzerdaten**: Übermittelte Daten werden nicht für das Training von KI-Modellen verwendet.
- **Ein Anbieter, viele Modelle**: Anstatt separate Verträge und Konten bei OpenAI, Anthropic und weiteren Anbietern zu unterhalten, genügt eine einzige Vertragsbeziehung mit einem deutschen Unternehmen.

Für Kanzleien, die Modelle wie GPT-5 nutzen möchten und dabei Wert auf Datenschutz legen, ist LangDock eine empfehlenswerte Alternative zur direkten Nutzung der US-amerikanischen Anbieter.

#### LangDock-Guthaben aufladen

Um die LangDock-Modelle in j-lawyer nutzen zu können, wird ein Guthaben bei [LangDock](https://www.langdock.com) benötigt. Dieses wird nach tatsächlichem Verbrauch abgerechnet.

#### API Key bei LangDock erstellen

1. Bei [LangDock](https://www.langdock.com) anmelden bzw. ein Konto erstellen.
2. Im Dashboard einen neuen API Key erstellen.
3. Den angezeigten Key kopieren und sicher aufbewahren – er wird nur einmal angezeigt.

#### API Key in j-lawyer hinterlegen

1. Im j-lawyer Client unter „Einstellungen" – „Assistent Ingo" – „eigene Prompts" einen Prompt anlegen oder bearbeiten.
2. Als Modell eines der LangDock-Modelle auswählen (bspw. **LangDock: GPT-5.2**).
3. In den daraufhin angezeigten Konfigurationsfeldern den kopierten API Key im Feld `api-key` eintragen.
4. Den Prompt speichern.

Der API Key ist für alle LangDock-Modelle identisch – er muss aber pro Prompt hinterlegt werden. Beim Teilen von Prompts per E-Mail wird der API Key automatisch entfernt.

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
