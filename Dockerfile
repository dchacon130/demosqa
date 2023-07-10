FROM python:3.9

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    firefox \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Configurar variables de entorno para ejecutar en modo headless
ENV MOZ_HEADLESS=1
ENV DISPLAY=:99

# Instalar Selenium y Behave
RUN pip install selenium behave
