FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copiar TODO el proyecto
COPY . .

# python debe ver el proyecto
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["python", "-m", "src.app"]
