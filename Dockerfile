FROM python:3

MAINTAINER Ramón Gago Carrera <ramongagocarrera@gmail.com>

WORKDIR /usr/src/app

# Instala python-pip
RUN pip3 install --no-cache-dir

# Instala flask y las librerías necesarias
RUN pip3 install flask flask-restful flask-jsonpify pymongo

COPY contenedores/server.py /app

ENTRYPOINT ["python"]
