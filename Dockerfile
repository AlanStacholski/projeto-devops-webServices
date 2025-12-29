FROM python:3.9-slim

WORKDIR /app

# Instala dependências
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY app/ .

# Roda a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]