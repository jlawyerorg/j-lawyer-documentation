# Externe Programme {#externe-programme}

j-lawyer geht wie folgt vor, um Dokumente zum Einsehen oder Bearbeiten zu öffnen:

- wenn das Dateiformat von LibreOffice unterstützt wird, dann wird es mit LibreOffice geöffnet
- alle anderen Dateiformate werden mit der im Betriebssystem definierten Standardapplikation geöffnet

Es kann Situationen geben, wo von LibreOffice unterstützte Formate zwingend mit einer anderen Applikation geöffnet werden sollen. Dazu gibt es unter „Einstellungen" – „Dokumente" – „externe Programme" entsprechende Konfigurationen.

## Einrichtung {#einrichtung-externe-programme}

Die Konfiguration erfolgt in folgenden Schritten:

1. **Programm hinzufügen**: Im Eingabefeld links einen frei wählbaren Namen eingeben (z.B. „Adobe PDF Reader" oder „Word") und mit „Hinzufügen" bestätigen. Das Programm erscheint daraufhin in der Liste.

2. **Programmbezeichnung**: Im rechten Bereich „Einstellungen" kann der Name des Programms geändert werden.

3. **Dateiendung(en)**: Die zu behandelnden Dateitypen werden ohne führenden Punkt angegeben. Mehrere Dateitypen können durch Komma getrennt werden, z.B. `pdf,html,jpg`.

4. **Ausführbare Datei**: Über den „…"-Knopf wird die ausführbare Datei des gewünschten Programms ausgewählt.

5. **Parameter (Schreibzugriff)**: Parameter, die beim Öffnen eines Dokuments zum Bearbeiten übergeben werden. Der voreingestellte Parameter `DATEINAME` wird von j-lawyer automatisch durch den tatsächlichen Dateipfad ersetzt und sollte in jedem Fall erhalten bleiben.

6. **Parameter (Lesezugriff)**: Parameter, die beim Öffnen eines Dokuments im Nur-Lese-Modus übergeben werden.

7. **Standardprogramm**: Ist diese Option aktiviert, wird das Programm bei Doppelklick auf ein passendes Dokument geöffnet. Ist die Option nicht aktiviert, ist das Programm nur über das Kontextmenü „Öffnen mit…" aufrufbar. So können für einen Dateityp mehrere Anwendungen konfiguriert werden, bspw. für PDFs einen schnell öffnenden Reader als Standardprogramm und eine weitere Anwendung für die PDF-Bearbeitung über das Kontextmenü.

8. **Einstellung testen**: Über diesen Knopf kann eine Datei ausgewählt werden, um die Konfiguration direkt zu prüfen.

Abschließend die Konfiguration mit „Speichern" sichern. Konfigurierte Programme können per Rechtsklick in der Liste und „Löschen" wieder entfernt werden.

## macOS

Auf Mac OS gibt es einen "Universalstarter" namens "open", der zum Öffnen von Dateien mit vorhandenen Programmen verwendet werden kann. Zu finden ist er unter `/usr/bin/open`, er erwartet als Parameter unter anderem auch den Namen des auszuführenden Programmes. Um bspw. PNG-Dateien mit "Preview" bzgw. "Vorschau" zu öffnen, lauten die Einstellungen im j-lawyer.org Client wie folgt:

![Abbildung 13](../../images/j-lawyer-org-UserGuide-de-019.png)

## Windows

Ein ähnliches "Universalstarter"-Verhalten kann unter Windows mit `cmd.exe` und dem `start`-Befehl erreicht werden. Dies ist insbesondere auch dann hilfreich, wenn bspw. Microsoft Word für .doc / .docx – Dokumente verwendet werden soll:

![Abbildung 14](../../images/j-lawyer-org-UserGuide-de-020.png)

!!! info "Hinweis"
    Sollte es mit den Einstellungen oben Probleme beim Öffnen von Dateien mit Leerzeichen im Dateinamen geben, so sind die Parameter zu ändern von `/c start /wait DATEINAME` nach `/c DATEINAME`.

!!! warning "Hinweis"
    Die Einstellung ist an jedem Arbeitsplatz durchzuführen. Sie wird im Nutzerprofil gespeichert.
