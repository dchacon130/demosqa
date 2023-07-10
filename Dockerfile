FROM python:3.9-slim

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    firefox-esr \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Configurar variables de entorno para ejecutar en modo headless
ENV MOZ_HEADLESS=1
ENV DISPLAY=:99

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos de la acción
COPY . /app

# Instalar dependencias de Python
RUN pip install -r requirements.txt

# Configurar el entorno para ejecutar los tests
CMD ["behave"]
