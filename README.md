# Propuesta Técnica: Plataforma de Contenido Digital (Spotify Style)

## 1. Información general
* **Repositorio:** [Enlace a tu repo de GitHub aquí]
* **Rama principal de trabajo:** `develop`

## 2. Entregables de la actividad
A continuación se detallan los archivos que componen la solución automatizada:

* **Automatización Bash:** [`setup_project.sh`](./setup_project.sh) - Simulación de preparación de entorno Linux.
* **Automatización Python:** [`project_report.py`](./project_report.py) - Script de verificación de integridad del proyecto.
* **Contenedores de Aplicación:**
    * Aplicación Principal (Flask): [`app/Dockerfile`](./app/Dockerfile)
    * Servicio Auxiliar (Status): [`helper/Dockerfile`](./helper/Dockerfile)
* **Orquestación:** [`docker-compose.yml`](./docker-compose.yml) - Ejecución de ambos servicios en conjunto.
* **CI/CD:** [`.github/workflows/ci.yml`](./.github/workflows/ci.yml) - Pipeline de validación automática.
* **Infraestructura como Código:** [`infraestructura-base.yaml`](./infraestructura-base.yaml) - Plantilla AWS CloudFormation.

---

## 3. Análisis de la solución 
* **Función de los contenedores:** Se separó la aplicación principal (reproductor) del servicio de monitoreo (`/status`). 
* **Resolución de problemas:** Esta división resuelve el problema de servicios ejecutados manualmente y permite que un fallo en el servicio auxiliar no afecte la disponibilidad del reproductor principal.

## 4. Diseño de infraestructura y despliegue 
* **Servicios en AWS:** Se propone el uso de **EC2** para hospedar el motor de Docker y **S3** para el almacenamiento persistente de contenido multimedia (canciones/imágenes).
* **Flujo de Despliegue:** El código viaja desde GitHub, es validado por GitHub Actions y finalmente se despliega en EC2 mediante Docker Compose, garantizando que el entorno sea idéntico en cada paso.

## 5. Estrategia de monitoreo 
Se propone el uso de **AWS CloudWatch** con:
* **Métricas:** Uso de CPU, conteo de errores 5XX y latencia de respuesta.
* **Alerta:** Alarma si el consumo de CPU supera el 85%.
* **Acción:** Notificación SNS al equipo técnico y escalado automático de la instancia.

## 6. Conclusión técnica de la actividad realizada
* **Estandarización:** Docker es la herramienta que mejor resuelve las inconsistencias entre equipos de desarrollo.
* **Automatización:** GitHub Actions elimina el error humano al validar archivos y pipelines antes de cada despliegue.
* **Modularidad:** Separar funciones en contenedores permite un mantenimiento más ágil y una infraestructura más resiliente y profesional.

Giselle Castillo :)