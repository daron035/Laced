###########
# BUILDER #
###########

# pull official base image
FROM python:3.12.0-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql postgresql-dev gcc python3-dev musl-dev zlib jpeg-dev libjpeg freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev

# lint
RUN pip install --upgrade pip
# RUN pip install flake8==6.0.0
COPY server /usr/src/app/
# RUN flake8 --ignore=E501,F401 .

# install python dependencies
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.12.0-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
# RUN addgroup --system app && adduser --system app --group app
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends netcat
RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint.prod.sh
# COPY ./entrypoint.prod.sh .
# RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.prod.sh
# RUN chmod +x  $APP_HOME/entrypoint.prod.sh

# copy project
COPY server $APP_HOME
# COPY ../docker/backend/entrypoint.sh $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app
# RUN chmod +x /home/app/web/entrypoint.sh

# run entrypoint.prod.sh
# ENTRYPOINT ["/home/app/web/entrypoint.prod.sh"]

##########################
##########################
# # poetry export --without-hashes --format=requirements.txt > requirements.txt
# FROM python:3.10-alpine

# WORKDIR /app
# ADD ./backend/requirements.txt /app/backend/

# RUN apk update \
#     && apk add postgresql postgresql-dev gcc python3-dev musl-dev zlib jpeg-dev libjpeg freetype-dev \
#     fribidi-dev \
#     harfbuzz-dev \
#     jpeg-dev \
#     lcms2-dev \
#     openjpeg-dev \
#     tcl-dev \
#     tiff-dev \
#     tk-dev \
#     zlib-dev

# RUN pip install --upgrade pip
# RUN pip install gunicorn
# RUN pip install -r backend/requirements.txt

# ADD ./backend /app/backend
# ADD ./docker /app/docker
##########################
##########################
# FROM python:3.10-alpine as builder

# WORKDIR /app

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# RUN apk update \
#     && apk add postgresql postgresql-dev gcc python3-dev musl-dev zlib jpeg-dev libjpeg freetype-dev \
#     fribidi-dev \
#     harfbuzz-dev \
#     jpeg-dev \
#     lcms2-dev \
#     openjpeg-dev \
#     tcl-dev \
#     tiff-dev \
#     tk-dev \
#     zlib-dev

# RUN /usr/local/bin/python -m pip install --upgrade pip

# COPY . .


# COPY ./requirements.txt .
# # https://stackoverflow.com/questions/45594707/what-is-pips-no-cache-dir-good-for
# # https://habr.com/ru/company/wunderfund/blog/586778/
# RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


# FROM python:3.9.13-alpine3.15

# RUN mkdir -p /home/app

# # https://stackoverflow.com/questions/49955097/how-do-i-add-a-user-when-im-using-alpine-as-a-base-image
# # https://wiki.alpinelinux.org/wiki/Setting_up_a_new_user#addgroup
# RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# # RUN groupadd app
# # RUN useradd -m -g app app -p PASSWORD
# # RUN usermod -aG app app

# ENV HOME=/home/app
# ENV APP_HOME=/home/app/web
# RUN mkdir $APP_HOME
# #RUN mkdir $APP_HOME/static

# WORKDIR $APP_HOME

# RUN apk update && apk add libpq postgresql postgresql-dev gcc python3-dev musl-dev libjpeg zlib jpeg-dev freetype-dev \
#     fribidi-dev \
#     harfbuzz-dev \
#     jpeg-dev \
#     lcms2-dev \
#     openjpeg-dev \
#     tcl-dev \
#     tiff-dev \
#     tk-dev \
#     zlib-dev

# COPY --from=builder /usr/src/app/wheels /wheels
# COPY --from=builder /usr/src/app/requirements.txt .
# RUN pip install --no-cache /wheels/*

# COPY ./entrypoint.sh $APP_HOME

# COPY . $APP_HOME

# # https://phoenixnap.com/kb/linux-chown-command-with-examples
# RUN chown -R appuser:appgroup $APP_HOME 

# USER appuser
# RUN chmod +x /home/app/web/entrypoint.sh

# ENTRYPOINT ["/home/app/web/entrypoint.sh"]
