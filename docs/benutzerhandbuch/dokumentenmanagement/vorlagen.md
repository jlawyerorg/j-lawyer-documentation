# Dokumentvorlagen {#vorlagen}

Unterstützt werden Vorlagen in den folgenden Formaten:

- ODT (LibreOffice-Textverarbeitung)
- ODS (LibreOffice-Tabellenkalkulation) – jedoch ohne Verwendung von Scripts
- DOCX (Microsoft Office-Textverarbeitung)
- XLSX (Microsoft Office-Tabellenkalkulation) – jedoch ohne Verwendung von Scripts
- PDF – PDF-Dateien, die Formulare enthalten; jedoch ohne Verwendung von Scripts

## Platzhalter {#platzhalter}

Folgende Platzhalterinhalte einer Dokumentvorlage werden beim Erstellen eines neuen Dokumentes aus einer Akte heraus automatisch mit Werten befüllt. Der Beteiligte / die Beteiligten in der Akte, deren Daten in das Dokument übernommen werden sollen, können entweder vorher markiert oder direkt im Dokument-erstellen-Dialog gewählt werden.

### Platzhalter für das Kanzleiprofil

| Platzhalter | Beschreibung |
|-------------|--------------|
| `{{PROFIL_FIRMA}}` | Firmenbezeichnung |
| `{{PROFIL_STRASSE}}` | Strasse |
| `{{PROFIL_STRASSE2}}` | Adresszusatz |
| `{{PROFIL_PLZ}}` | Postleitzahl |
| `{{PROFIL_ORT}}` | Ort |
| `{{PROFIL_LAND}}` | Land |
| `{{PROFIL_TEL}}` | Telefonnummer |
| `{{PROFIL_FAX}}` | Faxnummer |
| `{{PROFIL_MOBIL}}` | Mobilnummer |
| `{{PROFIL_EMAIL}}` | E-Mailadresse |
| `{{PROFIL_WWW}}` | Internetadresse |
| `{{PROFIL_STNR}}` | Steuernummer |
| `{{PROFIL_USTIDNR}}` | USt-IdNr. |
| `{{PROFIL_BANK}}` | Bank |
| `{{PROFIL_KONTONR}}` | Kontonummer |
| `{{PROFIL_BLZ}}` | Bankleitzahl |
| `{{PROFIL_BANK_AK}}` | Bank (Anderkonto) |
| `{{PROFIL_KONTONR_AK}}` | Kontonummer (Anderkonto) |
| `{{PROFIL_BLZ_AK}}` | Bankleitzahl (Anderkonto) |

### Platzhalter für die angemeldete Person

| Platzhalter | Beschreibung |
|-------------|--------------|
| `{{USER_AN}}` | Anzeigename |
| `{{USER_KRZ}}` | Kürzel |
| `{{USER_VORNAME}}` | Vorname |
| `{{USER_NAME}}` | Name |
| `{{USER_UNTERNEHMEN}}` | Firmenbezeichnung |
| `{{USER_FKT}}` | Funktion |
| `{{USER_STRASSE}}` | Strasse |
| `{{USER_ZUSATZ}}` | Adresszusatz |
| `{{USER_PLZ}}` | Postleitzahl |
| `{{USER_ORT}}` | Ort |
| `{{USER_LAND}}` | Land |
| `{{USER_TEL}}` | Telefonnummer |
| `{{USER_FAX}}` | Faxnummer |
| `{{USER_MOBIL}}` | Mobilnummer |
| `{{USER_EMAIL}}` | E-Mailadresse |
| `{{USER_WWW}}` | Internetadresse |
| `{{USER_STEUERNR}}` | Steuernummer |
| `{{USER_USTIDNR}}` | USt-IdNr. |
| `{{USER_BANK}}` | Bank |
| `{{USER_IBAN}}` | IBAN |
| `{{USER_BIC}}` | BIC |

### Allgemeine Platzhalter

| Platzhalter | Beschreibung |
|-------------|--------------|
| `{{KURZDATUM}}` | Datum in der Form TT.MM.JJJJ |
| `{{LANGDATUM}}` | Datum in der Form Wochentag, TT.MM.JJJJ |
| `{{DOK_DZ}}` | Diktatzeichen des Dokuments |
| `{{AUTOR_AN}}` | Autor des Dokuments / der Nachricht (Anzeigename) |
| `{{AUTOR_KRZ}}` | Kürzel des Autors des Dokuments / der Nachricht |
| `{{AUTOR_EMAIL}}` | E-Mail-Adresse des Autors |

### Platzhalter für Beteiligte

Die hier dargestellten Platzhalter sind für alle Beteiligtentypen verfügbar. Für GEGNER lauten diese dann bspw. `{{GEGNER_NAME}}` statt `{{MANDANT_NAME}}`.

