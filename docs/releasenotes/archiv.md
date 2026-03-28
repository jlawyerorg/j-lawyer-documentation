# Archiv

## j-lawyer.org 3.2

Desktop:

- n/a

Adressen:

- n/a

Akten:

- Ladezeiten für Akten optimiert, insbesondere hinsichtlich der Falldaten
- Löschen von Akten listet diese nun zwecks Kontrolle auf
- Aktensuche: Sachgebiet als Spalte aufgenommen

Dokumente:

- Dokumente können nun vollautomatisch etikettiert werden, bspw. der Dokumentname einen bestimmten Wert enthält
- PDF-Dokumente können nun mit einem Stempel versehen werden
- ein in der Akte vorliegendes Sprachmemo kann nun fortgeführt werden
- Unter macOS wird nun nur noch eine Microsoft-Word-Instanz geöffnet, nicht mehr eine Instanz pro Dokument.
- Fehlerkorrektur: bei Umbenennen und Bestätigung mit Enter wurde das Dokument im Anschluss geöffnet (Windows)

Finanzen:

- Import von Buchungen mittels Kontoauszug-Import
- Erstellen von Gutschriften zu einem Beleg
- Fehlerkorrektur: Rechnungstabelle wurde bei Nutzung von Microsoft Word-basierten Vorlagen immer mit Tabellenlinien dargestellt
- Fehlerkorrektur bzgl. Sortierung von Rechnungspositionen
- Fehlerkorrektur: es trat ein Fehler auf, wenn in den Tabelleneinstellungen “leere Zeilen einblenden” inaktiv war
- Fehlerkorrektur: Kontoinhaber darf im Girocode keine Umlaute enthalten

Zeiterfassung:

- Erfassen von Zeiten für andere Accounts erleichtert
- Direktes Erfassen absoluter Zeiten: bisher war ein Umrechnen in Minuten notwendig, nun wird ein Format wie “45m” oder “2h30m” unterstützt.

Assistent Ingo:

- Ergebnisse werden nun formatiert ausgegeben
- Unterstützung für Bilderkennung / Bildanalyse
- Transkription/Diktieren: automatische Erkennung der Sprache
- Transkription/Diktieren: Unterstützung für Bluetooth-Headsets
- Transkription/Diktieren: es können eigene Ersetzungen konfiguriert werden
- Chat: Nutzerführung verbessert. Bisher musste der eingehende Text dediziert in den Prompt übernommen werden – dies geschieht nun automatisch. Einschränkung durch Markieren möglich.
- Die Extraktion von Kontaktdaten bei Adressen-Neuanlage nutzt nun eine definierte Sortierung der Attribute.
- KI-basierte Extraktion der Adressdaten auch bei Schnellerfassung einer Adresse.

Auswertungen:

- Einige Auswertungen haben eine explizite Summenzeile erhalten. Aktuell führt dies zu unerwünschten Effekten beim Sortieren – eine Korrektur ist eingeplant.
- Neue Auswertung für Rechnungen im Entwurfsstatus
- Neue Auswertung für selbst gebuchte Zeiten
- Offene Zeiterfassungsprojekte: zusätzliche Tabellen (gebucht, abrechenbar, abgerechnet)

Kalender:

- Kalendereinträge können nun im Rahmen der Veraktung von Dokumenten / Scans / E-Mails / beA-Nachrichten erstellt werden.
- Rückfrage beim Löschen von Kalendereinträgen
- Im grafischen Kalenderblatt kann auf bestimmte Verantwortliche gefiltert werden

E-Mail:

- E-Mails können nun als Entwurf gespeichert und aus dem Entwürfe-Ordner versendet werden
- Anhänge können nun aus einer E-Mail gelöscht werden
- Spaltenreihenfolge im E-Mail-Posteingang angepasst
- Suchfunktion für E-Mail-Vorlagen bei Versand hinzugefügt
- Microsoft Exchange: Unterstützung für “shared mailboxes” (gemeinsam genutzte Postfächer)
- Rechtschreibprüfung für reine Text-E-Mails (noch nicht für HTML-formatierte E-Mails)
- Anhang aus Akte hinzufügen: Möglichkeit der Suche nach Dateinamen
- Automatische Veraktung: gab es zwei Nachrichten mit identischem Betreff am selben Tag, gab es einen Namenskonflikt wenn das Dateinamenschema keine Zeitangabe enthält. In dem Fall wird nun ein Index am Dokumentnamen angebracht, damit die Mail trotzdem veraktet wird.
- verschiedene Fehler bzgl. der Formatierung von HTML-E-Mails behoben
- Fehlerkorrektur Office 365: Übernehmen geänderter Postfacheinstellungen konnte zum Entkoppeln des Postfachs führen

beA:

- XJustiz-Standard in Version 3.5.1 implementiert (Strukturdatensätze)
- Automatische Übernahme des Empfänger-Aktenzeichens, wenn der Versand über die Dokumentenliste initiiert wird.

Drebis:

- Drebis-Funktionalität entfernt, da der Betreiber den Dienst einstellt.

E-POST:

- n/a

Nachrichten / Instant Messaging:

- Nachrichten, in denen alle Accounts erwähnt werden sollen, können mittels “@alle …” gesendet werden.
- Nachrichten anderer Accounts einsehen: Unterstützung für Mehrfachauswahl bzgl. der Accounts

Telefonie:

- n/a

Scans:

- n/a

Nextcloud:

- n/a

REST-API:

- Endpunkt zum Löschen von Kontakten hinzugefügt
- Endpunkt zum Auflisten aller nicht abgelegten Akten hinzugefügt

Webhooks:

- n/a

Sonstiges:

- Datensicherungen in verteilten Umgebungen: die automatischen Datensicherungen können auch dann genutzt werden, wenn bspw. Serveranwendung und Datenbank auf verschiedenen Hosts laufen.
- Datensicherungen in verteilten Umgebungen: Backupmanager zur Rücksicherung wurde erweitert, um in verteilten Umgebungen rücksichern zu können.
- Verzeichnis mit den Einstellungen des Arbeitsplatzes nun nicht mehr versteckt, um Kompatibilität mit neueren Mac-Versionen und Linux-Installationen mit Snap zu verbessern.
- Logindialog überarbeitet
- Client-Installer macOS: Berechtigungen hinzugefügt
- “Funktion” am Nutzer ist nun mehrzeilig

---

## j-lawyer.org 3.1

Desktop:

- Tooltip von Akten- und Dokumentetiketten zeigt deren  Aktivierungsdatum
- Sortierung etikettierter Akten nach Änderungsdatum absteigend

Adressen:

- n/a

Akten:

- Aktensuche durchsucht auch Anwalt/Anwältin und Sachbearbieter/Sachbearbeiterin
- Tooltip von Aktenetiketten zeigt der Aktivierungsdatum
- optionales Kopieren von Falldaten bei Duplizieren einer Akte

Dokumente:

- Tooltip von Dokumentetiketten zeigt der Aktivierungsdatum
- Anonymisieren / Schwärzen von PDF-Dateien
- Auswertung von EXIF-Daten für JPG- und PNG-Dateien für korrekte Ausrichtung im Viewer und beim PDF-Export
- Unscharfe PDF-Darstellung auf HiDPI-Displays beseitigt
- mögliche Endlosschleife bei Konfiguration eines Dateinamenschemas
- exakt ein Standard-Dateinamensschema erzwingen
- Bessere Formulierung beim Splitten von PDFs
- PDF-Export: Seitenzahlen und Inhaltsverzeichnis optional
- PDF-Export: einzelne Dokumente können im Exportassistenten noch entfernt werden
- Installer-Fehler: fehlende Bibliothek für Darstellung von Markdown-Dokumenten
- Konvertierung einer E-Mail in PDF konnte unter bestimmten Bedingungen fehlschlagen
- Layout des Dialoges zur Dokumenterstellung aus Vorlage für kleinere Displays optimiert

Finanzen:

- Datumsangaben und Geldbeträge in Belegdokumenten werden je nach Spracheinstellungen automatisch formatiert
- “bezahlt”-Markierung eines Belegs generierte eine Zahlung mit Betrag 0 EUR, wenn bei der Aktenkontobuchung auch Fremdgelder angegeben wurden
- Rundungsfehler Fremdgeld beseitigt

Zeiterfassung:

- neuer Tabellenplatzhalter {{ZE_SUMMEN}} erstellt eine Tabelle mit den aufsummierten Zeiten und deren Gesamtwerten pro mitarbeitende Person
- Tabelle mit Leistungsnachweis neu strukturiert, Spalten: Person, Datum, Dauer, Stundensatz, Total, Beschreibung; die Angabe “Projekt” entfällt.
- Datumsangaben und Geldbeträge werden je nach Spracheinstellungen automatisch formatiert
- offener Betrag wird für limitierte Projekte angezeigt
- Positionen werden erst gesperrt, wenn sie einem Beleg zugeordnet sind, der Beleg im Status offen, 1. / 2. / 3. Mahnstufe oder bezahlt ist; Positionen, die einem Beleg im Entwurfsstatus oder einem stornierten Beleg zugeordnet sind, bleiben vollständig bearbeitbar, auch inklusive deren Zuordnung zu einem anderen Beleg.
- Name und Beschreibung erfasster Zeiten bleiben stets bearbeitbar
- Beleg ermöglicht das Erstellen eines Leistungsnachweises, unabhängig vom Belegdokument
- Werden Zeiten verändert, die bereits einem Beleg zugeordnet sind, wird ein Hinweis ausgegeben, dass die Zeiten erneut in den Beleg zu importieren sind.
- alles / nichts auswählen im Dialog hinzugefügt, über den die Zeiten in einen Beleg importiert werden
- Rundungsfehler beseitigt

Assistent Ingo:

- Folgeaktionen für Zusammenfassungen und Chats auf Dokumente: Ergebnis in Notiz übernehmen
- Transkript bei Diktieren einer E-Mail erschien unterhalb der Signatur
- “Übernehmen” und “Kopieren”-Aktionen übernehmen nur einen selektierten Text (wenn Selektion vorhanden), ansonsten den gesamten Text.
- Chat-Funktion wiederholte Antworten, die bereits gegeben wurden.

Auswertungen:

- “Akten pro Monat”: zusätzliche Aufschlüsselung nach Sachgebiet
- Fehler(meldung) bei Export einer Tabelle nach Excel beseitigt
- “Alle Belege”: zusätzliche Tabellen mit kumulierten Werten
- neue Auswertung “Gebuchte Zeiten pro Mitarbeiter”

Kalender:

- Kalender-Eintragspaare: zweiter Eintrag übernimmt die Beschreibung des ersten als Vorschlag
- Fehler in Konfliktprüfung behoben, der unter bestimmten Umständen auftreten konnte

E-Mail:

- Akte aus E-Mail erzeugen: Assistent schlug fehl, wenn das Aktenzeichenschema die Angabe einer Gruppe benötigt
- Möglichkeit des Aus- und Einblendens von Ordnern per Kontextmenü im Postfach. Das Ausblenden sollte bei großen Ordnerstrukturen in einem Postfach auch bzgl. der Abrufgeschwindigkeit helfen.
- Integration von Office 365-Postfächern überarbeitet, inklusive Unterstützung von Office 365-Postfächern mit aktivierter 2-Faktor-Authentifizierung. Auch bereits angebundene Postfächer müssen über “Einstellungen” – “E-Mail-Postfächer” neu gekoppelt werden (neuer Button im Einstellungsdialog).
- Abrufgeschwindigkeit bei Ordnerwechsel optimiert.

beA:

- erneutes Login im beA schlug fehl

Drebis:

- Speichern zurücklaufender Dokumente zur Akte schlug fehl
- Hausnummer der Beteiligten wurde nicht in die Assistentendialoge übernommen.

E-POST:

- n/a

Nachrichten / Instant Messaging:

- n/a

Telefonie:

- n/a

Scans:

- n/a

Nextcloud:

- n/a

REST-API:

- n/a

Webhooks:

- n/a

Sonstiges:

- Client-Autoupdate auf Windows: Installerverzeichnis wurde nicht automatisch geöffnet
- bessere automatische Schriftgrößenskalierung auf HiDPI-Displays unter Windows
- Systemreport war nicht per “x” zu schließen
- Layout der Nutzerverwaltung für kleinere Displays optimiert

---

## j-lawyer.org 3.0

Desktop:

- Nach Aktualisierung der Etikettenansicht bleibt die Tab-Auswahl erhalten
- Anzeige für verfügbare Updates von Falldatenblättern direkt auf dem Desktop

Adressen:

- Bei Neueintrag eines Kontakts wird eine Ähnlichkeitssuche durchgeführt und ggf. gewarnt
- Eingabemöglichkeiten für SEPA-Mandatsreferenz und dazugehörigem Datum
- Tab “Übersicht” aktualisierte nicht immer
- Adressenanlage-Assistent: Fehler bei Handhabung von Mobilfunknummern

Akten:

- Änderungen an Beteiligten werden in der Aktenhistorie dokumentiert
- Beteiligte: Anzeige der Adresse auf Karte (Google Maps / OpenStreetMap)
- Beteiligte: Anzeige der Route (Google Maps / OpenStreetMap)
- Aktenzeichenschema: laufende Nummer lässt sich um beliebige Menge erhöhen (bspw. wenn 2er- oder 3er-Sprünge gewünscht sind)
- HTML-Export bildet Ordnerstruktur der Akte ab

Dokumente:

- Ausgewählte Dokumente (also ggf. auch die gesamte Akte) als PDF exportieren
- Per Drag & Drop lassen sich nun ganze Ordnerstrukturen in die Akte übernehmen
- Überarbeiteter PDF-Viewer: Drehen einzelner oder aller Seiten, verbessertes Scrollverhalten, Löschen einzelner Seiten
- Möglichkeit, PDFs zu komprimieren
- Es können verschiedene Namenskonventionen für Dateinamen erstellt werden. Dabei werden alle Platzhalter analog des Vorlagensystems unterstützt, auch solche aus Falldatenblättern.
- Datei umbenennen: aktuellen Namen vollständig vorselektieren
- Führende und abschließende Leerzeichen bei Platzhaltern in Vorlagennamen werden entfernt
- Skriptplatzhalter: Ist das Ergebnis eines Skriptes leer, so können u.U. Leerzeilen entstehen. Diese werden nun automatisch entfernt.
- PDF-Konvertierung auf macOS überarbeitet
- Anzeige von Zeitstempeln in Dokumentliste: Änderungsdatum, wenn nach Änderungsdatum sortiert wird, Erstellungsdatum, wenn nach Erstellungsdatum sortiert wird
- Öffnen einer Notiz änderte deren Änderungsdatum, auch wenn keine Änderungen getätigt wurden
- Änderung der Farbmarkierung oder des Favoritenstatus aktualisiert nicht mehr das Änderungsdatum eines Dokuments
- Mikrofonansteuerung unter macOS nun funktionsfähig (bspw. für Sprachmemo-Funktion)
- Editor für / Anzeige von Markdown-Dokumenten
- Unterstützung für PDF-Vorlagen: PDF-Dokumente, die Formulare enthalten, können als Vorlage verwendet werden
- Splitten von PDFs innerhalb der Akte

Finanzen:

- Sicherheitsabfrage beim Löschen aller Belegpositionen
- Aktenkonto-Buchungen: verbesserte Tastatursteuerung
- Elektronische Rechnungen: es können elektronische Rechnungen erstellt und eingelesen werden
    - Unterstütztung für ZUGFeRD und XRechnung
    - Angabe der Zahlungsmethode im Beleg
    - Angabe des Rechnungsabsenders im Beleg (bspw. um verschiedene Konten in die Rechnung aufnehmen zu können)
- Die Größe der generierten Girocodes kann über das Menü „Einstellungen“ – „Finanzen“ – „Girocodes“ konfiguriert werden.

Zeiterfassung:

- Auswählbare Stundensätze lassen sich nun pro Projekt definieren
- verschiedene Oberflächenverbesserungen
- Nutzer einer Buchung ist editierbar, um Buchungen für andere Nutzer zu ermöglichen
- Leerer Projektname führte zu Fehler in Auswertungen
- Warnen bei Erreichen des Projektlimits, prozentuale Anzeige im Zeit buchen-Dialog, Darstellung in Projektübersicht einer Akte
- Im Leistungsnachweis (Platzhalter “ZE_TABELLE”) wird der Anzeigename des Nutzers ausgegeben, nicht mehr der Nutzername.

Assistent Ingo:

- (todo)

Auswertungen:

- “Akten pro Monat”: zusätzliches Tabellenblatt mit Akten pro Monat und Anwalt/Anwältin

Kalender:

- Kalendereinträge können im graphischen Kalenderblatt auf erledigt gesetzt werden (Kontextmenü)
- Kalendereinträge können so konfiguriert werden, dass ein zweiter Eintrag automatisch aufgenommen wird (bspw. bei Erstellen einer Frist automatisch eine Vorfrist eintragen)
- Monatsansicht: Unterstützung für Scrollen hinzugefügt
- Anzeige von Akten mit fehlender WV/Frist: zwei weitere Tabs (Akten ohne WV, Akten ohne Frist)

E-Mail:

- Kopfdaten (An, Betreff, …) können per Klick in die Zwischenablage übernommen werden
- Die Sicherheitswarnungen bei Anzeige HTML-formatierter Mails unbekannter Absender kann dauerhaft abgeschaltet werden (Einstellung im Nutzerprofil)
- Bei Beantworten von E-Mails: Signatur unter der Antwort, aber oberhalb der zitierten Nachricht
- "Beteiligte aus Signatur erstellen" funktioniert nicht, wenn Absender gerade erst als vertrauenswürdig eingestuft wurde
- Kopiermöglichkeit für E-Mail-Vorlagen
- Darstellung reiner Text-Mails aus Outlook korrigiert (.msg-Dateien)
- Nutzername und Passwort sind keine Pflichtangabe für E-Mail-Versand
- E-Mails lassen sich samt Ihrer Anlagen in PDF konvertieren
- Automatische Veraktung von E-Mails: “kleine” eingebettete Grafiken können automatisch ignoriert werden (bspw. werden dann Logos in Signaturen nicht mehr als separate Datei in die Akte übernommen)
- Beteiligte waren nicht auswählbar, wenn E-Mail aus der Akte heraus beantwortet wurde
- Postfach-Konfiguration: Nutzername und Passwort für Postausgang dürfen leer sein (bspw. wenn Mailserver kein Authentifizierung erwartet, weil die IP des sendenden Clients geprüft wird)
- in j-lawyer.org vorbereitete E-Mail über Thunderbird versenden
- Rückgängig-Aktion im E-Mailversanddialog (Strg+Z bzw. Cmd+Z)

beA:

- Upgrade auf Version 9 der Schnittstelle der BRAK
- Logout / erneuten Login nach Timeout möglich

Drebis:

- n/a

E-POST:

- Statusaktualisierung konnte zum Erliegen kommen, wenn ein unbehandelter Fehler auftrat

Nachrichten / Instant Messaging:

- Bessere Handhabung bei großen Nachrichtenmengen. Nachrichten mit offenen Erwähnungen werden immer dargestellt.
- Nachrichten anderer können als gelesen markiert werden (nur möglich für Administratoren)
- Bei Aktenablage wird auf offene / unerledigte Nachrichten geprüft und es gibt die Option, diese Nachrichten auf erledigt zu setzen.

Telefonie:

- n/a

Scans:

- n/a

Nextcloud:

- Geburtsdaten von Kontakten können aus der Synchronisation ausgeschlossen werden (bspw. weil die Informationen auf mobilen Geräten zu einer hohen Anzahl an Geburtstagsbenachrichtigungen führen)
- Auflisten von Kalendern schlug fehl, wenn gerade eine Synchronisation lief

REST-API:

