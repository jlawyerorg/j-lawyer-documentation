# Volltextsuche {#volltextsuche}

j-lawyer beinhaltet eine integrierte Suchmaschine, mit der Sie alle textbasierten Dokumente durchsuchen können. Die Suche ist im Navigationsbereich unter **Dokumente** → **Suche** zu finden.

## Inhaltssuche {#inhaltssuche}

Bei einfacher Eingabe eines Suchbegriffs werden der Text der Dokumente sowie deren Bezeichnung und Schlagworte durchsucht. Mehrere Wörter werden ODER-verknüpft – es werden also Dokumente gefunden, die mindestens eines der Wörter enthalten. Die Treffer sind nach Relevanz sortiert; die Prozentangabe zeigt die Relevanz im Verhältnis zum besten Treffer.

!!! info "Einschränkungen der Inhaltssuche"
    Wortgruppen in Anführungszeichen, die Operatoren `AND`/`OR`/`NOT`, Ausschlüsse mit vorangestelltem Minus sowie Platzhalter (`*`, `?`) werden in der Inhaltssuche nicht unterstützt. Diese Zeichen werden als normaler Text behandelt.

## Feldsuche {#feldsuche}

Soll nicht im Inhalt, sondern gezielt in einem bestimmten Feld gesucht werden, wird das Feld über das Auswahlfeld neben dem Suchfeld gewählt. Alternativ kann der Feldname dem Suchbegriff direkt vorangestellt werden:

| Auswahl | Präfix | Durchsucht |
|---------|--------|------------|
| Inhalt | `text:` (optional) | Text des Dokuments (Standard) |
| Dateiname | `dateiname:` | Dateiname des Dokuments |
| Aktenname | `akte:` | Kurzrubrum der Akte, die das Dokument enthält |
| Aktenzeichen | `az:` | Aktenzeichen der Akte, die das Dokument enthält |
| Bezeichnung | `bezeichnung:` | Bezeichnung des Dokuments |
| Schlagwort | `schlagwort:` | Schlagworte des Dokuments – jedes Schlagwort wird einzeln geprüft |
| Von/An | `von:` | Absender bzw. Empfänger des Dokuments |

Ein selbst eingetipptes Präfix hat Vorrang vor der Auswahl im Auswahlfeld. Es kann jeweils nur **ein** Feld durchsucht werden; eine Kombination mehrerer Felder ist nicht möglich.

### Teiltreffer, Platzhalter und exakte Suche

Feldsuchen ignorieren Groß- und Kleinschreibung. Der gesamte Text nach dem Doppelpunkt ist der Suchwert. Für alle Felder außer `text:` gilt:

| Eingabe | Ergebnis |
|---------|----------|
| `dateiname:kostennote` | jeder Dateiname, der „kostennote" enthält |
| `dateiname:"Kostennote.pdf"` | nur Dokumente mit exakt diesem Dateinamen |
| `dateiname:*2026-08-??_Quittung*` | Platzhalter: `*` steht für beliebig viele Zeichen, `?` für genau ein Zeichen |
| `dateiname:"*2026-08-??_Quittung*"` | identisch – Platzhalter wirken auch innerhalb von Anführungszeichen |
| `az:035-2022` | alle Dokumente in Akten, deren Aktenzeichen „035-2022" enthält |
| `schlagwort:"Kündigung"` | alle Dokumente mit dem Schlagwort „Kündigung" (exakt) |
| `von:müller` | alle Dokumente, deren Von/An „müller" enthält |

Da Feldsuchen keine Relevanz berechnen, wird bei ihren Treffern keine Prozentangabe angezeigt.

!!! tip "Hilfe im Programm"
    Ein Klick auf das Fragezeichen-Symbol neben dem Suchfeld öffnet eine Übersicht der Suchsyntax.

!!! warning "Neuaufbau des Suchindex nach dem Update auf Version 3.6"
    Die Feldsuche nutzt zusätzliche Felder im Suchindex. Sie findet daher nur Dokumente, die mit Version 3.6 oder später indexiert wurden. Nach dem Update ist einmalig ein [Neuaufbau des Volltextindex](#volltextindex-neu-erstellen) erforderlich.

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
- Nach dem Update auf **Version 3.6**, damit die [Feldsuche](#feldsuche) für alle Dokumente funktioniert

### Vorgehen

Die Funktion ist über das Menü **Einstellungen** > **Dokumente** > **Volltextsuche** erreichbar. Dieses Menü steht nur Nutzern mit Administratorrechten zur Verfügung.

Im Dialog „Einstellungen Dokumentensuche" werden die Anzahl der Dokumente insgesamt sowie die Anzahl der bereits indexierten Dokumente angezeigt. Über die Schaltfläche **Suchindex neu erfassen** wird die vollständige Neuindexierung gestartet.

!!! warning "Hinweis"
    Die Neuindexierung läuft im Hintergrund auf dem Server. Je nach Anzahl und Größe der Dokumente kann dieser Vorgang sehr lange dauern. Während der Neuindexierung kann normal weitergearbeitet werden – die Suchergebnisse sind jedoch erst nach Abschluss des Vorgangs wieder vollständig. Grundsätzlich ist eine erneute Indexerstellung in "arbeitsfreien" Zeiten am sinnvollsten (bspw. nachts).
