# Forderungskonto

Das Forderungskonto ermöglicht eine strukturierte Verwaltung von Forderungen innerhalb einer Akte. Es bietet die Möglichkeit, Hauptforderungen, Kosten und Zinsen übersichtlich zu erfassen, Zahlungseingänge zu buchen und den aktuellen Forderungsstand jederzeit einzusehen.

## Grundlegender Ablauf {#grundlegender-ablauf}

Die Arbeit mit dem Forderungskonto erfolgt in zwei aufeinander aufbauenden Schritten:

```
┌─────────────────────────────────────────────────────────────────────┐
│  1. STRUKTUR ANLEGEN                                                │
│     ┌──────────────────┐    ┌──────────────────┐                    │
│     │ Forderungskonto  │───▶│    Positionen    │                    │
│     │    erstellen     │    │    hinzufügen    │                    │
│     └──────────────────┘    └──────────────────┘                    │
│                                      │                              │
│                                      ▼                              │
│                             ┌──────────────────┐                    │
│                             │   Zinsregeln     │                    │
│                             │   konfigurieren  │                    │
│                             └──────────────────┘                    │
├─────────────────────────────────────────────────────────────────────┤
│  2. BUCHUNGEN ERFASSEN                                              │
│     ┌──────────────────┐    ┌──────────────────┐                    │
│     │  Hauptforderung  │    │     Kosten       │                    │
│     │     buchen       │    │     buchen       │                    │
│     └──────────────────┘    └──────────────────┘                    │
│                                      │                              │
│                                      ▼                              │
│     ┌──────────────────┐    ┌──────────────────┐                    │
│     │    Zahlungen     │    │     Zinsen       │                    │
│     │     buchen       │    │   berechnen      │                    │
│     └──────────────────┘    └──────────────────┘                    │
└─────────────────────────────────────────────────────────────────────┘
```

**Schritt 1: Struktur anlegen**

Bevor Buchungen erfasst werden können, muss zunächst die Grundstruktur des Forderungskontos aufgebaut werden:

1. **Forderungskonto erstellen** - Ein neues Forderungskonto innerhalb der Akte anlegen
2. **Positionen definieren** - Die einzelnen Forderungsteile (Hauptforderung, Kosten) als Positionen anlegen
3. **Zinsregeln festlegen** - Für verzinsliche Positionen die Zinskonditionen konfigurieren

**Schritt 2: Buchungen erfassen**

Erst nachdem Positionen vorhanden sind, können Buchungen vorgenommen werden:

1. **Forderungsbeträge buchen** - Die eigentlichen Forderungssummen den Positionen zuordnen
2. **Kosten erfassen** - Zusätzlich anfallende Kosten buchen
3. **Zahlungseingänge verbuchen** - Eingehende Zahlungen des Schuldners erfassen
4. **Zinsen berechnen** - Aufgelaufene Zinsen berechnen und buchen

!!! info "Wichtig"
    Buchungen können nur auf bestehende Positionen gebucht werden. Daher müssen immer zuerst die Positionen angelegt werden, bevor Buchungen erfasst werden können.

## Übersicht {#uebersicht}

Ein Forderungskonto besteht aus mehreren Bausteinen:

| Baustein | Beschreibung |
|----------|--------------|
| Forderungskonto | Container für alle Forderungspositionen einer Akte |
| Position | Einzelne Forderungsteile (Hauptforderung, Kosten) |
| Buchung | Einzelne Transaktionen (Forderungen, Zahlungen, Zinsen, Korrekturen) |
| Zinsregel | Definition der Verzinsung im Zeitverlauf |

### Positionen {#positionen}

Jedes Forderungskonto kann mehrere Positionen enthalten. Folgende Typen sind verfügbar:

| Typ | Beschreibung |
|-----|--------------|
| Hauptforderung | Die eigentliche Forderungssumme |
| Kosten (verzinslich) | Nebenkosten, die verzinst werden |
| Kosten (unverzinslich) | Nebenkosten ohne Verzinsung |

Eine Position ist verzinslich, wenn mindestens eine Zinsregel für sie definiert ist.

### Buchungsarten {#buchungsarten}

Innerhalb eines Forderungskontos können verschiedene Buchungsarten erfasst werden:

| Buchungsart | Beschreibung |
|-------------|--------------|
| Hauptforderung | Buchung der ursprünglichen Forderungssumme |
| Zinsen | Berechnete oder manuell erfasste Zinsbeträge |
| Kosten | Zusätzliche Kosten (Anwaltsgebühren, Gerichtskosten etc.) |
| Zahlung | Eingegangene Zahlungen des Schuldners |
| Korrekturbuchung | Korrekturen bestehender Buchungen |

