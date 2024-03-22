#!/bin/sh

cd /app
echo "PWD"
pwd
echo "LS"
ls -lah
until cd /home/app/web
do
    echo "Waiting for server volume..."
    echo "PWD"
    pwd
done

./manage.py makemigrations
./manage.py migrate --noinput
./manage.py collectstatic --noinput

gunicorn server.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
# until ./manage.py migrate
# do
#     echo "Waiting for db to be ready..."
#     sleep 2
# done
#
# ./manage.py collectstatic --noinput

# gunicorn server.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
# gunicorn --reload server.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
# gunicorn config.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
