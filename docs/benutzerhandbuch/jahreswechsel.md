# Jahreswechsel {#jahreswechsel}

Zum Jahreswechsel sollten einige Einstellungen in j-lawyer.org geprüft und ggf. angepasst werden. Diese Seite gibt einen Überblick über die wichtigsten Aktionen.

## Belegnummernkreise zurücksetzen {#belegnummernkreise-zuruecksetzen}

Wenn Ihre Belegnummern eine feste Jahreszahl enthalten (z.B. `2024-001`, `2024-002`, ...), sollte zum Jahreswechsel das Nummernschema angepasst werden. Es ist ratsam, im Nummernschema die Platzhalter `yy` oder `yyyy` zu verwenden, statt fester Werte.

Bei Nutzung einer laufenden Nummer (Platzhalter `nnn` o.ä.) sollte diese zurückgesetzt werden (Button "Zurücksetzen").

### Vorgehensweise

1. Öffnen Sie das Menü **Einstellungen** - **Finanzen** - **Belegnummernkreise**
2. Wählen Sie den anzupassenden Nummernkreis aus
3. Passen Sie das **Schema** an (z.B. von `2024-` auf `2025-`)
4. Setzen Sie den **Start-Index** auf `1` (oder `0`, je nach gewünschter Startnummer)
5. Speichern Sie die Änderungen

!!! tip "Tipp"
    Wiederholen Sie diese Schritte für alle verwendeten Belegnummernkreise.

## Aktenzeichenschema prüfen {#aktenzeichenschema-pruefen}

Falls Ihr Aktenzeichenschema eine jahresweise laufende Nummer enthält (z.B. `00001/25`, `00002/25`, ...), sollten Sie prüfen, ob der Start-Index angepasst werden muss.

### Wann ist eine Anpassung erforderlich?

Eine Anpassung ist nur dann erforderlich, wenn Sie:

- Im Vorjahr mit j-lawyer.org begonnen haben und ein **Start-Aktenzeichen** vergeben haben, um mit einer beliebigen laufenden Nummer zu beginnen
- Das Schema eine **jahresweise laufende Nummer** enthält

### Vorgehensweise

1. Öffnen Sie das Menü **Einstellungen** - **Modul 'Akten'** - **Aktenzeichenschema**
2. Prüfen Sie, ob ein erhöhter Start-Index eingetragen ist
3. Setzen Sie den Start auf `1`, damit die Nummerierung im neuen Jahr wieder bei 1 beginnt
4. Speichern Sie die Änderungen

!!! warning "Hinweis"
    Ändern Sie das Schema nur, wenn Sie sicher sind, dass eine jahresweise Nummerierung verwendet wird (Platzhalter `n`). Bei fortlaufender Nummerierung über alle Jahre (Platzhalter `N`) ist keine Anpassung erforderlich.

## Datensicherung prüfen {#datensicherung-pruefen}

Der Jahreswechsel ist ein guter Zeitpunkt, um die Datensicherung zu überprüfen:

- **Automatische Sicherung aktiv?** Prüfen Sie unter **Administration** - **Datensicherung**, ob die automatische Datensicherung aktiviert und korrekt konfiguriert ist.
- **Synchronisation funktionsfähig?** Falls Sie eine Synchronisation auf externe Speicher eingerichtet haben, testen Sie die Erreichbarkeit des Zielsystems.
- **Rücksicherung testen:** Idealerweise sollte mindestens einmal jährlich eine Rücksicherung auf einem Testsystem durchgeführt werden, um sicherzustellen, dass die Sicherungen im Ernstfall verwendbar sind.

Weitere Informationen zur Datensicherung finden Sie im Abschnitt [Datensicherung und -synchronisation](administration.md#datensicherung).

## Checkliste Jahreswechsel {#checkliste}

| Aktion | Erforderlich | Erledigt |
|--------|--------------|----------|
| Belegnummernkreise anpassen | Ja, wenn Jahreszahl im Schema | [ ] |
| Aktenzeichenschema prüfen | Nur bei jahresweiser Nummerierung | [ ] |
| Datensicherung prüfen | Empfohlen | [ ] |
| Rücksicherung testen | Empfohlen | [ ] |
