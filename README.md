# Caso de Estudio: Plataforma de Contenido Digital (Spotify Style)

Este proyecto busca estandarizar el entorno de desarrollo, automatizar la validación y preparar la base para un despliegue escalable en la nube utilizando Docker, GitHub Actions y AWS.

## 1. Análisis de Contenedores y Roles (Parte 4)
Se diseñó una arquitectura de microservicios dividida en dos contenedores:
* **Contenedor 1 (App):** Ejecuta la aplicación principal en Flask. Es el núcleo que interactúa con el usuario.
* **Contenedor 2 (Helper):** Un servicio auxiliar que entrega métricas de estado (`/status`).
* **¿Por qué separar responsabilidades?** Esto mejora la organización del sistema al permitir que cada servicio se actualice o escale de forma independiente. Si el servicio de reportes falla, la aplicación principal de reproducción no se ve afectada (aislamiento de fallos).

## 2. Infraestructura como Código en AWS (Parte 6)
El archivo `infraestructura-base.yaml` define los siguientes recursos:
* **Amazon EC2:** Servidor donde se hospedarán los contenedores Docker mediante Docker Compose.
* **Amazon S3:** Bucket utilizado para el almacenamiento de archivos multimedia (canciones, portadas) y activos estáticos.
* **Apoyo al despliegue:** Esta base permite que el sistema crezca fácilmente, delegando el almacenamiento pesado a S3 y el cómputo a EC2.

## 3. Diseño de Monitoreo con CloudWatch (Parte 7)
Para reaccionar rápidamente a errores en producción, se propone:
* **Métricas a observar:** 1. `CPUUtilization` de la instancia EC2.
    2. `StatusCheckFailed` para verificar la salud del servidor.
    3. `HTTPCode_Target_5XX_Count` para detectar errores en el código Flask.
* **Alerta:** Configurar una alarma si el uso de CPU supera el 85% durante 5 minutos.
* **Acción sugerida:** Reiniciar el servicio mediante un script automático o disparar una política de Auto Scaling.

## 4. Diseño de Despliegue en AWS (Parte 8)
1. El código se sube a **GitHub**.
2. **GitHub Actions** valida automáticamente que todos los Dockerfiles y archivos de configuración estén presentes y sin errores.
3. Tras la validación, el código se despliega en la instancia **EC2**.
4. GitHub Actions actúa como un filtro de calidad antes de que cualquier cambio llegue al servidor.

## 5. Conclusión Técnica (Parte 9)
* **Inconsistencias entre entornos:** La contenedorización con **Docker** es la solución definitiva, ya que asegura que la aplicación corra exactamente igual en el equipo del desarrollador que en el servidor de producción.
* **Valor de GitHub Actions:** Aporta **automatización y confianza**, eliminando la necesidad de verificar manualmente cada cambio antes de integrar nuevas funciones.
* **Ventaja de los Contenedores:** Separar funciones en dos contenedores permite un sistema más modular, fácil de mantener y preparado para una arquitectura de microservicios moderna en lugar de un sistema manual monolítico.