- Neuer Endpunkt für Ähnlichkeitssuche in Adressen – bspw. wenn ein Client die doppelte Erfassung eines Kontakts vermeiden möchte
- Neuer Endpunkt zum Auflisten aller Gruppen
- Neuer Endpunkt zum Auflisten aller für eine Akte berechtigten Gruppen
- Neuer Endpunkt zum Ändern der für eine Akte berechtigten Gruppen
- Neuer Endpunkt zum Lesen aller aktenbezogenen Dokumente im Papierkorb
- Neuer Endpunkt zum Suchen von Adressen anhand eines Etiketts
- Neuer Endpunkt zum Suchen von Akten anhand eines Etiketts
- Neuer Endpunkt zum Suchen von Dokumenten anhand eines Etiketts
- Neuer Endpunkt zum Auflisten von E-Mail-Vorlagen
- Neuer Endpunkt zum Ausfüllen einer E-Mail-Vorlage

Webhooks:

- n/a

Sonstiges:

- Die meisten Informationen, die an einer Adresse gepflegt werden können, sind nun auch in der Nutzerverwaltung am Nutzer verfügbar. Die Informationen stehen auch per Platzhalter zur Verfügung. So ist es bspw. möglich, die Stellenbeschreibung / Position eines Autors eines Dokuments automatisch zu übernehmen.
- Zusätzliche Avatare hinzugefügt
- Zusätzliche Hintergrundbilder hinzugefügt
- Verschiedene Oberflächenverbesserungen
- Wichtige Einstellungen einer Installation können exportiert und importiert werden

---

## j-lawyer.org 2.6.1

Desktop:

- Ansicht "Nach Etikett" zeigt bei aktivierter Option “nur meine anzeigen” auch solche Akten, die weder “Anwalt” noch “Sachbearbeiter” haben
- Datumsangabe auf Desktop änderte sich nicht mit dem Tageswechsel

Adressen:

- Sortierung der Akten an einem Adressbucheintrag angepasst (alt: Sortierung nach Rolle aufsteigend; neu: Sortierung nach Erstellungsdatum der Akte absteigend)

Akten:

- Optimierung beim Laden von Akten: Historie erst Laden, wenn der Historientab geöffnet wird
- Optimierung beim Laden von Akten: Laden von Beteiligten optimiert / beschleunigt
- Fehlerkorrektur Aktenzeichenschema-Konfiguration: ungültige Konfiguration bei Verwendung zufälliger Buchstaben verhindern
- zuletzt genutzte Sortierung von Dokumenten in der Akte wird gespeichert und wiederhergestellt
- Ungültige Sortiereinstellung (mehrere Sortierbuttons aktiv) korrigiert
- “null”-Wert im Aktenvorblatt korrigiert

Dokumente:

- Optimierung beim Laden von Dokumenten: bis zu 2GB Dokumente werden nun lokal in einem Zwischenspeicher vorgehalten, um bei schmalbandiger Verbindung zum Server Bandbreite zu sparen und Dokumente schneller darstellen zu können
- PDF-Vorschau: per Mausrad oder Scrollbar blättern
- PDF-Vorschau: Zoomfunktion
- PDF-Vorschau: Auflösung erhöht / Darstellungsqualität verbessert
- neuer Dokumenttyp “Sprachmemo”: Aufnahme vom Mikrofon des jeweiligen Arbeitsplatzes, Speichern zur Akte
- Wiedergabe von Sounddateien (WAV) direkt in der Akte
- Anpassungen bzgl. der Verwendung von Tabellenplatzhaltern, um vom Nutzer definierte Spaltenbreiten zu ermöglichen (siehe Dokumentation)
- Volltextsuche: bestimmte Dateiformate werden nicht mehr per OCR aufbereitet
- Tabelleneinstellung “Zahl vor der Summe unterstreichen” funktionierte nicht (in Verbindung mit bestimmten anderen Konfigurationen)

Finanzen:

- neuer Button zum Duplizieren einer Buchung im Aktenkonto (bspw. bei turnusmäßigen Zahlungen)
- neuer Button zum Setzen einer Rechnung auf “bezahlt” – mit automatischer Eintragung des offenen Restbetrages im Aktenkonto
- Eintragungen im Aktenkonto: bei Eingabe von Auslagen sprang der Fokus immer automatisch auf “Speichern”
- bessere Fehlermeldung bei Auftreten eines Rechnungsnummerkonfliktes
- Generieren eines Girocodes für eine Rechnung ohne Positionen führte zu Fehler

Auswertungen:

- n/a

Kalender:

- n/a

E-Mail:

- Automatisches Verakten eingehender E-Mails: über die Konfiguration eines Postfaches können eingehende Nachrichten und Anhänge automatisch Akten zugeordnet werden, sofern eine eindeutige Zuordnung möglich ist.
- Weitere Ursache für “failed to parse”-Fehler beseitigt

beA:

- n/a

Drebis:

- n/a

E-POST:

- Bereitstellung der Sendungsnummer für Einschreiben
- Aus der zentralen E-POST-/Sipgate-Statusübersicht kann direkt zur Akte navigiert werden
- Bei vor / zurück – Navigation wurden Dokumente mehrfach dargestellt / zu PDF konvertiert
- Fehler bei Wechsel des Empfängers korrigiert: es wurde nicht alle Adresszeilen zurückgesetzt / neu gesetzt

Nachrichten / Instant Messaging:

- Menge der Nachrichten im zentralen Nachrichteneingang begrenzt

Telefonie:

- n/a

Scans:

- Lokale Scanordner werden nun spezifisch je nach verbundenem Server gespeichert, d.h. es kann unterschiedliche Scanordner auf einem Arbeitsplatz geben – einen pro Verbindungsprofil.
- Separate Aktion zum Zurücksetzen eines lokalen Scanordners
- Anzahl parallel laufender OCR-Prozesse begrenzt

Nextcloud:

- n/a

REST-API:

- neuer Endpunkt zum Erstellen von Optionen (bspw. Etiketten)
- neuer Endpunkt zum Löschen von Optionen (bspw. Etiketten)
- neuer Endpunkt zum Bearbeiten von Optionen (bspw. Etiketten)
- neuer Endpunkt zum Auflisten von Webhook Logs
- neuer Endpunkt zum Auslesen der Details einer Webhook-Ausführung

Webhooks:

- Log für Webhooks: Die Ausführung von Webhooks wird nun in der Datenbank protokolliert.
- Webhook-Payloads enthalten eine ID.
- Webhook-Logs können per REST API ausgelesen werden

Sonstiges:

- Konfiguration, um Aufnahme von Dokumenten in den Volltext zu deaktivieren (Voreinstellung: aus, d.h. neue Dokumente werden indexiert)
- Datenbankmigration Version 1.12.0.8 schlug für Debian&MariaDB fehl

---

## j-lawyer.org 2.6

Desktop:

- Fällige Kalendereinträge lassen sich nun anhand der verantwortlichen Nutzer filtern.
- Bessere und zeitnahe automatische Aktualisierung
- “Fällig”: Beschreibung in Tooltip aufgenommen

Adressen:

- Umfangreichere Layoutänderungen
- Erstellen von Adressen aus Zwischenablage
- Neues Feld “weitere Vornamen” – bspw. für eine vollständige Erfassung lt. Ausweispapieren. Der Platzhaltername lautet “_VORNAME2”.
- Schnellerfassung für neue Adressen um einige Felder erweitert

Akten:

- Aktensuche: offene Kalendereinträge werden in der Vorschau direkt angezeigt
- App-Synchronisationsstatus wird direkt in der Aktensuche angezeigt
- Der Tab “Handakte” wurde entfernt und ist nun nur noch per Button im Kopfbereich aufzurufen.
- Lücke in der Prüfung auf Interessenkonflikte geschlossen
- Aktenzeichen können direkt über die Oberfläche bearbeitet werden. Die Funktion ist nur für Administratoren verfügbar.

Dokumente:

- Anbindung E-POST-BUSINESS-API (Hybridmail): per Rechtsklick aus der Akte Dokumente versenden, die beim Empfänger als herkömmlicher Brief ankommen – es entfällt das Drucken, Eintüten, Wegbringen
- Dokumente haben nun eine separates Attribut für den Zeitpunkt der letzten Änderung. Die Sortierung in der Akte ist nun voreingestellt auf “nach zuletzt geändert, absteigend”.
- Sortierung nach Dateityp
- Sortierung nach erstellt / geändert
- Tabellenplatzhalter: Leerzeichen vor und nach dem Platzhalter werden automatisch entfernt
- Bei Ablage als PDF wird geprüft ob das Dokument noch geöffnet ist
- Beim Öffnen eines bereits geöffneten Dokumentes gab es unter bestimmten Bedinungen ein fehlerhaftes Fensterverhalten / sich blockierende Dialoge.
- Navigation per Pfeiltasten in der Dokumentenliste verbessert.
- Kleinere Verbesserungen der Nutzbarkeit im Datei-Zuordnen-Dialog
- Dokumentordner: “nur diesen anzeigen”
- Dokumentordner hatten manchmal einen horizontalen Scrollbalken
- Notizen müssen nicht mehr explizit gespeichert werden (geschieht automatisch)
- Bei Dokumenterstellung wird die Anzahl von Platzhaltern ohne Information angezeigt, sowie ein Hinweis dass direkt in der Tabelle bearbeitet werden kann
- Scaneingang: OCR / Texterkennung für PDFs
- Scaneingang: Anzeige von Nutzername und Gerät (Quelle des Scans)
- neuer Platzhalter AUTOR_EMAIL für die Mailadresse des angemeldeten Nutzers

Finanzen:

- Aktenkonto: Dokumentieren von Einnahmen / Ausgaben, Fremdgeld, Auslagen. Geldbewegungen können Beteiligten und / oder Belegen zugeordnet werden. So werden bspw. auch Teilzahlungen erfasst und dann in einem neuen Tab am Beleg angezeigt.
- Offene Rechnungen erhalten den ersten Mahnstufe-Status automatisch bei Fälligkeit.
- Aufnahme eines Girocodes (QR-Codes) in Rechnungen, sodass Empfänger die Rechnung einfach per Scan überweisen können.
- Anzeige Netto- und Bruttobeträge (verschiedene Stellen in der Oberfläche)
- Ausgabe der Höhe des Steuersatzes im Belegdokument – ggf. auch mehrere Angaben, wenn Positionen mit unterschiedlichen Steuersätzen enthalten sind.
- Anzeige gezahlter Beträge am Beleg
- Anzeige offener Beträge am Beleg
- Belegnummern lassen sich per Platzhalter BELNR in den Dateinamen übernehmen.
- Keine Ausgabe von USt-Informationen im Belegdokument, wenn keine USt berechnet wird.
- Konfigurierbares Format für Geldbeträge im Belegdokument (bspw. Tausendertrennzeichen etc.) - über Plugin “Tabelleneinstellungen”.
- Bei Anpassung des Erstellungsdatums wird das Fälligkeitsdatum automatisch neu berechnet.
- Aktenablage prüft nun auf offene Belege und Zeiterfassungsprojekte
- Zeiterfassungsdialog: besseres Scrollverhalten und Darstellung
- Zeiterfassungsdialog: bessere Rückmeldung nach manueller Zeitbuchung / direkter Minuteneingabe
- Fehler in Belegreihenfolge korrigiert

Auswertungen:

- Spalten sortierbar gemacht
- Anzeige von Netto-/Brutto-/Gesamtbeträgen in verschiedenen Auswertungen der Kategorie “Finanzen”
- Zeiterfassung mit Buchungen: es werden nicht nur die gebuchten Minuten, sondern auch der sich daraus ergebende Betrag ausgegeben
- neue Auswertung: Umsatz pro Kunde / Kundin
- neue Auswertung: Akten mit nicht ausgeglichenem Fremdgeld
- neue Auswertung: Ergebnis pro Akte
- neue Auswertung: Aktenkonto-Buchungen

Kalender:

- Bei Erstellung von Kalendereinträgen über das Kalenderblatt wird die verantwortliche Person vorbelegt.
- Auto-Vervollständigung für Kalendereinträge entfernt.
- Zuletzt gewählte Ansicht (Liste vs. Kalenderblatt) wird gespeichert und nach Neustart wiederhergestellt.
- Datumsauswahl-Fenster hebt sich stärker ab vom dahinterliegenden Fenster.

E-Mail:

- Es können mehrere E-Mails mit einem mal veraktet werden.
- Direkt aus dem Posteingang lassen sich nun über einen Assistenten neue Akten erstellen: Aktendaten samt Etikett, neue Adresse, neue Beteiligte etc.
- Neue Benachrichtigungsfunktion: bei Eintreten bestimmter Ereignisse kann man sich nun per E-Mail benachrichten lassen. Dazu muss vorab in der Nutzerverwaltung für den Nutzer eine E-Mailadresse hinterlegt werden. Die gewünschten Benachrichtigungen lassen sich durch Klick auf das Nutzericon auf dem Desktop konfigurieren. Unterstützt sind aktuell:
    - Erwähnung in Sofortnachricht
    - gesendete Sofortnachricht wurde als erledigt markiert
    - Rechnung fällig
    - neuer / geänderter Kalendereintrag mit Person als “verantwortlich”
- Support für Google Mail-Konten (Anbindung mittels App-Passwort). Das Feature ist als experimentell zu betrachten.
- Reduktion gleichzeitig offener Verbindungen (für Office 365, des dort ein Limit von 16 Verbindungen gibt)
- E-Mails lokal speichern: Doppelpunkte im Dateinamen vermeiden
- Anzeige, ob ein Empfänger verschlüsselte Anhänge empfangen kann (ein Passwort hat)
- Aktenzeichen im Betreff und ich Nachrichtentext werden erkannt und für die Aktenvorschläge verwendet
- Maximale Länge für Signaturen erhöht
- Fehler korrigiert, der beim Speichern von E-Mails mit sehr langem Dateinamen auftrat

beA:

- Bei Versand kann nun die Sendungspriorität angegeben werden
- Der XJustiz-Strukturdatensatz ist nun als technische / weitere Anlage kategorisiert, um die wichtigen Anlagen besser im Blick haben zu können.
- Selektionsverhalten bei beA-Anlagen verbessert.
- Layoutproblem korrigiert für Nachrichten mit sehr langer Betreffzeile
- XJustiz-Viewer entfernt. Alternative in Arbeit.
- Fehler bei Versand an mehrere Empfänger behoben.
- Austausch der Herstellerzertifikate für den Zugriff auf die beA-Schnittstelle
- zuletzt für Versand genutztes Postfach wird automatisch erneut ausgewählt für nächsten Versand

Drebis:

- In den Versand-Assistenten sind voreingestellt nur noch Mandanten für eine Übermittlung ausgewählt.

Nachrichten / Instant Messaging:

- Tabs im Nachrichteingang enthalten auch das Rubrum
- Scrollgeschwindigkeit im zentralen Nachrichteneingang korrigiert
- Kopieren von Nachrichten in die Zwischenablage
- Löschen von Sofortnachrichten
- Verhindern des Absendens leerer Nachrichten
- Bei Antworten über einen aktenbezogenen Tab bleibt der Aktenbezug erhalten.
- Unterstützung für individuelle / private Nachrichten:
    - wird eine Nachricht mit einem Aktenbezug gesendet, ist sie "öffentlich" - zu Dokumentationszwecken
    - ist ein User der Absender, sieht er / sie die Nachricht
    - wurde der angemeldete User erwähnt, sieht er / sie die Nachricht
    - ist die Nachricht ohne Aktenbezug und es gibt keine Erwähnungen, sieht er / sie die Nachricht
    - Das bedeutet: Nachrichten ohne Aktenbezug von Person A an Person B können nicht von C eingesehen werden.
- Indikator in der Hauptnavigation zeigte auch offene Nachrichten anderer Personen an

Telefonie:

- n/a

Scans:

- n/a

Nextcloud:

- n/a

REST-API:

- neuer Endpunkt zum Starten einer Datensicherung
- neuer Endpunkt zum Auflisten laufender Aufgaben (bspw. Datensicherungen)
- neuer Endpunkt zum Ermitteln des Status einer bestimmten Aufgabe
- neuer Endpunkt zum Auflisten der Kalender eines Nutzers

Webhooks:

- n/a

Sonstiges:

- Upgrade auf Java 17 für Server und Client
- Upgrade auf neue Wildfly-Version
- Es können nun externe Nutzer (Nutzer anderer Systeme) in der Datenbank vorgehalten werden, bspw. um sie für die Sofortnachrichten zur Verfügung zu haben.
- Verschiedene Bibliotheken-Updates
- Vorbereitung für automatische Downloads von Client-Updates.

---

## j-lawyer.org 2.5

Desktop:

- n/a

Adressen:

- n/a

Akten:

- n/a

Dokumente:

- Zeiterfassung und Rechnungen: Unterstützung Tabellenausgaben in französischer und niederländischer Sprache
- Nutzerkürzel als Platzhalter verfügbar
    - {{AKTE_SACHBEARBEITER_KRZ}} (Kürzel des verantwortlichen Sachbearbeiters)
    - {{AKTE_ANWALT_KRZ}} (Kürzel des verantwortlichen Anwalts)
    - {{AUTOR_KRZ}} (Kürzel des Autors des Dokuments / der Nachricht)
- Dokumente können per Kontextmenü in die Zwischenablage kopiert und dann außerhalb der Anwendung eingefügt werden.

Auswertungen:

- n/a

Kalender:

- n/a

E-Mail:

- n/a

beA:

- Implementierung des Xjusitz-Standards in Version 3.4.1 (wirksam ab / seit 31.10.2023)
- Feldbeschriftung für Safe-ID angepasst

Drebis:

- Integration des Postvorlagensystems (analog beA und E-Mail) für die per Drebis übertragenen Mitteilungen

Nachrichten / Instant Messaging:

- Neues Modul für Instant Messaging
- Nachrichten mit Aktenbezug verfassen (über ersten Tab in der Aktendarstellung)
- Nachrichten mit Akten- und Dokumentenbezug verfassen (über Kontextmenü in der Dokumentenliste)
- Erwähnungen: beim Verfassen einer Nachricht öffnet sich bei Eingabe von “@” eine Auswahl von Nutzern und Nutzerinnen, nach Auswahl kann mittels Leertaste bestätigt und weiterer Text eingegeben werden. Daraufhin wird eine – zu bestätigende – Erwähnung für den Nutzer oder die Nutzerin erstellt und im zentralen Nachrichteneingang angezeigt. Erwähnungen des eigenen Nutzers können durch Klick auf den roten Indikator vor der Nachricht bestätigt werden. Erwähnungen an andere Nutzer sind per Farbindikator und Tooltip hinsichtlich ihrer Abarbeitung nachvollziehbar.
- Hashtags: Nachrichten können mit “#” beginnende Hashtags enthalten, die in der Folge eine Gruppierung / Filterung ermöglichen. So können bspw. abrechnungsrelevante Themen mittels “#Abrechnung” markiert werden, oder beliebig andere Filterkriterien aufgenommen werden.
- Zentraler Nachrichteneingang: Darstellung aller Nachrichten eines ausgewählten Zeitraums
- Zentraler Nachrichteneingang: Gruppierung aller Nachrichten – alle Nachrichten, Nachrichten mit Erwähnugen an den angemeldeten Nutzer / Nutzerin, Nachrichten die vom angemeldeten Nutzer / Nutzerin verfasst wurden und Erwähnungen an andere enthalten, je ein eigener Tab pro Akte für Nachrichten mit Aktenbezug
- Zentraler Nachrichteneingang: Navigation zur Akte (für Nachrichten mit Aktenbezug)
- Zentraler Nachrichteneingang: Navigation zum Dokument einer Akte (für Nachrichten mit Dokumentbezug)
- Popout-Nachrichtenfenster: aus dem zentralen Nachrichteneingang lässt sich ein separates Fenster öffnen, das permanent geöffnet bleiben kann zwecks Kommunikation mit Teammitgliedern.
- Desktop: Anzeige unbearbeiteter Erwähnungen für den angemeldeten Nutzer / Nutzerin

Telefonie:

- n/a

Scans:

- n/a

Nextcloud:

- n/a

REST-API:

- Fehlende Authentifizierungs-Informationen in Open API-Spezifikation (swagger.json) ergänzt
- neuer Endpunkt zum Abholen aller Instant Messages einer Akte
- neuer Endpunkt zum Erstellen einer Instant Message
- neuer Endpunkt zum Löschen einer Instant Message
- Akten, Adressen und Dokumente enthalten nun eine “externe ID”, die bspw. den Kennzeichner in einem externen System speichern kann – so werden Synchronisationen möglich.

