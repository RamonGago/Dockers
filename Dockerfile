FROM projectatomic/atomicapp

MAINTAINER Ramón Gago Carrera <ramongagocarrera@gmail.com>

WORKDIR /microservice

# Actualiza la imagen con los últimos paquetes
RUN yum update -y; yum clean all

# Instala python-pip
RUN yum -y install epel-release && yum clean all
RUN yum -y install python-pip && yum clean all

# Instala bd
RUN pip install SQLAlchemy

# Instala flask y las librerías necesarias
RUN pip install flask flask-restful flask-jsonpify flask-sqlalchemy

COPY contenedores/microservice.py /microservice

ENTRYPOINT ["python","microservice.py"]
