FROM selenium/standalone-firefox:latest

# Instalar Python y dependencias necesarias
USER root
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*
USER seluser

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Agregar ~/.local/bin al PATH
ENV PATH="/home/seluser/.local/bin:${PATH}"