Webhooks:

- neuer Webhook zum Empfangen neuer Instant Messages

Sonstiges:

- n/a

---

## j-lawyer.org 2.4

Desktop:

- Sachbearbeiter / Sachbearbeiterin einer Akte wird auf dem Desktop angezeigt
- Kontrast- / Transparenzanpassungen
- Dateiname bei etikettierten Dokumenten ist nun klickbar

Adressen:

- Anzeige der Umsätze / Rechnungsbeträge (aktenübergreifend)
- Layoutfehler / Ausrichtung von Oberflächenelementen korrigiert
- Etiketten auf ersten Tab verschoben

Akten:

- Rechnungsfunktionalität: es lassen sich Rechnungen erstellen und nachverfolgen. Belegarten / Rechnungstypen sind dabei konfigurierbar. Es lassen sich oft verwendete Rechnungspositionen als Vorlage hinterlegen. Rechnungsdokumente können entweder generiert oder zur Rechnung geladen werden. Alle Berechnungs-Plugins wurden erweitert und können nun Rechnungspositionen innerhalb einer Rechnung bereitstellen.
- Zeiterfassung: für gewünschte Akten lassen sich ein oder mehrere Projekte erstellen und anschließend Zeiten auf das Projekt buchen. Projekte können eine definierte Taktung und ein optionales Limit haben. Zeiten lassen sich per Stoppuhr erfassen. Für oft genutzte Tätigkeiten lassen sich “Vorlagen” definieren. Projekte können ausgewertet und als CSV exportiert werden. Projekte (oder nur ausgewählte Zeiten) lassen sich abrechnen – die Rechnungsfunktionalität ist mit der Zeiterfassung integriert. Ein Zeitennachweis lässt sich – zusätzlich zur Rechnungstabelle – automatisch in ein Dokument übernehmen.
- Aktensuche: Anzeige mit der Zusammenfassung der ausgewählte Akte vergrößerbar gemacht
- Layoutfehler / Ausrichtung von Oberflächenelementen korrigiert
- Gegenstandswert in den Tab “Finanzen” verschoben
- Nutzerangabe fehlte bei manuellen Historieneinträgen
- Aktenzeichen kann in Zwischenablage kopiert werden´

Dokumente:

- Experimentell: es lassen sich Briefkopf und Vorlageninhalt getrennt hinterlegen. So ist es möglich, mehrere verschiedene Briefköpfe zu nutzen, ohne den Inhalt von Vorlagen mehrfach pflegen zu müssen. Diese Funktionalität ist stark abhängig von LibreOffice-/Microsoft Office-Formatierungs- und Layoutfeatures und unterstützt aktuell nur einen Teil der Möglichkeiten.
- Tabellen (bspw. RVG oder Rechnungen) können nun per Platzhalter auch in Microsoft Office-Vorlagen (DOCX) übernommen werden.
- Windows: Warnung, dass ein Dokument bereits geöffnet ist, erschien hinter der Fortschrittsanzeige und konnte nicht quittiert werden.
- Windows: Dokumente mit Doppelpunkten im Dateinamen vermeiden
- Cursorhandhabung beim Bearbeiten der Dateinamen im Zuordnen-Dialog verbessert.
- Dateiname einer Notiz ist in den Details der Notiz (d.h. im Inhalt der Notiz, im Kopfbereich) aufgeführt.
- Bei Erstellung eines Dokuments aus einer Vorlage kann wahlweise direkt ein PDF generiert werden (bspw. für Dokumente, die keine weitere manuelle Bearbeitung benötigen).
- Bei Zuordnung von Dokumenten zu einer archivierten Akte kann optional ein automatisches Reaktivieren der Akte ausgeführt werden.

Auswertungen:

- n/a

Kalender:

- Volltextsuche in “Kalender” – “suchen” hinzugefügt
- Falsche Klickposition für ganztägige Termine bei großen Bildschirmauflösungen korrigiert.

E-Mail:

- Unterstützung für Outlook .msg-Dateien.
- Für E-Mails in Form von .eml-Dateien lässt sich nun eine externe Anwendung konfigurieren
- Korrektur bzgl. der Kodierung von Anhangsnamen
- Manche Bilder innerhalb des Textes wurden nicht dargestellt
- “Gesendet”-Ordner wurde für IONOS-Mailkonten nicht erkannt
- Anhänge ohne Dateinamen wurden nicht angezeigt

beA:

- Upgrade auf neueste Schnittstellenversion.
- Fehler "null" nach Speichern einer beA-Nachricht zur Akte korrigiert.
- Umlauteproblem beim Speichern zur Akte behoben.

Drebis:

- n/a

Telefonie:

- n/a

Scans:

- n/a

Nextcloud:

- Fehler “503” beim Auflisten von Kalendern einer Nextcloud korrigiert (betraf nur bestimmte Nextcloud-Konfigurationen).
- Keine Semikolons in Werten bei Adressensynchronisation verwenden (geschütztes Zeichen im VCard-Standard)

REST-API:

- Adressen verfügen über eine zusätzliche (interne / technische) ID, bspw. um ein Mapping zu externen Datenquellen zu ermöglichen.
- Neuer Endpunkt zum Auslesen von Konfigurationen, bspw. Konfigurierte Etiketten
- Neuer Endpunkt zum Validieren eines Dokumentnamens innerhalb einer Akte – Aufrufer können so vor dem Hinzufügen eine explizite Prüfung durchführen.

Webhooks:

- n/a

Sonstiges:

- Speichern von Falldatenblättern robuster umgesetzt (betrifft insbesondere parallele Bearbeitung durch mehrere Personen).
- Fenstergröße und -position werden gespeichert und bei Anwendungsstart wiederhergestellt. Die Funktion funktioniert bei oft wechselnden Bildschirmkonfigurationen nur eingeschränkt (bspw. Notebooks, die wechselnd mit / ohne Dockingstation verwendet werden).
- Client-Installer löscht vor dem Update alte Bibliotheksversionen.
- Über das Menü “Administration” lässt sich ein Fehlerreport erstellen. Dazu sind administrative Rechte notwendig. Der Report kann exportiert und / oder per E-Mail verschickt werden.

---

## j-lawyer.org 2.3

Desktop:

- Zugriff auf Aktenhistorie optimiert. Aktualisierungszeit für “Zuletzt geändert” auf dem Desktop verringert.
- Oberflächenverbesserungen
- Sortierung der Kalendereinträge: Termine werden nun ganz oben dargestellt.

Adressen:

- Beteiligte sind nun anhand ihres Typs sortierbar. Die Sortierreihenfolge kann über die Einstellungen (Adressen – Beteiligtentypen) definiert werden.
- Warte-Cursor bei Adresssuche wurde manchmal nicht zurückgesetzt.
- Im “Akten”-Tab wird nun auch das Zeichen angezeigt, das für den Beteiligten / die Beteiligte in dieser Akte verwendet wird.

Akten:

- HTML-Export: Felder hinzugefügt: eigene Felder, archiviert, Etiketten
- HTML-Export: Notiz im Kopf des Exports entfernt (führte zu Layoutfehlern bei umfangreichen Notizen)
- Das Ablagedatum einer Akte ist nun ein separates Attribut und wird nicht mehr aus der Aktenhistorie ermittelt. Fügt man bspw. nochmals ein Dokument in eine archivierte Akte ein, ändert sich nun nicht mehr das Ablagedatum.
- In der Aktensuche wird für archivierte Akten das Ablagedatum angezeigt.
- Detailanzeige von Beteiligte innerhalb der Akte: Unternehmen, Abteilung, Fax hinzugefügt.
- Über das Kontextmenü an der Detailanzeige der Beteiligten kann die Adresse in die Zwischenablage kopiert werden.
- Warte-Cursor bei Aktensuche wurde manchmal nicht zurückgesetzt.
- Das automatische Löschen von Dokumenten aus dem Papierkorb wird nicht mehr in der Aktenhistorie dargestellt.
- Handaktenbogen teilweise mit abgeschnittenen Jahreszahlen bei den Kalendereinträgen

Dokumente:

- Neuer Dialog zum Abspeichern von Dokumenten aus beA / E-Mail / Scans / …:     Dokumente lassen sich nun unterschiedlich etikettieren, Dokumente können in unterschiedliche Aktenordner übernommen werden, Dokumente können anhand ihres Dateityps ein- oder ausgeschlossen werden, schnelle Angabe von Ordner und Etiketten für mehrere Dokumente, Anzeige der Dateianzahl und Gesamtgröße, optional: Favoriten setzen, Prüfung auf Dateinamenskonflikte – für die neuen Dateien untereinander als auch in der Akte vorhandene Dateien
- Farbliche Markierung von Dokumenten: Dokumente können mit bis zu zwei Farbmarkierungen versehen werden.
- Neuer Platzhalter für Mandatsbeginn / Aktenerstellung (AKTE_ERSTELLT)
- Verbesserungen beim lokalen Abspeichern mehrerer gewählte Dokumente als PDF
- nur Windows: Verzögerungen beim Öffnen / Speichern, wenn Netzlaufwerke angebunden waren, die nicht erreichbar sind.

Auswertungen:

- Neues Modul “Auswertungen” hinzugefügt. Es gibt zwei Kategorien von Auswertungen, welche mit getrennten Berechtigungen aufgerufen werden können. Die Berechtigungen sind in der Nutzerverwaltung zu pflegen.
- Neue Auswertung: Mitarbeiterreport. Die Auswertung gibt – auf Basis der Aktenhistorien – die ungeführe Arbeitszeit von Nutzerinnen und Nutzern aus. Sie ist nur aufrufbar, wenn die Berechtigungen für “vertrauliche” Reporte besteht.
- Neue Auswertung: Offene Rechnungen
- Neue Auswertung: Fällige Rechnungen
- Neue Auswertung: Alle Rechnungen / Belege
- Neue Auswertung: Akten pro Monat
- Neue Auswertung: Akten pro Jahr

E-Mail:

- Unterstützung für Office 365 - Mailkonten
- Es kann nun eine Suche im aktuellen Ordner ausgeführt werden
- Fehler “failed to parse” korrigiert (jedoch unklar, ob die Korrektur für alle möglichen Ursachen greift)
- E-Mail – Vorlagen können nun per Klick umbenannt oder dupliziert werden.
- Neu hinzugefügte / geänderte Falldaten (in Falldatenblättern) einer Akte waren nicht sofort für die Platzhalter in einer E-Mail-Vorlage verfügbar.
- Bei “Allen antworten” fehlte in der Trennzeile das Datum der ursprünglichen Nachricht.

beA:

- Ladezeitoptimierungen
- Nachrichten können nun als gelesen markiert werden
- EGVP-Laufzettel sind nun durchgängig verfügbar und können auch zu späterem Zeitpunkt nach Versand geladen werden.
- EGVP-Laufzettel für eEB-Abgaben und -Ablehnungen verfügbar
- Optimierungen Versandgeschwindigkeit
- eEB-Abgabe / eEB-Ablehnung kann zur Akte gespeichert werden.
- Verbesserte Verbindungswiederherstellung
- Nachrichten, die größer als 250 MB sind, konnten nicht geöffnet werden
- beA – Vorlagen können nun per Klick umbenannt oder dupliziert werden.
- Aktenzeichen / Betreff bei Nachrichten aus einem EGVP teilweise nicht sichtbar – für die betroffenen Nachrichten wird nun zumindest sichergestellt, dass die Daten nach Klick auf die Nachricht sichtbar sind. Es handelt sich um eine Beschränkung seitens der beA-Schnittstelle.
- Zertifikat-Updates
- Layoutverbesserungen in der Nachrichtenanzeige
- Anlagen eingeteilt in "relevant" und "weitere": technische Anhänge sind nun in einem separaten Tab zu finden, Nutzerinnen und Nutzer haben so die eigentlichen / wichtigen Anhänge besser im Blick.
- Anpassungen maximale Anhangsanzahl und -größe´
- Menge der zu ladenden Nachrichten einstellbar gemacht
- Warnung bzgl. VHN2 entfernt (ist nun immer aktiv)
- In Version 2.2 bestand ein Fehler, der unter bestimmten Bedingungen dazu führte, dass gelöschte Dokumente aus der Datenbank, nicht aber die Datei aus dem Datenverzeichnis gelöscht wurde. Verwaiste Dokumente werden im Rahmen der Installation von 2.3 automatisch gelöscht. Hinweis: Hat man manuell weitere Dokumente im Datenverzeichnis abgelegt, so werden diese ebenfalls entfernt, weil sie kein Pendant in der Datenbank haben.

Drebis:

- n/a

Telefonie:

- Wurde das Speichern eines Fax-Berichtes abgebrochen, entstand in der Akte ein Dokument mit leerem Namen, was weiteres Speichern von Berichten für diese Akte verhinderte.

Scans:

- Geringfügige Änderungen in der Nutzbarkeit (bspw. Klick auf “Akte suchen und zuordnen”, Umbenennungen im Kontextmenü)

Nextcloud:

- Passwörter, die bei Freigabeerstellung generiert wurden, waren nur 8 Zeichen lang, Nextcloud setzt in den Standardeinstellungen jedoch 10 Zeichen voraus. Standardlänge auf 10 angepasst.

REST-API:

- Alle API-Endpunkte fix auf UTF-8-Kodierung konfiguriert.
- Endpunkt zum Erstellen von Dokumenten benötigt nun nicht mehr alle Platzhalterwerte – sie werden automatisch ermittelt. Die vom Aufrufenden gelieferten Werte überschreiben die vorhandenen Werte, und sind vollständig optional.
- Fehler beim Laden von Akten im Client, wenn die Akte per API und ohne Notiz erstellt wurde.
- Fehler beim Erstellen von Dokumenten, wenn Ordner keinen führenden “/” hatte
- Fehler beim Erstellen von Dokumenten, wenn Akte keinen Anwalt / Sachbearbeiter hatte
- Versionsattribut für Dokumente hinzugefügt (wird nicht in der Oberfläche angezeigt, sondern wird verwendet, um API-Nutzern das Erkennen geänderter Dokumente zu ermöglichen)

Webhooks:

- n/a

Sonstiges:

- In der gesamten Anwendung wurden Änderungen an Layout, Typographie und Schriftenskalierung vorgenommen.

---

## j-lawyer.org 2.2

Desktop:

- Etiketten-Tabs nun alphabetisch sortiert.

Akten:

- Verbessertes Ladeverhalten für sehr große Aktenexporte.
- Die wichtigsten Informationen von Beteiligten werden direkt in der Akte angezeigt.
- Aktensuche: Anzeige des Sachbearbeiters in der Ergebnisliste.
- Layoutanpassungen im Dokumente-Tab.

Dokumente:

- Konfiguration von Schriftgrößen und Schriftarten für Tabellen, die per Platzhalter übernommen werden.
- Konvertierungen bei Nutzung von Microsoft Office: für von MS Office nicht unterstützte Konvertierungen wird nun LibreOffice als zusätzlicher Konverter verwendet.
- PDF-Konvertierung mittels Microsoft Office schlug fehl, wenn der Nutzername Leerzeichen enthält.
- Unterschiedliche Zeichenkodierungen (bspw. bei Nutzung unterschiedlicher Betriebssysteme für die Arbeitsplätze) gab es unter bestimmten Bedingungen Probleme beim Laden von Dokumenten mit Umlauten oder Sonderzeichen im Namen. Die Korrektur greift nicht für bestehende Dokumente, stellt aber sicher dass alle neu hinzugefügten Dokumente korrekt gehandhabt werden.
- Vollständig überarbeiteter Scan-Eingang: Layoutverbesserungen, Kontextmenü, Seitenleiste analog beA und E-Mail, Umbenennen von Scans vor Aktenzuordnung, Zuordnen mehrerer Scans mit einem mal.
- Automatisches Splitten von PDFs im Scan-Eingang.
- Verbessertes Ladeverhalten für sehr große Dokumente.
- Unterstützung für Skripte in DOCX-Vorlagen (Microsoft Office).
- Neue Skriptfunktion, die auf Vorhandensein von Falldaten prüft (“WENNFALLDATEN”).
- Neue Skriptfunktion, die auf ein gesetztes Aktenetikett prüft (“WENNETIKETT”).
- Neue Skriptfunktion für Kleinschreibung (“KLEIN”).
- Unterstützung für mehrzeilige Skript-Ergebniswerte.
- Verbessertes Ladeverhalten für die Dokumentvorschauen.
- Dokument duplizieren veränderte den Dateinamen (Leerzeichen wurden zu Bindestrichen).
- Bei Ablage als PDF: evtl. vorhandene Datei wahlweise ersetzen können.
- Microsoft Office-Installation automatisch suchen (manuelle Konfiguration sollte so in den allermeisten Fällen entfallen).
- Überarbeitete Druckroutine für PDFs (Vermeiden von Layoutfehlern).

Adressen:

- Vorgeschlagene Verschlüsselungspasswörter an Adresse enthalten nun automatisch auch Sonderzeichen.
- Anzeige der Akten an einer Adresse war auf 25 limitiert. Limit entfernt.

Wiedervorlagen / Fristen / Kalender:

- Terminkonfliktprüfung bei Erstellung oder Änderung von Kalendereinträgen.
- Verschieben von Kalendereinträgen: Popupdialog öffnete sich unter bestimmten Bedingungen auf anderem Bildschirm.
- Verbesserte Handhabung beim Eintragen von Kalendereinträgen über das grafische Kalenderblatt.
- Sortierung der Kalendereinträge in der Monatsansicht: Termine, Fristen, Wiedervorlagen.
- Suche von Kalendereinträgen anhand des Aktenzeichens.
- Mehrtägige Kalendereinträge wurden im Kalenderblatt nur am Starttag angezeigt.

E-Mail:

- Übernahme von Falldaten in E-Mail-Vorlagen ermöglicht.
- In E-Mail-Postvorlagen kann über den Platzhalter {{CURSOR}} der Cursor direkt positioniert werden. Das Eingabefeld wird dadurch auch automatisch selektiert, sodass direkt losgetippt werden kann. Die Funktionalität ist auf reine Textvorlagen (nicht: HTML-Vorlagen) beschränkt.
- Whitelist / vertrauenswürdige Absender wird ausschließlich über Absenderadresse identifiziert (vorher: Absenderadresse und -namen).
- Besseres Ladeverhalten beim Wechsel zwischen Ordnern.
- Versand: Absenderwechsel aktualisierte die Signatur nicht.
- Die zuletzt genutzte Vorlage für den Nachrichtentext wird beim nächsten Versandvorgang automatisch vorausgewählt.
- E-mail-Empfänger wurde mit Komma angezeigt.

beA:

- Implementierung des XJustiz-Standards in Version 3.3.1, gültig ab 31.10.2022.
- Kontaktdatenübernahme aus dem beA-Verzeichnis wahlweise vollständig oder nur die Safe-ID.
- Nachrichtentext wird automatisch als PDF-Anhang verschickt.
- In beA-Postvorlagen kann über den Platzhalter {{CURSOR}} der Cursor direkt positioniert werden. Das Eingabefeld wird dadurch auch automatisch selektiert, sodass direkt losgetippt werden kann.
- Fehler beim Laden von Nachrichten mit ungültigem Xjustiz-Strukturdatensatz.
- Bei Versand von Dokumenten mit Signaturdatei(en) als PDF werden die Signaturdateien nicht mehr in PDF konvertiert.
- Die zuletzt genutzte Vorlage für den Nachrichtentext wird beim nächsten Versandvorgang automatisch vorausgewählt.
- Adressdatenübernahme für Justizadressen war unvollständig.
- Wurde beim Speichern zur Akte der Vorgang abgebrochen, so wurde die Nachricht trotzdem in den “importiert”-Ordner verschoben.
- Fehlerhafte Datumsangabe bei Darstellung einer eEB-Abgabe korrigiert.

Drebis:

- n/a

Telefonie:

