# # FROM python:3.10-slim-buster
# FROM python:3.11.4-slim-buster
#
# ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1
#
# RUN apt-get update \
#   # dependencies for building Python packages
#   && apt-get install -y build-essential \
#   # psycopg2 dependencies
#   && apt-get install -y libpq-dev \
#   # Translations dependencies
#   && apt-get install -y gettext \
#   # Additional dependencies
#   && apt-get install -y procps \
#   # cleaning up unused files
#   && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
#   && rm -rf /var/lib/apt/lists/*
#
#
# # Requirements are installed here to ensure they will be cached.
# COPY backend/requirements.txt /requirements.txt
# RUN pip install -r /requirements.txt
#
# COPY docker/backend/entrypoint.sh /entrypoint.sh
# # RUN sed -i 's/\r$//g' /entrypoint.sh
# RUN chmod +x /entrypoint.sh
#
# WORKDIR /app
#
# ENTRYPOINT ["/entrypoint.sh"]

# pull official base image
FROM python:3.12.0-alpine

# set work directory
WORKDIR /home/app/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # install psycopg2 dependencies
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev
#
# RUN apk --update add postgresql zlib jpeg-dev libjpeg freetype-dev \
#     fribidi-dev \
#     harfbuzz-dev \
#     jpeg-dev \
#     lcms2-dev \
#     openjpeg-dev \
#     tcl-dev \
#     tiff-dev \
#     tk-dev \
#     zlib-dev

# install psycopg2 dependencies
# RUN apk update \
#     && apk add postgresql-dev gcc python3-dev musl-dev \
#     && apk --update add postgresql zlib jpeg-dev libjpeg freetype-dev \
#     fribidi-dev harfbuzz-dev jpeg-dev lcms2-dev openjpeg-dev tcl-dev tiff-dev tk-dev zlib-dev

RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev \
            postgresql zlib jpeg-dev libjpeg freetype-dev \
            fribidi-dev harfbuzz-dev jpeg-dev lcms2-dev \
            openjpeg-dev tcl-dev tiff-dev tk-dev zlib-dev
# install psycopg2
RUN pip install psycopg2
# install dependencies
RUN pip install --upgrade pip
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY docker/backend/entrypoint.sh /entrypoint.sh
# RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /entrypoint.sh

# copy project
COPY backend/server .

# run entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
