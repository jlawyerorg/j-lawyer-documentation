# Schnittstellen und Integration

Ein Großteil der Funktionalität des j-lawyer.org-Servers ist über eine RESTful API nutzbar. Daten werden in Form von JSON über http(s) ausgetauscht. Eine Nutzung der Schnittstellle ist unabhängig von der verwendeten Programmiersprache möglich. Auch ein einfaches Scripting ist möglich.

Zusätzlich können externe Anwendungen über sogenannte „Web Hooks“ aktiv benachrichtigt werden, sobald ein Ereignis (bspw. Änderung bestimmter Daten) in j-lawyer.org auftritt.

### REST API: Swagger UI {#rest-api}



Die API liefert auch eine interaktiv nutzbare Weboberfläche aus, welche unter <http://localhost:8080/j-lawyer-io/swagger-ui/> aufgerufen werden kann (Host / Port ggf. anpassen). Eine Anmeldung ist mit den Zugangsdaten eines Nutzers der Kanzleisoftware möglich.

Die Swagger UI liefert sowohl eine vollständige Dokumentation der Schnittstellen, als auch eine Möglichkeit die Aufrufe interaktiv im Browser zu auszuführen. Auch werden vollständige Kommandozeilenaufrufe geliefert. Wer sich bestimmte Schritte per Skript automatisieren möchte, kann diese Kommandozeilen direkt nutzen, bspw in Shell- oder Batchscripts.

### REST API: Security



Eine Nutzung der Schnittstelle ist grundsätzlich über HTTP Basic-Authentifizierung möglich. Es müssen die Zugangsdaten eines Nutzers der Kanzleisoftware angegeben werden. So ist sichergestellt, dass auch bei Nutzung der Schnittstelle – insbesondere beim Ändern von Daten – die Berechtigungen berücksichtigt werden, und die automatisch geführte Aktenhistorie auch Schnittstellenzugriffe mit dem richtigen Nutzer dokumentieren kann.

### REST API: Umgang mit großen Dokumenten {#rest-api-grosse-dokumente}

Beim Upload großer Dokumente über die REST API kann es zu Fehlern kommen, wenn die Dateigröße das Standard-Limit von Wildfly überschreitet. Der Server lehnt dann die Anfrage ab.

Um größere Dokumente zu ermöglichen, muss das `max-post-size`-Attribut an den HTTP-Listenern in der Wildfly-Konfiguration angepasst werden:

1. Die Datei `standalone.xml` im Wildfly-Konfigurationsverzeichnis öffnen
2. Die Einstellungen für `http-listener` und `https-listener` anpassen (max-post-size - Attribut anpassen, ggf. hinzufügen):

```xml
<http-listener name="default" socket-binding="http" max-post-size="524288000" redirect-socket="https" enable-http2="true"/>
<https-listener name="https" socket-binding="https" max-post-size="524288000" ssl-context="applicationSSC" enable-http2="true"/>

```

Der Wert wird in Bytes angegeben. Im Beispiel oben sind 500 MB (524288000 Bytes) konfiguriert.

Nach der Änderung muss der Wildfly-Server neu gestartet werden.

### Web Hooks {#webhooks}



Unter „Administration“ – „Web Hooks“ können beliebig viele Benachrichtigungen für Drittapplikationen konfiguriert werden.

Unterstützt werden folgende Ereignistypen:
- DOCUMENT_CREATED: Dokument erstellt

- DOCUMENT_UPDATED: Dokument geändert

- DOCUMENT_REMOVED: Dokument gelöscht

- ADDRESS_CREATED: Adresse erstellt

- ADDRESS_UPDATED: Adresse geändert

- ADDRESS_REMOVED: Adresse gelöscht

- CASE_CREATED: Akte erstellt

- CASE_UPDATED: Akte geändert

- CASE_REMOVED: Akte gelöscht

- ADDRESSTAG_CHANGED: Etikett an Adresse aktiviert / deaktiviert

