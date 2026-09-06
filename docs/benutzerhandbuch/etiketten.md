# Etiketten {#etiketten}

Etiketten sind eine Art digitale Haftnotiz: Sie lassen sich per Klick an Akten, Dokumente und Adressen anheften, wieder abnehmen und als Filter verwenden. Damit lassen sich Arbeitsvorgänge abbilden, ohne die eigentlichen Stammdaten zu verändern – etwa ein Etikett „unbearbeiteter Posteingang", das nach der Bearbeitung wieder entfernt wird.

## Etiketten im Überblick {#etiketten-ueberblick}

Es gibt drei voneinander unabhängige Etikettenarten. Jede hat einen eigenen Vorrat an Etiketten und wird an einer eigenen Stelle konfiguriert:

| Etikettenart | Wird gesetzt in | Wird konfiguriert unter |
|--------------|-----------------|-------------------------|
| **Akten-Etiketten** | Akte, Tab „Allgemeine Daten", Bereich „Akten-Etiketten" | **Einstellungen** → **Akten** → **Akten-Etiketten** |
| **Dokument-Etiketten** | Akte, Tab „Dokumente", Bereich „Dokument-Etiketten" | **Einstellungen** → **Dokumente** → **Etiketten konfigurieren** |
| **Adress-Etiketten** | Adresse, Bereich „Etiketten" | **Einstellungen** → **Adressen** → **Adress-Etiketten** |

Unabhängig von der Etikettenart gibt es zwei Bauformen:

- **Ja/Nein-Etiketten** sind Umschaltknöpfe. Sie sind entweder gesetzt oder nicht gesetzt. Ein gesetztes Etikett wird grün dargestellt, ein nicht gesetztes grau. Die Farben sind fest vorgegeben und nicht konfigurierbar.
- **Listenetiketten** sind Auswahlfelder. Sie tragen zusätzlich zum Namen genau einen Wert aus einer vorgegebenen Werteliste – zum Beispiel das Etikett „Priorität" mit den Werten „hoch", „mittel" und „niedrig".

Listenetiketten werden immer vor den Ja/Nein-Etiketten dargestellt, innerhalb der beiden Gruppen alphabetisch.

## Etiketten setzen und entfernen {#etiketten-setzen}

Ein Klick auf ein Ja/Nein-Etikett aktiviert es, ein erneuter Klick deaktiviert es. Bei Listenetiketten wird der gewünschte Wert im Auswahlfeld gewählt; der leere erste Eintrag bedeutet „Etikett nicht gesetzt". Die Änderung wird sofort gespeichert.

