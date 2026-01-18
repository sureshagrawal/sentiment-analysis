from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Sentiment Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentimentRequest(BaseModel):
    text: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/sentiment")
def analyze_sentiment(request: SentimentRequest):
    return {
        "sentiment": "Positive",
        "confidence": 0.95
    }
