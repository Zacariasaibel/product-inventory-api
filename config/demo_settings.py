"""Public, disposable API demo with an independent SQLite database."""
import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
from .settings import *

DEMO_MODE = True
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "")
if not SECRET_KEY:
    raise ImproperlyConfigured("Set a private DJANGO_SECRET_KEY for the demo.")
DEBUG = os.environ.get("DJANGO_DEBUG", "0") == "1"
ALLOWED_HOSTS = [host.strip() for host in os.environ.get(
    "DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1"
).split(",") if host.strip()]
DEMO_DATABASE = Path(os.environ.get("DJANGO_DEMO_DB", BASE_DIR / "demo.sqlite3")).resolve()
if DEMO_DATABASE.name != "demo.sqlite3":
    raise ImproperlyConfigured("DJANGO_DEMO_DB must point to a separate demo.sqlite3 file.")
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": DEMO_DATABASE}}
STATIC_ROOT = BASE_DIR / "staticfiles"
LANGUAGE_CODE = "de"
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_AUTHENTICATION_CLASSES": [],
}
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