Ein Verweilen mit der Maus über einem gesetzten Ja/Nein-Etikett zeigt an, seit wann es gesetzt ist (zum Beispiel „aktiv seit 06.09.2026, 14:32:10"). Der Nutzer, der das Etikett gesetzt hat, wird nicht angezeigt.

### An einer Akte {#etiketten-akte}

Die Akten-Etiketten befinden sich im Tab „Allgemeine Daten" im Bereich **Akten-Etiketten**.

!!! info "Hinweis"
    Ist die Akte noch nicht gespeichert, erscheint die Rückfrage „Bevor Etiketten aktiviert werden können, muss die Akte gespeichert werden. Jetzt speichern?". Bei archivierten Akten und in Akten, auf die nur lesender Zugriff besteht, sind die Etiketten deaktiviert.

### An einem Dokument {#etiketten-dokument}

Die Dokument-Etiketten befinden sich im Tab „Dokumente" im Bereich **Dokument-Etiketten** und beziehen sich auf das in der Dokumentenliste ausgewählte Dokument.

Es können auch **mehrere Dokumente gleichzeitig** ausgewählt und gemeinsam etikettiert werden. Die Etikettenknöpfe zeigen dann drei Zustände:

| Darstellung | Bedeutung |
|-------------|-----------|
| gesetzt | Das Etikett ist an allen ausgewählten Dokumenten vergeben („aktiv in allen ausgewählten Dokumenten") |
| nicht gesetzt | Das Etikett ist an keinem der ausgewählten Dokumente vergeben („nicht vergeben in der Auswahl") |
| fett und kursiv | Das Etikett ist nur an einem Teil der Auswahl vergeben. Der Tooltip nennt die Anzahl („teilweise vergeben (3/7)") und listet die betroffenen Dokumente auf |

### An einer Adresse {#etiketten-adresse}

In der Adresse befinden sich die Etiketten im Bereich **Etiketten**. Auch hier gilt: Ist die Adresse noch nicht gespeichert, wird vor dem Setzen eines Etiketts zum Speichern aufgefordert.

## Listenetiketten {#listenetiketten}

Ein Listenetikett verbindet einen Etikettennamen mit einer festen Werteliste. Statt vieler einzelner Ja/Nein-Etiketten („Priorität hoch", „Priorität mittel", „Priorität niedrig") gibt es ein Etikett „Priorität" mit drei zulässigen Werten. Pro Objekt kann genau ein Wert gesetzt sein.

In Filterlisten erscheint ein Listenetikett mit einer Zeile je Wert im Format `Name: Wert`, also zum Beispiel „Priorität: hoch". So lässt sich gezielt nach einem einzelnen Wert filtern.

## Etiketten konfigurieren {#etiketten-konfigurieren}

Bevor ein Etikett an einer Akte, einem Dokument oder einer Adresse gesetzt werden kann, muss es einmalig angelegt werden.

### Ja/Nein-Etiketten anlegen {#etiketten-anlegen}

Die Dialoge für Akten-, Dokument- und Adress-Etiketten sind identisch aufgebaut:

- Neuen Etikettennamen in das Textfeld eingeben und **Hinzufügen** wählen (die Eingabetaste bewirkt dasselbe).
- Rechtsklick auf einen vorhandenen Eintrag öffnet ein Kontextmenü mit **Bearbeiten** (umbenennen) und **Löschen**.
- Über **Schliessen** wird der Dialog verlassen.

Die Liste wird immer alphabetisch sortiert; eine eigene Reihenfolge lässt sich nicht festlegen. Eine Farbwahl je Etikett gibt es nicht.

### Listenetiketten anlegen {#listenetiketten-anlegen}

Listenetiketten werden in einem eigenen, zweispaltigen Dialog gepflegt:

| Menüpunkt | Öffnet |
|-----------|--------|
| **Einstellungen** → **Akten** → **Akten-Listenetiketten** | Listenetiketten für Akten |
| **Einstellungen** → **Dokumente** → **Listenetiketten konfigurieren** | Listenetiketten für Dokumente |
| **Einstellungen** → **Adressen** → **Adress-Listenetiketten** | Listenetiketten für Adressen |

Links werden die Etikettennamen gepflegt, rechts die Werte des links markierten Etiketts. Die rechte Seite ist so lange gesperrt, bis links ein Etikett ausgewählt wurde. Beide Listen bieten per Rechtsklick **Umbenennen** und **Löschen**.

!!! warning "Wichtig"
    Ein neu angelegter Etikettenname wird erst dann dauerhaft gespeichert, wenn ihm der **erste Wert** hinzugefügt wurde. Ein Listenetikett ohne Werte ist nach dem Schließen des Dialogs wieder verschwunden.

Für Namen und Werte gelten zwei Einschränkungen:

- Sie dürfen **keinen Doppelpunkt, kein Gleichheitszeichen und kein Komma** enthalten.
- Ja/Nein-Etiketten und Listenetiketten teilen sich einen gemeinsamen Namensraum. Ein Name kann nicht doppelt vergeben werden.

### Umbenennen und Löschen {#etiketten-umbenennen}

Beim Umbenennen eines Etiketts erscheint die Rückfrage, ob vorhandene Etiketten an den bereits damit versehenen Akten, Dokumenten beziehungsweise Adressen ebenfalls umbenannt werden sollen.

!!! warning "Wichtig"
    Wird diese Rückfrage mit **Nein** beantwortet, bleibt das alte Etikett an den bestehenden Objekten stehen – obwohl es in der Konfiguration nicht mehr existiert. In aller Regel ist **Ja** die richtige Antwort.

Beim Löschen verhalten sich die beiden Bauformen unterschiedlich:

- Das Löschen eines **Ja/Nein-Etiketts** entfernt es nur aus der Konfiguration. An bereits etikettierten Objekten bleibt es bestehen und taucht in Filterlisten weiterhin auf.
- Beim Löschen eines **Listenetiketts** oder eines einzelnen Werts wird ausdrücklich gefragt, ob die vorhandenen Etiketten an den Objekten ebenfalls entfernt werden sollen.

### Berechtigungen {#etiketten-berechtigungen}

| Aktion | Erforderliche Berechtigung |
|--------|----------------------------|
| Etiketten an einer Akte oder einem Dokument setzen | Schreibrecht für Akten |
| Etiketten an einer Adresse setzen | Schreibrecht für Adressen |
| Etiketten anlegen, umbenennen, löschen | Rechte „erstellen", „ändern" und „löschen" im Bereich **Einstellungen** der [Nutzerverwaltung](nutzerverwaltung.md#berechtigungen-einstellungen) |
| Listenetiketten umbenennen oder löschen inklusive Nachziehen an bestehenden Objekten | Unternehmens-Administrator |
| [Etiketten-Automatik](#etiketten-automatik) konfigurieren | Unternehmens-Administrator |

## Mit Etiketten arbeiten {#etiketten-arbeiten}

### Etiketten abonnieren {#etiketten-abonnieren}

Der Desktop-Bereich [„Nach Etikett"](oberflaeche.md#nach-etikett) zeigt genau die Akten und Dokumente, die mit den von Ihnen abonnierten Etiketten versehen sind. So bleibt ein Arbeitsvorrat dauerhaft im Blick.

Abonniert wird über die beiden Etiketten-Schaltflächen in der Kopfleiste des Bereichs:

- **Akten-Etiketten** – öffnet eine Liste mit Ankreuzfeldern für alle Akten-Etiketten
- **Dokument-Etiketten** – öffnet dieselbe Liste für Dokument-Etiketten

Angeboten werden alle konfigurierten Etiketten sowie zusätzlich alle Etiketten, die tatsächlich in Verwendung sind. Für jedes abonnierte Etikett entsteht am unteren Rand des Bereichs ein eigener Tab; der Tab „alle" zeigt alle Einträge zusammen.

!!! info "Hinweis"
    Das Abonnement ist **pro Nutzer** gespeichert und wird sofort übernommen. Solange kein Etikett abonniert ist, bleibt der Bereich leer.

### Nach Etiketten suchen und filtern {#etiketten-filtern}

- In der **Aktensuche** lässt sich die Trefferliste über Akten-Etiketten und über Dokument-Etiketten einschränken. Der Etikettenfilter wird mit der Textsuche UND-verknüpft.
- In der **Adresssuche** lässt sich analog über Adress-Etiketten filtern.
- In der Trefferliste zeigt die Spalte **Etiketten** die gesetzten Etiketten je Treffer.
- Innerhalb einer Akte kann die Dokumentenliste über Dokument-Etiketten gefiltert werden.

## Etiketten-Automatik {#etiketten-automatik}

Die Etiketten-Automatik vergibt **Dokument-Etiketten automatisch anhand des Dateinamens**. Damit lässt sich eingehende Post ohne manuellen Aufwand vorsortieren: Sobald ein Dokument in eine Akte gelangt, prüft der Server eine Liste von Regeln und setzt die passenden Etiketten.

Der Dialog wird über **Einstellungen** → **Dokumente** → **Etiketten-Automatik** geöffnet. Links werden die Regeln verwaltet, rechts wird die markierte Regel konfiguriert.

!!! warning "Nur für Administratoren"
    Der Dialog steht ausschließlich Unternehmens-Administratoren offen. Die angelegten Regeln gelten systemweit für alle Nutzer.

### Wann Regeln ausgeführt werden {#automatik-ausloeser}

Die Regeln werden serverseitig ausgewertet, sobald ein Dokument

- **zu einer Akte hinzugefügt** wird – unabhängig vom Weg: Drag & Drop, [Scanner-Eingang](dokumentenmanagement/scanner.md), [E-Mail-Veraktung](email.md), [beA](addon-bea.md), Telefonnotizen, PDF-Konvertierung oder [Schnittstellen](schnittstellen.md),
- **aus einer Vorlage erstellt** wird,
- **umbenannt** wird.

Nicht ausgelöst wird die Automatik beim Wiederherstellen eines Dokuments aus dem [Papierkorb](dokumentenmanagement/papierkorb.md), bei der Aktenanlage und beim Speichern einer neuen Version eines bereits vorhandenen Dokuments.

!!! info "Hinweis"
    Regeln wirken nur ab dem Zeitpunkt ihrer Anlage. Bereits vorhandene Dokumente werden nicht nachträglich etikettiert.

!!! warning "Umbenennen entfernt keine Etiketten"
    Beim Umbenennen werden die Regeln erneut gegen den **neuen** Dateinamen geprüft und passende Etiketten **hinzugefügt**. Bereits gesetzte Etiketten bleiben dabei erhalten. Wird ein Dokument von `Klage.pdf` in `Urteil.pdf` umbenannt, trägt es anschließend die Etiketten beider Regeln.

### Eine Regel anlegen {#automatik-regel-anlegen}

1. Über der Regelliste die Schaltfläche **+** wählen.
2. Im Dialog „Neue Regel für automatische Etikettierung" einen **Regelnamen** eingeben.
3. Rechts unter **Regel - Konfiguration** die Felder ausfüllen und mindestens eine [Bedingung](#automatik-bedingungen) anlegen.
4. Mit **Übernehmen** speichern.

| Feld | Beschreibung |
|------|--------------|
| **Name** | Bezeichnung der Regel; erscheint in der Spalte „Name" der Regelliste |
| **Etiketten (kommasepariert, Listenetiketten: Name=Wert)** | Die zu setzenden Dokument-Etiketten, zum Beispiel `Posteingang, Priorität=hoch` |
| **Ausführen wenn** | `eine Bedingung erfüllt ist` (ODER-Verknüpfung, Voreinstellung) oder `alle Bedingungen erfüllt sind` (UND-Verknüpfung) |
| **bei Treffer keine weitere Regel anwenden** | Beendet die Prüfung nach dem ersten Treffer (voreingestellt aktiv) |

!!! warning "Wichtig"
    Nur **Übernehmen** speichert die Regel. Wird der Dialog mit **Schliessen** verlassen, ohne vorher zu übernehmen, gehen die Änderungen verloren. Das Löschen einer Regel erfolgt ohne Sicherheitsabfrage.

Zum Feld **Etiketten**: Mehrere Etiketten werden durch Komma getrennt. Bei einem Listenetikett wird der Wert mit einem Gleichheitszeichen angehängt (`Bearbeitungsstand=neu`).

!!! warning "Etikettennamen werden nicht geprüft"
    Ja/Nein-Etiketten werden nicht gegen die [konfigurierten Etiketten](#etiketten-anlegen) abgeglichen. Ein Tippfehler erzeugt stillschweigend ein neues, nirgends konfiguriertes Etikett. Bei Listenetiketten verweigert der Dialog das Speichern, wenn der Wert fehlt: „'Priorität' ist ein Listenetikett. Bitte einen Wert angeben (z.B. Priorität=Wert)."

### Bedingungen {#automatik-bedingungen}

Jede Bedingung besteht aus dem festen Feld **Dateiname**, einem Operator und einem Vergleichswert. Über **+** wird eine weitere Bedingung hinzugefügt, das Papierkorb-Symbol entfernt eine Zeile.

| Operator | Bedeutung |
|----------|-----------|
| **ist** | Der Dateiname stimmt exakt mit dem Vergleichswert überein |
| **ist nicht** | Der Dateiname stimmt nicht mit dem Vergleichswert überein |
| **enthält** | Der Dateiname enthält den Vergleichswert (Voreinstellung) |
| **enthält nicht** | Der Dateiname enthält den Vergleichswert nicht |

Groß- und Kleinschreibung wird ignoriert. Verglichen wird der vollständige Dateiname einschließlich Dateiendung.

!!! info "Hinweis"
    Bedingungszeilen ohne Vergleichswert werden beim Speichern verworfen. Eine Regel ohne Bedingung oder ohne Etikett wird zur Laufzeit übersprungen.

### Reihenfolge und Abbruch {#automatik-reihenfolge}

Die Regeln werden in der Reihenfolge der Regelliste von oben nach unten abgearbeitet. Mit den Pfeiltasten neben der Liste lässt sich eine Regel nach oben oder unten verschieben.

Ist bei einer zutreffenden Regel die Option **bei Treffer keine weitere Regel anwenden** gesetzt, endet die Prüfung an dieser Stelle – nachfolgende Regeln werden nicht mehr betrachtet.

- Für sich **gegenseitig ausschließende Kategorien** die Option aktiviert lassen und die spezifischste Regel nach oben stellen.
- Sollen **mehrere unabhängige Etiketten** gesetzt werden, die Option in den betroffenen Regeln abwählen.

### Anwendungsszenarien {#automatik-szenarien}

**Posteingang sichtbar machen.** Eine Regel „Posteingang" mit der Bedingung `Dateiname enthält scan` setzt das Etikett `unbearbeiteter Posteingang`. Wird dieses Etikett auf dem Desktop [abonniert](#etiketten-abonnieren), steht der Arbeitsvorrat aus dem Scan-Eingang an zentraler Stelle zur Verfügung und verschwindet dort, sobald das Etikett nach der Bearbeitung entfernt wird.

**Fristsachen erkennen.** Eine Regel mit ODER-Verknüpfung und den Bedingungen `enthält Klage`, `enthält Mahnbescheid` und `enthält Vollstreckung` setzt das Etikett `Fristsache`. Die Regel gehört mit aktiviertem Abbruch an den Anfang der Liste.

**Buchhaltung vorsortieren.** `enthält Rechnung` ODER `enthält RE-` setzt das Etikett `Buchhaltung`.

**Bearbeitungsstand vorbelegen.** Ein Listenetikett `Bearbeitungsstand` mit dem Wert `neu` wird über die Angabe `Bearbeitungsstand=neu` im Etikettenfeld gesetzt.

**Eigene Entwürfe ausnehmen.** Eine UND-verknüpfte Regel mit `enthält Schriftsatz` und `enthält nicht Entwurf` etikettiert nur die fertigen Schriftsätze.

!!! tip "Tipp"
    Die Automatik ist umso wirksamer, je verlässlicher die Dateinamen benannt sind. Über die [Dateinamen-Konfiguration](dokumentenmanagement/dateinamen.md) und die Benennungsregeln des [Scan-Eingangs](dokumentenmanagement/scanner.md) lassen sich Dateinamen gezielt so gestalten, dass Regeln daran andocken können.

### Grenzen der Etiketten-Automatik {#automatik-grenzen}

- Geprüft wird **ausschließlich der Dateiname**. Dokumentinhalt, Absender, Dateityp, Dokumentordner, Aktendaten und Herkunft (Scan, E-Mail, beA) können nicht ausgewertet werden.
- Regeln können Etiketten nur **setzen**, niemals entfernen.
- Es werden ausschließlich **Dokument-Etiketten** gesetzt – keine Akten- und keine Adress-Etiketten.
- Andere Aktionen wie das Anlegen einer Wiedervorlage, eine Benachrichtigung, das Verschieben in einen Dokumentordner oder eine Änderung des Aktenstatus sind nicht möglich.
- Regeln gelten systemweit; eine Einschränkung auf einzelne Nutzer, Sachgebiete oder Akten ist nicht vorgesehen.

!!! tip "Tipp"
    Bei der UND-Verknüpfung müssen alle Bedingungen einen Vergleichswert enthalten. Eine Bedingungszeile mit leerem Wert führt dazu, dass die Regel nie zutrifft.

## Weitere automatische Etikettierungen {#etiketten-weitere-automatik}

Die Etiketten-Automatik ist nicht die einzige Stelle, an der Etiketten ohne manuelles Zutun gesetzt werden:

| Quelle | Beschreibung |
|--------|--------------|
| [Postfach-Automation](email.md) | Je Postfach kann ein Etikett hinterlegt werden, das bei der automatischen Veraktung gesetzt wird – **zusätzlich** zu den Etiketten aus der Etiketten-Automatik |
| [beA](addon-bea.md) | Beim Speichern einer beA-Nachricht zur Akte kann optional ein Dokument-Etikett vergeben werden |
| [Kontoauszugimport](kontoauszugimport.md) | Setzt Akten-Etiketten anhand des Zahlungsabgleichs |
| [KI-Agenten](ki-assistent/agenten.md#tools-etiketten) | Können Akten- und Dokument-Etiketten lesen und setzen |
| [Dokumentvorlagen](dokumentenmanagement/vorlagen.md) | Die Funktion `WENNETIKETT` wertet Etiketten beim Erzeugen von Dokumenten aus |
| [Schnittstellen](schnittstellen.md) | Die Webhooks `CASETAG_CHANGED`, `DOCUMENTTAG_CHANGED` und `ADDRESSTAG_CHANGED` melden Etikettenänderungen an externe Systeme |
