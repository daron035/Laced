#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from os import getenv, path
from pathlib import Path
import dotenv

BASE_DIR = Path(__file__).resolve().parent
dotenv_file = BASE_DIR / ".env.dev"
# dotenv_file = BASE_DIR / ".env.prod"
if path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)


def main():
    """Run administrative tasks."""
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", getenv("DJANGO_SETTINGS_MODULE"))
    os.environ.setdefault("D", "uifuiowequrqiowurioqwuriuq")
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        getenv("DJANGO_SETTINGS_MODULE", "server.settings.development"),
    )
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
