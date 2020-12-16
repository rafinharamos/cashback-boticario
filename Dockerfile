FROM python:3.7-slim

LABEL maintainer="rafael.ramos@boticario.com"

RUN mkdir /boticario_app

WORKDIR /boticario_app

COPY . /boticario_app/

COPY requirements.txt  boticario_app/

RUN apt-get update && \
        apt-get install -y -q --no-install-recommends build-essential \
        libpq-dev && \
        apt-get clean && \
        apt-get autoremove

RUN pip install -r /boticario_app/requirements.txt