# Nutzerverwaltung {#nutzerverwaltung}

Die Nutzerverwaltung ermöglicht das Anlegen, Bearbeiten und Löschen von Benutzerkonten sowie die Konfiguration von Berechtigungen und Integrationen.

Der Dialog ist über das Menü **Einstellungen** → **Nutzerverwaltung** erreichbar.

## Nutzer anlegen und verwalten {#nutzer-anlegen}

Auf der linken Seite des Dialogs befindet sich die Liste aller Nutzer. Über das Textfeld und den Button **Hinzufügen** kann ein neuer Nutzer angelegt werden. Der Nutzername muss eindeutig sein.

Ein Rechtsklick auf einen Nutzer in der Liste öffnet ein Kontextmenü mit folgenden Optionen:

- **Löschen**: Entfernt den Nutzer
- **Passwort ändern**: Setzt ein neues Passwort für den Nutzer

Mit der Option **Nutzer aus externen Systemen anzeigen** können auch Nutzer angezeigt werden, die über externe Authentifizierungssysteme verwaltet werden.

## Stammdaten {#stammdaten}

Im Tab **Stammdaten** werden die persönlichen Daten des Nutzers erfasst:

**Persönliche Angaben:**

- Anzeigename
- Vorname
- Name
- Unternehmen
- Funktion (mehrzeilig)
- Nutzer ist Anwalt (Kennzeichnung)

**Adresse:**

- Straße
- Adresszusatz
- PLZ
- Ort
- Ländercode

**Kontakt und Bankverbindung:**

- E-Mail
- Telefon
- Telefax
- Mobil
- Website
- Bank
- BIC
- IBAN
- Steuernummer
- USt-ID-Nr.

Über den Button **Daten aus Kanzleiprofil übernehmen** können die Unternehmensdaten automatisch aus dem hinterlegten Kanzleiprofil übernommen werden.

## Berechtigungen {#berechtigungen}

Im Tab **Berechtigungen** werden die Zugriffsrechte des Nutzers konfiguriert.

### Allgemein {#berechtigungen-allgemein}

| Berechtigung | Beschreibung |
|--------------|--------------|
| Login | Nutzer darf sich anmelden |
| Datenimport | Nutzer darf Daten importieren |
| Unternehmens-Administrator | Zugriff auf Unternehmenseinstellungen |
| System-Administrator | Voller Zugriff auf Systemeinstellungen |

### Adressen {#berechtigungen-adressen}

| Berechtigung | Beschreibung |
|--------------|--------------|
| einsehen | Adressen lesen |
| ändern | Bestehende Adressen bearbeiten |
| erstellen | Neue Adressen anlegen |
| löschen | Adressen entfernen |

### Akten {#berechtigungen-akten}

| Berechtigung | Beschreibung |
|--------------|--------------|
| einsehen | Akten lesen |
| ändern | Bestehende Akten bearbeiten |
| erstellen | Neue Akten anlegen |
| löschen | Akten entfernen |

### Einstellungen {#berechtigungen-einstellungen}

| Berechtigung | Beschreibung |
|--------------|--------------|
| ändern | Einstellungen bearbeiten |
| erstellen | Neue Einstellungen anlegen |
| löschen | Einstellungen entfernen |

### Auswertungen {#berechtigungen-auswertungen}

| Berechtigung | Beschreibung |
|--------------|--------------|
| allgemeine | Zugriff auf allgemeine Auswertungen |
| vertrauliche | Zugriff auf vertrauliche Auswertungen |

### Weitere Optionen {#berechtigungen-weitere}

- **Dokumente bei Bearbeitung automatisch sperren**: Verhindert gleichzeitige Bearbeitung von Dokumenten durch mehrere Nutzer

## Kalender {#kalender}

Im Tab **Kalender** wird konfiguriert:

- **Land**: Auswahl des Landes für Feiertage
- **Besondere Feiertagsregelungen**: Regionale Feiertagsregelungen (z.B. Bundesland)
- **Zugriff auf Kalender**: Auswahl der Kalender, auf die der Nutzer Zugriff hat

## E-Mail {#email}

Im Tab **E-Mail** wird festgelegt, auf welche E-Mail-Postfächer der Nutzer zugreifen darf. Die verfügbaren Postfächer werden in einer Liste angezeigt und können einzeln aktiviert oder deaktiviert werden.

Bevor Postfächer zugewiesen werden können, müssen diese zunächst angelegt werden. Die Einrichtung von E-Mail-Postfächern wird unter [E-Mail](email.md) beschrieben.

## beA {#bea}

Im Tab **beA** (besonderes elektronisches Anwaltspostfach) werden die beA-Zugangsdaten konfiguriert:

- **Zertifikat**: Upload des beA-Zertifikats
- **Passwort**: Passwort für das Zertifikat
- **Anmeldemodus**:
  - Automatisch mit Zertifikat anmelden
  - Manueller Login mit Zertifikat oder Kartenleser

Eine ausführliche Anleitung zur Einrichtung finden Sie unter [beA - Inbetriebnahme in j-lawyer.org](addon-bea.md#inbetriebnahme).

## Nextcloud {#nextcloud}

Im Tab **Nextcloud** können die Zugangsdaten für die Nextcloud-Integration des Nutzers hinterlegt werden.

## Sipgate / E-POST {#sipgate-epost}

Im Tab **Sipgate / E-POST** werden die Zugangsdaten für die Telefonie-Integration (Sipgate) und den E-POST-Dienst konfiguriert.

## Kürzel und Gruppen {#kuerzel-gruppen}

Im Tab **Kürzel und Gruppen** wird die Zugehörigkeit des Nutzers zu Gruppen verwaltet:

- **Primäre Gruppe**: Die Hauptgruppe des Nutzers
- **Gruppenmitgliedschaften**: Auswahl aller Gruppen, denen der Nutzer angehört

Gruppen werden verwendet, um Berechtigungen auf Aktenebene zu steuern und den Zugriff auf bestimmte Akten einzuschränken.

## Belege {#belege}

Im Tab **Belege** wird der Zugriff auf Rechnungs-Nummernkreise konfiguriert. Der Nutzer kann nur Belege aus den ihm zugewiesenen Nummernkreisen erstellen.
