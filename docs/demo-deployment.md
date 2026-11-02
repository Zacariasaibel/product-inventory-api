# Isolierte API-Demo

Für die Demo eine eigene WSGI-App mit Django-Unterstützung und eine eigene virtuelle Umgebung verwenden. Keine Datenbank vom Arbeitsplatz hochladen. PythonAnywhere unterstützt Django und SQLite; eine kostenlose App ist auf ein Web-Projekt begrenzt. Die vorhandene ZABYTE-App bleibt unverändert.

## Lokal mit Beispieldaten

```powershell
$env:DJANGO_SETTINGS_MODULE = "config.demo_settings"
$env:DJANGO_SECRET_KEY = & .\.venv\Scripts\python.exe -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py reset_demo
.\.venv\Scripts\python.exe manage.py collectstatic --noinput
.\.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8020 --noreload --insecure
```

`--insecure` dient ausschließlich der lokalen Vorschau der DRF-Styles bei ausgeschaltetem DEBUG. Die API ist unter `http://127.0.0.1:8020/api/products/` erreichbar. Unter `/api/products/create/` ein Produkt anlegen und dessen ID unter `/api/products/<id>/` ändern oder löschen. GET liefert 200, POST 201, PUT/PATCH 200, DELETE 204, ungültige Eingaben 400 und fehlende IDs 404.

## Hosting vorbereiten

1. Eine zusätzliche bereits autorisierte freie WSGI-App bereitstellen. Keine neue App über ZABYTE legen und keine kostenpflichtige Option aktivieren.
2. Repository hochladen, virtuelle Umgebung erstellen, `requirements.txt` installieren. In der privaten WSGI-Umgebung `DJANGO_SETTINGS_MODULE=config.demo_settings`, einen zufälligen `DJANGO_SECRET_KEY` und `DJANGO_ALLOWED_HOSTS` mit dem echten Host setzen. DEBUG bleibt aus.
3. Mit denselben Variablen `migrate`, `reset_demo` und `collectstatic --noinput` ausführen. Die neue `demo.sqlite3` enthält nur drei fiktive Produkte. `DJANGO_DEMO_DB` darf alternativ einen absoluten Pfad mit diesem Dateinamen angeben.
4. WSGI lädt `config.wsgi.application`. Statische Zuordnung `/static/` auf `staticfiles/` setzen und HTTPS verwenden.
5. App neu laden und CRUD samt Fehlerfällen und Browserformularen öffentlich prüfen. Erst die geprüfte öffentliche URL ins Portfolio übernehmen.

`reset_demo` ist ein Betreiberbefehl. Er verweigert den Zugriff ohne Demo-Einstellungen. In der Demo löscht er alle Produkte samt Beständen und stellt die drei Beispiele wieder her. Die Daten werden gemeinsam bearbeitet; ausschließlich fiktive Angaben eingeben. Die Demo bietet keine dauerhafte Speicherung oder privaten Konten.

Offizielle Quellen: https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/ und https://help.pythonanywhere.com/pages/FreeAccountsFeatures/

Status: lokal vorbereitet. Eine zusätzliche verfügbare Hosting-App und deren Zugriff fehlen; keine öffentliche URL behauptet.
