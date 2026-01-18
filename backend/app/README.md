# Backend – Sentiment Analysis API

This directory contains the **FastAPI backend** and **machine learning inference logic**.

The backend is responsible for:
- Serving sentiment predictions
- Managing ML inference
- Providing a stable API contract

---

## 🚀 Features

- RESTful sentiment analysis endpoint
- Confidence-based neutral handling
- Standardized API responses
- Health check endpoint for monitoring
- CORS enabled for frontend integration

---

## 🛠 Tech Stack

- FastAPI
- Pydantic
- Scikit-learn
- Joblib
- Uvicorn

---

## 📌 API Endpoints

### POST `/sentiment`

**Request**
```json
{
  "text": "I am feeling okay today"
}
```

**Response**
```json
{
  "status": "success",
  "data": {
    "sentiment": "Neutral",
    "confidence": 0.54
  },
  "meta": {
    "model": "TF-IDF + RandomForest",
    "version": "v1"
  }
}
```

---

### GET `/health`

```json
{
  "status": "ok",
  "service": "sentiment-analysis-api",
  "version": "1.0"
}
```

---

## 🧪 Local Development

### Activate virtual environment
```bash
venv\Scripts\activate
```

### Run server
```bash
uvicorn main:app --reload
```

Server runs at:
```
http://127.0.0.1:8000
```

---

## 🤖 Machine Learning Notes

- TF-IDF used for text vectorization
- RandomForest used for classification
- Confidence derived from prediction probabilities
- Neutral sentiment triggered below confidence threshold

---

## 🔐 Engineering Decisions

- `.pkl` files are generated locally and ignored in Git
- API logic and ML inference are tightly coupled
- Errors handled gracefully to avoid crashes

---

## 🔮 Future Improvements

- Model retraining automation
- Performance optimization
- Logging and monitoring integration
