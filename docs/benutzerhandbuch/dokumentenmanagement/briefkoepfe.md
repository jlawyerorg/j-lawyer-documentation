# Briefköpfe {#briefkoepfe}

Briefköpfe ermöglichen es, Grafikdateien (z.B. PNG, JPG) als Hintergrund der ersten Seite eines Dokuments einzufügen. Dies ist nützlich wenn das Design / die Corporate Identity (Logos etc.) und der fachliche Inhalt von Schriftsätzen getrennt voneinander gepflegt werden sollen. Briefköpfe können automatisch bei der Dokumenterstellung eingefügt werden.

## Funktionsweise

Ein Briefkopf wird als **ganzseitiges Hintergrundbild** auf der ersten Seite des erstellten Dokuments eingefügt. Das Bild wird dabei:

- auf die volle Seitengröße skaliert
- als unterste Ebene (Hintergrund) positioniert
- so eingefügt, dass der Text darüber fließt

!!! info "Unterstützte Formate"
    Briefköpfe können als PNG- oder JPG-Dateien hinterlegt werden. Die Grafik sollte die Abmessungen einer DIN-A4-Seite haben (oder entsprechend der verwendeten Papiergröße), um ein optimales Ergebnis zu erzielen.

## Briefkopf erstellen {#briefkoepfe-erstellen}

Es empfiehlt sich das folgende Vorgehen:

- Briefkopf als normales Dokument in LibreOffice Writer oder Microsoft Word erstellen und für eventuelle spätere Anpassungen speichern
- Briefkopf als Grafikdatei exportieren: in LibreOffice via "Datei" - "Exportieren..." als PNG-Datei exportieren; in Microsoft Office gibt es keine Möglichkeit, ein Dokument als Grafik zu exportieren - hier kann man ggf. auf Online-Konverter zurückgreifen (Suche nach [DOCX zu PNG](https://www.google.com/search?q=docx+to+png) o.ä.)
- Grafikdatei in der Hauptnavigation links, ganz unten unter **Vorlagen** → **Akten: Briefköpfe** per Drag and Drop hinterlegen

!!! info "Von Textverarbeitung zu PDF zu Grafikdatei"
    - Wenn der direkte Export vom Format der Textverarbeitung zur PNG-Datei zu verlustbehaftet ist, kann ein "Umweg" über PDF genutzt werden
    - Aus Microsoft Word oder LibreOffice Writer möglichst verlustfrei in PDF konvertieren, danach das PDF in eine PNG-Datei umwandeln (bspw. mittels [PDF24](https://tools.pdf24.org/de/von-pdf-umwandeln) o.ä.)


## Briefköpfe verwalten {#briefkoepfe-verwalten}

Die Verwaltung der Briefköpfe erfolgt über die Hauptnavigation links, ganz unten unter **Vorlagen** → **Akten: Briefköpfe**.

### Briefkopf hinzufügen

1. Öffnen Sie den Briefkopf-Manager über die Navigation
2. Klicken Sie auf **Hinzufügen**
3. Wählen Sie eine Bilddatei (PNG oder JPG) von Ihrem Computer oder ziehen Sie diese per Drag&Drop in die Briefkopfliste
4. Der Briefkopf wird auf dem Server gespeichert und steht allen Nutzern zur Verfügung

### Ordnerstruktur

Briefköpfe können - im Gegensatz zu Dokumentvorlagen - nicht in einer Ordnerstruktur organisiert werden

### Briefkopf löschen

1. Wählen Sie den zu löschenden Briefkopf aus
2. Klicken Sie auf **Löschen**
3. Bestätigen Sie die Löschung

!!! warning "Hinweis"
    Gelöschte Briefköpfe können nicht wiederhergestellt werden. Bereits erstellte Dokumente, die den Briefkopf verwenden, sind davon nicht betroffen.

## Briefkopf bei Dokumenterstellung verwenden {#briefkopf-verwenden}

Die Auswahl eines Briefkopfs erfolgt im Rahmen der Dokumenterstellung. Siehe [Dokument aus einer Vorlage erstellen](dokumente-erstellen.md#dokument-erstellen) für Details.

j-lawyer.org merkt sich die Briefkopf-Zuordnung pro Vorlage. Wenn Sie für eine bestimmte Vorlage einen Briefkopf auswählen, wird dieser bei der nächsten Verwendung derselben Vorlage automatisch vorausgewählt. Um eine gespeicherte Zuordnung zu entfernen, wählen Sie den leeren Eintrag (erste Option) in der Briefkopf-Dropdown-Liste.

## Anwendungsbeispiele {#anwendungsbeispiele}

### Unterschiedliche Briefköpfe für verschiedene Anwälte

In einer Sozietät kann jeder Anwalt einen eigenen Briefkopf haben:

- `Briefkopf_Mueller.png`
- `Briefkopf_Schmidt.png`
- `Briefkopf_Weber.png`

Bei der Dokumenterstellung wählt jeder Anwalt seinen persönlichen Briefkopf.

### Briefköpfe für verschiedene Dokumenttypen

Sie können verschiedene Briefköpfe für unterschiedliche Zwecke anlegen:

- `Briefpapier_Standard.png` - für normale Korrespondenz
- `Briefpapier_Mahnung.png` - für Mahnschreiben mit anderem Design
- `Briefpapier_Rechnung.png` - für Rechnungen

### Kanzlei mit mehreren Standorten

Bei mehreren Standorten können standortspezifische Briefköpfe verwendet werden:

- `Standort_Hamburg.png`
- `Standort_Berlin.png`
- `Standort_München.png`

## Tipps zur Briefkopf-Erstellung {#tipps}

### Bildgröße und Auflösung

- **Empfohlene Auflösung**: 300 DPI für optimale Druckqualität
- **Abmessungen für DIN A4**: 2480 × 3508 Pixel (bei 300 DPI)
- **Dateigröße**: Halten Sie die Dateigröße moderat (unter 2 MB), um die Dokumenterstellung nicht zu verlangsamen

### Transparenz

- PNG-Dateien können Transparenz enthalten
- Verwenden Sie Transparenz für Bereiche, in denen der Dokumenttext sichtbar sein soll

### Vorschau

Erstellen Sie zunächst ein Testdokument, um zu prüfen, ob der Briefkopf korrekt positioniert ist und der Text gut lesbar bleibt.

## Kompatibilität {#kompatibilitaet}

Briefköpfe werden für folgende Dokumentformate unterstützt:

| Format | Unterstützung |
|--------|---------------|
| ODT (LibreOffice) | Ja |
| DOCX (Microsoft Word) | Ja |
| PDF | Nein (Briefkopf wird bei PDF-Vorlagen nicht unterstützt) |
