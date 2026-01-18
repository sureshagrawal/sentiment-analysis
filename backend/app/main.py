from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sentiment Analysis API")


class SentimentRequest(BaseModel):
    text: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/sentiment")
def analyze_sentiment(request: SentimentRequest):
    # Dummy response for now
    return {
        "sentiment": "Positive",
        "confidence": 0.95
    }
