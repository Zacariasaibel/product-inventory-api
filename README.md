# Product Inventory API

REST-API zum Verwalten von Produkten und Beständen. Django REST Framework bietet JSON und eine Oberfläche im Browser. Es gibt kein separates Frontend.

## Ausprobieren

Python 3.13 oder neuer und die Abhängigkeiten aus `requirements.txt` werden benötigt:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py seed_demo
.\.venv\Scripts\python.exe manage.py runserver
```

Unter `http://127.0.0.1:8000/api/products/` die Liste ansehen. Unter `/api/products/create/` ein Produkt anlegen. Unter `/api/products/<id>/` ein Produkt lesen, mit PUT oder PATCH ändern und mit DELETE entfernen. Die Browseroberfläche enthält die passenden Formulare. Preis und Bestand dürfen nicht negativ sein. Ein Produkt und sein Bestand werden gemeinsam gespeichert.

## Technik und Grenzen

Python, Django, Django REST Framework, SQLite und django-cors-headers. Die API hat keine Benutzerverwaltung für Produktzugriffe. Nur fiktive Daten verwenden; die Entwicklungs-Konfiguration ist kein privater Produktivdienst.

Eine öffentliche Demo ist noch nicht veröffentlicht. Die [vorbereitete Demo-Konfiguration](docs/demo-deployment.md) trennt Beispieldaten von lokalen Daten und dokumentiert das Zurücksetzen. Es wurde kein zusätzlicher kostenpflichtiger Dienst eingerichtet.

Prüfen: `.\.venv\Scripts\python.exe manage.py test products`. Ergebnisse und Grenzen stehen im [Prüfbericht](docs/verification.md).
