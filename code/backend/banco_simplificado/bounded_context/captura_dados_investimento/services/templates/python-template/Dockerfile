FROM python:3.13-slim

WORKDIR /app

# Instala dependências primeiro (cache de camadas)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY . .

EXPOSE 3500

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3500"]
