# Usa Python oficial
FROM python:3.9-slim

# Configuración básica
WORKDIR /app
COPY docker/requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la app
COPY app/ ./app
COPY app/model.joblib .
COPY app/feature_names.json .

# Expone el puerto
EXPOSE 8000

# Comando para iniciar FastAPI con Uvicorn
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
