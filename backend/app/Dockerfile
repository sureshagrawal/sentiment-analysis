# =========================
# Base Image
# =========================
FROM python:3.11-slim

# =========================
# Environment
# =========================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# =========================
# System dependencies
# =========================
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       build-essential \
    && rm -rf /var/lib/apt/lists/*

# =========================
# Install Python dependencies
# =========================
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# =========================
# Copy application code
# =========================
COPY . .

# =========================
# Expose port
# =========================
EXPOSE 10000

# =========================
# Run FastAPI
# =========================
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
