# HITO 5 - Containers for deployment in the cloud ([Docker](https://www.docker.com/))

## Introducción

Para realizar el despliegue del microservicio propuesto se ha utilizado el servicio proporcionado por [Docker](https://www.docker.com/).
Tras el estudio de diversas imágenes de sistemas operativo para la creación del contenedor se ha optado por una distribución [Atomic](https://getfedora.org/es/atomic/download/).
Por otro lado se ha utilizado [Azure](https://azure.microsoft.com/es-es/) como plataforma para desplegar la imagen creada en [Dockerhub](https://hub.docker.com/r/rgcarrera/cloud-computing_project/).

## Contenedor

### Creación de la imagen a desplegar

En primer lugar se procede a la creación de la imagen a través del "Dockerfile" que ejecutará el microservicio realizado.
En este caso, el microservicio devolverá `status: "OK"`.

Una vez realizado tanto el dockerfile como el microservicio, ha de crearse una cuenta en [Dockerhub](https://hub.docker.com/) para la creación de la imagen a desplegar en Azure. Tras el registro y la vinculación de la cuenta de Dockerhub con la cuenta de Githu, para la sincronización del repositorio, automaticamente se ejecutará el Dockerfile presente en el repositorio.

Desde ese momento la imagen quedará lista para ser desplegada.

### Despliegue de la imagen en azure

Para realizar el despliegue de la imagen creada se seguirán los siguientes pasos:

- `az login` para loguearse en Azure.

- `az webapp deployment user set --user-name ramongago --password $PASSWORD` para crear un [deployment user](https://docs.microsoft.com/en-us/cli/azure/webapp/deployment/user?view=azure-cli-latest).

- `az group create --name Microservice_Group --location westeurope` para crear un [grupo de recursos](https://docs.microsoft.com/es-es/azure/azure-resource-manager/resource-group-overview).

- `az appservice plan create --name Microservice_Plan --resource-group Microservice_Group --sku S1 --is-linux` para crear un [plan de servicio](https://docs.microsoft.com/es-es/azure/app-service/azure-web-sites-web-hosting-plans-in-depth-overview).

- `az webapp create --resource-group Microservice_Group --plan Microservice_Plan --name microservicecloudcomputing --deployment-container-image-name rgcarrera/cloud-computing_project` para desplegar el microservicio en la nube.

- `az webapp config appsettings set -g Microservice_Group -n microservicecloudcomputing --settings PORT=5000` para indicar el puerto que utilizará el microservicio.

Tras realizar todos los pasos del despliegue el microservicio mostrará su resultado:

![alt text](/contenedores/images/statusOK.png "Status")

## Más información
Para más información visitar el siguiente [enlace](https://goto.docker.com/rs/929-FJL-178/images/WP_BusinessValueofDocker_06.26.2017.pdf).
