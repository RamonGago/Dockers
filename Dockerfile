FROM jfloff/alpine-python

MAINTAINER Ramón Gago Carrera <ramongagocarrera@gmail.com>

WORKDIR /app

RUN apk update && apk upgrade

# Instala flask y las librerías necesarias
RUN pip3 install flask flask-restful flask-jsonpify pymongo

COPY contenedores/server.py /app

ENTRYPOINT ["python"]
