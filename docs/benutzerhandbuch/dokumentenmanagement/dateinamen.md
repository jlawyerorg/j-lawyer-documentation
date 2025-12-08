# Dateinamen konfigurieren {#dateinamen}

Im Menüpunkt „Einstellungen" – „Dokumente" – „Dateinamen" lassen sich ein oder mehrere Dateinamenskonventionen konfigurieren.

![Abbildung 9](../../images/j-lawyer-org-UserGuide-de-015.png)

Mit den Voreinstellungen wird j-lawyer.org Dateinamen in dieser Form nutzen:

```
2024-10-30_Schriftsatz.odt
```

Im Einstellungsdialog lassen sich sowohl das Standardschema anpassen, als auch weitere Bildungsvorschriften für Dateinamen definieren. Dateinamen können dabei aus Platzhaltern generiert werden:

- Platzhalter für Zeitangaben – in eckigen Klammern
    - y = Jahr
    - m = Monat
    - d = Tag
    - M = Minute
    - H = Stunde
- Platzhalter für ursprünglichen Dateinamen
    - DATEINAME
- Weitere Platzhalter analog Vorlagensystem
    - bspw. {{MANDANT_NAME}}
    - Für Dokumente, die aus einem Beleg heraus erstellt werden, kann die Belegnummer (sowie weiter BEL-Platzhalter) in den Dateinamen übernommen werden, bspw. die Belegnummer per {{BEL_NR}}

Es sollte auf Groß- und Kleinschreibung geachtet werden.

## Beispiele {#dateinamen-beispiele}

**Beispielschema für erstellte Vollmachten:**

```
[yyyy][mm][dd]_Vollmacht_{{MANDANT_NAME}}
```

Wird zu:

```
20241030_Vollmacht_Müller.odt
```

**Beispiel für erhaltene E-Mail im Verkehrsrecht:**

```
[yyyy][mm][dd]_DATEINAME_{{AKTE_ZEICHEN}}_{{MANDANT_NAME}}-vs-{{GEGNER_NAME}}_{{VRKHR_KENNZEICHEN}}
```

wird zu:

```
20241030_Anfrage Schadenregulierung_003-24_Müller-vs-Meier_HH-XY 1234.eml
```

Nur exakt ein Schema kann das „Standardschema" sein (Option „als Standard verwenden" ist aktiv).

Im Dialog zur Zuordnung von Dokumenten kann das Dateinamensschema für alle Dokumente oder einzelne Dokumente angepasst werden:

![Abbildung 10](../../images/j-lawyer-org-UserGuide-de-016.png)

Eine entsprechende Einstellmöglichkeit gibt es im Rahmen der Erstellung von Dokumenten aus einer Vorlage.
