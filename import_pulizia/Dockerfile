FROM python:3.9-slim

# Installare dipendenze di sistema
RUN apt-get update && apt-get install -y \
    openjdk-17-jre-headless \
    curl \
    tar \
    && rm -rf /var/lib/apt/lists/*

# Impostare la variabile d'ambiente per OpenRefine
ENV OPENREFINE_HOME=/app/openrefine

# Creare la directory per OpenRefine
RUN mkdir -p $OPENREFINE_HOME

# Scaricare e estrarre OpenRefine
RUN curl -L https://github.com/OpenRefine/OpenRefine/releases/download/3.8.7/openrefine-linux-3.8.7.tar.gz | tar zx -C $OPENREFINE_HOME --strip-components=1

# Assicurarsi che il file 'refine' sia eseguibile
RUN chmod +x $OPENREFINE_HOME/refine

# Copiare il codice dell'applicazione
COPY src/ /app/src/
COPY tests/ /app/tests/
COPY requirements.txt /app/requirements.txt
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Installare le dipendenze Python
RUN pip install --no-cache-dir -r /app/requirements.txt

# Impostare la directory di lavoro
WORKDIR /app

# Esportare le porte per FastAPI e OpenRefine
EXPOSE 8000 3333

# Avviare l'applicazione tramite lo script di avvio
CMD ["/start.sh"]