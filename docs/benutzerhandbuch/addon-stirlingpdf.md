# Add-Ons: Stirling PDF-Integration

Stirling PDF (<https://stirlingpdf.io/>) ist ein leistungsfähiges Open-Source-Werkzeug zur Arbeit mit PDF-Dokumenten. Es kann separat installiert und an j-lawyer.org angebunden werden, um serverseitige PDF-Konvertierungen und OCR-Funktionen zu ermöglichen.

## Nutzen der Integration {#nutzen}

Die Integration von Stirling PDF bietet folgende Vorteile:

- **Serverseitige PDF-Konvertierung**: Office-Dokumente (Word, Excel, LibreOffice etc.) können automatisch in PDF umgewandelt werden

- **Automatisierung über API**: Dokumente, die über die j-lawyer.org API erstellt werden, können direkt als PDF konvertiert und in Akten abgelegt werden

- **OCR-Funktionalität**: PDF-Dokumente können mit Texterkennung versehen werden (Sprachen: Deutsch, Englisch)

- **Batch-Verarbeitung**: Mehrere Dokumente können parallel verarbeitet werden

## Installation von Stirling PDF {#installation}

Stirling PDF wird als Docker-Container betrieben. Die Installation erfolgt auf dem Server, auf dem auch j-lawyer.org läuft, oder auf einem separaten Server im Netzwerk.

### Docker-Container starten

Für die vollständige Funktionalität (inklusive zusätzlicher Schriftarten) wird die `latest-fat`-Variante empfohlen:

```bash
docker run -d \
  --name stirling-pdf \
  -p 6080:8080 \
  -v /pfad/zu/daten:/usr/share/tessdata \
  -v /pfad/zu/config:/configs \
  stirlingtools/stirling-pdf:latest-fat
```

| Parameter | Beschreibung |
|-----------|--------------|
| `-p 6080:8080` | Port-Mapping: Stirling PDF ist unter Port 6080 erreichbar |
| `-v /pfad/zu/daten:/usr/share/tessdata` | Verzeichnis für OCR-Sprachdaten |
| `-v /pfad/zu/config:/configs` | Verzeichnis für Konfigurationsdateien |
| `latest-fat` | Variante mit zusätzlichen Schriftarten und Funktionen |

### Systemanpassungen für Linux

Auf Linux-Systemen müssen ggf. die inotify-Limits angepasst werden. Fügen Sie folgende Zeilen in `/etc/sysctl.conf` hinzu:

```
fs.inotify.max_user_instances=8192
fs.inotify.max_user_watches=524288
```

Anschließend die Einstellungen aktivieren:

```bash
sudo sysctl -p
```

### Erreichbarkeit prüfen

Nach dem Start ist Stirling PDF über einen Webbrowser erreichbar, z.B. unter `http://localhost:6080/`. Die Weboberfläche kann auch für manuelle PDF-Operationen genutzt werden.

## Konfiguration in j-lawyer.org {#konfiguration}

Die Anbindung erfolgt über das Menü „Einstellungen" - „Dokumentoptionen" - „Stirling PDF".

Im Konfigurationsdialog wird der API-Endpunkt hinterlegt:

| Einstellung | Beschreibung | Beispiel |
|-------------|--------------|----------|
| API-Endpunkt | URL der Stirling PDF-Installation | `http://localhost:6080/` |

Nach dem Speichern ist die Integration aktiv.

## Unterstützte Funktionen {#funktionen}

### Konvertierung zu PDF

Folgende Dateiformate können zu PDF konvertiert werden:

- Microsoft Word (.doc, .docx)

- Microsoft Excel (.xls, .xlsx)

- Microsoft PowerPoint (.ppt, .pptx)

- LibreOffice/OpenOffice-Dokumente (.odt, .ods, .odp)

- Bilder (.jpg, .png, .gif, .bmp, .tiff)

- Textdateien (.txt, .rtf)

Die Konvertierung erfolgt über den API-Endpunkt `/api/v1/convert/file/pdf`.

### OCR (Texterkennung)

PDF-Dokumente können mit Texterkennung versehen werden. Dabei werden folgende Sprachen unterstützt:

- Deutsch (deu)

- Englisch (eng)

Der OCR-Modus „skip-text" überspringt bereits vorhandenen Text und führt OCR nur auf Bildbereichen durch.

## Nutzung über die j-lawyer.org API {#api}

Über die j-lawyer.org REST-API können Dokumente programmatisch konvertiert werden:

```
POST /v6/cases/document/{id}/to-pdf
```

Dies ermöglicht die automatische Konvertierung von Dokumenten in Workflows und Automatisierungen.

## Fehlerbehebung {#fehlerbehebung}

### Verbindung nicht möglich

- Prüfen Sie, ob der Stirling PDF-Container läuft: `docker ps`

- Prüfen Sie die Erreichbarkeit im Browser

- Stellen Sie sicher, dass der Port nicht durch eine Firewall blockiert wird

### Konvertierung schlägt fehl

- Prüfen Sie die Stirling PDF-Logs: `docker logs stirling-pdf`

- Bei Speicherproblemen ggf. dem Container mehr RAM zuweisen

### OCR-Qualität verbessern

- Stellen Sie sicher, dass die Sprachdaten (tessdata) korrekt eingebunden sind

- Verwenden Sie die `latest-fat`-Variante für bessere Schriftunterstützung