- Unterstützung für mehre Rufnummern für das selbe Gerät.
- Datei umbenennen-Dialog beim Speichern der Faxberichte.
- Rufnummernnormalisierung funktionierte nicht für französische Rufnummern.

Nextcloud:

- Die Kalendersynchronisationen können nun so konfiguriert werden, dass erledigte Kalendereinträge in Nextcloud verbleiben.
- Stabilere Synchronisation sehr großer Adressbücher.

REST-API:

- Neuer Service zum Auslesen aller Nutzernamen.
- Neuer Service zum Auslesen aller konfigurierten Kalender.
- Neuer Service zum Erstellen von Kalendereinträgen.
- Neuer Service zum Ändern von Kalendereinträgen.
- Neuer Service zum Erstellen eines Eintrages in der Aktenhistorie.
- Neuer Service zum Auslesen der Vorlagenordner
- Neuer Service zum Auslesen der Vorlagen eines Vorlagenordners
- Neuer Service zum Auslesen der Platzhalter einer Vorlage
- Neuer Service zum Erstellen eines Dokumentes aus einer Vorlage

Webhooks:

- n/a

Sonstiges:

- Tastenkürzel für die wichtigsten Module. Die Tastenkürzel werden als Tooltip des jeweiligen Moduls angezeigt (bspw. Shift+F3 für die Aktensuche).
- Die verschiedenen Einstellungen für Schriftgrößen wurden durch eine Einstellung der Oberflächenskalierung ersetzt.
- Intelligente Eingabefelder / automatische Vervollständigung – betrifft verschiedene Module.
- Backup-Manager: Datenbankverbindung mit expliziter Angabe der Zeitzone.
- “Services”-Menü hinzugefügt.
- Nutzername wird nun bei erfolgreichem Login automatisch im Profil gespeichert.
- Verschiedene Menüeinträge von “Einstellungen” nach “Administration” verschoben.

---

## j-lawyer.org 2.1

Desktop:

- n/a

Akten:

- Falldatenblatt für die Anbindung von Wordpress-Formularen. So können in Wordpress beliebige Formulare erstellt, von externen Parteien ausgefüllt und deren Eingaben dann ohne weitere Konfiguration in eine Akte übernommen werden. Alle so importierten Daten sind auch automatisch für die Verwendung in Vorlagen aufbereitet.
- Wahlweise automatisches Schließen aller offenen WV / Fristen / Termine bei Ablage einer Akte.
- Bei Wechsel in die Aktensuche ist der Fokus nun automatisch im Suchfeld. Eine evtl. vorhandene Suchanfrage ist vollständig markiert.
- Handaktenbogen enthält nun auch Termine.
- Layoutkorrekturen im Handaktenbogen.
- Warnung / Bestätigung, wenn mehrere Akten auf einmal dupliziert werden sollen.

Dokumente:

- Windows: PDF-Konvertierung mittels Microsoft Word, wenn Word als primäre Textverarbeitung verwendet wird.
- Vorerst nur für LibreOffice-Vorlagen: Verwendung von Skriptlogik in Vorlagen. Unter Nutzung dieser Funktionalität lässt sich der Automatisierungsgrad bei der Dokumenterstellung noch wesentlich steigern. Es sind bspw. Funktionen wenn-dann, wenn-gleich, wenn-leer, wenn-enthält und wenn-grösser verfügbar, es lassen sich geschlechterabhängig unterschiedliche Inhalte einfügen, mit Datumsangaben rechnen u.v.m.
- Es können nun pro Dateityp beliebig viele externe Programme konfiguriert werden, bspw. für PDF ein schnell öffnendes Anzeigeprogramm und ein PDF-Editor. Eines der Programme kann als “Standard” eingestellt werden und wird daraufhin bei Doppelklicks auf ein Dokument verwendet.
- Die Dokumentvorschau kann wahlweise nur für Dateien bis zu einer gewissen Größe aktiviert werden. Das Limit ist einstellbar, voreingestellt sind 2MB. Bei sehr großen Dateien und / oder schmalbandiger Netzanbindung werden so Wartezeiten vermieden.
- Wurde ein Dokument per Drag&Drop direkt auf einen Ordner der Akte hinzufgefügt, entstanden zwei identische Einträge in der Aktenhistorie.
- Möglichkeit individueller Datumsformate (neben den bisherigen KURZDATUM und LANGDATUM-Platzhaltern).
- Warnung / Rückfrage bei Abbruch einer Notizerstellung.
- Neues Icon-Set für Dokumente unter Windows, Angleichen an das Design unter macOS und Linux. Damit haben mehr Dokumente auch unter Windows nun spezifische icons (bspw. beA-Nachrichten), und die Icons werden größere dargestellt.
- Dokument duplizieren veränderte unter bestimmten Bedingungen den Dateinamen nach manueller Änderung.

Adressen:

- Bei Wechsel in die Adressensuche ist der Fokus nun automatisch im Suchfeld. Eine evtl. vorhandene Suchanfrage ist vollständig markiert.
- Die zuletzt für eine Adresse genutzte Beteiligtenrolle wird automatisch gespeichert. Bei erneuter Aufnahme der Adresse in eine andere Akte wird automatisch diese Rolle verwendet.

Wiedervorlagen / Fristen / Kalender:

- WV / Fristen / Termine können direkt im Tabellenblatt eingetragen werden.
- Weitere Schnellauswahlen für die Fälligkeiten von Kalendereinträgen (3 Monate, 6 Monate, 1 Jahr).
- Bei Doppelklick in der chronologischen Liste wird direkt der “Kalender”-Tab der entsprechenden Akte angezeigt.
- Beim Duplizieren eines Termins wird nun auch das Enddatum automatisch gesetzt.
- Fristen wurden in der Monatsansicht mit Zeiten angezeigt.
- In der Kalenderansicht sind einzelne Kalender ein- und ausblendbar.

E-Mail:

- Bei Antwort / Weiterleitung einer E-Mail wird die ausgehende E-Mail automatisch in den selben Aktenordner gespeichert.
- Warnung beim Senden einer E-Mail mit leerem Betreff.
- Verbesserte Absender-/Empfängervorbelebung bei Antwort und Weiterleitung.
- Darstellung für HTML-formatierte E-Mails verbessert.
- Bei Anlage eines neuen E-Mail-Postfaches erhält der anlegende Nutzer automatisch Zugriff. Zusätzlich wird ein Hinweis eingeblendet bzgl. Rechtevergabe für weitere Nutzer.
- Beim Speichern von Anhängen zur Akte ist die Akte bereits vorausgewählt, wenn sich die E-Mail in einer Akte befindet.
- Unter bestimmten Bedingungen wurden Postfächer (Ordner) nicht vollständig geladen.
- Test des Mailversands schlug fehl, wenn Anmeldename nicht gleich der E-Mail-Adresse war.
- Aus j-lawyer.org gesendete Anhänge sind bei einigen älteren Outlook- und Thunderbird-Versionen als unbekannte Anlage empfangen worden.

beA:

- Upgrade auf V6 der beA-Schnittstelle.
- VHN2 (“vertrauenswürdiger Herkunftsnachweis 2”) implementiert.
- Anzeige des Übermittlungsstatus.
- Signaturprüfung hinzugefügt.
- Neue Anforderungen an Dateinamen werden nun forciert / automatisch umgesetzt.
- Prüfung auf maximale Datenmenge / Anhangsanzahlen auf die aktuell vom beA unterstützten Werte angepasst.
- Beim Speichern von Anhängen zur Akte ist die Akte bereits vorausgewählt, wenn sich die beA-Nachricht in einer Akte befindet.
- Fehler beim Laden von XJustiz-Strukturdatensätzen einiger Gerichte behoben.
- Anzeige einer Warnung, wenn der temporäre Ordner des beA “zu voll” ist und die Bediengeschwindigkeit beeinträchtigt.
- Verschiedene Layoutverbesserungen.
- Fehlerhafte Umlaute-Darstellung in der eEB-Anzeige behoben.

Drebis:

- n/a

Telefonie:

- n/a

Nextcloud:

- Anpassung der inhaltlichen Details synchronisierter Kalendereinträge.
- Länge des Passwortfeldes für die Kalendersynchronisation erhöht.
- Fehlerkorrektur für Adressbuch- / Kalendersynchronisation, wenn Nextcloud in einem Unterverzeichnis des Webservers installiert ist.

REST-API:

- Neuer Service zum Aktivieren / Deaktivieren der Aktensynchronisation (App).
- Neuer Service zum Ermitteln der zu synchronisierenden Akten für einen Nutzer (App).
- Neuer Service zum Setzen / Entfernen von Aktenetiketten.
- Neuer Service zum Auflisten von Adressetiketten.
- Neuer Service zum Setzen / Entfernen von Adressetiketten.
- Neuer Service zum Auflisten von Dokumentetiketten.
- Neuer Service zum Setzen / Entfernen von Dokumentetiketten.
- Neuer Service zum Auflisten aller Akten eines Kontaktes.

Webhooks:

- Aufbau einer völlig neuen Schnittstellenart. Während die REST-API “passiv” ist – also von außen gesteuert wird – sind Webhooks eine Möglichkeit, aus j-lawyer.org heraus externe Anwendungen über das Eintreten bestimmter Ereignisse zu informieren.
- Neuer Hook: Dokument hinzugefügt
- Neuer Hook: Dokument geändert
- Neuer Hook: Dokument gelöscht
- Neuer Hook: Adresse hinzugefügt
- Neuer Hook: Adresse geändert
- Neuer Hook: Adresse gelöscht
- Neuer Hook: Akte hinzugefügt
- Neuer Hook: Akte geändert
- Neuer Hook: Akte gelöscht
- Neuer Hook: Etikett Akte an
- Neuer Hook: Etikett Akte aus
- Neuer Hook: Etikett Adresse an
- Neuer Hook: Etikett Adresse aus
- Neuer Hook: Etikett Dokument an
- Neuer Hook: Etikett Dokument aus
- Neuer Hook: Falldaten geändert

Sonstiges:

- Zahlreiche Oberflächenverbesserungen
- Unter macOS wurden Klickereignisse teilweise nicht erkannt.
- Datensicherung: “Jetzt sichern” brach mit Fehlermeldung ab, wenn bestimmte Sonderzeichen im Passwort enthalten waren.
- Datensicherung: Passworteingabe bei “Jetzt sichern” nicht mehr im Klartext.
- App-Vorbereitung: Aktensynchronisation aktivieren / deaktivieren
- Verschiedene Bibliotheken-Updates
- Verbindungsprofile-Dropdown ist nun sortiert.
- Nativer Installer für M1-Macs.

---

## j-lawyer.org 2.0.1

Akten:

- Aktensuche nach Etiketten funktionierte nicht für Akten, die noch kein Dokument haben
- Prüfung auf offene Wiedervorlagen / Fristen beim Verlassen einer Akte erschien nur wenn an der Akte etwas geändert wurde

Wiedervorlagen / Fristen / Kalender:

- Wiedervorlagensuche ohne Ergebnis, wenn “von” und “bis” auf den gleichen Tag gestellt sind.

Kalender:

- Oberflächen- / Darstellungsfehler im Einstellungsdialog korrigiert, der nach der Änderung eines Kalenders auftrat.

E-Mail:

- Filter “ungelesene” funktionierte nicht zuverlässig

Drebis:

- Bei Abbruch des Speicherns zur Akte wurde die eingehende Nachricht trotzdem im Drebis-Portal bestätigt und war nicht mehr zugängig.

beA:

- Beim Import der Gerichtsadressen erschien keine klare Fehlermeldung, wenn noch kein beA-Softwarezertifikat hinterlegt war.

Telefonie:

- Sipgate Teams mit mehreren Nutzern: je nachdem welchem Nutzer ein Gerät zugeordnet ist, konnte es vorkommen dass es in der Anwendung nicht auswählbar war.

Sonstiges:

- Ladezeitoptimierungen Wiedervorlagen-Übersicht und E-Mail-Posteingang
- “+”-Knopf zum Hinzufügen von Verbindungsprofilen im Logindialog war je nach Fensterdimension schwer erkennbar

---

## j-lawyer.org 2.0

Desktop:

- Icons für Wiedervorlagen / Fristen / Termine angepasst, um eine bessere Unterscheidbarkeit für Personen mit Rot-/Grünschwäche zu gewährleisten.
- Wiedervorlagen, Fristen und Termine werden auf dem Desktop nun in separaten Tabs angezeigt.
- Auf dem Desktop wird für jede Wiedervorlage / Frist / Termin in einer dritten Zeile die Aktenbezeichnung angezeigt.

Akten:

- Notizenfenster skalierte nicht korrekt, wenn Größe des Anwendungsfensters verändert wurde.
- Hausnummer fehlte in der Handakte.
- Beim Duplizieren einer Akte werden nun auch die (Gruppen-)Berechtigungen mit kopiert.
- Akten mit einem bestimmten Etikett wurden erst dann auf dem Desktop angezeigt, wenn sie mindestens ein Dokument enthielten.
- Anzeige der Aktenhistorie nun sekundengenau.
- Aktenhistorie zeigt nun auch den Wochentag.
- Ladezeiten in Aktensuche waren zu lang, wenn sehr viele Akten mit Berechtigungen gesichert sind.

Dokumente:

- Dokumente können nun aus der Akte heraus als PDF in ein lokales Verzeichnis abgelegt werden.
- Neuinstallationen: mitgelieferte Vorlagen haben nun einen einheitlichen Präfix.
- Versteckte / ungültige Dateien im Vorlagenordner werden nun ausgeblendet.
- Wenn bei Anlage einer Ordnervorlage ein Namenskonflikt vorlag, war die Fehlermeldung zu technisch / schwer interpretierbar.
- Sicherheitsabfrage bei Leeren des gesamten Papierkorbs hinzugefügt.
- Volltextsuche war nicht möglich, wenn die Suchanfrage einen Schrägstrich enthielt.
- Kleinere Layoutanpassungen in der Volltextsuche.
- Tastaturnavigation in der Dokumentenliste: “Enter” öffnet nun das Dokument.
- Bei Erstellung eines Dokumentes aus einer Vorlage gibt es nun einen zusätzlichen Knopf “Erstellen und Öffnen” – das separate Öffnen durch Doppelklick entfällt in diesem Fall.
- JPG- / JPEG-Dateien können nun ebenfalls nach PDF konvertiert werden.
- Es können nun mehrere Dateien auf einmal in eine andere Akte kopiert werden.
- Es können nun mehrere Dateien auf einmal als PDF abgelegt werden.
- Springt man vom Desktop direkt zu einem Dokument einer Akte, so wird dessen Ordner automatisch eingeblendet, sofern er ausgeblendet war.

Adressen:

- Addresssuche: Hausnummer fehlte in der Ergebnistabelle
- Kleinere Usability-Verbesserungen bei der Bankensuche.

Wiedervorlagen / Fristen / Kalender:

- Es steht nun eine erstmals ein Terminkalender zur Verfügung. Die Umsetzung ist noch nicht vollständig, bietet aber die wichtigsten Funktionalitäten. Innerhalb der Akte können nun Termine (mit Start- und Endzeit, Ort, ...) erfasst werden. Es gibt eine chronologische / grafische Tages-/Wochen-/Monatsansicht. Es können unter Menü “Einstellungen” – “Kalender” mehrere Kalender angelegt werden (bspw. einer pro Mitarbeiter / Mitarbeiterin). In der Nutzerverwaltung können Zugriffe auf diese Kalender pro Nutzer freigeschalten werden.
- Wiedervorlagen und Fristen haben nun zusätzlich ein Bemerkungs-/Kommentarfeld.
- Feiertagskalender wurden aktualisiert.

E-Mail:

- Pro Nutzer können nun mehrere Mailkonten angebunden werden. Dabei wird jedes Konto nur einmal konfiguriert (Menü “Einstellungen” – “E-Mail – Posfächer”) und dann in der Nutzerverwaltung am jeweiligen Nutzer aktiviert.
- Ordnerzustände (aufgeklappt / zugeklappt) werden nun gespeichert und beim nächsten Start wiederhergestellt.
- Hinweis: aufgrund eines Fehlers in einer Programmbibliothek kann es zu Verzögerungen beim Öffnen des Posteingangs kommen, insbesondere wenn viele E-Mail-Ordner zur Anzeige kommen und eine hohe Bildschirmauflösung verwendet wird. Das “Verstecken” von Ordnern (siehe vorhergehender Punkt) kann die Wartezeiten erheblich reduzieren.
- Das Layout im Fenster mit den E-Mail-Vorlagen kann nun stärker angepasst werden.
- Im Kontextmenü der E-Mails im Posteingang fehlte die Option, E-Mail und Anhänge separat in die Akte zu speichern.
- Verschlüsselung von Anhängen: war inaktiv, auch wenn nicht verschlüsselbares Dokument aus der Anhangliste entfernt wurde.
- Sporadischer Fehler beim Laden eingebetteter Grafiken behoben.

beA:

- Update auf neueste KSW-Toolkitversion der BRAK
- Implementierung des XJustiz-Standards in Version 3.2.1
- Unter bestimmten Bedingungen war der Trennbalken für die Anhänge so weit nach unten geschoben, dass keine Anhänge sichtbar waren.
- Anhang lokal speichern überschrieb existierende Datei ohne Rückfrage.
- Bei eEB-Abgabe kann kein Datum in der Zukunft mehr gewählt werden.
- E-Mail-Adressen aus dem Adressverzeichnis des beA wurden nicht immer angezeigt.
- Verschlüsselung für Zertifikatspasswort.
- Es kann nun mit mehreren Clients auf dem selben Arbeitsplatz mit dem beA gearbeitet werden.

Drebis:

- Wenn ein Versicherer mit einem ungültigen Nachrichtenformat antwortet, waren diese Nachrichten im Drebis-Posteingang nicht löschbar. In diesen Fällen wird das Nachrichtenformat nun ignoriert, sodass der Posteingang bereinigt werden kann.

Telefonie:

- Sipgate-Anbindung auf neue Schnittstellenversion aktualisiert.
- Faxberichte haben nun das offizielle Format / entsprechen dem offiziell von Sipgate erstellten Dokument.

Nextcloud:

- Adressen können in eine Nextcloud (und somit auch auf Smartphone / Tablet) synchronisiert werden. Die Synchronisation ist aktuell nur in eine Richtung möglich (j-lawyer.org → Nextcloud).
- Termine, Wiedervorlagen, Fristen können in eine Nextcloud (und somit auch auf Smartphone / Tablet) synchronisiert werden. Die Synchronisation ist aktuell nur in eine Richtung möglich (j-lawyer.org → Nextcloud).

REST-API:

- Neuer Service zum Auflisten konfigurierter Kalender.

Sonstiges:

- Im Logindialog können nun mehrere Verbindungsprofile verwaltet werden. Auf dem ersten Tab des Logindialogs kann dann ein Profil ausgewählt werden. Die Funktion ist hilfreich für Anwender, die sich regelmäßig zu verschiedenen j-lawyer.org-Serverinstallationen verbinden.
- Clients, die über einen SSH-Tunnel verbunden sind, verbinden sich nach einem Verbindungsabbruch selbständig neu.
- Führende / angefügte Leerzeichen in den Verbinungsdaten des SSH-Tunnels werden nun automatisch entfernt.
- Installer-Verbesserungen bzgl. der MySQL-Installation unter Windows.
- j-lawyer.org Client auf Java 11 migriert.
- Berechtigungsfehler beim Import des Bankenverzeichnisses behoben.
- Über die Einstellungen kann nun eine Mindestkomplexität für Nutzerpasswörter forciert werden.
- Präfix für Datensicherungs - E-Mail.

---

## j-lawyer.org 1.14

HINWEISE: manuelle Aktionen nach Update
- Nach dem Update müssen neue Versionen aller genutzten Falldatenblätter installiert werden: Menü “Einstellungen” – “Modul ‘Akten’” – “Falldatenblätter”.
- Für Nutzer die per SSH-Tunnel verbinden: das Passwort des SSH-Nutzers wurde bisher per DES verschlüsselt am Arbeitsplatz gespeichert. Diese Verschlüsselung wurde durch eine AES-basierte Verschlüsselung ersetzt, welche ein höheres Sicherheitsniveau bietet. Nach Installation des Updates muss daher einmalig das Passwort erneut eingegeben werden.
- Für Nutzer welche den j-lawyer.org per Direktstart nutzen: die zu übergebenden Parameter haben sich geändert – siehe Kapitel “Direktstart des j-lawyer.org Clients in die Desktopansicht”.

