# Caso de Estudio: Plataforma Spotify-Cloud

## Análisis de Contenedores 
* **App:** Gestiona la interfaz principal.
* **Helper:** Gestiona el estado y reportes del sistema.
* **Separación de responsabilidades:** Dividir el sistema en dos contenedores permite que si el servicio de estado falla, la aplicación principal siga funcionando. Mejora la escalabilidad y el mantenimiento.

## Infraestructura como Código 
Se incluye `infraestructura-base.yaml` que define:
* **EC2:** Donde se desplegarán los contenedores Docker.
* **S3:** Para almacenar contenido estático (canciones, imágenes).

## Estrategia de Monitoreo 
Propuesta de CloudWatch:
1. **Métricas:** CPU Utilization, Request Count, Error Rate (5XX).
2. **Alerta:** Si el CPU supera el 80% por más de 5 minutos.
3. **Acción:** Escalamiento automático o reinicio de contenedores.

## Despliegue en AWS 
El código se envía desde GitHub. GitHub Actions valida los archivos y construye las imágenes. Luego, mediante un runner, se ejecuta `docker-compose up -d` dentro de la instancia EC2 para actualizar el servicio.

## Conclusión Técnica 
* **Inconsistencias:** Docker resuelve esto al estandarizar el entorno.
* **GitHub Actions:** Aporta validación automática y confianza en cada integración.
* **Ventaja:** Separar funciones en contenedores permite aislar fallos y optimizar recursos.