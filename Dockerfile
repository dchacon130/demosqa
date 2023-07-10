FROM selenium/standalone-firefox:latest

# Actualizar e instalar dependencias necesarias
USER root
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    gnupg2 \
    wget \
    ca-certificates \
    apt-transport-https \
    && rm -rf /var/lib/apt/lists/*

# Descargar y agregar clave GPG de apt-utils
RUN wget -qO - https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.asc.gpg \
    && mv microsoft.asc.gpg /etc/apt/trusted.gpg.d/ \
    && wget -q https://packages.microsoft.com/config/debian/10/prod.list \
    && mv prod.list /etc/apt/sources.list.d/microsoft-prod.list

# Actualizar e instalar apt-utils
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    && rm -rf /var/lib/apt/lists/*

USER seluser

# Instalar dependencias de Python
COPY requirements.txt .
RUN pip3 install --user -r requirements.txt

# Agregar ~/.local/bin al PATH en el archivo .bashrc
RUN echo "export PATH=/home/seluser/.local/bin:$PATH" >> /home/seluser/.bashrc