Desktop:

- Verbesserte Etikettenübersicht auf dem Desktop: neben der Gesamtansicht ist es nun möglich, gezielt Akten / Dokumente mit einem bestimmten Etikett anzuzeigen. Dazu werden die abonnierten Etiketten in verschiedenen Tabs dargestellt.

Akten:

- Nutzerführung – bei Aktenneuanlage wurde bei Bearbeitung eines Beteiligten nicht in die Akte zurückgesprungen
- Aktensuche anhand Aktenzeichenerweiterung möglich (bspw. für Suche nach Dezernat / Gruppe)
- Ordner: Status (eingeblendet / ausgeblendet) wird für jede Akte nutzerspezifisch gespeichert.
- Ordner: leere Ordner und Ordner mit Dokumenten sind durch unterschiedliche Icons besser unterscheidbar.
- Ordner: Dokumente per Drag & Drop in Ordner verschieben.
- Ordner: Zuordnungsdialoge (bspw. Scans, beA, E-Mail, …) ermöglichen ein direkte Zuordnung zu Ordnern. Auch die Neuanlage von Ordnern ist in diesem Schritt möglich.
- Ordner: Dokument wurde nicht ausgeblendet, wenn es in einen ausgeblendeten Ordner verschoben wurde.
- Ordner: Hinweis, dass beim Löschen eines Ordners alle darin befindlichen Dokumente gelöscht werden.
- Ordner: Dokumentenanzeige beinhaltet nun den vollständigen Pfad des Ordners.
- Falldatenblätter: die Platzhalterübersicht eines Falldatenblattes zeigt nun auch die Beschreibung / die Bedeutung des Platzhalters an.
- Falldatenblätter: Scrollgeschwindigkeit (Mausrad) korrigiert.
- Wiedervorlagen/Fristen: Sachbearbeiter der Akte als Verantwortlicher voreingestellt.
- Wiedervorlagen/Fristen: Schnellauswahl von +1 Woche / +2 Wochen / +4 Wochen für die Fälligkeiteines
- Wiedervorlagen/Fristen: nach Anlage einer Wiedervorlage oder Frist wird die Auswahl der Gründe zurückgesetzt.
- Wiedervorlagen/Fristen: Doppelklick auf Datumsfeld trägt das aktuelle Datum ein.
- Beim Hinzufügen von Beteiligten wird nun der zuletzt genutzte Beteiligtentyp gespeichert.
- Im Tooltip der Beteiligten fehlte die Hausnummer.

Dokumente:

- Papierkorbfunktion: Dokumente werden durch Löschen zuerst in einen Papierkorb verschoben. Eine Wiederherstellung aus dem Papierkorb ist möglich. Der Papierkorb kann optional automatisch nach x Tagen gelöscht werden.
- Bei Notizerstellung kann direkt ein Etikett vergeben werden.
- Dokumentenliste mit größeren Icons (macOS, Linux)
- Dokumentsortierung sprang nach drittem Klick immer auf Sortierung nach Datum.
- Bei Dokumenterstellung und Nutzung der Vorlagensuche wurden zu viele Ordner aufgeklappt – inklusive solcher die keine passenden Vorlagen enthalten.
- Scans: Mehrfachuploads werden vermieden, wenn mehrere Arbeitsplätze den selben lokalen Ordner überwachen.
- Scans: bei Nutzung eines lokalen Scanordners wird verhindert dass unvollständige Dateien hochgeladen werden (bspw. bei einem sehr großen Dokument, das gerade noch gescannt wird).
- Scans: die Trennerposition im Scaneingang war u.U. auf “ganz oben” gesetzt, so dass es aussah als gäbe es keine Scans.
- Scans: Aktualisieren hat Spaltenbreiten zurückgesetzt.
- Etikettenbereich kann per Trenner größer oder kleiner dargestellt werden.
- Dokumentvorschaubereich lässt sich ausblenden.
- Dokumentenvorschau für .odt-Dokumente scrollt automatisch zum “relevanten” Teil des Dokuments.
- Verschiedene Layout- und Usability-Verbesserungen.
- Umbenennung von Dokumenten war nicht möglich, wenn nur Gross-/Kleinschreibung angepasst wurden.
- Bei langen Dateinamen wird der vollständige Name als Tooltip angezeigt.
- Etikettenfilter war nach Aktenwechsel noch aktiv.
- Ablegen als PDF / anderes Format legt das neue Dokument in den selben Ordner wie das Originaldokument.
- Volltextsuche: fortgeschrittene Suchmöglichkeiten sind im Kopfbereich direkt verlinkt.
- Rechtsklick auf ein Dokument deselektiert alle anderen Dokumente.

Adressen:

- Neuer Button “Anschrit kopieren” im Kopfbereich – kopiert die vollständige Anschrift in die Zwischenablage, zwecks Verwendung in anderen Programmen.
- Layoutfehler korrigiert.
- Bei Suche anhand von Etiketten wurde eine Adresse ggf. mehrfach ausgegegeben (wenn mehrere Filteretiketten übereinstimmten).
- Hausnummer fehlte in Schnellerfassung neuer Adressen.

beA:

- Anhänge einer beA-Nachricht werden mit einem mal ohne Bestätigung des Dokumentnamens in die Akte übernommen. Bei Nachrichten mit hoher Anzahl an Anlagen (bspw. Akteneinsichten) war das bisherige Vorgehen nicht nutzerfreundlich.
- Upgrade auf neueres KSW-Toolkit der BRAK.
- Beim Schließen des Clients wird auf nicht versendete Nachrichten im Postausgang des Postfachs geprüft – i.d.R. ein Zeichen für eine beA-Störung oder andere Probleme beim Versand. In solchen Fällen gibt es eine Warnung an den Nutzer.
- Anlagen mit Aliasnamen wurden mit falscher Dateiendung gespeichert.
- Fehlermeldungen wurden teilweise hinter der Fortschrittsanzeige dargestellt.
- Trennerpositionen im beA-Posteingang werden gespeichert / wiederhergestellt.
- Justizbehörden werden alphabetisch sortiert.
- Fehler bei Übernahme von Adressdaten aus dem beA-Verzeichnis korrigiert.

Drebis:

- Bei Übernahme von Nachrichten in die Akte kann ein Etikett vergeben werden.
- Bei Verwendung bestimmter Aktenzeichenschemata konnten eingehende Drebis-Nachrichten nicht in die Akte übernommen werden.
- Fehler bei Übermittlung von Schadenmeldungen mit Zentralruf korrigiert.

E-Mail:

- Ladezeiten für Ordner signifikant reduziert.
- Für einige Mailserver / Postfächer wurden nicht alle IMAP-Ordner angezeigt (bspw. Office 365).
- Bei Löschen vieler Nachrichten auf einmal sind nicht alle gelöscht worden.
- Fehlende / fehlerhafte Zeilen- und Absatzumbrücke behoben (HTML-formatierte E-Mails).
- Darstellung aller Arten eingebetteter Grafiken.
- Anderes Icon für E-mail-Aktionen (@-Zeichen)

Telefonie:

- Sipgate-Zugangsdaten werden nicht mehr global hinterlegt, sondern am jeweiligen Nutzer. So können – bspw. in Bürogemeinschaften – unterschiedliche Nutzer auch unterschiedliche Sipgate-Zugänge verwenden.
- Aus eingehenden E-Mails und beA-Nachrichten werden Telefonnummern extrahiert und können durch einfachen Klick in der Seitenleiste für einen Anruf verwendet werden.
- Integration von Softphones: es können Softphones eingebunden werden. Somit ist die Telefoniefunktionalität nicht mehr an Sipgate gebunden.

Nextcloud:

- Unterstützung für Nextcloud-Installationen, die sich nicht in der Wurzel des Webservers befinden.

REST-API:

- applyFolderTemplates funktioniert nun anhand der ID des Templates, nicht anhand des Namens. (ACHTUNG: keine Rückwärtskompatibilität!)

Sonstiges:

- Upgrade auf LibreOffice 7 (Neuinstallationen)
- In der Nutzerverwaltung kann für jeden Nutzer ein “Anzeigename” hinterlegt werden. Der Name steht auch als Platzhalter zur Verfügung.
- Anzeigedauer der Tooltips erhöht.
- “Einstellungen” im linken Navigationsbereich in “Vorlagen” umbenannt.
- Bei Öffnen der “suchen”-Ansichten ist das Suchfeld bereits fokkussiert.
- Nutzer ohne Loginrecht erscheinen nicht mehr in Auswahlfeldern. So kann – bspw. anstelle des Löschens eines Nutzers – einfach das Loginrecht entzogen werden.
- Nach Passwortänderungen war unter bestimmten Bedingungen noch eine Zeit lang ein Login mit dem alten Passwort möglich.
- Nutzer können ihr Passwort nun selbst ändern, es ist kein Administratorzugang notwendig.
- Datensicherung: es wird nun erst nach HTML exportiert (sofern aktiviert) und anschließend synchronsiert (sofern aktiviert). Somit ist es möglich, die HTML-Exporte mit auf den entfernten Speicher zu synchronisieren.
- Datensicherung: Option, eine E-mail nur bei fehlgeschlagener Sicherung zu versenden.
- Datensicherung: ad-hoc Sicherung nicht möglich, wenn der Client per SSL verbunden ist.
- Sicherheit: Passwörter werden nur noch als Hashes abgespeichert.
- Sicherheit: Signierte Installer für macOS und Windows – somit entfallen Sicherheitswarnungen der Betriebssysteme.
- Sicherheit: DES-Verschlüsselungen durch AES ersetzt.
- Sicherheit: bei Nutzung der Synchronisation der Datensicherungen wurde bei Benutzung bestimmter Protokolle das Passwort im Log mitgeschrieben.
- Sicherheit: möglichen Angriffsvektor für DOS-Attacken geschlossen (nur relevant für j-lawyer.org Server die öffentlich im Internet betrieben werden).
- Verbindung per SSH-Tunnel: der lokale Port wird nun dynamisch ausgewählt – so werden Konflikte behoben und es ist ein Starten mehrerer Clients ohne Anpassung der Einstellungen möglich.
- Verbindung per SSH-Tunnel: die Verbindungsparameter können nun auch per Kommandozeilenparameter übergeben werden.
- Fehlermeldungen bei Standby des Arbeisplatzes vermeiden / verringern.
- Servermonitoring unter Linux hat unter bestimmten Bedingungen eine Division durch 0 ausgeführt und konnte nicht geöffnet werden.
- Servermonitoring: Emailbenachrichtigung kann getestet werden.
- Servermonitoring: Versand an eine kommaseparierte Liste von E-Mails möglich.

---

## j-lawyer.org 1.13

HINWEISE: manuelle Aktionen nach Update
- Im Rahmen der Überarbeitung der Adressverwaltung gibt es umfangreiche Änderungen bzgl. der Platzhalter. Folgende Platzhalter wurden ersetzt:
    - _FIRMA wird zu _UNTERNEHMEN (also bspw. MANDANT_FIRMA zu MANDANT_UNTERNEHMEy file: /home/jens/dev/j-lawyer-org/j-lawyer-client/build/built-jar.properties
    - Compiling 1 source file to /home/jens/dev/j-lawyer-org/j-lawyer-client/build/classes
    - Note: /home/jens/dev/j-lawyer-org/j-lawyer-client/src/com/jdimension/jlawyer/client/editors/addresses/AddressPanel.java uses unchecked or unsafe operations.
    - Note: Recompile with -Xlint:unchecked for details.
    - compile:N)
    - _TITEL wird zu _ANREDE1
    - _ANREDE wird zu _BEGRUESSUNG
- Die alten Platzhalter sind in Version 1.13 noch unterstützt, um Anwendern Zeit für eine Anpassung der Vorlagen zu geben. In Version 1.14 werden die alten Platzhalter entfernt werden.

Desktop:

- Einstellungen des Desktops werden nun nicht mehr arbeitsplatzspezifisch, sondern nutzerspezifisch gespeichert. D.h. dass man seine Einstellungen unabhängig vom Arbeitsplatz “mitnimmt”.
- Optische Verbesserungen, Hintergrundbilder, Transparenz, größere Status-Anzeigen im Kopfbereich, Schriftarten, uvm.
- Layoutverbesserungen für kleine Bildschirme
- Bei höheren Anzahlen abonnierter Etiketten war die Selektion nach Neustart des Clients unter bestimmten Bedingungen unvollständig.

Akten:

- Ordnerstrukturen für Dokumente. Ordnerstrukturen lassen sich als “Vorlage” definieren, zwecks wiederkehrender Nutzung in mehreren Akten.
- Aktenzeichenschema: Anwaltskürzel und Gruppenkürzel im Einstellungsdialog verkehrtherum beschriftet
- Der HTML-Export einer Akte enthält nun mehr Informationen zu den Beteiligten.
- An Stellen, wo Akten vorab gesucht werden müssen (bspw. zwecks Zuordnung von Dokumenten), sind direkt alle zuletzt geänderten Akten angezeigt. In der Regel kann eine Texteingabe und folgende Suche somit entfallen.
- Datenfelder für Falldatenblätter vergrößert. Bei Eingabe längerer Text kam es zu “failed to read response”-Fehlern.
- Sicherheitsabfrage beim Löschen von Falldatenblättern hinzugefügt.
- Bei Aktenanlage wurden unter bestimmten Bedingungen die Berechtigungen nicht gespeichert.
- Bei Speichern der Akte wurde bisher gewarnt, wenn es keine offene WV gab oder alle offenen WV in der Vergangenheit lagen. Eine Warnung erfolgt nun nur noch dann, wenn keine offene WV existiert, unabhängig von ihrer Fälligkeit.
- Fehler beim Speichern des Handaktenbogens als PDF beseitigt.

Dokumente:

- Dokumente per Nextcloud freigeben: Dokument können aus der Akte heraus in eine Nextcloud geladen, dort freigeben, und der Link per E-Mail verteilt werden. Das ist eine Option mit höherem Sicherheitsniveau im Vergleich zu unverschlüsselten E-Mails und auch geeignet für größere Dateien.
- Unterstützung für lokale Scanordner: es lässt sich an jedem Arbeitsplatz ein Ordner konfigurieren, welcher auf Dokumente überwacht wird. Dokumente, die in diesem Ordner abgelegt werden, werden automatisch in den zentralen Scanordner auf dem Server transferiert und dann vom Arbeitsplatz gelöscht. So können Dokumente von überall für eine zentrale Abarbeitung bereitgestellt werden.
- Bei Zuordnung von Scans wird der übliche Dateinamenspräfix angeboten.
- Layoutverbesserungen im Scaneingang – die Dokumentvorschau nimmt jetzt den kompletten rechten Teil des Bildschirms ein.
- Windows, macOS: native Anbindung von Powerpoint und Excel
- Änderungen bei der Überwachung von Dokumenten, die nicht per Microsoft Office / LibreOffice geöffnet werden. Hiermit sollte bspw. behoben sein, dass Änderungen an PDFs o.ä. nicht zurück in die Akte gespeichert wurden.
- In Bearbeitung befindliche Dokumente werden für eine Dauer von 7 Tagen am Arbeitsplatz belassen. Sollte – bspw. bei einem Verbindungsverlust zum j-lawyer.org Server – ein Dokument nicht zurück in die Akte gespeichert worden sein, so ist der letzte Stand noch am Arbeitsplatz verfügbar.
- Die erste PDF-Konvertierung nach Programmstart schlägt sporadisch fehl. In diesen Fällen wird nun - automatisch und für den Nutzer nicht sichtbar - ein zweiter Versuch durchgeführt.
- Linux: Prüfung auf Dateinamenkollision beim Umbenennen von Dokumenten funktionierte nicht.
- macOS, Windows: .docx-Dateien können per Rechtsklick in der Akte als Dokumentvorlage gespeichert werden.
- Bei Kopieren einer .docx-Vorlage wurde eine falsche Dateierweiterung vergeben.
- Bei Drag&Drop von Dateien in die Akte kann nun eine Umbenennung stattfindern, sofern Dateinamenskollisionen auftreten.

Adressen:

- Grundlegende Überarbeitung der Adressverwaltung: es können mehr als 20 zusätzliche Felder erfasst und über Platzhalter verwendet werden. Alle Änderungen sind auch in der j-lawyer.IO API umgesetzt.
- Anzeige des Alters, inklusive einer U18-Warnung
- Notizfeld an einer Adresse (analog zu den Notizen an einer Akte)
- Änderungen an einer Adresse werden sofort in die Akte übernommen (erforderten bisher Neuladen der Akte, wenn die Adressbearbeitung über die Akte initiiert wurde).
- Die Adresssuche durchsucht nun zusätzliche weitere Felder.
- Teilweise fehlende Sortierung der Beteiligten korrigiert.

beA:

- Unterstützung für Nachrichtentypen – so ist jetzt bspw. auch das Senden als “Mahnantrag” möglich.
- Mit jeder Nachricht werden nun vollständige Visitenkartendaten gesendet.
- Nachrichten können nun als PDF angezeigt und somit auch gedruckt werden.
- Treten beim Laden der Postfach-Ordner Fehler auf, so wird im Hintergrund automatisch mehrmals erneut versucht.
- Fehler bei Versand von Nachrichten mit “&” im Betreff behoben.
- Bei Weiterleitung von beA-Nachrichten wurden die Anlagen nicht mit übernommen.
- Bei Weiterleitung von beA-Nachrichten wurden die Aktenzeichen nicht übernommen.
- Anzahl der ungelesenen Nachrichten wird nur für den Posteingangsordner ermittelt. Somit werden Postfächer wesentlich schneller geladen.
- Bei Abgabe / Ablehnung eines eEB mussten die Aktenzeichen getauscht werden.
- Dateityp-Icons für Signaturdateien hinzugefügt.
- Suche im beA-Verzeichnis vereinfacht.
- Verzeichnissuche im Sendedialog öffnete sich hinter dem Sendedialog.

Drebis:

- Drebis-Posteingang konnte eingehende Nachrichten nicht automatisch zur Akte hinzufügen, wenn erweiterte Aktenzeichen genutzt werden.

E-Mail:

- Unterstützung für Emailanbieter die ausschließlich TLS 1.2 unterstützen (bspw. mailbox.org).
- Bei Übernahme von E-Mails in die Akte wird nun das Sendedatum als Dokumentdatum verwendet, nicht das Datum der Zuordnung.
- Bei Übernahme von E-Mails in die Akte gibt es die Möglichkeit das Dokument umzubenennen, sofern bereits eines mit selbem Namen existiert.
- Fehler durch zu lange Dateinamen bei Versand verschlüsselter Anlagen korrigiert
- Möglichkeit des Testens von E-Mail-Einstellungen hinzugefügt – das sollte die Konfiguration von Mailkonten vereinfachen.

Sonstiges:

- Verschiedene Layoutverbesserungen für die Darstellung auf kleinen Bildschirmen.
- macOS: Schriftarten der Anwendungsoberfläche angepasst, sodass sich die Darstellung noch näher am nativen macOS-Look and Feel orientiert.
- macOS: native Umsetzung des Anwendungsmenüs. Es wird nun – wie für alle anderen macOS-Anwendungen üblich – ganz oben dargestellt und nicht als Teil des Anwendungsfensters.
- Verbindung vom Client zum Server über einein SSH-Tunnel: Anwender, die den j-lawyer.org Server auf einem Linux oder macOS betreiben, können auf diesem Weg nahezu konfigurationslose Transporterschlüsselung erreichen. Die Einstellungen sind im Login-Dialog unter “Verbindung” zu finden.
- Verschiedene Bibliotheken aktualisiert.
- Eine einmal aktivierte Datensicherungsautomatik ließ sich nicht mehr deaktivieren.
- Verbesserungen an der Synchronisation von Datensicherungen auf externe Speicher.
- Installer: Wichtigkeit / Bedeutung des Datenbankpasswortes etwas prominenter dargestellt.
- Nach Anwendungsstart ist der Cursor direkt im Passwortfeld des Logindialogs, sodass eine direkte Passworteingabe und Login ohne Mausnutzung möglich sind.
- Windows: vor Download des XJustiz-Viewers werden Hinweise zur erlaubten Nutzung eingeblendet.
- Bessere Darstellung der Warnung, wenn man sich zu einer j-lawyer.BOX verbindet, welche sich als passive Instanz in einem Verbund mit einer weiteren synchronisierten j-lawyer.BOX befindet.
- Servermonitoring: Farbgebung korrigiert für bessere Lesbarkeit.
- Scrollgeschwindigkeit bei Nutzung des Mausrades an verschiedenen Stellen angepasst.
- Die aktenübergreifende Recherche in den Historien wurde zusammengeführt und ist nun nur noch ein Hauptmenüpunkt.

