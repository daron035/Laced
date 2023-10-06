#!/bin/sh

until cd /home/app/web/server
do
    echo "Waiting for server volume..."
done

until ./manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

./manage.py collectstatic --noinput

gunicorn django.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
# gunicorn config.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