| Platzhalter | Beschreibung |
|-------------|--------------|
| `{{MANDANT_NAME}}` | Name des Mandanten |
| `{{MANDANT_VORNAME}}` | Vorname / Rufname des Mandanten |
| `{{MANDANT_VORNAME2}}` | weitere Vornamen des Mandanten |
| `{{MANDANT_GESCHLECHT}}` | Geschlecht des Mandanten |
| `{{MANDANT_INITIAL}}` | Initialen des Mandanten |
| `{{MANDANT_AGRAD1}}` | akademischer Grad des Mandanten, vor dem Namen |
| `{{MANDANT_AGRAD2}}` | akademischer Grad des Mandanten, nach dem Namen |
| `{{MANDANT_BERUF}}` | Beruf des Mandanten |
| `{{MANDANT_FKT}}` | Funktion des Mandanten |
| `{{MANDANT_ZUSATZ}}` | Adresszusatz des Mandanten |
| `{{MANDANT_NOTIZ}}` | Notiz des Mandanten |
| `{{MANDANT_STA}}` | Staatsangehörigkeit des Mandanten |
| `{{MANDANT_ABTLG}}` | Abteilung des Mandanten |
| `{{MANDANT_UNTERNEHMEN}}` | Unternehmensbezeichnung |
| `{{MANDANT_USTIDNR}}` | Umsatzsteuer-Ident-Nr. des Mandanten |
| `{{MANDANT_STEUERNR}}` | Steuernummer / TIN des Mandanten |
| `{{MANDANT_RFORM}}` | Rechtsform des Mandanten |
| `{{MANDANT_REGNR}}` | Registernummer des Mandanten (juristische Person) |
| `{{MANDANT_REGGERICHT}}` | Registergericht des Mandanten (juristische Person) |
| `{{MANDANT_ANREDE1}}` | Anrede des Mandanten |
| `{{MANDANT_ANREDE2}}` | Briefanrede des Mandanten, bspw. „Herrn" statt „Herr" |
| `{{MANDANT_BEGRUESSUNG}}` | Begrüßung in Briefanrede des Mandanten |
| `{{MANDANT_NACHTEXT}}` | Nachtext des Mandanten |
| `{{MANDANT_STRASSE}}` | Strasse des Mandanten |
| `{{MANDANT_HAUSNR}}` | Hausnummer des Mandanten |
| `{{MANDANT_ORTSTEIL}}` | Ortsteil des Mandanten |
| `{{MANDANT_ORT}}` | Ort des Mandanten |
| `{{MANDANT_PLZ}}` | Postleitzahl des Mandanten |
| `{{MANDANT_LAND}}` | Land des Mandanten |
| `{{MANDANT_TEL}}` | Telefonnummer des Mandanten |
| `{{MANDANT_MOBIL}}` | Mobilnummer des Mandanten |
| `{{MANDANT_FAX}}` | Faxnummer des Mandanten |
| `{{MANDANT_EMAIL}}` | Emailadresse des Mandanten |
| `{{MANDANT_WWW}}` | Homepage des Mandanten |
| `{{MANDANT_BANK}}` | Bank des Mandanten |
| `{{MANDANT_BLZ}}` | Bankleitzahl der Bank des Mandanten |
| `{{MANDANT_KONTONR}}` | Kontonummer des Mandanten |
| `{{MANDANT_RECHTSSCHUTZ}}` | Rechtsschutz des Mandanten |
| `{{MANDANT_VRECHTSSCHUTZ}}` | Verkehrsrechtsschutz des Mandanten |
| `{{MANDANT_EIGENE1}}` | Eigenes Feld 1 |
| `{{MANDANT_EIGENE2}}` | Eigenes Feld 2 |
| `{{MANDANT_EIGENE3}}` | Eigenes Feld 3 |
| `{{MANDANT_GEB}}` | Geburtsdatum des Mandanten |
| `{{MANDANT_GEBNAME}}` | Geburtsname des Mandanten |
| `{{MANDANT_ALTER}}` | Alter des Mandanten |
| `{{MANDANT_GEBORT}}` | Geburtsort des Mandanten |
| `{{MANDANT_GEST}}` | Sterbedatum des Mandanten |
| `{{MANDANT_AKTE_KONTAKT}}` | Ansprechpartner des Mandanten innerhalb einer Akte |
| `{{MANDANT_AKTE_ZEICHEN}}` | AZ1/Referenz des Mandanten innerhalb einer Akte |
| `{{MANDANT_AKTE_EIGENE1}}` | Eigenes Feld 1 des Mandanten innerhalb einer Akte |
| `{{MANDANT_AKTE_EIGENE2}}` | Eigenes Feld 2 des Mandanten innerhalb einer Akte |
| `{{MANDANT_AKTE_EIGENE3}}` | Eigenes Feld 3 des Mandanten innerhalb einer Akte |

### Platzhalter für die Akte

| Platzhalter | Beschreibung |
|-------------|--------------|
| `{{AKTE_NR}}` | Aktennummer |
| `{{AKTE_ERSTELLT}}` | Erstellungsdatum der Akte |
| `{{AKTE_ZEICHEN}}` | Aktenzeichen |
| `{{AKTE_KURZRUBRUM}}` | Bezeichnung der Akte |
| `{{AKTE_NOTIZ}}` | Notiz zur Akte |
| `{{AKTE_SCHADENNR}}` | Schadennummer zur Akte |
| `{{AKTE_GEGENSTANDSWERT}}` | Gegenstandswert |
| `{{AKTE_WEGEN}}` | wegen |
| `{{AKTE_ANWALT}}` | Anwalt (Nutzername) |
| `{{AKTE_ANWALT_AN}}` | Anwalt (Anzeigename) |
| `{{AKTE_ANWALT_KRZ}}` | Kürzel des verantwortlichen Anwalts |
| `{{AKTE_SACHBEARBEITER}}` | Bearbeiter (Nutzername) |
| `{{AKTE_SACHBEARBEITER_AN}}` | Bearbeiter (Anzeigename) |
| `{{AKTE_SACHBEARBEITER_KRZ}}` | Kürzel des verantwortlichen Sachbearbeiters |
| `{{AKTE_EIGENE1}}` | Eigenes Feld 1 |
| `{{AKTE_EIGENE2}}` | Eigenes Feld 2 |
| `{{AKTE_EIGENE3}}` | Eigenes Feld 3 |

