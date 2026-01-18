FROM python:3.11-slim

WORKDIR /app

# System deps
RUN apt-get update \
 && apt-get install -y curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
 && pip install --no-cache-dir gdown

# App code
COPY . .

# Create model directory
RUN mkdir -p ml/models

# ✅ CORRECT Google Drive download (large file safe)
RUN gdown --fuzzy https://drive.google.com/file/d/1XPUF-WyMf9GFK9NFdgd7ZXnK-sjGVEsw -O ml/models/sentiment_model.pkl \
 && gdown --fuzzy https://drive.google.com/file/d/1gROH25ADggHROyD7hzaBs4ZJcRiRv9jA -O ml/models/vectorizer.pkl

EXPOSE 10000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
