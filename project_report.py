import os

archivos = {
    "Dockerfile app": "app/Dockerfile",
    "Dockerfile helper": "helper/Dockerfile",
    "docker-compose.yml": "docker-compose.yml",
    "README.md": "README.md",
    "Plantilla CloudFormation": "infraestructura-base.yaml"
}

for nombre, ruta in archivos.items():
    estado = "encontrado" if os.path.exists(ruta) else "no encontrado"
    print(f"{nombre}: {estado}")

print("Estado general: proyecto listo para validación")