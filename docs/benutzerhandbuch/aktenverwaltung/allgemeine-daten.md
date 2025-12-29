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

## Akte exportieren {#akte-exportieren}

Die Export-Funktion ermöglicht es, eine Akte als HTML-Paket zu exportieren, das vollständig offline im Browser genutzt werden kann. Dies ist besonders nützlich, um Akteninhalte ohne Zugang zum j-lawyer-Server einzusehen - beispielsweise für externe Besprechungen, Gerichtstermine oder zur Archivierung.

![Abbildung 7](../../images/case-export-html.png)

### Exportvorgang

1. Öffnen Sie die gewünschte Akte
2. Klicken Sie auf das Export-Symbol in der Werkzeugleiste (Tooltip: "gesamte Akte als HTML exportieren")
3. Wählen Sie ein Zielverzeichnis für den Export
4. Der Fortschritt wird während des Exports angezeigt

Nach Abschluss des Exports wird das Ergebnis automatisch im Standard-Browser geöffnet. Das exportierte Verzeichnis enthält alle Dateien und kann auf beliebige Datenträger kopiert oder weitergegeben werden.

### Exportierte Inhalte

Der Export umfasst alle wesentlichen Akteninformationen:

| Bereich | Enthaltene Daten |
|---------|-----------------|
| **Grunddaten** | Aktenzeichen, Kurzrubrum, Grund, Sachgebiet, Anwalt, Sachbearbeiter, Streitwert, Erstellungs- und Änderungsdatum |
| **Beteiligte** | Namen, Beteiligungsart, Adressen, Telefonnummern, Referenzzeichen |
| **Etiketten** | Alle der Akte zugewiesenen Etiketten |
| **Notizen** | Freitext-Notizen zur Akte |
| **Dokumente** | Alle Dokumente mit vollständiger Ordnerstruktur |
| **Kalender** | Wiedervorlagen, Fristen und Termine mit Status |
| **Finanzen** | Belege/Rechnungen und Aktenkonto-Buchungen |
| **Historie** | Vollständiges Änderungsprotokoll |

### Funktionen der exportierten HTML-Seite

Die generierte HTML-Seite bietet eine interaktive Oberfläche mit folgenden Funktionen:

#### Tab-Navigation

Die Inhalte sind in fünf Bereiche gegliedert:

- **Übersicht**: Grunddaten, Beteiligte, Etiketten und Notizen auf einen Blick
- **Dokumente**: Durchsuchbare Dokumentenansicht mit Ordnerstruktur
- **Fälligkeiten**: Wiedervorlagen, Fristen und Termine
- **Finanzen**: Belege und Aktenkonto
- **Aktenhistorie**: Chronologisches Änderungsprotokoll

#### Erscheinungsbild

Über die Schaltfläche in der Kopfzeile kann zwischen einem dunklen und hellen Farbschema gewechselt werden. Die Einstellung wird im Browser gespeichert und bei erneutem Öffnen beibehalten.

#### Dokumenten-Funktionen

Die Dokumentenansicht bietet umfangreiche Möglichkeiten zur Navigation:

- **Suche**: Dokumente können über ein Suchfeld gefiltert werden
- **Sortierung**: Sortierung nach Name, Datum oder Dateigröße (auf- oder absteigend)
- **Ordner auf-/zuklappen**: Alle Ordner können gleichzeitig geöffnet oder geschlossen werden
- **Dateityp-Filter**: Bestimmte Dateitypen (Medien, Bilder, Dokumente, PDF, HTML, EML, BEA, MD) können ausgeblendet werden
- **Direkter Zugriff**: Dokumente können direkt durch Anklicken geöffnet werden

!!! tip "Offline-Nutzung"
    Der Export funktioniert vollständig offline - es ist keine Internetverbindung erforderlich. Alle Dokumente, Stylesheets und Skripte sind im Export-Verzeichnis enthalten.

!!! tip "Alternative: PDF-Export"
    Wenn Sie nur ausgewählte Dokumente als einzelne PDF-Datei benötigen, nutzen Sie die Funktion [Ausgewählte Dokumente als ein PDF exportieren](../dokumentenmanagement/pdf.md#akte-ausgewahlte-dokumente-als-ein-pdf-exportieren).

