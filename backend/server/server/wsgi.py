"""WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/

"""

import os
from os import getenv
from pathlib import Path

# print("3030303030303030\n", getenv("D"))
from django.core.wsgi import get_wsgi_application


#
BASE_DIR = Path(__file__).resolve().parent.parent
#
# dotenv_file = BASE_DIR / ".env.dev"
#
# if path.isfile(dotenv_file):
#     dotenv.load_dotenv(dotenv_file)

# dotenv.load_dotenv()
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", getenv("DJANGO_SETTINGS_MODULE"))
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    getenv("DJANGO_SETTINGS_MODULE", "server.settings.development"),
    # getenv("DJANGO_SETTINGS_MODULE"),
)

application = get_wsgi_application()
