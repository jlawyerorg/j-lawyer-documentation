# Allgemeine Daten {#allgemeine-daten}

Der Tab "Allgemeine Daten" enthält die grundlegenden Informationen einer Akte.

## Aktenkopf

Im oberen Bereich "Aktenkopf" werden die Stammdaten der Akte gepflegt:

| Feld | Beschreibung |
|------|--------------|
| **Aktenzeichen** | Wird automatisch vergeben, kann aber auch manuell eingegeben werden |
| **Kurzrubrum** | Kurze Bezeichnung der Akte (z.B. "Müller ./. Schmidt") |
| **wegen** | Gegenstand des Mandats |
| **Sachgebiet** | Rechtsgebiet der Akte |
| **Anwalt** | Zuständiger Anwalt / Eigentümer der Akte |
| **Sachbearbeiter** | Zuständiger Sachbearbeiter |

## Etiketten

Im mittleren Bereich können Etiketten aktiviert werden. Etiketten dienen der Kategorisierung und ermöglichen ein schnelles Filtern von Akten.

### Etiketten verwenden

- Klicken Sie auf ein Etikett, um es zu aktivieren (farbig hinterlegt)
- Klicken Sie erneut, um es zu deaktivieren
- In der Aktensuche können Sie nach Etiketten filtern

### Etiketten verwalten

Neue Etiketten können über **Einstellungen** → **Modul 'Akten'** → **Etiketten** erstellt werden.

## Notizen

Im unteren Bereich können freie Notizen zur Akte eingetragen werden. Diese sind nur innerhalb der Akte sichtbar und dienen der internen Dokumentation.

## Aktenablage / Archivierung {#archivierung}

Im Tab "Allgemeine Daten" kann eine Archivierung durchgeführt werden. Die Akte ist somit aus dem "aktiven" Datenbestand heraus – sie ist dann in Suchdialogen nur dann auffindbar, wenn explizit eine Suche im Archiv aktiviert wird.

### Prüfungen vor der Archivierung

Beim Archivieren einer Akte werden automatisch verschiedene Prüfungen durchgeführt, um sicherzustellen, dass keine offenen Vorgänge übersehen werden. Der Archivierungsdialog zeigt den Status jeder Prüfung an:

| Prüfung | Beschreibung | Mögliche Aktion |
|---------|--------------|-----------------|
| **Offene Kalendereinträge** | Prüft, ob noch unerledigte Termine, Wiedervorlagen oder Fristen zur Akte existieren | Einträge können direkt als erledigt markiert werden |
| **Offene Belege** | Prüft, ob Rechnungen in der Offene-Posten-Liste existieren, die weder bezahlt noch storniert sind | Kann ignoriert werden |
| **Offene Zahlungen** | Prüft, ob ausgehende Zahlungen existieren, die weder ausgeführt noch storniert sind | Kann ignoriert werden |
| **Offene Zeiterfassungsprojekte** | Prüft, ob aktive Zeiterfassungsprojekte zur Akte existieren | Projekte können direkt abgeschlossen werden |
| **Fremdgelder nicht ausgeglichen** | Prüft, ob das Fremdgeldkonto einen Saldo ungleich Null aufweist | Kann ignoriert werden |
| **Auslagen nicht ausgeglichen** | Prüft, ob das Auslagenkonto einen Saldo ungleich Null aufweist | Kann ignoriert werden |
| **Unerledigte Nachrichten** | Prüft, ob Nachrichten mit offenen Erwähnungen (@-Mentions) existieren | Erwähnungen können als erledigt markiert werden |

Jede Prüfung wird mit einem Symbol gekennzeichnet:

- **Grün (✓)**: Prüfung bestanden, keine Aktion erforderlich
- **Rot (✗)**: Offene Punkte vorhanden, Handlungsbedarf

!!! tip "Empfehlung"
    Es wird empfohlen, alle Prüfungen zu bestehen, bevor eine Akte archiviert wird. So ist sichergestellt, dass keine offenen Vorgänge übersehen werden. Die Archivierung ist jedoch auch möglich, wenn einzelne Prüfungen nicht bestanden sind.

### Archivnummern für Papierakten

Werden zusätzlich noch Papierakten geführt, so kann über ein Plugin eine neue Archivnummer generiert werden:

1. Öffnen Sie das Menü **Berechnungen** → **Archivnummern-Generator**
2. Die Nummer wird erstellt
3. Kopieren Sie die Nummer in das Notizfeld oder in eines der "Eigenen Felder"

So ist eine konsistente Nummerierung gewährleistet.

## Zugriff auf Akten beschränken {#berechtigungen}

Der Zugriff auf Akten kann auf bestimmte Personenkreise (Gruppen) beschränkt werden. Voraussetzung ist das Vorhandensein von Gruppen (**Einstellungen** → **Gruppen**) sowie die Aufnahme von Nutzern in Gruppen (**Einstellungen** → **Nutzer** → Tab "Kürzel und Gruppen").

### Eigentümer

Als Eigentümer gelten der unter "Anwalt" geführte Nutzer, sowie alle Mitglieder der Eigentümergruppe.

Nur die Eigentümer sind berechtigt:

- Weitere Gruppen über den Tab "Berechtigte" hinzuzufügen
- Gruppen vom Zugriff auszuschließen
- Die Eigentümergruppe zu ändern (nur auf eine Gruppe, in welcher der aktuelle Nutzer auch Mitglied ist)

![Abbildung 5](../../images/j-lawyer-org-UserGuide-de-011.png)

### Berechtigte

Im Tab "Berechtigte" werden alle Gruppen aktiviert, welche Zugriff auf die Akte haben sollen:

- Wird **KEINE** Gruppe gewählt, so ist der Zugriffsschutz für die Akte deaktiviert, es haben alle Nutzer Zugriff!
- Wird mindestens eine Gruppe gewählt, so haben nur solche Nutzer Zugriff auf die Akte, die in mindestens einer der ausgewählten Gruppen Mitglied sind.

!!! info "Berechtigungen vs. Sichtbarkeit"
    Die Angabe berechtigter Gruppen bestimmt ausschließlich die Sichtbarkeit / Zugriffsmöglichkeit auf eine Akte. Welche Aktionen innerhalb der Akte möglich sind, leitet sich aus den Berechtigungen des Nutzers in der Nutzerverwaltung ab.

![Abbildung 6](../../images/j-lawyer-org-UserGuide-de-012.png)