- CASETAG_CHANGED: Etikett an Akte aktiviert / deaktiviert

- DOCUMENTTAG_CHANGED: Etikett an Dokument aktiviert / deaktiviert

- CASE_FORM_UPDATED: Falldatenblatt geändert

Für jeden Ereignistyp sind beliebig viele Hooks möglich. Daten zum Ereignis werden im JSON-Format per HTTP POST gesendet.

Beispieldokumente:

```json
{
  "hookType": "ADDRESS_CREATED",
  "addressId": "21f3f7b07f0001012cdc167fafd982c3"
}
```

```json
{
  "hookType": "ADDRESS_UPDATED",
  "addressId": "21f3f7b07f0001012cdc167fafd982c3"
}
```

```json
{
  "active": true,
  "tagName": "abweisen",
  "hookType": "ADDRESSTAG_CHANGED",
  "addressId": "21f3f7b07f0001012cdc167fafd982c3"
}
```

```json
{
  "active": false,
  "tagName": "abweisen",
  "hookType": "ADDRESSTAG_CHANGED",
  "addressId": "21f3f7b07f0001012cdc167fafd982c3"
}
```

```json
{
  "hookType": "ADDRESS_REMOVED",
  "addressId": "21f3f7b07f0001012cdc167fafd982c3"
}
```

```json
{
  "caseId": "21f8bd6c7f0001010d3542018c45d739",
  "hookType": "CASE_CREATED"
}
```

```json
{
  "caseId": "21f8bd6c7f0001010d3542018c45d739",
  "hookType": "CASE_UPDATED"
}
```

```json
{
  "caseId": "21f8bd6c7f0001010d3542018c45d739",
  "documentId": "21f9f1b97f000101574dffb8d1fce05f",
  "documentName": "2022-01-03_Notiz.html",
  "hookType": "DOCUMENT_CREATED"
}
```

```json
{
  "caseId": "21f8bd6c7f0001010d3542018c45d739",
  "active": true,
  "documentId": "21f9f1b97f000101574dffb8d1fce05f",
  "tagName": "Korrektur RA Müller",
  "hookType": "DOCUMENTTAG_CHANGED"
}
```

```json
{
  "caseId": "21f8bd6c7f0001010d3542018c45d739",
  "active": false,
  "documentId": "21f9f1b97f000101574dffb8d1fce05f",
  "tagName": "Korrektur RA Müller",
  "hookType": "DOCUMENTTAG_CHANGED"
}
```

```json
{
  "caseId": "21f8bd6c7f0001010d3542018c45d739",
  "documentId": "21f9f1b97f000101574dffb8d1fce05f",
  "documentName": "2022-01-03_Notiz.html",
  "hookType": "DOCUMENT_UPDATED"
}
```

```json
{
  "caseId": "21f8bd6c7f0001010d3542018c45d739",
  "documentId": "21f9f1b97f000101574dffb8d1fce05f",
  "documentName": "2022-01-03_Notiz.html",
  "hookType": "DOCUMENT_REMOVED"
}
```

```json
{
  "caseId": "21f8bd6c7f0001010d3542018c45d739",
  "active": true,
  "tagName": "bevorzugtes Mandat",
  "hookType": "CASETAG_CHANGED"
}
```

```json
{
  "caseId": "21f8bd6c7f0001010d3542018c45d739",
  "active": false,
  "tagName": "bevorzugtes Mandat",
  "hookType": "CASETAG_CHANGED"
}
```

```json
{
  "caseId": "21f8bd6c7f0001010d3542018c45d739",
  "hookType": "CASE_REMOVED"
}
```

```json
{
  "formId": "369161647f00010160fa4bb8450ccbb3",
  "caseId": "6a7bd5367f000101364966678df1572d",
  "hookType": "CASE_FORM_UPDATED"
}
```

Die Authentifizierung gegenüber der Drittapplikation kann optional per HTTP Basic Authentication stattfinden.
