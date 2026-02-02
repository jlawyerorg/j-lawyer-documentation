# Volltextsuche {#volltextsuche}

j-lawyer beinhaltet eine integrierte Suchmaschine, mit der Sie alle textbasierten Dokumente durchsuchen können. Dabei stehen folgende durchsuchbare Felder zur Verfügung:

| Feld | Beschreibung |
|------|--------------|
| `text` | Text des Dokumentes (Standardfeld) |
| `dateiname` | Dateiname des Dokumentes |
| `autor` | Nutzername des Autors des Dokumentes |
| `akte` | Rubrum der Akte, die das Dokument enthält |
| `az` | Aktenzeichen der Akte, die das Dokument enthält |

## Suchsyntax

Bei einfacher Eingabe eines Suchbegriffs wird immer der Text der Dokumente durchsucht (Standardfeld). Suche in anderen Feldern ist durch Voranstellen des Feldnamens möglich. Bspw. sucht `autor:anwalt1` nach allen Dokumenten, die von einem Nutzer mit dem Nutzernamen „anwalt1" erstellt wurden.

Suchen nach Wortgruppen sind über Hochkommata möglich, bspw. `"Klage gegen Müller"`. Suchen in mehreren Feldern sind durch Nutzung der Operatoren `AND` und `OR` möglich, bspw. `text:klage AND autor:anwalt1` oder einfach `klage AND autor:anwalt1`.

## Wildcards

Es werden Wildcards unterstützt:

- `?` als Wildcard für EIN Zeichen
- `*` als Wildcard für beliebig viele Zeichen

Suche nach `te?t` sucht bspw. nach "text" und "test", `test*` sucht nach allen Wörtern die mit „test" beginnen.

## Volltextsuche deaktivieren / aktivieren

In manchen Situationen kann es hilfreich sein, die Indexierung neuer Dokumente zu unterbinden – bspw. wenn im Rahmen einer Datenmigration in sehr kurzer Zeit viele Dokumente hinzugefügt werden. In diesen Fällen ist das vollständige Indexieren des Datenbestandes zu einem definierten / späteren Zeitpunkt die bessere Lösung.

Zum Deaktivieren der Indexierung neuer Dokumente kann in „Administration" – „Administrator-Konsole" folgender Befehl genutzt werden:

```
setsetting jlawyer.server.searchindex.skip true
```

Zum Aktivieren:

```
setsetting jlawyer.server.searchindex.skip false
```

Die Einstellung beeinflusst ausschließlich neu hinzugefügte Dokumente. Dokumentänderungen oder -löschungen werden weiterhin abgearbeitet (d.h. dass in diesen Situationen weiterhin der Volltextindex aktualisiert wird).

## Volltextindex neu erstellen {#volltextindex-neu-erstellen}

In bestimmten Szenarien kann es notwendig oder sinnvoll sein, den gesamten Volltextindex neu zu erstellen:

- Nach einer **Datenmigration**, bei der die Indexierung vorübergehend deaktiviert war (siehe oben)
- Wenn der Index **beschädigt oder unvollständig** ist, z.B. nach einem Serverausfall
- Wenn die Volltextsuche **keine oder fehlerhafte Ergebnisse** liefert
- Nach einem **Update**, das Änderungen an der Suchindexierung beinhaltet

### Vorgehen

Die Funktion ist über das Menü **Einstellungen** > **Dokumente** > **Volltextsuche** erreichbar. Dieses Menü steht nur Nutzern mit Administratorrechten zur Verfügung.

Im Dialog „Einstellungen Dokumentensuche" werden die Anzahl der Dokumente insgesamt sowie die Anzahl der bereits indexierten Dokumente angezeigt. Über die Schaltfläche **Suchindex neu erfassen** wird die vollständige Neuindexierung gestartet.

!!! warning "Hinweis"
    Die Neuindexierung läuft im Hintergrund auf dem Server. Je nach Anzahl und Größe der Dokumente kann dieser Vorgang sehr lange dauern. Während der Neuindexierung kann normal weitergearbeitet werden – die Suchergebnisse sind jedoch erst nach Abschluss des Vorgangs wieder vollständig. Grundsätzlich ist eine erneute Indexerstellung in "arbeitsfreien" Zeiten am sinnvollsten (bspw. nachts).
