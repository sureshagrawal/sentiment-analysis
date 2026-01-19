FROM python:3.11-slim

WORKDIR /app

# --------------------------------------------------
# System dependencies
# --------------------------------------------------
RUN apt-get update \
 && apt-get install -y ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# --------------------------------------------------
# Python dependencies
# --------------------------------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
 && pip install --no-cache-dir huggingface_hub

# --------------------------------------------------
# Application source
# --------------------------------------------------
COPY . .

# --------------------------------------------------
# Create model directory
# --------------------------------------------------
RUN mkdir -p ml/models

# --------------------------------------------------
# Download models from Hugging Face (BUILD TIME)
# --------------------------------------------------
RUN python - <<EOF
from huggingface_hub import hf_hub_download

hf_hub_download(
    repo_id="sureshagrawal/sentiment-analysis-rf",
    filename="sentiment_model.pkl",
    local_dir="ml/models"
)

hf_hub_download(
    repo_id="sureshagrawal/sentiment-analysis-rf",
    filename="vectorizer.pkl",
    local_dir="ml/models"
)
EOF

# --------------------------------------------------
# Expose Render port
# --------------------------------------------------
EXPOSE 10000

# --------------------------------------------------
# Start FastAPI
# --------------------------------------------------
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
