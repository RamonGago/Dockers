FROM python:3

MAINTAINER Ramón Gago Carrera <ramongagocarrera@gmail.com>

WORKDIR /usr/src/app

RUN apk update
RUN apk upgrade


# Instala flask y las librerías necesarias
RUN pip3 install flask flask-restful flask-jsonpify pymongo

COPY contenedores/server.py /app

ENTRYPOINT ["python"]
