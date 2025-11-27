# Zeiterfassung {#zeiterfassung}



Die Konfiguration und das Buchen von Zeiten sind als Videotutorial in der j-lawyer.ACADEMY verfügbar: <https://j-lawyer.cloud/j-lawyer-academy/>

## Projekt- / aktenbezogene Stundensätze



Alle relevanten Stundensätze lassen sich im Menü unter „Einstellungen" – „Zeiterfassung" – „Zeiterfassungspositionen" verwalten. Die dort hinterlegten Positionen oder Stundensätze lassen sich dann bei Buchung einer Zeit auswählen.

In manchen Fällen kann es sinnvoll sein, die Menge der auswählbaren Positionen für ein Projekt zu beschränken – bspw. weil man ausschließen möchte, versehentlich einen Stundensatz zu wählen, der mit dem Auftraggeber nicht vereinbart wurde. Dazu kann direkt im Zeiterfassungsprojekt (Akte öffnen, Tab „Finanzen", Sub-Tab „Zeiterfassung", dort ein vorhandenes Projekt öffnen) eine entsprechende Beschränkung konfiguriert werden:

![Abbildung 23](../images/j-lawyer-org-UserGuide-de-030.png)


## Projektumfang/-leistung beschränken



Sofern benötigt, lässt sich die Leistung / lassen sich die Kosten eines Zeiterfassungsprojektes beschränken, bspw. weil ein Auftraggeber nur ein Kontingent von x Euro in Auftrag gegeben hat.

Dazu wird direkt im Projekt ein Netto-Limit hinterlegt. Es spielt also keine Rolle, mit welchen (auch unterschiedlichen) Stundensätzen gebucht wird – die Anwendung wird dabei unterstützen, dass nicht mehr geleistet als bestellt wurde.

![Abbildung 25](../images/j-lawyer-org-UserGuide-de-031.png)


Nach Aktivierung eines Limits werden sowohl in der Akte als auch beim Buchen von Zeiten Hinweise in Form kleiner Diagramme mit Farbgebung angezeigt, bspw. wie folgt:

![Abbildung 26](../images/j-lawyer-org-UserGuide-de-032.png)


Verweilt man mit dem Mauszeiger auf dem Diagramm, werden weitere Informationen eingeblendet, bspw. die prozentuale Abarbeitung und das absolute Limit.

Wird ein Limit erreicht oder überschritten, so wird der „Finanzen"-Tab der Akte rot eingefärbt.

## Zeiten erfassen



Zeiten können erfasst werden, indem in der Akte oben rechts auf die Stoppuhr oder – unabhängig von der aktuellen Ansicht – in der Fußzeile der Anwendung auf das Stoppuhrsymbol geklickt wird. Danach im Popup links das zu verwendende Zeiterfassungsprojekt durch Klick auf das Playzeichen in die rechte Spalte zur Bearbeitung hinzufügen. Dort kann etwa durch Klick auf das große grüne Playzeichen die Zeit gestartet, später gestoppt und auch noch verändert werden durch Klick in das Datums- und Uhrzeitenfeld, um ordnungsgemäße Korrekturen vorzunehmen. Der korrekte Stundensatz kann ausgewählt werden und darunter eine Beschreibung hinzugefügt werden, die in das Rechnungsdokument übernommen werden kann (der Mandant also ggf. sieht). Mit einem Klick auf die Diskette rechts vom Eintrag speichert man diesen.

Soll keine Erfassung durch Stoppuhr genutzt, sondern die Zeit manuell angegeben werden, so gibt es die Möglichkeit, oberhalb der Beschreibung einer zu erfassenden Zeit eine Eingabe in der Form 2h45m (Beispiel für 2 Stunden und 45 Minuten) zu tätigen und mit Enter zu bestätigen.

### Eingabeformat für manuelle Zeiterfassung

Bei der manuellen Zeiterfassung können Zeiten in verschiedenen Formaten eingegeben werden:

| Format | Beispiel | Bedeutung |
|--------|----------|-----------|
| `Xh` | `2h` | 2 Stunden |
| `Xm` | `45m` | 45 Minuten |
| `XhYm` | `2h45m` | 2 Stunden und 45 Minuten |

Die Eingabe wird mit Enter bestätigt.

### Eingabeformat ohne Einheit konfigurieren

Wird eine reine Zahl ohne Einheit eingegeben (z.B. `30` statt `30m`), bestimmt eine Einstellung, wie diese interpretiert wird. Die Konfiguration erfolgt über das Menü **Einstellungen** → **Zeiterfassung** → **Eingabeformat**.

| Einstellung | Verhalten |
|-------------|-----------|
| als Minuten gewertet | Eine Eingabe von `30` wird als 30 Minuten interpretiert |
| als Stunden gewertet | Eine Eingabe von `2` wird als 2 Stunden interpretiert |
| abgelehnt | Eingaben ohne Einheit werden nicht akzeptiert |

Die Standardeinstellung ist „als Minuten gewertet".

Ein Tooltip am Eingabefeld zeigt an, welche Einstellung aktuell aktiv ist.

## Zeiten in anderes Projekt verschieben

Erfasste Zeiten können nachträglich in ein anderes Zeiterfassungsprojekt verschoben werden – auch aktenübergreifend. Dies ist hilfreich, wenn Zeiten versehentlich im falschen Projekt erfasst wurden oder eine nachträgliche Umorganisation notwendig ist.

### Vorgehensweise

1. Öffnen Sie die Akte und navigieren Sie zum Tab **Zeiten**
2. Klicken Sie beim gewünschten Projekt auf den Button **Zeiten in anderes Projekt verschieben** (Symbol mit zwei Dokumenten)
3. Es öffnet sich ein Dialog mit allen noch nicht abgerechneten Zeiteinträgen des Projekts
4. Wählen Sie die zu verschiebenden Einträge aus (Checkbox in der ersten Spalte)
5. Klicken Sie auf **in anderes Projekt verschieben**
6. Es erscheint ein Menü mit allen offenen Zeiterfassungsprojekten aus allen Akten
7. Wählen Sie das Zielprojekt aus

### Hinweise

- Nur Zeiteinträge, die noch keiner Rechnung zugeordnet wurden, können verschoben werden
- Das aktuelle Projekt wird in der Auswahlliste nicht angezeigt (kein Transfer in dasselbe Projekt)
- Die Verschiebung erfolgt aktenübergreifend – es werden alle offenen Projekte aller Akten angezeigt
- Im Auswahlmenü wird neben dem Projektnamen auch das Aktenzeichen und der Aktenname angezeigt, um das Zielprojekt eindeutig zu identifizieren
