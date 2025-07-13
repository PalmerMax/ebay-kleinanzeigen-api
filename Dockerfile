FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install chromium 
RUN playwright install-deps

COPY . .

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $EBAY_API_PORT"]