### Platzhalter für Berechnungsergebnisse / RVG

Zum Übernehmen von Ergebnistabellen aus Plugins (bspw. RVG-Plugins) wird eine Tabelle mit exakt einer Zelle erstellt und ein Platzhalter wie folgt eingefügt:

| `{{TABELLE_1}}` |
|-----------------|

### Platzhalter für Belege / Rechnungen

| Platzhalter | Beschreibung |
|-------------|--------------|
| `{{BEL_NR}}` | Belegnummer |
| `{{BEL_TYP}}` | Art des Belegs, bspw. „Rechnung", „Angebot" |
| `{{BEL_NAME}}` | Name / Bezeichnung des Belegs |
| `{{BEL_BESCHR}}` | Beschreibung des Belegs |
| `{{BEL_DTFAELLIG}}` | Fälligkeitsdatum |
| `{{BEL_DTLZVON}}` | Datum, Beginn des Leistungszeitraumes |
| `{{BEL_DTLZBIS}}` | Datum, Ende des Leistungszeitraumes |
| `{{BEL_DTERSTELLT}}` | Erstellungsdatum des Belegs |
| `{{BEL_TOTAL}}` | Gesamtbetrag des Belegs |
| `{{BEL_WHRG}}` | Währung des Belegs |

Geldbeträge und Datumsangaben werden dabei entsprechend der Spracheinstellungen des Belegs formatiert.

Zum Übernehmen der Belegpositionen in Form einer Tabelle wird eine Tabelle mit exakt einer Zelle erstellt und ein Platzhalter wie folgt eingefügt:

| `{{BEL_TABELLE}}` |
|-------------------|

Die Spalten der Belegtabelle lassen sich derzeit nicht über die Tabelleneinstellungen anpassen. Stattdessen ist es möglich, eine Tabelle mit der korrekten Anzahl an Spalten und deren Breite zu erstellen. Beispielsweise wie folgt (es ist unerheblich, in welcher Zelle sich der Platzhalter {{BEL_TABELLE}} befindet):

|  | {{BEL_TABELLE}} |  |  |  |  |
| --- | --- | --- | --- | --- | --- |

Darüber hinaus ist es möglich, die Tabelle um weitere Zeilen (mit und ohne Inhalte) zu ergänzen. So lassen sich Bezeichnungen ergänzen, damit beim Bearbeiten direkt sichtbar ist, welche Breite welcher Spalte hier gerade geändert wird. Eventuell eingefügter Text wird im Anschluss durch den Text überschrieben, der in das jeweilige Feld gehört. Ein Umbenennen / Umsortieren / Weglassen von Spalten folgt in einer der nächsten Versionen.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | {{BEL_TABELLE}} |  |  |  |  |

Oder:

|  | Beschreibung | Menge | Einzel | USt. | Betrag |
| --- | --- | --- | --- | --- | --- |
|  | {{BEL_TABELLE}} |  |  |  |  |

Sollte aus einer Vorlage ein Dokument erstellt werden, bleiben die Spaltenbreiten erhalten.

### Platzhalter für Zeiterfassung

Zum Übernehmen gebuchter Zeiten eines Zeiterfassungsprojektes in Form einer Tabelle (=Leistungsnachweis, Spalten: Person, Datum, Dauer, Stundensatz, Total, Beschreibung) wird eine Tabelle mit exakt einer Zelle erstellt und ein Platzhalter wie folgt eingefügt:

| {{ZE_TABELLE}} |
| --- |

Wird eine pro Person aufsummierte Aufstellung der geleisteten Zeiten benötigt (Person, geleistete Zeit, Wert), so kann ein Tabellenplatzhalter wie folgt verwendet werden:

| {{ZE_SUMMEN}} |
| --- |

Geldbeträge und Datumsangaben werden dabei entsprechend der Spracheinstellungen des Belegs formatiert.

### Platzhalter für Texte aus KI-Assistenzfunktionen („Assistent Ingo")

| Platzhalter | Beschreibung |
|-------------|--------------|
| `{{INGO_TEXT}}` | Ergebnistext des jeweiligen Dialogs (bspw. KI-Assistenten oder Sprachmemo) |

## Umgang mit leeren Platzhalterwerten

Gegeben sei eine beispielhafte Anrede in einem Schriftsatz, die wie folgt in der Vorlage abgebildet ist:

```
{{MANDANT_ANREDE}} {{MANDANT_AGRAD1}} {{MANDANT_NAME}},
```

Sind alle Daten des Mandanten gepflegt, so ergibt sich bei Dokumenterstellung bspw.

```
Sehr geehrter Herr Prof. Dr. Müller,
```

Ist nun kein akademischer Grad vorhanden, so entsteht im Dokument ein doppeltes Leerzeichen:

```
Sehr geehrter Herr  Müller,
```

Um solche Konstellationen zu vermeiden, kann das Leerzeichen zwischen Platzhaltern weggelassen werden, die Vorlage würde dann wie folgt aussehen:

```
{{MANDANT_ANREDE}}{{MANDANT_AGRAD1}}{{MANDANT_NAME}},
```

