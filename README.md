# Product Inventory API

Dieses Projekt entstand aus einer Backend-Aufgabe während meiner Umschulung: Produkte und ihre Bestände sollten über eine REST-API verwaltet werden können.

Dabei wollte ich lernen, wie Datenmodelle, Eingabeprüfung und Datenbankzugriffe zusammenspielen. Das Ergebnis ist eine API, die sich direkt im Browser ausprobieren lässt.

## Was die API kann

Produkte lassen sich anlegen, anzeigen, bearbeiten und löschen. Zu jedem Produkt gehört ein Bestand.

| Methode | Adresse | Funktion |
| --- | --- | --- |
| GET | `/api/products/` | Alle Produkte anzeigen |
| POST | `/api/products/create/` | Ein Produkt anlegen |
| GET | `/api/products/<id>/` | Ein einzelnes Produkt anzeigen |
| PUT / PATCH | `/api/products/<id>/` | Ein Produkt und seinen Bestand bearbeiten |
| DELETE | `/api/products/<id>/` | Ein Produkt entfernen |

Django REST Framework liefert die Daten als JSON und stellt eine Browseroberfläche mit passenden Formularen bereit. Ein separates Frontend wird dafür nicht benötigt.

## Technische Entscheidungen

Die Anwendung verwendet Python, Django, Django REST Framework, SQLite und django-cors-headers.

Preis und Bestand dürfen nicht negativ sein. Ungültige Eingaben werden mit einer Fehlermeldung zurückgewiesen.

Produkt und Bestand werden gemeinsam in einer Datenbanktransaktion gespeichert. Schlägt die Speicherung fehl, wird die Änderung zurückgerollt. Dadurch bleiben die zusammengehörigen Daten konsistent.

## Lokal ausprobieren

Voraussetzung: Python 3.13. Im Projektordner ein PowerShell-Terminal öffnen:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py seed_demo
.\.venv\Scripts\python.exe manage.py runserver
```

Anschließend <http://127.0.0.1:8000/api/products/> öffnen.

Zum Anlegen eines Produkts die Adresse <http://127.0.0.1:8000/api/products/create/> aufrufen. Für ein vorhandenes Produkt wird dessen ID in die Detailadresse eingesetzt, beispielsweise `/api/products/1/`.

## Demo und Grenzen

Eine öffentliche Demo ist noch nicht veröffentlicht. Die [vorbereitete Demo-Konfiguration](docs/demo-deployment.md) verwendet eine getrennte Datenbank für Beispieldaten und erklärt das Zurücksetzen.

Produktzugriffe sind ohne Anmeldung möglich. Bitte ausschließlich fiktive Daten verwenden. Die Entwicklungs-Konfiguration ist für lokale Tests vorgesehen.

## Prüfungen

Die Backend-Tests lassen sich im Projektordner ausführen:

```powershell
.\.venv\Scripts\python.exe manage.py test products
```

Die dokumentierten Ergebnisse und Grenzen stehen im [Prüfbericht](docs/verification.md).