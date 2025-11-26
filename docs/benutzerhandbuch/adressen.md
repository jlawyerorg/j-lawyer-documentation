# Kontakte / Adressen

### Adressen suchen {#suchen}



Im Navigationsbaum am linken Bildschirmrand unter “bearbeiten” bzw. “einsehen” können Sie Adressen über eine Schnellsuche finden. Durchsucht werden
- Name

- Vorname

- Firma

- eigene Felder (alle)

Zusätzlich ist eine Einschränkung über Tags möglich.

### Adresse importieren {#import}



Ab j-lawyer.org Version 1.7 können Adresse im vCard-Format importiert werden. Dabei werden in der Datenbank existierende Kontakte weder geändert noch gelöscht, es werden ausschließlich neue Adressen angelegt. Nach Auswahl einer Importdatei bekommen Sie eine Übersicht der darin enhaltenen Kontakte und können über ein Auswahlfeld exakt bestimmen welche Adressen sie importieren / nicht importieren wollen.

### Beteiligtentypen konfigurieren {#beteiligtentypen}



Je nach Anwendungsgebiet der Software ergibt sich der Bedarf nach spezifischen Beteiligtentypen – bspw. “Gericht”, “Mandant”, “Gegner” oder “Mieter”, “Vermieter” etc. Unter “Einstellungen” - “Modul ‘Adressen’” - “Beteiligtentypen” lassen sich diese Rollen erstellen und konfigurieren. Jeder Typ verfügt über
- Bezeichnung: ein “sprechender” Name, der an verschiedenen Stellen der Anwendung angezeigt wird, bspw. bei der Erstellung von Dokumenten oder dem Versenden von E-Mails und beA-Nachrichten.

- Platzhalter: der Präfix für die in Dokumenten verwendbaren Platzhalter. Vergibt man bspw. für einen Beteiligtentyp “Hausverwalter” den Platzhalter “HV”, so sind dessen Informationen in Dokumenten über {{HV_NAME}} etc. nutzbar.

- Markieren in: eine Farbe, welche für die Darstellung der Beteiligten verwendet wird. So lassen sich bei vielen Beteiligten auf einen Blick verschiedene Typen erkennen.

Da keine Beziehungen zwischen Beteiligtentypen konfiguriert werden, ist eine Prüfung auf Interessenkonflikte nicht einfach umsetzbar. Die Anwendung wird daher informieren, sobald eine Beteiligte / Adresse in verschiedenen Rollen verwendet wird.
