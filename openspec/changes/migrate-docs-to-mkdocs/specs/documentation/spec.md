## ADDED Requirements

### Requirement: MkDocs-basierte Dokumentation

Das Dokumentationssystem SHALL auf MkDocs mit Material Theme basieren und Markdown als Quellformat verwenden.

#### Scenario: Lokale Entwicklung

- **WHEN** ein Entwickler `mkdocs serve` ausführt
- **THEN** wird ein lokaler Server mit Live-Reload gestartet
- **AND** Änderungen an Markdown-Dateien werden sofort angezeigt

#### Scenario: Dokumentation bearbeiten

- **WHEN** ein Benutzer eine Markdown-Datei im `docs/` Verzeichnis bearbeitet
- **THEN** kann die Änderung in Git versioniert werden
- **AND** der Inhalt ist lesbar ohne spezielle Tools

### Requirement: Volltextsuche

Das Dokumentationssystem SHALL eine clientseitige Volltextsuche mit deutscher Sprachunterstützung bereitstellen.

#### Scenario: Suche nach Begriff

- **WHEN** ein Benutzer einen Suchbegriff in die Suchleiste eingibt
- **THEN** werden passende Ergebnisse aus allen Dokumentationsseiten angezeigt
- **AND** die Suche funktioniert ohne Server-Requests

### Requirement: Stabile URLs

Das Dokumentationssystem SHALL stabile, verlinkbare URLs bereitstellen, die auch bei Erweiterung der Dokumentation erhalten bleiben.

#### Scenario: Dateibasierte URLs

- **WHEN** eine Datei `docs/installation/server.md` existiert
- **THEN** ist diese unter der URL `/installation/server/` erreichbar

#### Scenario: Explizite Anker

- **WHEN** eine Überschrift mit `{#mein-anker}` annotiert ist
- **THEN** kann dieser Abschnitt über `#mein-anker` direkt verlinkt werden
- **AND** der Anker bleibt stabil auch wenn die Überschrift geändert wird

### Requirement: PDF-Export

Das Dokumentationssystem SHALL einen PDF-Export der gesamten Dokumentation unterstützen.

#### Scenario: PDF generieren

- **WHEN** der Build-Prozess ausgeführt wird
- **THEN** wird eine PDF-Datei der Dokumentation erstellt
- **AND** die PDF enthält Cover, Inhaltsverzeichnis und alle Seiten

### Requirement: Automatisierter Build

Das Dokumentationssystem SHALL über GitHub Actions automatisch gebaut und auf GitHub Pages veröffentlicht werden.

#### Scenario: Push auf master Branch

- **WHEN** Änderungen auf den master Branch gepusht werden
- **THEN** wird automatisch ein GitHub Actions Workflow gestartet
- **AND** die Dokumentation wird auf GitHub Pages veröffentlicht

#### Scenario: Build-Fehler

- **WHEN** der Build fehlschlägt
- **THEN** wird der fehlerhafte Commit nicht auf GitHub Pages veröffentlicht
- **AND** der Workflow-Status zeigt den Fehler an

### Requirement: Deutsche Spracheinstellungen

Das Dokumentationssystem SHALL deutsche Spracheinstellungen für UI und Suche verwenden.

#### Scenario: UI-Sprache

- **WHEN** ein Benutzer die Dokumentation öffnet
- **THEN** werden alle UI-Elemente (Navigation, Suche, Footer) auf Deutsch angezeigt

### Requirement: Bildintegration

Das Dokumentationssystem SHALL Bilder unterstützen, die aus den .fodt-Dateien extrahiert wurden.

#### Scenario: Bild einbinden

- **WHEN** ein Bild im `docs/images/` Verzeichnis liegt
- **THEN** kann es über Markdown-Syntax eingebunden werden
- **AND** das Bild wird korrekt in HTML und PDF angezeigt