Die Anwendung hat für diese Fälle eine „Intelligenz" und fügt automatisch Leerzeichen an benötigten Stellen ein, bspw. zwischen den Platzhaltern, aber keines vor einem Komma.

## PDF-Formulare als Vorlagen verwenden

PDF-Dateien, die Formulare enthalten, können als Vorlage verwendet werden. Dabei können in allen Textfeldern ein oder mehrere Platzhalter eingegeben werden, also bspw. `{{MANDANT_VORNAME}} {{MANDANT_NAME}}`

Alternativ kann ein Platzhaltername als Name des Formularfeldes genutzt werden, bspw. hat das Feld dann den Bezeichner `MANDANT_NAME`. In diesem Fall kann das Feld jedoch nur einen einzelnen Platzhalterwert aufnehmen. Die Empfehlung ist daher die Anwendung von Variante 1 (direkte Aufnahme von Platzhaltern in die Textfelder).

Weitere Arten von Formularfeldern (bspw. anklickbare ja/nein – Felder) werden nicht unterstützt.

Die Nutzung von Skriptfunktionen in PDF-Vorlagen wird nicht unterstützt.

## Aussehen generierter Tabellen konfigurieren

Über das Menü „Plugins", „Tabelleneinstellungen" kann das Aussehen der über das Vorlagensystem generierten Tabellen beeinflusst werden, bspw.

- Schriftart und -größe
- Tabellenlinien
- fett / kursiv / unterstrichen
- weitere

Ebenso kann das Format von in der Tabelle enthaltenen Geldbeträgen konfiguriert werden. Dazu kann das gewünschte Format in einer bestimmten Syntax definiert werden:

| Format | Beispiel |
| --- | --- |
| 0.00 | 12345,67 |
| 0.0 | 12345,7 |
| 0.000 | 12345,671 |
| #,##0.00 | 12.345,67 |
| ###,##0.00 | 12.345,67 |
| 000,000.00 | 012.345,67 |

Eine Dokumentation zu weiteren Formatmöglichkeiten ist hier zu finden: <https://docs.oracle.com/javase/8/docs/api/java/text/DecimalFormat.html>

## Flexible Nutzung von Vorlagen für verschiedene Beteiligtentypen

Es ist nicht notwendig, für jeden möglichen Beteiligtentyp eigene Vorlagen zu erstellen. Auch wenn eine Vorlage mit Platzhaltern `{{MANDANT_…}}` belegt ist, so kann zum Zeitpunkt der Dokumenterstellung aus dieser Vorlage eine beliebige Beteiligte auf diese Platzhalterkategorie verknüpft werden.

Nach Auswahl einer Vorlage wird auf Vorhandensein von Platzhaltern geprüft, und die in der Vorlage verwendeten Beteiligtentypen werden angezeigt (Spalten). Zusätzlich werden alle in der Akte geführten Beteiligten angezeigt und deren Beteiligtentyp ist vorausgewählt. Es ist nun problemlos möglich, eine als Mandantin geführte Beteiligte nur für die Erstellung eines Dokuments als Gegner o.a. zu verwenden. Ein Klick in der Tabelle genügt. Eine Beteiligte kann dabei auch mehreren Beteiligtentypen zugeordnet werden (bspw. "Kundin" und "Lieferant"), aber es kann immer nur eine Beteiligte pro Typ geben (also bspw. kein zwei Beteiligte die als "Versicherung" genutzt werden sollen), da sonst keine eindeutige Befüllung der Platzhalter möglich wäre.

![Abbildung 8](../../images/j-lawyer-org-UserGuide-de-014.png)

## Verwendung einfacher Logik / Funktionen in Vorlagen {#skripte}

Die Nutzung herkömmlicher Platzhalter ermöglicht eine grundlegende Automatisierung der Dokumenterstellung. Für fortgeschrittene Szenarien ist jedoch eine manuelle Nachbearbeitung notwendig, bspw. um geschlechterspezifische Formulierungen zu automatisieren, oder auf Basis vorhandender Daten aus der Akte, den Beteiligten oder einem Falldatenblatt Varianten bestimmter Inhalte hinzuzufügen.