Jede Buchung enthält:

- Datum der Buchung

- Betrag

- Beschreibung

- Optionaler Kommentar

- Zuordnung zu einer Position (optional)

## Zinsverwaltung {#zinsverwaltung}

### Zinsregeln {#zinsregeln}

Für jede Position können Zinsregeln definiert werden, die festlegen, wie die Verzinsung berechnet wird. Zinsregeln sind zeitlich gestaffelt und können sich im Laufe der Zeit ändern.

Zwei Zinsarten werden unterstützt:

| Zinsart | Beschreibung |
|---------|--------------|
| Fester Zinssatz | Ein fixer prozentualer Zinssatz |
| Basiszinsbezogen | Zinssatz basierend auf dem Basiszinssatz plus Aufschlag |

### Basiszinsbezogene Verzinsung {#basiszins}

Bei der basiszinsbezogenen Verzinsung wird der aktuelle Basiszinssatz der Deutschen Bundesbank als Grundlage verwendet und ein Aufschlag (Marge) hinzugerechnet. Dies entspricht der gesetzlichen Regelung für Verzugszinsen nach § 288 BGB.

Beispiel: Basiszinssatz 3,62 % + 5 Prozentpunkte = 8,62 % Verzugszinsen

### Effektiver Zinssatz {#effektiver-zinssatz}

Der effektive Zinssatz wird wie folgt berechnet:

- Bei festem Zinssatz: Der konfigurierte Prozentsatz wird direkt verwendet

- Bei basiszinsbezogenem Zinssatz: Basiszinssatz + konfigurierte Marge

## Saldenübersicht {#salden}

Das Forderungskonto berechnet automatisch folgende Summen:

| Saldo | Beschreibung |
|-------|--------------|
| Gesamte Hauptforderung | Summe aller Hauptforderungsbeträge |
| Gesamte Kosten | Summe aller Kostenbeträge |
| Zinsen auf Hauptforderung | Berechnete/gebuchte Zinsen auf die Hauptforderung |
| Zinsen auf Kosten | Berechnete/gebuchte Zinsen auf verzinsliche Kosten |
| Gesamte Zahlungen | Summe aller eingegangenen Zahlungen |
| Offene Forderung | Verbleibender Forderungsbetrag nach Abzug der Zahlungen |

### Positionssalden {#positionssalden}

Für jede Position werden einzeln berechnet:

- Ursprünglicher Betrag (Hauptsumme)

- Aufgelaufene Zinsen

- Erhaltene Zahlungen

- Offene Hauptsumme

- Offene Zinsen

- Gesamter offener Saldo

- Status (vollständig bezahlt oder offen)

## Zahlungsverteilung {#zahlungsverteilung}

Bei Eingang einer Zahlung wird geprüft, wie diese auf die verschiedenen Positionen und deren Zinsen verteilt wird. Die Software unterstützt dabei die Berechnung von Verteilungsvorschlägen gemäß gesetzlicher Verrechnungsregeln.

## Anwendung in der Praxis {#praxis}

### Forderungskonto anlegen {#anlegen}

Ein Forderungskonto wird innerhalb einer Akte angelegt und erhält einen Namen sowie eine optionale Beschreibung.

### Positionen hinzufügen {#positionen-hinzufuegen}

Nach Anlage des Kontos werden die einzelnen Positionen definiert:

1. Hauptforderung mit dem ursprünglichen Forderungsbetrag

2. Optional: Verzinsliche Kosten (z.B. vorgerichtliche Anwaltskosten)

3. Optional: Unverzinsliche Kosten

### Zinsregeln konfigurieren {#zinsregeln-konfigurieren}

Für verzinsliche Positionen werden Zinsregeln angelegt:

1. Gültig-ab-Datum festlegen (z.B. Verzugseintritt)

2. Zinsart wählen (fest oder basiszinsbezogen)

3. Bei festem Zinssatz: Prozentsatz eingeben

4. Bei basiszinsbezogenem Zinssatz: Aufschlag (Marge) eingeben

### Buchungen erfassen {#buchungen-erfassen}

Im laufenden Betrieb werden Buchungen erfasst:

- Zahlungseingänge buchen

- Zinsen berechnen und buchen

- Zusätzliche Kosten erfassen

- Bei Bedarf Korrekturbuchungen vornehmen

### Forderungsstand abrufen {#forderungsstand}

Jederzeit kann der aktuelle Forderungsstand abgerufen werden mit:

- Gesamtübersicht aller Salden

- Aufschlüsselung nach Positionen

- Historische Entwicklung der Buchungen
