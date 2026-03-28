# Agentische KI {#agenten}

Ein KI-Agent ist ein KI-Modell, das nicht nur Text generiert, sondern selbstständig Aktionen in j-lawyer.org ausführen kann. Der Agent plant Schritte, ruft passende Werkzeuge (Tools) auf, verarbeitet deren Ergebnisse und fährt iterativ fort, bis die Aufgabe erledigt ist. So kann ein Agent bspw. aus einer E-Mail heraus eine komplette Akte anlegen – inklusive Kontakten, Beteiligten, Wiedervorlage und Aktennotiz.

Um einen Agenten zu nutzen, muss in den [eigenen Prompts](eigene-prompts.md) ein agentenfähiges Modell ausgewählt werden (erkennbar am Hinweis „agentenfähig" im Prompt-Dialog). Agenten stehen ausschließlich für die Funktion **chat** zur Verfügung.

## Genehmigungsstufen {#genehmigung}

Jedes Werkzeug hat eine Risikostufe, die bestimmt, ob vor der Ausführung eine Genehmigung erforderlich ist:

| Risikostufe | Beschreibung | Genehmigung |
|-------------|-------------|-------------|
| **Niedrig** | Leseoperationen (Suchen, Auflisten, Abrufen) | Automatisch |
| **Mittel** | Schreiboperationen (Anlegen, Ändern) | Genehmigung erforderlich |
| **Hoch** | Löschoperationen | Genehmigung erforderlich |

Wird eine Genehmigung angefordert, stehen folgende Optionen zur Verfügung:

- **Einmalig erlauben**: Nur dieser einzelne Aufruf wird genehmigt
- **Für diese Sitzung erlauben**: Alle weiteren Aufrufe dieses Werkzeugs in der aktuellen Sitzung werden automatisch genehmigt
- **Dauerhaft erlauben**: Alle zukünftigen Aufrufe dieses Werkzeugs werden automatisch genehmigt
- **Ablehnen**: Der Aufruf wird nicht ausgeführt; der Agent erhält eine Ablehnungsmeldung und kann alternativ vorgehen

## Verfügbare Werkzeuge {#werkzeuge}

Dem Agenten stehen die folgenden Werkzeuge zur Verfügung, gruppiert nach Funktionsbereich.

!!! tip "Tipp"
    Im Chat kann Assistent Ingo jederzeit gefragt werden: „Welche Tools oder Funktionen kannst du nutzen?" – er listet dann seine verfügbaren Werkzeuge auf.

### Akten {#tools-akten}

| Werkzeug | Beschreibung | Risiko |
|----------|-------------|--------|
| `search_cases` | Sucht Akten anhand eines Suchbegriffs | Niedrig |
| `get_case` | Ruft Aktendetails inkl. Beteiligten und Notizen ab | Niedrig |
| `get_case_by_id` | Ruft Aktendetails anhand der internen ID ab | Niedrig |
| `create_case` | Legt eine neue Akte an (Aktenzeichen wird automatisch vergeben) | Mittel |
| `update_case` | Ändert Aktendetails (Name, Grund, Sachgebiet, Anwalt, Sachbearbeiter, Notiz) | Mittel |
| `get_history_for_case` | Ruft die Änderungshistorie einer Akte ab | Niedrig |
| `get_parties_for_case` | Ruft alle Beteiligten einer Akte mit vollständigen Kontaktdaten ab | Niedrig |

### Dokumente {#tools-dokumente}

| Werkzeug | Beschreibung | Risiko |
|----------|-------------|--------|
| `list_case_documents` | Listet Dokumente einer Akte auf (paginiert, 20 pro Seite) | Niedrig |
| `list_case_documents_by_date` | Listet Dokumente innerhalb eines Zeitraums auf | Niedrig |
| `search_case_documents` | Durchsucht Dokumente nach Dateiname | Niedrig |
| `get_document_text` | Extrahiert den Textinhalt eines PDF- oder Textdokuments | Niedrig |
| `get_document_content` | Ruft den Dokumentinhalt als Base64-kodierten String ab | Niedrig |
| `rename_document` | Benennt ein Dokument um | Mittel |
| `delete_document` | Löscht ein Dokument in den Papierkorb (wiederherstellbar) | Hoch |

### Ordner und Vorlagen {#tools-ordner}

| Werkzeug | Beschreibung | Risiko |
|----------|-------------|--------|
| `list_case_folders` | Ruft die Ordnerstruktur einer Akte ab | Niedrig |
| `create_case_folder` | Erstellt einen Ordner in einer Akte | Mittel |
| `apply_folder_template` | Wendet eine Ordnervorlage auf eine Akte an | Mittel |
| `list_folder_templates` | Listet verfügbare Ordnervorlagen auf | Niedrig |
| `search_templates` | Durchsucht Dokumentvorlagen nach Name | Niedrig |
| `create_document_from_template` | Erstellt ein Dokument aus einer Vorlage mit automatischer Platzhalterersetzung | Mittel |
| `move_document_to_folder` | Verschiebt ein Dokument in einen Ordner innerhalb derselben Akte | Mittel |

### Kontakte {#tools-kontakte}

| Werkzeug | Beschreibung | Risiko |
|----------|-------------|--------|
| `search_contacts` | Sucht Kontakte/Adressen anhand eines Suchbegriffs | Niedrig |
| `create_contact` | Legt einen neuen Kontakt an | Mittel |
| `create_or_get_contact` | Legt einen Kontakt an oder gibt einen ähnlichen bestehenden zurück (Ähnlichkeitsprüfung) | Mittel |
| `update_contact` | Ändert einen bestehenden Kontakt (nur angegebene Felder werden geändert) | Mittel |
| `add_party_to_case` | Fügt einen Kontakt als Beteiligten zu einer Akte hinzu | Mittel |

### Kalender {#tools-kalender}

| Werkzeug | Beschreibung | Risiko |
|----------|-------------|--------|
| `list_calendars` | Listet alle verfügbaren Kalender auf | Niedrig |
| `list_event_types` | Gibt die verfügbaren Eintragstypen zurück (Wiedervorlage, Frist, Termin) | Niedrig |
| `get_events_for_case` | Ruft alle Kalendereinträge einer Akte ab | Niedrig |
| `get_all_open_events` | Ruft alle offenen Kalendereinträge ab (optional nach Typ filterbar) | Niedrig |
| `get_all_open_events_between_dates` | Ruft offene Kalendereinträge in einem Zeitraum ab | Niedrig |
| `find_free_slots` | Findet freie Zeitfenster im Kalender | Niedrig |
| `create_event` | Erstellt einen Kalendereintrag (Wiedervorlage, Frist oder Termin) | Mittel |
| `update_event` | Ändert einen bestehenden Kalendereintrag | Mittel |

### Rechnungen {#tools-rechnungen}

| Werkzeug | Beschreibung | Risiko |
|----------|-------------|--------|
| `list_invoice_pools` | Listet verfügbare Rechnungsnummernkreise auf | Niedrig |
| `get_all_open_invoices` | Ruft alle offenen Rechnungen ab (paginiert, 20 pro Seite) | Niedrig |
| `search_invoices` | Durchsucht Rechnungen nach Rechnungsnummer, Name oder Firma | Niedrig |
| `search_invoices_by_date` | Sucht Rechnungen in einem Zeitraum | Niedrig |
| `create_invoice` | Erstellt eine neue Rechnung in einer Akte | Mittel |
| `create_invoice_position` | Fügt eine Position zu einer Rechnung hinzu | Mittel |

### Zeiterfassung {#tools-zeiterfassung}

| Werkzeug | Beschreibung | Risiko |
|----------|-------------|--------|
| `get_all_open_timesheets` | Listet alle offenen Zeiterfassungsprojekte auf | Niedrig |
| `get_open_timesheets_for_case` | Ruft offene Zeiterfassungsprojekte einer Akte ab | Niedrig |
| `get_timesheet_positions` | Ruft alle Zeiteinträge eines Projekts ab | Niedrig |
| `create_timesheet_position` | Erstellt einen neuen Zeiteintrag | Mittel |

### Etiketten {#tools-etiketten}

| Werkzeug | Beschreibung | Risiko |
|----------|-------------|--------|
| `list_document_tags` | Listet alle verfügbaren Dokumentetiketten auf | Niedrig |
| `list_case_tags` | Listet alle verfügbaren Aktenetiketten auf | Niedrig |
| `set_document_tag` | Setzt oder entfernt ein Etikett an einem Dokument | Mittel |
| `set_case_tag` | Setzt oder entfernt ein Etikett an einer Akte | Mittel |

### Notizen und Nachrichten {#tools-notizen}

| Werkzeug | Beschreibung | Risiko |
|----------|-------------|--------|
| `create_note` | Erstellt eine Aktennotiz als HTML-Dokument | Mittel |
| `create_instant_message` | Erstellt eine Sofortnachricht mit Aktenbezug | Mittel |

### Webzugriff {#tools-web}

| Werkzeug | Beschreibung | Risiko |
|----------|-------------|--------|
| `web_search` | Führt eine Websuche durch und gibt Titel, URL und Auszug zurück | Niedrig |
| `fetch_url` | Lädt den Textinhalt einer Webseite | Niedrig |

### System {#tools-system}

| Werkzeug | Beschreibung | Risiko |
|----------|-------------|--------|
| `get_current_date_time` | Gibt das aktuelle Datum und die Uhrzeit zurück | Niedrig |
| `list_users` | Listet alle Systembenutzer auf (Name, Anzeigename, E-Mail) | Niedrig |
| `get_my_groups` | Gibt die Gruppen des angemeldeten Nutzers zurück | Niedrig |

## Beispiel-Prompts {#beispiele}

Die folgenden Beispiele zeigen, wie agentische Prompts für typische Kanzleiaufgaben formuliert werden können. Um sie zu nutzen, legen Sie einen [eigenen Prompt](eigene-prompts.md) mit der Funktion **chat** und einem agentenfähigen Modell an.

### Akte aus einer E-Mail aufsetzen

Dieser Prompt erstellt aus dem Inhalt einer E-Mail eine vollständige neue Akte:

> Analysiere den folgenden Text einer E-Mail. Führe dann folgende Schritte aus:
>
> 1. Erstelle für jede im Text genannte Person oder Organisation einen Kontakt (nutze create_or_get_contact, um Duplikate zu vermeiden).
> 2. Lege eine neue Akte an. Verwende als Aktenname eine kurze Bezeichnung des Sachverhalts (z.B. „Müller ./. Schmidt") und als Grund eine knappe Zusammenfassung.
> 3. Füge die erstellten Kontakte als Beteiligte zur Akte hinzu. Der Mandant erhält den Beteiligtentyp „Mandant", die Gegenseite „Gegner". Ermittle die Rollen aus dem Kontext der E-Mail.
> 4. Ermittle das aktuelle Datum und erstelle eine Wiedervorlage in 7 Tagen mit dem Grund „Erstberatung vorbereiten".
> 5. Erstelle eine Aktennotiz mit einer strukturierten Zusammenfassung des Sachverhalts.
>
> Hier der Text der E-Mail:

### Fristenkontrolle für die nächste Woche

Dieser Prompt erstellt eine Übersicht aller anstehenden Fristen und Wiedervorlagen:

> Ermittle das heutige Datum. Suche dann alle offenen Fristen und Wiedervorlagen der nächsten 7 Tage. Erstelle eine übersichtliche Zusammenfassung, gruppiert nach Tag, mit folgenden Angaben:
>
> - Datum und Uhrzeit
> - Aktenzeichen und Aktenname
> - Art (Frist/Wiedervorlage/Termin)
> - Zusammenfassung
> - Verantwortliche Person
>
> Hebe überfällige Einträge besonders hervor.

### Mandatsabschluss vorbereiten

Dieser Prompt prüft, ob eine Akte abschlussreif ist:

> Prüfe für die Akte {{AKTE_ZEICHEN}} folgende Punkte und erstelle einen Statusbericht:
>
> 1. Gibt es offene Kalendereinträge (Fristen, Wiedervorlagen, Termine)? Liste sie auf.
> 2. Gibt es offene Zeiterfassungsprojekte? Wenn ja, liste die nicht abgerechneten Zeiten auf.
> 3. Gibt es offene Rechnungen? Liste deren Status und Beträge auf.
> 4. Erstelle abschließend eine Empfehlung, ob die Akte archiviert werden kann oder welche Schritte noch ausstehen.

### Recherche mit Aktenbezug

Dieser Prompt recherchiert im Web und speichert die Ergebnisse in der Akte:

> Recherchiere per Websuche aktuelle Rechtsprechung zum Thema „{{AKTE_GRUND}}". Gehe dabei wie folgt vor:
>
> 1. Führe 2-3 Websuchen mit unterschiedlichen Suchbegriffen durch.
> 2. Lade die vielversprechendsten Ergebnisse und extrahiere die relevanten Informationen.
> 3. Erstelle in der Akte {{AKTE_ZEICHEN}} eine Aktennotiz mit einer strukturierten Zusammenfassung der Rechercheergebnisse, inklusive Quellenangaben (URLs).
