# Prüfbericht · 02.11.2026

## Lokal ausgeführt

- 12 Django-Tests: CRUD, ungültige und fehlende Werte, Teiländerungen, Stock nach Admin-Erstellung, transaktionales Zurückrollen sowie Demo-Befehle: bestanden.
- `makemigrations --check --dry-run`: keine Änderungen. `git diff --check`: ohne Fehler.
- Eigene `demo.sqlite3` migriert und mit drei fiktiven Produkten befüllt. DRF-Styles mit `collectstatic` gesammelt.
- Chrome und echtes HTTP: GET 200, POST 201, PUT/PATCH 200, negative Preise/Bestände 400 mit Feldfehlern, DELETE 204, danach GET 404. Ungültige Änderungen erhalten den vorherigen Zustand.
- DRF-Liste und Erstellformular direkt geöffnet und neu geladen, bei 1440 und 390 Pixeln ohne horizontales Überlaufen. Keine JavaScript-Ausnahmen.

Die Prüfungen liefen lokal, nicht gegen einen öffentlichen Dienst. Es gibt noch keine verifizierte öffentliche Demo-URL. Ein zusätzlicher Hosting-Zugang wird benötigt.

## Codeprüfung

Negative Werte werden jetzt vor dem Datenbankzugriff abgewiesen. Produkt und Bestand werden atomar gespeichert. Bei Änderungen wird auch die Antwort mit dem aktuellen Stock gefüllt. `select_related` vermeidet einzelne Stock-Abfragen pro Produkt. Die drei vorhandenen generischen Endpunkte bleiben erhalten. Redundante View-Docstrings und das leere Testgerüst wurden ersetzt.

Kein neues Frontend, keine zusätzliche Abhängigkeit und keine Modellmigration. Eine echte private Warenverwaltung würde Authentifizierung, Berechtigungen und ein anderes Betriebskonzept benötigen; dafür wurde keine große Umstrukturierung begonnen.
