from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# from ml.model import predict_sentiment
from ml.inference import predict_sentiment

app = FastAPI(
    title="Sentiment Analysis API",
    version="1.0"
)

# ---------------- CORS ----------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- SCHEMA ----------------

class SentimentRequest(BaseModel):
    text: str

# ---------------- HEALTH ----------------

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "sentiment-analysis-api",
        "version": "1.0"
    }

# ---------------- SENTIMENT API ----------------

# old code : retrieving data from model.py
# @app.post("/sentiment")
# def analyze_sentiment(request: SentimentRequest):
#     sentiment = predict_sentiment(request.text)
#     return {
#         "sentiment": sentiment
#     }

@app.post("/sentiment")
def analyze_sentiment(request: SentimentRequest):

    text = request.text.strip()

    if not text or len(text) < 3:
        raise HTTPException(
            status_code=400,
            detail="Input text is too short"
        )

    result = predict_sentiment(text)

    if result["sentiment"] == "Error":
        raise HTTPException(
            status_code=500,
            detail="Model inference failed"
        )

    return {
        "status": "success",
        "data": {
            "sentiment": result["sentiment"],
            "confidence": result["confidence"]
        },
        "meta": {
            "model": "TF-IDF + RandomForest",
            "version": "v1"
        }
    }
