"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from os import getenv, path
from pathlib import Path
import dotenv

from django.core.wsgi import get_wsgi_application

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = BASE_DIR / ".env.dev"

if path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", getenv("DJANGO_SETTINGS_MODULE"))
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    getenv("DJANGO_SETTINGS_MODULE"),
    # getenv("DJANGO_SETTINGS_MODULE", "server.settings.development"),
)

application = get_asgi_application()
