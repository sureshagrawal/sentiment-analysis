# --------------------------------------------------
# Base image
# --------------------------------------------------
FROM python:3.11-slim

# --------------------------------------------------
# Working directory
# --------------------------------------------------
WORKDIR /app

# --------------------------------------------------
# System dependencies
# --------------------------------------------------
RUN apt-get update \
 && apt-get install -y curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# --------------------------------------------------
# Python dependencies
# --------------------------------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --------------------------------------------------
# Application source code
# --------------------------------------------------
COPY . .

# --------------------------------------------------
# Create model directory
# --------------------------------------------------
RUN mkdir -p ml/models

# --------------------------------------------------
# 🔥 Download ML models at BUILD TIME (Google Drive)
# --------------------------------------------------
RUN curl -L \
  "https://drive.google.com/uc?export=download&id=1XPUF-WyMf9GFK9NFdgd7ZXnK-sjGVEsw" \
  -o ml/models/sentiment_model.pkl \
 && curl -L \
  "https://drive.google.com/uc?export=download&id=1gROH25ADggHROyD7hzaBs4ZJcRiRv9jA" \
  -o ml/models/vectorizer.pkl

# --------------------------------------------------
# Expose Render port
# --------------------------------------------------
EXPOSE 10000

# --------------------------------------------------
# Start FastAPI app
# --------------------------------------------------
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
