from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# from ml.model import predict_sentiment
from ml.inference import predict_sentiment

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

# @app.post("/sentiment")
# def analyze_sentiment(request: SentimentRequest):
#     sentiment = predict_sentiment(request.text)
#     return {
#         "sentiment": sentiment
#     }

@app.post("/sentiment")
def analyze_sentiment(request: SentimentRequest):
    result = predict_sentiment(request.text)
    return {
        "sentiment": result["sentiment"],
        "confidence": result["confidence"],
        "model": "TF-IDF + RandomForest"
    }



