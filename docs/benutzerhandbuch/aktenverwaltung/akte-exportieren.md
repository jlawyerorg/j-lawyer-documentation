# Akte exportieren {#akte-exportieren}

Die Export-Funktion ermöglicht es, eine Akte als HTML-Paket zu exportieren, das vollständig offline im Browser genutzt werden kann. Dies ist besonders nützlich, um Akteninhalte ohne Zugang zum j-lawyer-Server einzusehen - beispielsweise für externe Besprechungen, Gerichtstermine oder zur Archivierung.

![Abbildung 1](../../images/case-export-html.png)

## Exportvorgang

1. Öffnen Sie die gewünschte Akte
2. Klicken Sie auf das Export-Symbol in der Werkzeugleiste (Tooltip: "gesamte Akte als HTML exportieren")
3. Wählen Sie ein Zielverzeichnis für den Export
4. Der Fortschritt wird während des Exports angezeigt

Nach Abschluss des Exports wird das Ergebnis automatisch im Standard-Browser geöffnet. Das exportierte Verzeichnis enthält alle Dateien und kann auf beliebige Datenträger kopiert oder weitergegeben werden.

## Exportierte Inhalte

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

## Funktionen der exportierten HTML-Seite

Die generierte HTML-Seite bietet eine interaktive Oberfläche mit folgenden Funktionen:

### Tab-Navigation

Die Inhalte sind in fünf Bereiche gegliedert:

- **Übersicht**: Grunddaten, Beteiligte, Etiketten und Notizen auf einen Blick
- **Dokumente**: Durchsuchbare Dokumentenansicht mit Ordnerstruktur
- **Fälligkeiten**: Wiedervorlagen, Fristen und Termine
- **Finanzen**: Belege und Aktenkonto
- **Aktenhistorie**: Chronologisches Änderungsprotokoll

### Erscheinungsbild

Über die Schaltfläche in der Kopfzeile kann zwischen einem dunklen und hellen Farbschema gewechselt werden. Die Einstellung wird im Browser gespeichert und bei erneutem Öffnen beibehalten.

### Dokumenten-Funktionen

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
