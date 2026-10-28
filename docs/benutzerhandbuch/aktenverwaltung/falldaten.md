# Falldaten {#falldaten}

Der Tab "Falldaten" ermöglicht die strukturierte Erfassung von fallspezifischen Informationen über Falldatenblätter.

## Zweck

Falldatenblätter bieten strukturierte Formulare für bestimmte Rechtsgebiete oder Falltypen. Sie ermöglichen:

- Systematische Erfassung relevanter Informationen für einen schnelleren Überblick
- Nutzung der erfassten Daten in Dokumentvorlagen
- Standardisierte Arbeitsabläufe

## Falldatenblatt hinzufügen

1. Klicken Sie auf den Reiter **Falldaten hinzufügen**
2. Wählen Sie das gewünschte Falldatenblatt aus der Liste
3. Das Falldatenblatt wird zur Akte hinzugefügt

### Verfügbare Falldatenblätter

Die verfügbaren Falldatenblätter werden über Updates bereitgestellt. Folgende Falldatenblätter sind verfügbar:

| Rechtsgebiet | Falldatenblatt | Beschreibung | [mit Ingo ausfüllen](#falldaten-ki-befuellung) |
|--------------|----------------|--------------|:---:|
| **Verkehrsrecht** | Verkehrsunfalldaten | Erfassung von Verkehrsunfalldaten mit Schwerpunkt Sachschäden | ✓ |
| **Verkehrsrecht** | Verkehrsrecht Owi | Erfassung von Daten zu einer Ordnungswidrigkeit | ✓ |
| **Mietrecht** | Mietrechtssachen | Erfassung von Mieter-/Vermieterinformationen | ✓ |
| **Arbeitsrecht** | Arbeitsrecht: Kündigungsschutz | Kündigungsschutzklage | ✓ |
| **Arbeitsrecht** | Arbeitsrecht: Elternzeit | Elternzeiten erfassen und darstellen |  |
| **Arbeitsrecht** | Arbeitsrecht: Vertragsprüfung | Arbeitsvertrag prüfen |  |
| **Arbeitsrecht** | Arbeitsrecht: Teilzeit in Elternzeit | Teilzeit in Elternzeit |  |
| **Familienrecht** | Familienrecht | Allgemeine Familienrechtssachen |  |
| **Familienrecht** | Unterhalt | Einkommen/Ausgaben, Kindes- und Ehegattenunterhalt (in Entwicklung) |  |
| **Erbrecht** | Erbrecht | Daten zu Beteiligten und Testament |  |
| **Strafrecht** | Strafrecht | Erfassung von Strafrechtsverfahren |  |
| **Betreuungsrecht** | Betreuung | Erfassung von Betreuten-Stammdaten |  |
| **Betreuungsrecht** | Betreuung 2026 | Erfassung von Betreuten-Stammdaten, ab dem Jahr 2026 |  |
| **Sozialrecht** | Untätigkeitsklage SGG | Untätigkeitsklagen-Generator |  |
| **Inkasso** | Inkasso | Inkasso und Forderungsmanagement |  |
| **Inkasso** | Inkasso: Forderung | Erfassungsbogen für offene Forderung |  |
| **Datenschutz** | SCHUFA-Auskunft | Erfassung und Auswertung einer SCHUFA-Datenkopie nach Art. 15 DS-GVO (Verträge, Zahlungsstörungen, Anfragen, Scores) | ✓ |
| **Reiserecht** | Fluggastrechte | Fluggastrechtesachen (EU-VO 261/2004, Montrealer Übereinkommen, Ticketerstattung), inkl. RVG-Gebührenrechner |  |
| **Wettbewerbsrecht** | UWG-Verfahren | Erfassung von UWG-Verfahren |  |
| **Wettbewerbsrecht** | UWG-Auswertung | Auswertungen zu UWG-Verfahren |  |
| **Verbraucherschutz** | UKlaG Beanstandung | Beanstandung nach UKlaG |  |
| **Verbraucherschutz** | UKlaG Scorecard | Statistik-relevante Daten nach UKlaG |  |
| **Verbraucherschutz** | UKlaG Dokumente | Dokumentenerfassung nach UKlaG |  |
| **Notariat** | Notariat: Kaufvertrag | Notarielle Kaufverträge | ✓ |
| **Notariat** | Notariat: UVZ | Eintragungen im Urkundenverzeichnis |  |
| **Geldwäscheprävention** | GWG/PEP-Prüfung | Dokumentation der Prüfung nach dem Geldwäschegesetz (Identifizierung, wirtschaftlich Berechtigter, politisch exponierte Personen) |  |
| **Rechtspsychologie** | psych. Gutachten | Bearbeitung rechtspsychologischer Gutachten |  |
| **Gewerblicher Rechtsschutz** | gew. Schutzrecht | Gewerbliches Schutzrecht |  |
| **Allgemein** | Allg. Falldaten | Frei konfigurierbares Falldatenblatt mit verschiedenen Oberflächenelementen |  |
| **Integration** | Gravity Forms | Übernahme von Eingaben aus WordPress Gravity Forms |  |
| **Integration** | Justin Legal | Digitale Mandatsannahme via Justin Legal |  |

!!! info "Regelmäßige Erweiterung"
    Die Liste der Falldatenblätter wird regelmäßig erweitert. Prüfen Sie unter **Einstellungen** → **Akten** → **Falldatenblätter** auf verfügbare Updates.

## Falldatenblatt ausfüllen

Nach dem Hinzufügen erscheint das Falldatenblatt als eigener Reiter. Die Felder können manuell ausgefüllt werden.

### Mit Ingo ausfüllen {#falldaten-ki-befuellung}

Falldatenblätter können mit Hilfe von [Assistent Ingo](../ki-assistent/index.md) automatisch aus Dokumenten der Akte befüllt werden:

1. Klicken Sie im Falldatenblatt auf **mit Ingo ausfüllen**
2. Wählen Sie im Dialog „Quelldatei(en) auswählen" ein oder mehrere Dokumente der Akte
3. Ingo extrahiert die Falldaten aus den Dokumenten
4. Die erkannten Informationen werden in das Falldatenblatt übernommen

!!! info "Verfügbarkeit"
    Die KI-basierte Befüllung wird nur von einem Teil der Falldatenblätter unterstützt (siehe Spalte „mit Ingo ausfüllen" in der [Übersicht](#verfugbare-falldatenblatter)). Weitere folgen. Der Button ist nur aktiv, wenn das Falldatenblatt die Befüllung unterstützt und ein Prompt der Funktion **extract** mit Unterstützung für eigene Prompts konfiguriert ist.

## Ingo-Chat zu Falldaten {#falldaten-ingo-chat}

Über den Button **Ingo Chat** im Falldatenblatt lässt sich direkt ein Chat mit Assistent Ingo starten, der die Falldaten bereits kennt. Ein Klick öffnet eine Auswahl der verfügbaren Chat-Prompts.

Ingo erhält automatisch folgenden Kontext:

- ID und Aktenzeichen der Akte, sodass Ingo über seine [Werkzeuge](../ki-assistent/agenten.md#werkzeuge) weitere Informationen zur Akte abrufen kann (bspw. Beteiligte, Dokumente, Termine)
- Name und ggf. Beschreibung des Falldatenblatts
- alle aktuellen Werte des Falldatenblatts samt Feldbeschriftung, in derselben Darstellung wie beim Speichern der Falldaten als Dokument

!!! tip "Ungespeicherte Eingaben"
    Der Kontext wird beim Öffnen des Chats erzeugt. Auch noch nicht gespeicherte Eingaben im Falldatenblatt werden daher an Ingo übergeben.

Typische Anwendungsfälle:

- Plausibilitätsprüfung: „Sind die Angaben zum Unfallhergang vollständig und widerspruchsfrei?"
- Fristen und nächste Schritte aus den erfassten Daten ableiten
- Entwurf eines Schreibens auf Basis der Falldaten

!!! note "Voraussetzungen"
    Angeboten werden nur Prompts der Funktion **chat**, deren Modell agentenfähig ist (siehe [Agentische KI](../ki-assistent/agenten.md)). Ist kein solcher Prompt konfiguriert, ist der Button deaktiviert. Damit Ingo auf die Akte zugreifen kann, ist zudem die Berechtigung **KI-Agentenfunktionen** erforderlich.

## Mehrere Falldatenblätter

Eine Akte kann mehrere Falldatenblätter enthalten. Dies ist sinnvoll bei:

- Kombinierten Rechtsgebieten
- Mehreren Beteiligten mit jeweils eigenen Daten
- Verschiedenen Verfahrensabschnitten

## Falldatenblatt entfernen

Per Rechtsklick auf den Reiter des Falldatenblatts → **Entfernen** kann ein Falldatenblatt aus der Akte entfernt werden.

!!! warning "Datenverlust"
    Beim Entfernen eines Falldatenblatts gehen alle eingegebenen Daten verloren.

## Platzhalter in Dokumentvorlagen

Die in Falldatenblättern erfassten Daten können in Dokumentvorlagen als Platzhalter verwendet werden. Die Platzhalternamen sind im jeweiligen Falldatenblatt dokumentiert ("?"-Symbol oben rechts im Falldatenblatt) und können direkt als Übersicht angezeigt, gefiltert und mit einem Klick in die Zwischenablage übernommen werden.

## Updates für Falldatenblätter

Falldatenblätter werden unabhängig von j-lawyer.org Releases aktualisiert:

1. Öffnen Sie **Einstellungen** → **Akten** → **Falldatenblätter**
2. Prüfen Sie auf verfügbare Updates
3. Installieren Sie die gewünschten Updates

Alle Updates können auch mit einem Klick installiert werden.