Zu diesem Zweck können einfache Logiken / Programmcode („Skripte") in einer Vorlage verwendet werden. Skripte werden über einen eigenen Platzhalter eingefügt, der wie folgt aussieht:

```
[[SCRIPT:…]]
```

Anstelle des `…` wird die eigentliche Logik – bspw. eine Funktion oder eine Kombination mehrerer Funktionen - eingefügt. Das Ergebnis eines Skriptes muss immer eine Zeichenkette (also ein Text) sein.

Innerhalb eines Skriptes können Standardplatzhalter verwendet werden, bspw. als Parameter. In diesem Fall werden die doppelt geschweiften Klammern weggelassen.

Innerhalb von Werten sind keine Absatzumbrüche zu verwenden (Enter). Zeilenumbrüche sind zulässig (Shift+Enter).

Werden über Platzhalter die Werte mehrzeiliger Eingabefelder übernommen, so sind die Platzhalternamen in 2fache doppelte Anführungszeiten aufzunehmen, also bspw.

```
[[SCRIPT: WENNGLEICH(UKSC_7EINLASSGJANEIN,"ja",""UKSC_7EINLASSGINH"");]]
```

Zeilenumbrüche können ebenfalls mittels `\n` eingefügt werden, Einrückungen mittels `\t`. Der Wert

```
"Hallo hier folgt eine neue Zeile,\nund das folgende Wort ist eingerückt:
\teingerückt"
```

ergibt die Ausgabe

```
"Hallo hier folgt eine neue Zeile,
und das folgende Wort ist eingerückt:	eingerückt"
```

Ist ein Skriptausdruck der einzige Inhalt einer Zeile, und ergibt einen leeren Wert, so wird die Zeile aus dem Dokument entfernt.

### Funktion DATUMZEIT

Gibt das aktuelle Datum und / oder die aktuelle Zeit im gewünschten Format aus.

| Signatur | DATUMZEIT(Format) |  |
| --- | --- | --- |
| Parameter: Format | Format, in welchem Datum / Zeit ausgegeben werden sollen | "EEEEE, dd. MMMMM yyyy" |
| Rückgabewert: | Datum / Zeit im angegebenen Format | Freitag, 11. Februar 2022 |

Folgende Buchstaben können im Format verwendet werden:

| Buchstabe | Bedeutung |
|-----------|-----------|
| `y` | Jahr |
| `M` | Monat im Jahr |
| `w` | Woche im Jahr |
| `W` | Woche im Monat |
| `D` | Tag im Jahr |
| `d` | Tag im Monat |
| `E` | Name des Wochentages |
| `a` | am/pm |
| `H` | Stunde (0-23) |
| `k` | Stunde (1-24) |
| `K` | Stunde in am/pm (0-11) |
| `h` | Stunde in am/pm (0-12) |
| `m` | Minute |
| `s` | Sekunde |
| `z` | Zeitzone |
| `Z` | Zeitzone |
| `X` | Zeitzone |

**Beispiele:**

Fr., 11.02.2022:
```
[[SCRIPT:DATUMZEIT("EEE, dd.MM.yyyy");]]
```

Fr., 11. Februar 2022 15:30:
```
[[SCRIPT:DATUMZEIT("EEE, dd. MMMMM yyyy HH:mm");]]
```

Freitag, 11. Februar 2022:
```
[[SCRIPT:DATUMZEIT("EEEEE, dd. MMMMM yyyy");]]
```

Details zu Formatmöglichkeiten: <https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html>

### Funktion FRIST

Gibt ein errechnetes Datum x Tage nach einem gegebenen Datum zurück.

| Signatur | FRIST(Referenzdatum, Tage) FRIST(Referenzdatum, Tage, Format) |  |
| --- | --- | --- |
| Parameter: Referenzdatum | Referenzdatum, welches für die Berechnung verwendet wird. | "31.12.2021" KURZDATUM KSCHUTZ_ZUGANGK |
| Parameter: Tage | Anzahl der zu addierenden Tage, angegeben in Hochkommata | "14" |
| Parameter: Format | Gewünschtes Datumsformat, siehe Funktion DATUMZEIT |  |
| Rückgabewert: | Das errechnete Datum im Format "TT.MM.JJJJ". | 13.01.2022 |

**Beispiele:**

14 Tage nach aktuellem Datum:
```
Als Frist habe ich mir den [[SCRIPT:FRIST(KURZDATUM,"14");]] notiert.
```

10 Tage nach fixem Datum:
```
Als Frist habe ich mir den [[SCRIPT:FRIST("01.01.2022","10");]] notiert.
```

### Funktion FRISTBANKTAG

Gibt ein errechnetes Datum x Tage nach einem gegebenen Datum zurück. Fällt das errechnete Datum auf einen Samstag oder Sonntag, wird der darauf folgende Montag zurückgegeben.

| Signatur | FRISTBANKTAG(Referenzdatum, Tage) FRISTBANKTAG(Referenzdatum, Tage, Format) |  |
| --- | --- | --- |
| Parameter: Referenzdatum | Referenzdatum, welches für die Berechnung verwendet wird. | "31.12.2021" KURZDATUM KSCHUTZ_ZUGANGK |
| Parameter: Tage | Anzahl der zu addierenden Tage, angegeben in Hochkommata | "14" |
| Parameter: Format | Gewünschtes Datumsformat, siehe Funktion DATUMZEIT |  |
| Rückgabewert: | Das errechnete Datum im Format "TT.MM.JJJJ". | 13.01.2022 |

**Beispiele:**

14 Tage nach aktuellem Datum:
```
Als Frist habe ich mir den [[SCRIPT:FRISTBANKTAG(KURZDATUM,"14");]] notiert.
```

10 Tage nach fixem Datum:
```
Als Frist habe ich mir den [[SCRIPT:FRISTBANKTAG("01.01.2022","10");]] notiert.
```

### Funktion MWDJU

Gibt in Abhängigkeit eines Geschlechts einen vorgegebenen Text zurück.

| Signatur | MWDJU(g, m, w, d, j, u) |  |
| --- | --- | --- |
| Parameter: g | Referenzwert für Geschlecht, welcher für den Vergleich verwendet wird. Wird in der Regel über einen Platzhalter definiert. | "weiblich" "männlich" MANDANT_GESCHLECHT |
| Parameter: m | Ergebnis des Skriptes, wenn der Referenzwert "männlich" ist, angegeben in Hochkommata |  |
| Parameter: w | Ergebnis des Skriptes, wenn der Referenzwert "weiblich" ist, angegeben in Hochkommata |  |
| Parameter: d | Ergebnis des Skriptes, wenn der Referenzwert "divers" ist, angegeben in Hochkommata |  |
| Parameter: j | Ergebnis des Skriptes, wenn der Referenzwert "juristische Person" ist, angegeben in Hochkommata |  |
| Parameter: u | Ergebnis des Skriptes, wenn der Referenzwert "undefiniert" ist, angegeben in Hochkommata |  |
| Rückgabewert: | Der Wert eines der Parameter m, w, d, j oder u als Zeichenkette |  |

**Beispiel:** eine Anrede die dynamisch erstellt wird, je nachdem ob die Mandantin weiblich / männlich / divers / juristische Person / undefiniert ist

```
[[SCRIPT:MWDJU(MANDANT_GESCHLECHT,"Sehr geehrter Herr " + MANDANT_NAME,"Sehr geehrte Frau " + MANDANT_NAME,"Guten Tag, " + MANDANT_VORNAME + " " + MANDANT_NAME, "Sehr geehrte Damen und Herren", "Sehr geehrte Damen und Herren");]]
```

### Funktion GROSS

Wandelt einen gegebenen Text in Großschreibung um, bspw. weil der Wert eines Platzhalters an einem Satzanfang verwendet werden soll.

| Signatur | GROSS(Text) |  |
| --- | --- | --- |
| Parameter: Text | Text, welcher in Großschreibung zurückgegeben werden soll. | MANDANT_GESCHLECHT |
| Rückgabewert: | Der gegebene Text in Großschreibung. | Weiblich |

**Beispiel:**
```
[[SCRIPT:GROSS(MANDANT_GESCHLECHT);]] ist in der Akte kleingeschrieben, hier im Text aber gross.
```

### Funktion KLEIN

Wandelt einen gegebenen Text in Kleinschreibung um.

| Signatur | KLEIN(Text) |  |
| --- | --- | --- |
| Parameter: Text | Text, welcher in Kleinschreibung zurückgegeben werden soll. | MANDANT_GESCHLECHT |
| Rückgabewert: | Der gegebene Text in Kleinschreibung. | weiblich |

**Beispiel:**
```
[[SCRIPT:KLEIN(MANDANT_GESCHLECHT);]] erscheint hier im Text klein.
```

### Funktion WENNGLEICH

Gibt einen Text aus, wenn ein Referenzwert einem Vergleichswert entspricht, oder optional einen anderen Wert, wenn die Werte voneinander abweichen.

| Signatur | WENNGLEICH(Referenz, Vergleichswert, Gleichheitswert) WENNGLEICH(Referenz, Vergleichswert, Gleichheitswert, Ungleichheitswert) |  |
| --- | --- | --- |
| Parameter: Referenz | Text, welcher als Referenz für den Vergleich genutzt wird. | MANDANT_ORT |
| Parameter: Vergleichswert | Text, welcher mit dem Referenzwert verglichen wird. | "Hamburg" PROFIL_ORT |
| Parameter: Gleichheitswert | Text, welcher ausgegeben wird wenn Referenzwert und Vergleichswert übereinstimmen. Unterschiede in Gross- und Kleinschreibung werden als Gleichheit gewertet. | "Moin Moin" |
| Parameter: Ungleichheitswert | Optional. Text, welcher ausgegeben wird wenn Referenzwert und Vergleichswert voneinander abweichen. Unterschiede in Gross- und Kleinschreibung werden als Gleichheit gewertet. | "Guten Tag" |
| Rückgabewert: | Der Gleichheitswert oder Ungleichheitswert als Text. Stimmen Referenz und Vergleichswert nicht überein und es ist kein Ungleichheitswert angegeben, so wird ein leerer Text zurückgegeben. |  |

**Beispiele:**
```
[[SCRIPT:WENNGLEICH(MANDANT_ORT, "Hamburg", "Moin moin " + MANDANT_VORNAME + " " + MANDANT_NAME);]]
```

```
[[SCRIPT:WENNGLEICH(MANDANT_ORT, "Hamburg", "Moin moin " + MANDANT_VORNAME + " " + MANDANT_NAME, "Guten Tag " + MANDANT_VORNAME + " " + MANDANT_NAME);]]
```

### Funktion WENNENTHAELT

Gibt einen Text aus, wenn ein Referenzwert einen Vergleichswert enthält, oder optional einen anderen Wert, wenn der Vergleichswert nicht enthalten ist.

| Signatur | WENNENTHAELT(Referenz, Vergleichswert, WennEnthalten) WENNENTHAELT(Referenz, Vergleichswert, WennEnthalten, WennNichtEnthalten) |  |
| --- | --- | --- |
| Parameter: Referenz | Text, welcher als Referenz für die Suche genutzt wird. | MANDANT_STA |
| Parameter: Vergleichswert | Text, welcher im Referenzwert gesucht wird. | "deutsch" |
| Parameter: WennEnthalten | Text, welcher ausgegeben wird wenn der Vergleichswert im Referenzwert enthalten ist. Unterschiede in Gross- und Kleinschreibung werden ignoriert. | "Die Person hat die deutsche Staatsangehörigkeit." |
| Parameter: WennNichtEnthalten | Optional. Text, welcher ausgegeben wird wenn der Vergleichswert nicht im Referenzwert enthalten ist. Unterschiede in Gross- und Kleinschreibung werden ignoriert. | "Die Person verfügt nicht über die deutsche Staatsangehörigkeit." |
| Rückgabewert: | Der Wert von WennEnthalten oder WennNichtEnthalten als Text. Wird der Vergleichswert nicht gefunden und es ist kein WennNichtEnthalten angegeben, so wird ein leerer Text zurückgegeben. |  |

**Beispiele:**
```
[[SCRIPT:WENNENTHAELT(MANDANT_STA, "deutsch", "Die Person hat die deutsche Staatsangehörigkeit.");]]
```

```
[[SCRIPT:WENNENTHAELT(MANDANT_STA, "deutsch", "Die Person hat die deutsche Staatsangehörigkeit.", "Die Person verfügt nicht über die deutsche Staatsangehörigkeit.");]]
```

### Funktion WENNLEER

Gibt einen Text aus, wenn ein Referenzwert leer ist, oder optional einen anderen Wert, wenn der Referenzwert nicht leer ist.

| Signatur | WENNLEER(Referenz, WennLeer) WENNLEER(Referenz, WennLeer, WennNichtLeer) |  |
| --- | --- | --- |
| Parameter: Referenz | Text, welcher als auf Vorhandensein geprüft wird. | KSCHUTZ_GRUNDK |
| Parameter: WennLeer | Text, welcher ausgegeben wird wenn der Referenzwert leer ist. |  |
| Parameter: WennNichtLeer | Optional. Text, welcher ausgegeben wird wenn der Referenzwert nicht leer ist. |  |
| Rückgabewert: | Der Wert von WennLeer oder WennNichtLeer als Text. Ist der Referenzwert nicht leer und es ist kein WennNichtLeer angegeben, so wird ein leerer Text zurückgegeben. |  |

**Beispiele:**
```
[[SCRIPT:WENNLEER(KSCHUTZ_GRUNDK, "Ein Grund für die Kündigung wurde nicht mitgeteilt.");]]
```

```
[[SCRIPT:WENNLEER(KSCHUTZ_GRUNDK, "Ein Grund für die Kündigung wurde nicht mitgeteilt.", "Eine Begründung der Kündigung liegt uns vor.");]]
```

### Funktion WENNGROESSER

Gibt einen Text aus, wenn ein Referenzwert ein numerisches Limit übersteigt, oder optional einen anderen Wert, wenn der Referenzwert unterhalb des Limits liegt oder identisch ist.

| Signatur | WENNGROESSER(Vergleichswert, Limit, WennGroesser) WENNGROESSER(Vergleichswert, Limit, WennGroesser, Anderenfalls) |  |
| --- | --- | --- |
| Parameter: Vergleichswert | Text, welcher mit dem Limit verglichen wird. | AKTE_GEGENSTANDSWERT |
| Parameter: Limit | Text, welcher das numerische Limit definiert. | "50000" |
| Parameter: WennGroesser | Text, welcher ausgegeben wird wenn der Vergleichswert größer ist. |  |
| Parameter: Anderenfalls | Optional. Text, welcher ausgegeben wird wenn der Vergleichswert kleiner oder gleich ist. |  |
| Rückgabewert: | Der Wert von WennGroesser oder Anderenfalls als Text. Ist der Vergleichswert nicht größer und es ist kein Anderenfalls angegeben, so wird ein leerer Text zurückgegeben. |  |

**Beispiele:**
```
[[SCRIPT:WENNGROESSER(AKTE_GEGENSTANDSWERT, "50000", "Das wird ein tolles Mandat!");]]
```

```
[[SCRIPT:WENNGROESSER(AKTE_GEGENSTANDSWERT, "50000", "Das wird ein tolles Mandat!", "Manche Dinge müssen halt einfach erledigt werden.");]]
```

### Funktion WENNFALLDATEN

Gibt einen Text aus, wenn ein Falldatenblatt in der betroffenen Akte vorhanden ist, oder optional einen anderen Wert, wenn das Falldatenblatt nicht existiert.

| Signatur | WENNFALLDATEN(Präfix, WennVorhanden) WENNFALLDATEN(Präfix, WennVorhanden, WennNichtVorhanden) |  |
| --- | --- | --- |
| Parameter: Präfix | Platzhalterpräfix des Falldatenblattes. | FAMR |
| Parameter: WennVorhanden | Text, welcher ausgegeben wird wenn ein Falldatenblatt mit diesem Präfix in der Akte vorhanden ist. |  |
| Parameter: WennNichtVorhanden | Optional. Text, welcher ausgegeben wird wenn das Falldatenblatt nicht vorhanden ist. |  |
| Rückgabewert: | Der Wert von WennVorhanden oder WennNichtVorhanden als Text. |  |

!!! info "Hinweis"
    Im Gegensatz zu den anderen Funktionsaufrufen wird der Präfix-Parameter hier in Hochkommata angegeben.

**Beispiel:**
```
[[SCRIPT:WENNFALLDATEN("UKBEA", "Falldaten UKBEA vorhanden", "Falldaten UKBEA nicht vorhanden");]]
```

### Funktion GENDERN

Gibt einen geschlechts- und fallspezifischen Wert für einen Begiff aus.

| Signatur | GENDERN(Begriff, Geschlecht, Fall) |  |
| --- | --- | --- |
| Parameter: Begriff | Text, für welchen ein geschlechts- und fallspezifischer Wert ausgegeben werden soll. | "Kläger" |
| Parameter: Geschlecht | Geschlecht, bspw. "weiblich", "männlich", "divers", "juristische Person", "undefiniert" | "weiblich" MANDANT_GESCHLECHT |
| Parameter: Fall | Fall | "Nominativ" "Genitiv" "Dativ" "Akkusativ" |
| Rückgabewert: | Der gegenderte Wert des gegebenen Begriffes. |  |

**Beispiele:**
```
Die weibliche Form von „Kläger" lautet [[SCRIPT:GENDERN("Kläger","weiblich","Nominativ");]].
```

```
[[SCRIPT:GENDERN("Kläger",MANDANT_GESCHLECHT,"Nominativ");]]
```

### Funktion ZUORDNEN

Gibt anhand eines, zweier oder dreier Kriterien einen passenden Wert aus.

| Signatur | ZUORDNEN(Zuordnungstabelle, Schlüssel1, Schlüssel2, Schlüssel3) ZUORDNEN(Zuordnungstabelle, Schlüssel1, Schlüssel2) ZUORDNEN(Zuordnungstabelle, Schlüssel1) |  |
| --- | --- | --- |
| Parameter: Zuordnungstabelle | Name der Zuordnungstabelle. Pflege der Tabelle im Menü "Einstellungen" – "Dokumente" – "Zuordungstabelle" und "Zuordnungsregeln" | "Tabelle xyz" |
| Parameter: Schlüssel1, Schlüssel2, Schlüssel3 | Wert der Kriterien |  |
| Rückgabewert: | Der Wert, der anhand der gegebenen Schlüssel in der Zuordnungstabelle gefunden wird. |  |

**Beispiel:**

Zuordnungstabelle:

- Name: Gesellschaftsform
- Schlüssel 1: Rechtsform

Zuordnungsregeln:

| Rechtsform | Wert |
| --- | --- |
| GmbH | Kapitalgesellschaft |
| GbR | Personengesellschaft |
| AG | Kapitalgesellschaft |

```
Mein Mandant leitet eine [[SCRIPT:ZUORDNEN("Gesellschaftsform",MANDANT_RFORM);]].
```

Ergibt (wenn in den Stammdaten des Mandanten die Rechtsform „GmbH" ausgewählt ist):

```
Mein Mandant leitet eine Kapitalgesellschaft.
```

### Funktion WENNETIKETT

Gibt einen Wert aus, sofern für die Akte ein bestimmtes Etikett gesetzt ist.

| Signatur | WENNETIKETT(Etikett, WennVorhanden) WENNETIKETT(Etikett, WennVorhanden, Anderenfalls) |  |
| --- | --- | --- |
| Parameter: Etikett | Name des Etiketts, auf dessen Vorhandensein geprüft wird. | "VIP" |
| Parameter: WennVorhanden | Text, welcher ausgegeben wird wenn das Etikett gesetzt ist. |  |
| Parameter: Anderenfalls | Optional. Text, welcher ausgegeben wird wenn das Etikett nicht gesetzt ist. |  |
| Rückgabewert: | Der Wert von WennVorhanden oder Anderenfalls als Text. Ist das Etikett nicht vorhanden und es ist kein Anderenfalls angegeben, so wird ein leerer Text zurückgegeben. |  |

**Beispiel:**
```
[[SCRIPT:WENNETIKETT("bevorzugtes Mandat", "Gern biete ich Ihnen einen kurzfristigen Termin an.", "Einen Termin können wir gern für die übernächste Woche vereinbaren.");]]
```

### Funktionen schachteln

Funktionen können ineinander geschachtelt werden, bspw. MWDJU innerhalb von WENNGLEICH, um bei Gleichheit zweier Werte einen geschlechterspezifischen Ausgabetext zu erhalten. Zu diesem Zweck können Parameter einer übergeordneten Funktion durch die Angabe einer inneren Funktion definiert werden.

**Beispiel:** wenn laut Falldatenblatt „Kündigungsschutz" ein Betriebsrat vorhanden ist, gib einen geschlechterspezifischen Wert aus

```
[[SCRIPT:WENNGLEICH(KSCHUTZ_BTRAT,"Betriebsrat vorhanden",MWDJU(GEGNER_GESCHLECHT," Beim Beklagten ","Bei der Beklagten " ,"Bei der beklagten Partei ", "Bei den Beklagten ", "Bei der beklagten Partei ") + "ist ein Betriebsrat gebildet. Die ordnungsgemäße Anhörung des Betriebsrats wird (hilfsweise mit Nichtwissen) bestritten.","Es ist kein Betriebsrat gebildet");]]
```

### Mehrere Bedingungen in einem Skript, UND / ODER

In einigen Fällen kann eine Prüfung mehrerer Bedingungen notwendig sein. Die Syntax hierfür ist noch nicht anwenderfreundlich umgesetzt, kann aber bereits realisiert werden.

**Anwendungsfall:** Wenn Bedingungen 1 UND 2 erfüllt sind, gib Wert 1 aus, anderenfalls Wert 2

Syntax: `Bedingung1 && Bedingung2 ? Wert1 : Wert2`

**Beispiel:**
```
[[SCRIPT:(MANDANT_NAME.equals("Müller") && MANDANT_ORT.equals("Dingsstadt")) ? "Frau Müller aus Dingsstadt" : "jemand anderes";]]
```

**Anwendungsfall:** Wenn Bedingung 1 ODER 2 erfüllt sind, gib Wert 1 aus, anderenfalls Wert 2

Syntax: `Bedingung1 || Bedingung2 ? Wert1 : Wert2`

**Beispiel:**
```
[[SCRIPT:(MANDANT_NAME.equals("Müller") || MANDANT_NAME.equals("Meier")) ? "Müller oder Meier" : "jemand anderes";]]
```