---

## j-lawyer.org 1.12

HINWEISE: manuelle Aktionen nach Update
- Bisher werden bei Übernahme von Ortschaften aus dem Verzeichnis immer Ort und Bundesland übernommen. Ist dieses Verhalten nicht gewünscht, so ist ein erneuter Import des Postleitzahlenverzeichnisses notwendig. Er kann über Menü “Datei” - Menüpunkt “Import Postleitzahlenverzeichnis” gestartet werden. Vorhandene Adressen werden nicht automatisch angepasst.
- macOS-Nutzer:  mit dieser Version wird auch eine PDF-Konvertierung im Zusammenspiel mit LibreOffice 6 und höher unterstützt. Eine Deinstallation von LibreOffice 4 und Installation einer aktuellen LibreOffice-Version wird empfohlen.

Akten:

- erweiterte Aktenzeichen mit Gruppe / Dezernat, Anwaltskürzel, ...
- Falldatenblätter-Funktionalität: Akten können um weitere fallspezifische Stammdaten erweitert werden. Die Daten können per Platzhalter in Dokumente übernommen werden.
- Neues Falldatenblatt Mietrecht
- Neues Falldatenblatt Verkehrsrecht
- Neues Falldatenblatt Betreuung
- Gruppenbasierte Zugriffsbeschränkungen für Akten
- Neues Beteiligtensystem: es lassen sich beliebige Beteiligtentypen konfigurieren, inklusive Platzhalter. Das Erstellen von Vorlagenvarianten für bestimmte Beteiligtentypen ist nicht mehr grundsätzlich notwendig. Die Prüfung auf Interessenkonflikte wurde überarbeitet.
- Aktenablge: über einen Archivnummerngenerator lassen sich nun eindeutige Ablagenummern erstellen.
- Integration des Xjustiz-Viewers (https://ervjustiz.de/neue-version-des-xjustiz-aktenviewers)
- Beim Bearbeiten von Wiedervorlagen ist die Auswahl der konfigurierten Gründe verfügbar.
- Anlegen mehrerer Wiedervorlagen / Fristen in einem Schritt
- Dialogverbesserungen bei Dokumenterstellung
- Aktenvorblatt: Ansprechpartner aufgenommen
- Fortschrittsbalken bei HTML-Export
- Option “Archivsuche” wird nun gespeichert und wiederhergestellt
- Nach “Reaktivieren” einer Akte aus dem Archiv muss die Akte nicht neu geladen werden.
- MacOS: Wiedervorlage bearbeiten – Datumsauswahl erschien hinter dem Dialog

Dokumente:

- Verhindern dass Dokumente weiterverarbeitet werden, wenn noch ein Speichern-Vorgang aktiv ist (oder aussteht)
- Vollwertige Unterstützung von Microsoft Word als Textverarbeitung. LibreOffice muss weiterhin installiert sein, wird aber bei Nutzung von Microsoft Office nur noch für den Nutzer unsichtbar im Hintergrund für bpsw. Dateikonvertierungen verwendet.
- Unterstützung von LibreOffice 6 auf macOS
- PDF-Konvertierung nutzt nun grundsätzlich PDF/A als Ausgabeformat
- Windows: aus Vorlage neu erstelltes .docx-Dokument kann nicht umbenannt werden

Adressen:

- Bei Übernahme eines Ortes / einer PLZ wird nicht mehr das Bundesland übernommen.
- Adresssuche durchsucht nun auch die Abteilung
- Ergebnisse bei Adresssuche zeigen nun auch die Abteilung an
- Abteilung wird bei Beteiligtensuche angezeigt
- Bei Adressenimport via VCard wird die Abteilung mit importiert
- Vereinfachter Text bei Versand einen Verschlüsselungspasswortes per SMS

beA:

- Authentifizierung per Karte / Lesegerät?
- Bei Versand an ein Gerichtspostfach werden nun die EGVP-Laufzettel mit gespeichert, wenn die Nachricht in eine Akte übernommen wird
- Es ist nun möglich, bei Versand den Anlagentyp anzugeben.
- Die Information, ob ein eEB angefordert wurde, wird nicht mehr aus den beA-Schnittstelleninformationen bezogen, sondern immer aus dem Xjustiz-Strukturdatensatz.
- Anlagen können per Drag & Drop in das Versandfenster gezogen werden.
- Anmeldung an fremdem Postfach schlug fehl, wenn Berechtigungen fehlten.
- Einkürzen von Dateinamen beim Speichern in die Akte, falls notwendig
- Wurde erst bei Versand in das beA eingeloggt, so blieb anschließend der Posteingang leer.
- Update auf neueste beA-Schnittstellenversionen
- Erfolgs- / Fehlermeldung bei Versand
- Im Posteingang wurde die Spalte “gesendet” in “erhalten” umbenannt
- Spezifischere Fehlermeldung, wenn eine j-lawyer.org-Version nicht mehr für die Nutzung der beA-Schnittstelle freigegeben ist
- Sortierung nach “permant gelöscht” im Papierkorb funktioniert nicht
- bessere Fehlermeldung bei unzulässigen Verschiebevorgängen (zwischen Ordnern)
- Nachricht wurde unter bestimmten Bedingungen ohne Empfänger-Aktenzeichen verschickt
- Aktenzeichenfelder vergrößert (Sendedialog)
- Layout Sendedialog verbessert
- Ordnerreihenfolge geändert – analog beA-Weboberfläche
- macOS: Pfeiltastennavigation funktionierte nicht im Sendedialog
- Layoutfehler beA-Teilnehmersuche korrigiert
- Auswahl Justizbehörde: nach “Abbrechen” wurde die Nachricht trotzdem verschickt

Fax:

- Fehler beim Bestätigen von Faxberichten unter macOS beseitigt.
- Guthabenanzeige war falsch formatiert
- Mehrfachselektionen (zum Bestätigen mehrerer Faxe auf einmal), alle auswählen über zusätzlichen Knopf

Sonstiges:

- Unterstützung für verschlüsselte (SSL-) Verbindungen zwischen j-lawyer.org Client und Server
- Nahezu die gesamte Funktionalität des j-lawyer.org Servers ist nun via REST-API nutzbar. So werden eigene Integrationen ermöglicht.
- Im Anmeldedialog werden die letzten Server für spätere Auswahl gespeichert.
- F-Tastenkürzel wieder entfernt

---

## j-lawyer.org 1.11

Akten:

- Bei Anlage von Wiedervorlagen / Fristen wurde die Auswahl des Typs bisher „gemerkt“ und wiederverwendet. Ab sofort ist die Vorauswahl immer „Wiedervorlage“.
- Angabe eines „Start-Aktenzeichens“ ist nun bei mehreren Aktenzeichenschemata möglich.
- Korrektur: Einstellungsdialog für Aktenzeichenschema hat unter bestimmten Bedingungen eine falsche Auswahl angezeigt.
- Korrektur: Aktenvorblatt bricht langes Rubrum um.

Dokumente:

- Beim Anpassen des Dokumentdatums kann nun der aktuelle Tag mit einem Klick übernommen werden.
- Besserer Umgang mit Dateinamenskonflikten bei Zuordnung von Scans zu einer Akte.
- Dokumente können in einer Akte nun mehrfach als PDF abgelegt werden.
- Mehr Formatierungsmöglichkeiten bei der Übernahme von RVG-Plugin-Ergebnissen in Dokumente.
- Erste prototypische Unterstützung für Dokumentvorlagen im Microsoft Office DOCX-Format.
- Beim Ersetzen von Platzhaltern wurden bisher evtl. um den Platzhalter herum existierende Tabulatoren entfernt. Das hat das Formatieren / Strukturieren via Tabs erschwert.

Adressen:

- Neues Feld für Ansprechpartner / Abteilung, plus dazugehörige Platzhalter für die Übernahme in Dokumente.

beA:

- In der Nachrichten-Entwurfsansicht hat man beim Anhängen von Dokumenten auch direkten Zugriff auf alle Dokumente der Akte.
- Update auf letzte Schnittstellenversion der BRAK
- Konsequente Nutzung / Übernahme der Aktenzeichen Absender / Empfänger.
- Bei Import einer Nachricht in eine Akte kann die Nachricht automatisch in einen bestimmten Unterordner des Postfachs verschoben werden. So behält man besseren den Überblick, welche Nachrichten sich schon in Akten befinden.
- Nachrichten können – anstelle eines direkten Versands – als Entwurf in einem Ordner gespeichert werden. Das ermöglicht ein arbeitsteiliges Vorgehen (Person A erstellt Nachrichten, Person B signiert und verschickt).
- Nachrichten können aus dem Papierkorb wiederhergestellt werden.
- Im Papierkorb wird nun das Datum des endgültigen Löschens (durch die Betreiber des beA) angezeigt.
- Vor dem Senden wird auf Vorhandensein von Empfängern geprüft.
- Verhindern des Sendens von .bea-Dokumenten als PDF (wird nicht unterstützt)
- Aus dem beA-Posteingang kann der Absender samt allen bei der BRAK geführten Kontaktinformationen als neue Adresse erstellt werden.
- Neue Aktion in der Seitenleiste: „nur Anhänge speichern“
- Seitenleiste: relevante Akten werden nach letzter Änderung absteigend sortiert
- Das Senden von Nachrichten mit leerem Betreff wird verhindert.
- Beim Verfassen von Nachrichten können nun Empfänger und Anhänge wieder gelöscht werden.
- Bei der eEB-Abgabe gibt es nun zusätzlich zum Freitext eine Auswahl an Ablehnungsgründen, vergleichbar mit denen der beA-Weboberfläche.
- Bei automatischer Anmeldung per Softwarezertifikat findet das Anmelden und das Laden der Postfachstruktur nun in einem Hintergrundprozess statt. „Hängt“ das beA / die beA-Anmeldeserver, so wird der Start des j-lawyer.org Clients nicht mehr verzögert.
- Korrektur: beim Speichern von beA-Nachrichten in die Akte überlagerten sich Fortschrittsanzeige und „Datei umbenennen“-Fenster.
- Korrektur: endgültiges Löschen von Nachrichten aus dem Papierkorb funktionierte nicht.
- Korrektur: bei Abgabe eines eEB wird die Auswahl eines Datums in der Zukunft verhindert.
- Korrektur: Sendedialog hat nicht alle Beteiligten zur Auswahl angezeigt.
- Korrektur: im Sendedialog wurden innerhalb des Nachrichtentextes nicht alle Platzhalte ersetzt
- Korrektur: ein Strukturdatensatz wird nur dann erzeugt, wenn Anhänge versendet werden.
- Korrektur: Übernahme von Kontaktdaten aus dem beA nicht funktionsfähig für einige SafeIDs (bspw. govello-*)
- beA-Anmeldung per Karte
- beA: Angabe von Aliasnamen für versendete Anhänge

E-Mail:

- In der E-Mail-Entwurfsansicht hat man beim Anhängen von Dokumenten auch direkten Zugriff auf alle Dokumente der Akte.
- Konfiguration Mailserver-Ports (bei Abweichungen von Standardports) möglich
- Anzeige von BCC: (bspw. für gesendete E-Mails)
- Beim Verfassen von E-Mails können nun Empfänger und Anhänge wieder gelöscht werden.
- Neue Aktion in der Seitenleiste: „nur Anhänge speichern“
- Seitenleiste: relevante Akten werden nach letzter Änderung absteigend sortiert
- Korrektur: bei Absenden ohne gültigen Empfänger ging der E-Mail-Entwurf verloren.
- Korrektur: bei Weiterleiten einer E-Mail aus der Akte heraus waren die Beteiligten der Akte nicht als mögliche Empfänger auswählbar.
- Korrektur: sporadische Fehlermeldung „null“ beim Öffnen von E-Mails.
- Korrektur: E-Mails mit mehreren HTML-Nachrichtenteilen wurden unter bestimmten Bedingungen nicht vollständig dargestellt.

Design / Oberfläche
- Umfangreiche Designänderungen – Umstellung auf Material Design, neues Menü, Icons, Farben
- „Tags“ in „Etiketten“ umbenannt.
- „Tipp des Tages“ entfernt
- Desktoplayout angepasst, um Bildschirmfläche besser zu nutzen
- Korrektur: Aktualisierungsprobleme für „Markierte“-Bereich auf dem Desktop.

Sonstiges:

- Kanzleiprofil: es kann nun ein Anderkonto angegeben und über Platzhalter in Dokumente übernommen werden
- Kanzleiprofil: es kann ein UStID angegeben und über Platzhalter in Dokumente übernommen werden
- Tags / Etiketten können nun umbenannt werden. Dabei können wahlweise auch alle vorhandenen Tags an Akten / Adressen / Dokumenten vollautomatisch angepasst werden.
- Monitoring Arbeitsspeicher: E-Mail-Benachrichtigung erst nach drei aufeinander folgenden Messungen über Limit
- Intelligentere Updateprüfung – so erhalten auch Pilotanwender, die der öffentlichen Version „voraus sind“, keine inkorrekten Updatebenachrichtigungen mehr.
- Datensicherungseinstellungen können nur gespeichert werden, wenn ein Datenbankpasswort angegeben wurde.
- Datensicherung nutzt für die Datenbank nun das Encoding entsprechend der Datenbankeinstellungen.
- Kleinere Usability-Verbesserungen beim Import der Banken- und Ortschaftenverzeichnisse.
- macOS-Installer lädt nun auch das deutsche Sprachpaket für LibreOffice mit runter.
- Korrektur: Synchronisation der Datensicherung hat gelöschte Akten nicht aus dem Synchronisationsziel gelöscht
- Korrektur: Workaround für MySQL-Datenbankfehler unter macOS bei bestimmten Schemaänderungen.
- Korrektur: sporadische „ClassCastException“ beim Starten des j-lawyer.org Clients.

---

## j-lawyer.org 1.10

Akten und Adressen:

- Kopieren von Adressen – kopiert werden Adresstammdaten sowie Tags.
- Kopieren von Akten – kopiert werden Aktenstammdaten und Beteiligte sowie Tags. Die Kopie ist nicht archiviert und erhält eine neue Historie. Dokumente und Wiedervorlagen / Fristen werden nicht übernommen.
- Der Handaktenbogen enthält nun auch das Zeichen der Beteiligten
- Aktensuche durchsucht nun auch das Sachgebiet
- verschiedene Erweiterungen und Korrekturen in den Berechnungsplugins
- Angabe eines Geburtsdatums in einer Adresse nun über eine Kalenderauswahl möglich
- Aktenexport: Änderungdatum der exportierten Dokumente entspricht dem Datum des Hinzufügens zur Akte
- Bessere Aktualisierung der Beteiligtendaten innerhalb der Akte

Dokumente:

- Scaneingang: neue Standardsortierung nach Änderungsdatum absteigend, Korrekturen bzgl. der Aktualisierung der Ansicht
- Dokumente können in (fast) beliebige Formate konvertiert werden.
- Verschlüsseltes PDF generieren: neben Eingabe eines nutzerdefinierten Passwortes können auch die Passwörter der Beteiligten der Akte ausgewählt werden.
- Tagging / Markierung für Dokumente – die Tags sind als Filter auf dem Desktop nutzbar und können bei Scanzuordnung, Emailzuordnung, uvm. gesetzt werden

beA:

- Upgrade auf neueste Schnittstellenversion
- Verschieben von Nachrichten in andere Ordner
- Safe ID an Adresse speichern, verifizieren, aus beA-Eingang ins Adressbuch übernehmen
- Seitenleistenaktionen analog E-Mail-Posteingang implementiert
- Nachrichtenjournal einer bereits in die Akte exportierten Nachricht aktualisierbar machen / Abgleich mit beA-Server
- Anzeige und Export von EGVP-Laufzetteln
- Vorlagensystem (analog E-Mail-Integration)

E-Mail-Integration:

- E-Mail-Vorlagen: Platzhalterbereich ist nun in der Größe veränderbar
- Löschen mehrerer E-Mail-Vorlagen auf einmal
- E-Mail senden: Dialog enthält Möglichkeit eine Wiedervorlage/Frist anzulegen
- E-Mail-Zitag: Datum und Uhrzeit in Trennzeile

Sonstige Erweiterungen:

- Upgrade auf neueste Install4J-Version für die Installer
- Automatische Datenbank-Updates. Die Aktualisierungen finden nun nicht mehr durch den Installer statt, sondern durch die Anwendung selbst. Somit wird es ab Version 1.10 möglich sein, Updates zu überspringen (bspw. direkt von 1.10 auf 2.2). Die Updates werden außerdem noch leichter und weniger fehleranfällig (bspw. bei Eingabe falscher Datenbankpassworte).
- Startzeit des j-lawyer.org Clients stark reduziert

Korrekturen:

- Titel einer Adresse war nicht zurücksetzbar auf leeren Wert
- Darstellungsfehler bei sehr langen Tag-Listen
- Fehler bei der Behandlung von E-Mail-Anhängen mit leerem Dateinamen behoben
- Zu lange Dateinamen bei Speichern von Emails
- Verhindern von Timeouts bei der Synchronisation von Datensicherungen mit einem SSH-Ziel
- Backup Manager-Korrektur bzgl. Wiederherstellung sehr großer Datenbanksicherungen
- Export von Akten schlug sporadisch fehl.
- Doppelte Trefferausgaben bei Filtern nach mehreren Tags.
- Sporadische Fehler beim Speichern von Dokumenten unter Windows mit LibreOffice 6.0.2
- Stark verzögerte Aktualisierung der Faxstatusansicht
- PDFs werden nicht angezeigt wenn JGIB2-Images enthalten sind
- Akten wurden beim Verlassen fälschlicherweise als geändert erkannt, wenn bestimmte Werte im Gegenstandswert erfasst waren.
- Datumsauswahldialog immer auf dem selben Bildschirm wie der öffnende Dialog darstellen.
- Notizen: bei Anlegen einer Notiz mit WV/Frist ist nun sichergestellt dass die WV/Frist angelegt werden kann bevor die Notiz erstellt wird.

Sonstiges:

- Nutzerverwaltung: Berechtigung zum Lesen von Einstellungen wurde entfernt
- Nutzerverwaltung: Hinweise beim Löschen von Nutzern, dass es in der Regel die bessere Alternative ist, lediglich das Loginrecht zu entziehen.
- Upgrade von Wildfly 9 auf Wildfly 15. Die gesamte j-lawyer.org Serverplattform ist somit auf dem neuesten Stand.
- DEB/RPM-Packages für j-lawyer.org Client
- urteile-gesetze.de – Integration: Trefferlisten-Highlighting
- urteile-gesetze.de – Integration: Scrollgeschwindigkeit
- urteile-gesetze.de – Integration: Anzahl der gelieferten Treffer erhöht

---

## j-lawyer.org 1.9.1

Akten und Adressen:

- Schnellerfassung einer Adresse aus der Akte heraus – es müssen nicht mehr alle Beteiligten bereits angelegt sein
- Zeichen von Beteiligten erfassen
- Filterung mit Angabe mehrerer Tags
- Grundlagen für automatisch aktualisierbare RVG-/Gebühren-Plugins
- Wiedervorlagen: Suchparameter erscheinen auf ausgedruckter Liste
- Editieren von Wiedervorlagen / Fristen per Doppelklick
- Aktenzeichen können (in Ausnahmefällen) bearbeitet werden
- Suchoptionen der Wiedervorlagensuche per Knopfdruck zurücksetzen

Dokumente:

- Favoritenfunktion für Dokumente – häufig genutzte Dokumente können als Favoriten markiert werden und sind anschließend immer über einen Klick im Aktenkopf verfügbar
- direkter Druck von PDFs
- Dokument als Vorlage speichern
- Ordnerstruktur für Dokumentvorlagen
- Unterstützung für beliebige Dateiformate in den Vorlagen
- Vorlagen umbenennen
- Vorlage zur Zeiterfassung aufgenommen (Autor: mneumann)
- Notizbutton im Aktenkopf
- Wechsel auf LibreOffice 6 (neue Installationen)
- Notizfunktion: Telefon- und Aktennotizen können direkt in der Akte und ohne LibreOffice erstellt und bearbeitet werden
- Serienbrieffunktionen
- Dokumente als passwortgeschützte PDFs exportieren
- Dokumente verschlüsselt versenden
- Dokumente hinzufügen: zuletzt genutztes Verzeichnis wird beim nächsten mal wieder geöffnet
- enthält eine Zeile in einem Dokument ausschließlich einen Platzhalter, und gibt es keinen Wert für diesen Platzhalter, so wird die Zeile vollständig entfernt
- Handaktenbogen enthält nun auch die Faxnummer von Beteiligten
- Sortierung im Scaneingang wird gespeichert

E-Mail-Integration:

- verschlüsselte PDFs per E-Mail versenden
- E-Mails können nach Zuordnung zu einer Akte optional gelöscht werden
- neue Aktion in der Seitenleiste im Posteingang: bei unbekanntem Absender kann zwecks Zuordnung nach einer Akte gesucht werden
- Anlagen können aus dem “E-Mail senden”-Dialog nochmals geöffnet werden

Sonstige Erweiterungen:

- symmetrische Verschlüsselung für Datensicherungen
- durchgehende Nutzung von SSL (bspw. auch für das Prüfen auf Updates)
- es ist nicht mehr notwendig den j-lawyer.org Server an eine bestimmte IP zu binden – das erleichtert die Konfiguration
- Unterstützung für inkrementelle Datensicherungen
- feiner einstellbares Systemmonitoring (die einzelnen zu überwachenden Werte können separat an- und ausgeschalten werden)
- schnellere Aktualisierung bei Hinzufügen / Entfernen von Tags
- Abbrechen-Möglichkeit beim Schliessen des j-lawyer.org Clients, wenn noch Dokumente geöffnet sind
- Anzeige einer Warnung, wenn der j-lawyer.org Client mit einer replizierten j-lawyer.BOX gestartet wird
- Login-Dialog: Button zum Herunterfahren einer j-lawyer.BOX

Korrekturen:

- sporadischer Fehler nach Zuordnen von Scans behoben
- Aussagekräftigere Fehlermeldung bei falschen Sipgate-Zugangsdaten
- wenn viele Anlagen per E-Mail versendet werden, wurde der vorgeschlagene Dateiname zu lang
- Korrektur Webservice-Endpunkt für die Integration von urteile-gesetze.de

Sonstiges:

- Umstellung auf APGLv3-Lizenz – die Software ist nun als Open Source verfügbar
- neues separates Programm zur Wiederherstellung des Datenbestands aus Datensicherungen

---

## j-lawyer.org 1.9

Akten und Adressen:

- schnelle Anlage von Akten-/Telefonnotizen
- die Unterscheidung “bearbeiten” und “einsehen” entfällt und wird durch “suchen” ersetzt – ob die Akte schreibgeschützt geöffnet wird bestimmen die Berechtigungen des jeweiligen Nutzers
- das Fälligkeitsdatum einer Wiedervorlage kann verschoben werden
- Usability-Verbesserungen bei der Auswahl von Beteiligten
- Anzeige von Tags in Akten- und Adressentabellen
- Usability-Verbesserungen bei Angabe von Ort und PLZ in einer Adresse
- Usability-Verbesserungen bei Aktenauswahl
- zusätzlicher “Übernehmen”-Knopf im Aktensuchedialog
- Tags können nun direkt bei Neuanlage von Akte / Adresse vergeben werden
- erweiterte Tooltip-Anzeige für Beteiligte in einer Akte
- Aktensuche: Ergebnis initial nach Aktenzeichen (aufsteigend) sortiert
- Bearbeiten von Wiedervorlagen
- Adresssuche sucht nun auch nach Telefonnummern
- neue Standardsortierung: neuere Wiedervorlagen / Fristen oben
- neue Standardsortierung: neuere Historieneinträge oben
- Dropdowns mit längerer Darstellung der Auswahllisten

Dokumente:

- native Anbindung von Microsoft Office als Editor für Microsoft-Dokumentformate
- Schnellfilter in der Aktenansicht – es kann schnell nach Dokumentnamen recherchiert werden
- in der Dokumenttabelle wird die Größe des Dokumentes angezeigt
- in den Dokumentvorlagen können existierende Dokumente hinzugefügt werden
- Dokumentdatum ist editierbar
- Dokumentvorschau für E-Mail-Dokumente zeigt nun alle Kopfinformationen
- Scaneingang: Akten können optional getagged werden
- Scaneingang: Löschen der Dokumente aus dem Scaneingang ist jetzt optional
- Scaneingang: Usability-Verbesserungen
- Dateinamenautomatik mit vorangestelltem Datum
- .docx als von LibreOffice unterstütztes Format konfiguriert
- Öffnen mehrerer markierter Dokumente per Kontextmenü
- Sliderposition der Dokumentvorschau wird für den Nutzer gespeichert
- breiteres Fenster für das Umbenennen von Dokumenten
- neue Standardsortierung: neue Dokumente oben

E-Mail-Integration:

- Die Anzahl der abzurufenden E-Mails kann begrenzt werden, der Posteingang lädt somit schneller
- aus dem Posteingang heraus kann eine neue Adresse erstellt werden
- in einer Seitenleiste des Posteingangs werden alle Akten des Absenders angezeigt
- über die Seitenleiste des Posteingangs kann die Nachricht mit einem Klick in eine Akte des Absenders übernommen werden
- bei Übernahme von E-Mails in die Akte kann optional ein Tag vergeben werden
- bei Übernahme von E-Mails in die Akte können die Anlagen als separate Dokumente übernommen werden
- aus dem Posteingang heraus kann direkt zu den Kontaktdaten (Adresse) des Absenders navigiert werden
- Rechtsklick auf einen Anhang in einer Email selektiert den Anhang
- größere Icons
- werden Anlagen per E-Mail verschickt, so enthält der Name des E-Mail-Dokumentes in der Akte die Dateinamen der Anlagen

Sonstige Erweiterungen:

- Integration von urteile-gesetze.de – Recherche in Gesetzestexten und Urteilen
- Desktopansicht: Fälligkeiten und Akten ermöglichen eine Filterung auf diejenigen des angemeldeten Nutzers
- Desktopansicht: Filterung nach Tags
- Absendername für Servermonitoring-E-Mails ist konfigurierbar
- Servermonitoring-E-Mails nicht mehr im Intervall sondern nur bei Statuswechsel
- keine Klartextpassworte in der E-Mail-Konfiguration des Nutzers
- Direktstart des j-lawyer.org Clients über Kommandozeilenargumente
- j-lawyer.BOX Management Console kann aus dem Logindialog heraus geöffnet werden
- Aktualisierung einiger Bibliotheken
- Drebis-Posteingang mit einstellbarem Bildschirmteiler / Slider
- Drebis-Statusinformationen auf Desktopansicht und in der Statusleiste
- besserer Farbkontrast für inaktive Tags
- Einstellung “Themes” entfernt

Korrekturen:

- Änderungen an Präsentationen (.odp, .fodp) wurden unter Linux nicht gespeichert
- Wiedervorlagegründe im Dokumenterstellen-Dialog waren nicht sortiert
- falsches Tabellenlayout bei Abbrechen des Ladevorgangs im E-Mail-Posteingang
- E-Mail: “Allen antworten” hat nicht alle Adressaten übernommen
- beim Weiterleiten von E-Mails fehlten die Anlagen
- archivierte Akten wurden unter bestimmten Umständen mit einer (fehlerhaften) Warnung geöffnet (“es müssen erst alle Wiedervorlagen geschlossen werden”)
- Aktenzeichenschema RRR/YY konnte in Endlosschleife laufen
- Umbenennen von Dokumenten filterte nicht alle Sonderzeichen und erlaubte das Ändern der Dateinamenerweiterung
- nach Hinzufügen von Dokumenten aktualisierte sich die Ansicht nicht zuverlässig
- leere Fehlermeldung bei falsches Drebis-Zugangsdaten
- Installer unter macOS zeigte eine fehlerhafte Meldung bzgl. der MySQL-Installation
- SFTP-Synchronisation der Datensicherungen funktionierte nicht wenn kein Shell-Zugriff erlaubt ist
- höherer maximaler Speicher für Client und Server
- schnellere Desktopaktualisierung
- Fehlerkorrektur im Adressenimport
- Layoutfehler im Aktenvorblatt
- Titel waren nicht sortierte bei Eingabe einer neuen Adresse
- bessere Schriftfarbe selektierter Tabellenzeilen
- LibreOffice-Dokumente werden schreibgeschützt geöffnet, wenn Sie aus einer nur lesend geöffneten Akte heraus geöffnet werden
- falsche Feldbezeichnung in Drebiseinstellungen
- falscher Dialogtitel bei “Andreden”-Konfiguration in den Einstellungen

---

## j-lawyer.org 1.8.1

Akten und Adressen:

- Die Suche schließt nun die “Eigenen Felder” mit ein
- Archivierung einer Akte generiert einen expliziten Eintrag in der Aktenhistorie
- “fehlende Wiedervorlagen”-Report: Anzeige aller nicht archivierte Akten ohne offene Wiedervorlage
- Archivierung von Akten wird verhindert, wenn noch offene Wiedervorlagen vorhanden sind
- Beim Speichern archivierter Akten wird keine Wiedervorlageprüfung mehr durchgeführt
- archivierte Akten sind gesperrt und können ausschließlich dearchiviert werden
- Auswahl eines Tags in der Suche aktualisiert sofort die Ergebnisanzeige

Dokumente:

- Dokumenten-Handling vollständig überarbeitet: beliebig viele Dokumente aus beliebig vielen Akten öffnen
- Zwischenspeichern (bisher: nur Speichern und Schließen des Dokuments) in LibreOffice oder anderem externen Programm transferiert die Änderung an den j-lawyer.org Server
- Dokumentmonitor – Anzeige aktuell geöffneter Dokumente und deren Stausinformationen
- Dokumente einer Akte können per Rechtsklick (“als PDF ablegen”) nach PDF konvertiert in der Akte abgelegt werden
- Die meisten Dokumentformate können in der Akte nun als native Vorschau eingesehen werden
- Die “Mastervorlagen”-Funktionalität wurde entfernt
- Dokumente können per Kontextmenü geöffnet werden (zusätzlich zum Doppelklick)
- Dateinamen beim Dokumenterstellen können automatisch Mandanten-/Gegner-/Dritte-Bezeichnung beinhalten

Sonstige Erweiterungen:

- Steuerelemente im Kopf der Dialog wurden vom rechten an den linken Rand verlagert, um Mauswege zu sparen
- Das Öffnen von Kontextmenüs selektiert nun automatisch den entsprechenden Eintrag in Tabellen und Listen
- viele Tabellendarstellungen können direkt nach LibreOffice exportiert werden
- Anzahl der vorzuhaltenden historischen Datensicherungen ist nun einstellbar. Achtung: Nach Installation des Updates ist die Voreinstellung “2” - beim nächsten Lauf der Datensicherungen werden also einige Dateien gelöscht. Bitte vorher die Einstellung anpassen, sofern weiterhin mehr Sicherungen vorgehalten werden sollen.
- Datensicherungen können nun automatisch mit externem Speicherort synchronisiert werden (bspw. Speicherung auf externem Server)
- gesamter Datenbestand kann mit der Datensicherung als HTML exportiert werden. Im Fall eines Systemausfalls haben Sie so lesenden Zugriff auf alle Informationen, es wird lediglich ein Browser benötigt
- Netzwerkeinstellungen für Mehrbenutzerbetrieb können nun direkt aus dem j-lawyer.org Client heraus angepasst werden
- verschiedene vorbereitende Arbeiten für eine beA-Integration
- direkter Zugriff auf j-lawyer.BOX-Funktionen im Login-Dialog
- Verbesserungen der Bedienung im E-Mail-Senden-Dialog
- automatische Bereinigung der Server- und Clientprotokolldateien
- E-Mail mit Zusammenfassung der Datensicherung sowie Monitoring-E-Mails enthalten nun den Servernamen
- Systemmonitoring-Einstellungen sind nun etwas feiner abgestuft einstellbar
- Die mitgelieferte Java-Version wurde aktualisiert. Achtung Linux-Anwender: Java ist im Gegensatz zu Windows und Mac nicht Bestandteil der Installer – bitte VOR dem Update sicherstellen dass Java 8 installiert ist (in der Konsole sollte ein “java -version” mindestens 1.8.0 oder später ausgeben).

Korrekturen:

- Fehler bei Anzeige von E-Mails ohne gültigen Absender
- Historienanzeige nach Start des j-lawyer.org Clients leer
- Server und Client bevorzugen IPv4 auf Geräten mit IPv4- und IPv6-Unterstützung

---

## j-lawyer.org 1.8

Akten und Adressen:

- vollständig überarbeitete „Mein Desktop“-Ansicht
- es werden keine archivierten Akten mehr auf „Mein Desktop“ angezeigt
- verbesserte Darstellung von Wiedervorlagen und Fristen
- verbesserte Darstellung von Akten an einer Adresse, inklusive Navigation zur Akte
- Anzeige von Tags alphabetisch sortiert, unabhängig vom Auswahlzustand
- Nutzerdefinierte Aktenzeichen – das Schema für Aktenzeichen kann nun frei gewählt werden

Dokumente:

- direkte Anzeige einiger Dokumentformate (PNG, JPG, TIFF, PDF, …)
- Kopieren von Dokumenten in andere Akten
- verbessertes Handling von Platzhaltern, insbesondere bei leeren Platzhalterwerten
- Dokumente können nun per Drag & Drop hinzugefügt werden

Sonstige Erweiterungen:

- Historie / Timeline analog sozialer Netzwerke
- automatische Layoutanpassung aller Tabellen – in Abhängigkeit vom Inhalt
- Skalierung für Popup-Dialoge werden gespeichert
- Kopierbare Links / URLs
- intelligenteres Handling für Aktenzeichen im Austausch zwischen j-lawyer.org Client und Drebis (z.B. führende Nullen)
- automatische Installer für j-lawyer.org Server und Client, für Windows, Linux und Mac OS X
- weitere Übersetzung des Clients ins Englische
- Login-Dialog gibt Hinweis, wenn versucht wird zum Demosystem zu verbinden
- Dokumenterstellungsdialog: Skalierung / Design verändert
- einige Links im Menü des Clients werden jetzt vom j-lawyer.org Webserver geladen (Forum, Hilfe)
- Sipgate: Unterstützung weiterer Landesvorwahlen (Kuba, Niederlande, Spanien, Uruguay, Russland, Portugal, Italien, Argentinien)
- Migration von JBoss 6 auf Wildfly 9
    - Achtung: im Tab “Verbindung” des “j-lawyer.org Login”-Dialogs sind ab Version 1.8 beide Ports auf den Wert 8080 zu setzen!
- Update einiger Bibliotheken, inklusive Simple ODF, unoconv
    - Achtung: unoconv (zur Konvertierung von Dokumenten, bspw. in PDF) derzeit nur lauffähig mit  32Bit LibreOffice!
    - Achtung: unoconv unter Mac OS X derzeit nicht lauffähig mit LibreOffice 5

Korrekturen:

- alle Plattformen: Update auf die neueste Version der Drebis-Schnittstelle. Dies behebt insbesondere einen Fehler bei der Übermittlung an Versicherungsunternehmen mit spezifischer Geschäftsstelle (VUGS).
- alle Plattformen: Sipgate-Schnittstellenpassungen auf neues Verhalten seitens der Sipgate XML-RPC API
- alle Plattformen: Sipgate-SMS nur noch ohne lokale Absendernummer
- alle Plattformen: Fehlerkorrektur in den Drebis-Wizards, wenn „leere“ Daten aus Kontakten übernommen wurden
- alle Plattformen: Korrektur der Email-Integration für outlook.com und einige andere Mailserver (STARTTLS, IMAP Idle)
- alle Plattformen: Status-Emails mit falschem Absender (Host statt From)
- alle Plattformen: Sortierung Sachgebiete-Dropdown
- Windows: hohe CPU-Last bei aktiven Tags und aktiviertem „allgemeine Daten“-Tab in der Aktenansicht
- Mac OS X: RAM-Überwachung funktioniert nicht
- Mac OS X: Unter bestimmten Bedingungen wurde bei der Datensicherung die MySQL-Datenbank nicht gesichert
- Mac OS X: Überwachung geöffneter Dokumente in LibreOffice teilweise unzuverlässig

---

## j-lawyer.org 1.7.1

Korrekturen:

- Sicherheitsabfrage eingefügt beim Löschen von Dokumenten.
- Die Sachgebiete-Auswahl in der Akte war nicht sortiert.
- Gegenstandswert war falsch formatiert.
- Beim Senden einer E-Mail, wenn die Nachricht als Dokument in die Akte übernommen wird, erschien die Abfrage für den Dokumentnamen hinter der Fortschrittsanzeige und nicht im Vordergrund.
- Fehler behoben beim Löschen mehrerer E-Mails.
- Fehler behoben beim Verschieben von E-Mails in andere Ordner.

Sonstiges:

- Der j-lawyer.org Client enthält nun eine run-mac.sh zum Starten des Clients. Das Aufnehmen von LibreOffice in den Pfad im Rahmen der Installation entfällt.
- Exakte Versionsangabe (Patch Level) im „Über“-Dialog und im Startdialog.

---

## j-lawyer.org 1.7

Akten und Adressen:

- Tagging für Akten und Adressen: es können bestimmte “Markierungen” vordefiniert werden, welche dann an einer Akte oder Adresse aktiviert werden können. In der Suche ist dann eine Einschränkung via Tags möglich.
- Aktenzeichen und Rubrum werden im Kopf aller Aktendialoge angezeigt.
- Fortschrittsanzeige beim Laden von Akten
- Aktensuche voreingestellt nur in nicht archivierten Akten – wenn alle Akten durchsucht werden sollen, muss die Option „Archivsuche“ aktiviert sein
- Es gibt nun eine Anzahl eigener Datenfelder an Adressen und Akten, inklusive automatischer Übernahme dieser Daten in Dokumente.
- An Adressen können nun auch Geburtsdatum und Titel erfasst werden.
- Vorhandene Adressdaten können in j-lawyer.org importiert werden (vCard-Format).
- Es können manuell Einträge in der (automatisch geführten) Aktenhistorie angelegt werden.
- Es gibt nun eine klare Unterscheidung zwischen Wiedervorlagen und Fristen.
- Beim Duplizieren von Wiedervorlagen oder Fristen gibt es nun eine 3-Monats-Übersicht zur Datumsauswahl.
- Unterstützung für Feiertage in Holland / Niederlande und Belgien

E-Mail – Integration:

- Unterstützung für E-Mails via SSL.
- E-Mails können nach dem Senden automatisch in die Akte übernommen werden.
- E-Mails können ohne Anhängen in die Akte übernommen werden – hilfreich insbesondere wenn Anhänge grundsätzlich als separate Dokumente in die Akte kopiert werden.
- Es können mehrere Anhänge einer E-Mail mit einem mal in eine Akte übernommen werden.

Dokumente:

- Volltextsuche: j-lawyer.org beinhaltet nun eine vollständige Suchmaschine für Ihre Dokumente.
- Dokumentenvorschau: Textinhalte von Dokumenten werden in einem Vorschaufenster angezeigt. So kann man schnell Inhalte erfassen ohne das Dokument öffnen zu müssen.
- Unterstützung für .ods-Vorlagen (Tabellenkalkulation)
- Das Vorlagenpaket wurde überarbeitet/erweitert.
- Direktes Drucken: ein oder mehrere Dokumente können per Rechtsklick direkt gedruckt werden, ohne die Dokumente zu öffnen.
- Es kann zu jedem Dateityp das zu verwendende Programm konfiguriert werden.
- Beim Erstellen von Dokumenten kann optional eine Wiedervorlage oder Frist angelegt werden.

Sonstige Erweiterungen:

- j-lawyer.org Projektneuigkeiten können direkt über die Statusleiste angezeigt werden.
- Ad-hoc – Datensicherungen: Backups können per Knopfdruck angefordert werden.
- Nach Datensicherung schickt der j-lawyer.org Server eine Zusammenfassung an die hinterlege E-Mailadreasse des Administrators.
- Der MySQL-Datenbankport ist nun in den Datensicherungseinstellungen konfigurierbar, falls abweichend vom Standard “3306”.
- Das j-lawyer.org – Logo ist in verschieden Größen im Verzeichnis des Clients zu finden und kann bspw. für Verknüpfungen auf dem Desktop verwendet werden.

Korrekturen:

- E-Mails mit leerem Betreff konnten nicht in Akten übernommen werden.
- Beim Übernehmen von E-Mails in die Akte wurde ein Datumssuffix vergeben, der das aktuelle Datum anzeigte. Ab Version 1.7 wird das Empfangsdatum verwendet.
- Die Anzahl paralleler Verbindungen bei E-Mail-Konten via IMAP wurde reduziert – so sollte es nun möglich sein, auch sehr restriktive Maildienstleister zu nutzen.
- Drebis-Freitextnachrichten an Versicherungsunternehmen lassen sich nun auch ohne Versicherungsschein-Nr. übertragen.
- Unter bestimmten Bedingungen wurden bei Drebis Kfz-Schadenmeldungen keine Schadennummer übertragen.
- Laden einer Akte “klemmt” sporadisch – hier konnte keine eindeutige Ursache ausgemacht werden, jedoch wurde das Laden überarbeitet.
- Beim Speichern einer Akte traten Fehler auf, wenn “Anwalt” oder “Sachbearbeiter” mehr als 15 Zeichen umfasste.

---

## j-lawyer.org 1.6

Erweiterungen:

- Kontakt mit zusätzlichen Feldern für Verkehrsrechtsschutz und Kraftfahrtversicherung
- integrierte Drebis-Schnittstelle mit zentralem Posteingang zum Übermitteln von
    - Deckungsanfragen / -erweiterungen
    - Kfz-Schadenmeldungen
    - freier Korrespondenz
- Export von Akten inklusive aller Dokumente und Daten zur Offline-Nutzung auf Notebook, Tablet oder Smartphone
- Aktensuche sucht nun auch in „wegen“
- Aktenvorblatt (Druck) enthält jetzt auch die E-Mailadressen der Beteiligten
- der Client sollte nun auch unter Mac OS X lauffähig sein
- E-Mails werden standardmäßig chronologisch sortiert
- E-Mails und Anhänge werden mit Datumspräfix versehen, wenn sie als Dokument in einer Akte gespeichert werden
- Bankenverzeichnis nutzt nun SEPA (Import der BIC statt der Bankleitzahl)
- Darstellung von HTML-E-Mails auch nach Doppelklick im Inhaltsfenster

Korrekturen:

- verbesserte Kompatibilität mit den neueren Versionen von Libre Office
- Posteingang zeigte Fehler bei IMAP-Konten, wenn E-Mails über externes Mailprogramm gelöscht oder verschoben wurden
- im Aktenvorblatt gab es keinen Zeilenumbruch bei langen Notizen (danke an Forennutzer Frank für die Meldung)
- beim Import von Banken- und Ortsverzeichnis gab es unter bestimmten Umständen mit Sonderzeichen unter Windows
- E-Mails und Anhänge mit Sonderzeichen im Betreff oder Dateinamen wurden falsch dargestellt / behandelt

---

## j-lawyer.org 1.5

Erweiterungen:

- Erweiterungen der E-Mail-Integration
    - volle Unterstützung für HTML-formatierte E-Mails (Versand, Vorlagen, etc.)
    - Unterstützung für CC: und BCC:
    - „Weiterleiten“ und „Allen antworten“ fertiggestellt.
    - Dokumente können aus einer Akte heraus automatisch nach PDF konvertiert und als Anhang verschickt werden.
    - HTML-formatierte E-Mails werden erst nach expliziter Bestätigung durch den Nutzer angezeigt (Spamschutz). Der Absender der E-Mail wird dadurch permanent als vertrauenswürdig eingestuft und weitere E-Mails werden sofort dargestellt.
    - In allen Ordnern im Posteingang werden die Empfängerinformationen in der Tabelle dargestellt.
    - E-Mails, die als Dokument in einer Akte abgelegt wurden, können per Rechtsklick in einem externen E-Mail-Programm geöffnet werden (und dort bspw. gedruckt oder anderweitig weiterverarbeitet werden).
    - Fortschrittsanzeigen für umfangreiche Aktionen.
    - Bei IMAP-Konten werden gelöschte E-Mails in den Papierkorb verschoben.
    - Ordner „Papierkorb“ und „Gesendet“ werden automatisch angelegt, sofern noch nicht vorhanden.
    - Möglichkeit, Lesebestätigungen zu beantworten, für E-Mails die sie erhalten.
    - Suche in der Adressdatenbank beim Versenden von E-mails (für An:, CC:, BCC)
- Wiedervorlagen können optional einem Nutzer zugeordnet werden. Wiedervorlagen, für die der angemeldete Nutzer verantwortlich ist, werden auf dem j-lawyer – Desktop gesondert angezeigt.
- Neues Feld für Mobilnummer in der Adressverwaltung, inklusive dazugehörigem Platzhalter zur Verwendung in Vorlagen.
- Das Wiederherstellen von Datensicherungen ist in der Dokumentation beschrieben.
- Dokumentvorlagen (nicht Mastervorlagen) sind jetzt grundsätzlich von allen angemeldeten Benutzern editierbar. Es sind keine Administrationsrechte mehr notwendig.
- Bei den Beteiligten einer Akte wurde der Typ „Gegnervertreter“ in „Dritte“ umbenannt. Die Platzhalter GEGNERVT* wurden in DRITTE* umbenannt. Eine Abwärtskompatibilität ist gewährleistet – keine Ihrer bestehenden Vorlagen muß angepasst werden. Für neue Vorlagen sollten die neuen Platzhalter verwendet werden.
- Beim Verlassen einer Akte oder Adresse erscheint eine Rückfrage, ob gespeichert werden soll – sofern Daten geändert worden sind.
- Das Speichern einer Akte führt nicht mehr zum Zurücksetzen der Dialoginhalte – somit wird ein Zwischenspeichern möglich.
- Voice-over-IP – Funktionalität über eine Sipgate-Integration: (zur Nutzung tragen Sie über die Einstellungen Nutzernamen und Passwort Ihres Sipgate Basic oder Sipgate Plus-Kontos ein)
    - Tätigen von Anrufen aus einer Akte oder Adresse
    - Versenden von SMS aus einer Akte oder Adresse
    - Versenden von Dokumenten als Fax
    - Übersicht zum Status verschickter Faxe
    - erneutes Senden von nicht übertragenen Faxen
    - Speichern von Übertragungsberichten als Dokumente in der Akte

Korrekturen:

- Die maximale Länge für E-Mail-Signaturen wurde erhöht.
- Die maximale Länge für E-Mail-Nutzernamen wurde erhöht.
- Beim Verschieben von E-Mail-Anhängen in eine Akte wird sichergestellt, daß der Dateityp unverändert bleibt.
- Umlaute in Absenderbezeichnungen einer E-Mail werden korrekt dargestellt.
- Sporadisch auftretende Fehler „unable to load body structure“ beim Laden einer E-Mail wurden behoben.
- In der „Tipps des Tages“-Übersicht auf dem j-lawyer – Desktop gab es unter Windows fehlerhafte Anzeigen von Sonderzeichen.
- Das Servermonitoring hat für j-lawyer – Server, die auf Linux laufen, Fehlalarme/falsche Werte bei der Überwachung des Arbeitsspeichers geliefert.

Hinweise:

- Mit Version 1.4 erstellte E-Mail-Signaturen müssen nach dem Update einmalig neu formatiert werden, die diese jetzt grundsätzlich als HTML gespeichert werden.
- Die automatische Konvertierung in PDF (genutzt für E-Mail- und Fax-Funktionalität) ist unter Windows dahingehend beschränkt, daß keine offene LibreOffice / OpenOffice – Anwendung offen sein darf.
- Beim Erstellen von HTML-E-Mail-Vorlagen werden Platzhalter immer am Anfang eingefügt und müssen von Hand an die richtige Stelle kopiert werden. Dies ist eine Limitierung durch eine von j-lawyer verwendete externe Bibliothek. An einer Lösung wird gearbeitet.

---

## j-lawyer.org 1.4

Erweiterungen:

- E-Mail-Integration – dieses Feature ist aufgrund des Umfangs noch nicht abgeschlossen und nicht final getestet – wird daher als „experimentell“ bzw. „beta“ freigegeben. Eventuell auftretende Fehler können im Forum gemeldet werden.
    - Konfiguration der Emailkonten und Signaturen am Nutzer in der Nutzerverwaltung
    - Unterstützung von POP3 und IMAP – IMAP ist die empfohlene und derzeit besser getestete Variante!
    - Empfang von Emails direkt im j-lawyer Client
    - direkter Versand aus der Adressverwaltung
    - direkter Versand aus der Akte: per Rechtsklick auf Beteiligten oder per Rechtsklick auf ein Dokument (um es als Anhang zu verschicken)
    - direkter Versand aus dem Posteingang
    - Empfangsbestätigungen
    - Speichern von Emails als Dokument in der Akte
    - Organisation von Emails in Ordnern, Ordner anlegen/ändern/löschen, Drag&Drop von Emails in Ordner
    - Emailvorlagenverwaltung: analog zu Dokumentvorlagen können Inhalte mit Platzhaltern definiert werden – so wird das Schreiben von Emails auf ein Minimum reduziert
    - Anzeige neuer Emails / ungelesener Emails in der Statuszeile
    - noch NICHT fertig und geplant für 1.5: Emailvorlagen und zu verschickende Emails nur im Textformat – HTML noch nicht umgesetzt, Fortschrittsanzeige beim Emailversand v.a. großer Emails, CC: und BCC:, „Allen Antworten“ und „Weiterleiten“
- Firmenprofil inkl. Dokumentplatzhalter: allgemeine Informationen Ihrer Kanzlei können in einem Profil hinterlegt und über Dokumentplatzhalter verwendet werden. Das ermöglicht die Nutzung allgemeingültiger Vorlagen (da kanzleispezifische Informationen erst bei Dokumenterstellung gefüllt werden) und vermeidet die aufwändige Anpassung aller Vorlagen bspw. wenn sich Adresse oder Kontaktinformationen der Kanzlei ändern.
- Vorlagenpaket: im Downloadbereich gibt es nun fertige Dokument- und Emailvorlagen als Einstiegshilfe.
- Feiertagskalender: In der Nutzerverwaltung kann einmalig angegeben werden, in welchem Land / Bundesland / Kanton sich ein Nutzer befindet – diese Information wird anschließend verwendet um auszuschließen, daß bspw. Wiedervorlagen auf Feiertage oder Wochenenden gelegt werden.
- Dokumente im Scaneingang können bei Zuordnung zu einer Akte direkt umbenannt werden.
- Einstellungen zur Scannerintegration können nun direkt im Client bearbeitet werden, das Bearbeiten von Konfigurationsdateien auf dem Server entfällt. Wurde die Integration in Version 1.3 bereits genutzt, muß das zu überwachende Serververzeichnis einmalig im Client nochmals angegeben werden – siehe dazu Hinweise im Readme des Updatepack-Downloads.
- Tipps des Tages – der j-lawyer Client zeigt mit jedem Start auf „Mein Desktop“ 5 Tipps zur Programmnutzung an (Detailansicht nur nach Klick). Die Tipps werden von j-lawyer.org geladen, sodaß auch über Funktionalität eventuell noch nicht installierter neuer Versionen informiert wird.
- Die Banken- und Postleitzahlenverzeichnisse werden direkt vom j-lawyer Client heruntergeladen. Es entfallen somit zwei separate manuelle Downloads.
- Änderungen an Wiedervorlagen (Neuanlage, Änderung, Löschen) werden nun direkt und automatisch gespeichert – ein explizites Speichern der Akte ist nicht mehr notwendig, wenn lediglich Wiedervorlagen geändert worden sind.
- Dokumente umbenennen per Rechtsklick.
- Sicherheitsabfragen beim Löschen von Adressen oder Akten.
- Der j-lawyer Server kann nun die Überwachung der wichtigsten Systemparameter übernehmen (RAM, Festplatte, CPU, Java-System) und bei potentiellen Problem automatisch eine definierte Emailadresse informieren. Im j-lawyer Client wird über eine Ampel in der Statuszeile der Gesamtzustand angezeigt, oder bei Klick die entsprechenden Details.
- Die automatische Datensicherung kann nun im j-lawyer Client konfiguriert werden: an/aus, an welchen Tagen, Uhrzeit etc.

Korrekturen:

- Mögliche Fehler nach Umsortierung der Spaltenreihenfolgen behoben.
- Die Dokumententabelle in der Akte skalierte nicht automatisch mit der Größe des Fensters / Bildschirms.
- Suchanfragen (Adressen, Akten) die „ß“ enthielten, lieferten eine leere Ergebnismenge.
- Änderungsdatum für Dokumente im Scaneingang wurde unter bestimmten Bedingungen falsch angezeigt.
- Wenn Sie beim Start des j-lawyer Clients eine Fehlermeldung „failed to create session factory“ sehen, folgen Sie den Anweisungen hier.

---

## j-lawyer.org 1.3

Erweiterungen:

- Scanner-Integration: Scans und / oder andere Dokumente lassen sich nun komfortabel und halbautomatisch zu Akten zuordnen – siehe dazu auch den Abschnitt „Dokumente“ in der Dokumentation.
- Es gibt eine Vielzahl an Verbesserungen in der Oberfläche und im Bedienkonzept:
    - alle Dialog haben nun eine Bezeichnung und dazugehörige Icons im Kopfbereich
    - alle Buttons sind nun im Kopfbereich der Dialoge zu finden, sodass die Notwendigkeit zu Scrollen minimiert wird.
    - es werden durchgehend Icons verwendet
    - die Anzeige „heute fällig“ auf „Mein Desktop“ ist jetzt nach Kurzrubrum sortiert
    - es gibt einen neuen ansprechenderen Startbildschirm / Splashscreen
    - in der Statuszeile gibt es grafische Anzeigen für die Anzahl der vorliegenden Scans sowie für evtl. vorliegende Updates
- Das Drucklayout des Aktenblattes wurde verbessert.
- Es gibt einen neuen Platzhalter (bei Dokumenterstellung) für Diktatzeichen.

Korrekturen:

- Die Grenze für die maximale Größe hinzuzufügender Dateien wurde angehoben.
- Beim Duplizieren von Dokumenten wird auf die Übernahme der Dateinamenserweiterung geprüft.
- Fehlerhafte Sortierung in der Dokumenttabelle einer Akte wurde behoben.
- Sporadische Probleme mit dem automatischen Updatecheck unter Linux wurden behoben.
- Beim Erstellen von Dokumenten mit „.“ im Dateinamen (bspw. für Abkürzungen) wird nun keine Warnung mehr ausgegeben weil der Dateityp unbekannt ist.
- In Version 1.2 war ein Login unter bestimmten Bedingungen nur für Nutzer mit Administrationsrechten möglich.

---

## j-lawyer.org 1.2

Erweiterungen:

- beim Bearbeiten einer Akte kann direkt in die Bearbeitung der Kontakte gewechselt (und zurückgewechselt) werden
- jedes Dokument einer Akte hat ein eigenes Diktatzeichen
- zusätzliche Daten an der Akte: „wegen“, „verantwortlicher Anwalt“, „Sachbearbeiter“
- zusätzliche Daten am Nutzer: „ist Anwalt“ ja/nein
- in der Adressverwaltung (Suche) wird im unteren Bereich angezeigt, in welcher Rolle der Kontakt in welchen Akten referenziert ist
- automatische Warnung bei Interessenkonflikten (Kontakt ist sowohl Mandant als auch Gegner, in verschiedenen Akten)
- beim Erstellen eines Dokumentes muss der Beteiligte (Mandant, Gegner, Gegnervertreter) nicht mehr ausgewählt werden – man kann die Auswahl zusätzlich auch direkt im Dokument-erstellen-Dialog vornehmen
- Änderungen am Aktendatenblatt (zusätzliche Daten, Layoutverbesserungen)
- Wiedervorlagen können jetzt dupliziert werden, mit Neuvergabe von Datum und optionalem Anpassen des Wiedervorlagegrundes
- Dokumente können jetzt dupliziert werden, mit Neuvergabe des Dokumentnamens
- „Mein Desktop“ wurde erweitert und bietet nun einen direkten Zugriff auf Akten die eine offene Wiedervorlage am jeweiligen Tag haben
- Wiedervorlagen können in der Akte direkt mit einem Klick erledigt/offen gesetzt werden
- Druckvorschau für Aktendatenblatt inklusive Möglichkeit, als PDF, ODT, XLS, DOC/DOCX, RTF, HTML u.a. zu speichern

Korrekturen:

- Sortierung nach Datum und Aktenzeichen in den Tabellenansichten
- Ausdruck des Aktendatenblattes war nur möglich wenn mindestens eine Wiedervorlage existierte

---

## j-lawyer.org 1.1

Erweiterungen:

- Einfacher Backupautomatismus, der wochentäglich eine Datensicherung anfertigt
- Bei der Datumsauswahl für Wiedervorlagen werden nun immer 3 Monate angezeigt, sodass Blättern minimiert wird
- Automatischer Update-Check: der j-lawyer-Client informiert Sie, sobald neue Programmversionen verfügbar ist
- In einigen Dialogen konnte mit ENTER noch nicht direkt die jeweilige Aktion angestossen werden (es musste mit der Maus der entsprechend Knopf gedrückt werden)
- Beim Erstellen von Dokumenten zu einer Akte kann jetzt innerhalb der Vorlagen gesucht werden (besonders sinnvoll bei einer großen Menge an Vorlagen)

Korrekturen:

- Sortierung nach Datum und Aktenzeichen in den Tabellenansichten teilweise unlogisch
- Öffnen von Dokumenten mit der Standardanwendung auf Linux-Desktops funktionierte unter einigen KDE-Versionen nicht
- Ein aus j-lawyer heraus geöffnetes Office-Dokument wurde nicht im Vordergrund geöffnet und musste explizit fokussiert werden
- Bei der Suche nach Wiedervorlagen anhand eines Datums wurden Zeiten beachtet (was nicht sinnvoll ist)
- Wurde ein Dokument erstellt und sofort danach geöffnet, gab es einen Fehler

---

## j-lawyer.org 1.0

Erweiterungen:

- vereinfachte Installation (es wird kein FTP-Server mehr benötigt)
- Hinzufügen beliebiger vorhandener Dokumente, Entfernen von Dokumenten
- Archivierung von Akten
- verbessertes Handling von .odt-Dokumenten, die durch eine Konvertierung aus Microsoft Word entstanden sind
- verschiedene optische Verbesserungen

Korrekturen:

- Beseitigung eines Problems mit LibreOffice/OpenOffice auf Windows-Systemen, wenn der eingebaute Schnellstarter verwendet wird
- Beseitigung eines Problems in der Nutzerverwaltung mit fehlender Warnung bei zu kurzen Nutzernamen (Danke an Forumsnutzer cjoost für die Meldung)

---

