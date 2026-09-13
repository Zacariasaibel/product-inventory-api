# Product Inventory API

Eine REST API zur Verwaltung eines Produktbestands, entwickelt mit Django und Django REST Framework.

Das Projekt entstand während meiner Umschulung zum Fachinformatiker für Anwendungsentwicklung und demonstriert die grundlegenden CRUD-Funktionen einer Backend-API.

## Funktionen

- Alle Produkte abrufen
- Einzelnes Produkt anhand seiner ID abrufen
- Neue Produkte erstellen
- Bestehende Produkte vollständig oder teilweise aktualisieren
- Produkte löschen
- Verarbeitung und Ausgabe von JSON-Daten
- CORS-Unterstützung für die Verbindung mit einem Frontend

## Technologien

- Python
- Django
- Django REST Framework
- SQLite
- django-cors-headers
- Git und GitHub

## API-Endpunkte

| Methode | Endpunkt | Beschreibung |
|---|---|---|
| GET | `/api/products/` | Alle Produkte abrufen |
| POST | `/api/products/create/` | Neues Produkt erstellen |
| GET | `/api/products/<id>/` | Einzelnes Produkt abrufen |
| PUT | `/api/products/<id>/` | Produkt vollständig aktualisieren |
| PATCH | `/api/products/<id>/` | Produkt teilweise aktualisieren |
| DELETE | `/api/products/<id>/` | Produkt löschen |

## Produktstruktur

```json
{
  "id": 1,
  "name": "Wireless Headphones",
  "short_description": "Compact wireless headphones",
  "product_description": "Wireless headphones with noise cancellation and long battery life.",
  "stock": 15,
  "price": "89.99"
}
```

## Lokale Installation

Repository klonen:

```bash
git clone https://github.com/Zacariasaibel/product-inventory-api.git
cd product-inventory-api
```

Virtuelle Umgebung erstellen und aktivieren:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Abhängigkeiten installieren:

```powershell
python -m pip install -r requirements.txt
```

Datenbank vorbereiten:

```powershell
python manage.py migrate
```

Entwicklungsserver starten:

```powershell
python manage.py runserver
```

Die API ist anschließend unter folgender Adresse erreichbar:

```text
http://127.0.0.1:8000/api/products/
```

## Sicherheit

Der Django `SECRET_KEY` wird über eine Umgebungsvariable eingelesen und nicht im Repository veröffentlicht. Lokale Datenbanken und virtuelle Umgebungen sind ebenfalls von Git ausgeschlossen.

## Autor

**Zacarias Aibbich Belhadj**

- Portfolio: https://zacariasaibel.github.io/
- GitHub: https://github.com/Zacariasaibel