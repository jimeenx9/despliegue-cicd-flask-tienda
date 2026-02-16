FROM python:3.13-slim

# Evita problemas de logs en contenedores
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias primero (cache docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY src/ .

# Puerto de la app
EXPOSE 8000

# Comando de arranque
CMD ["python", "app.py"]
