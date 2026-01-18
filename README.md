# Sentiment Analysis – AI Web Application

A production-ready **AI-powered Sentiment Analysis system** built with a clean, modular architecture.

The project focuses on:
- Machine Learning correctness
- Clean API design
- Premium frontend UX
- Deployment-readiness

Future platform extensions (mobile apps, etc.) will reuse the same core system without duplicating logic.

---

## 🧠 What This Project Does

- Analyzes text and predicts sentiment:
  - Positive
  - Negative
  - Neutral
- Returns a confidence score based on model probability
- Visualizes confidence in a premium, animated UI

---

## 🏗 High-Level Architecture

# Sentiment Analysis – AI Web Application

A production-ready **AI-powered Sentiment Analysis system** built with a clean, modular architecture.

The project focuses on:
- Machine Learning correctness
- Clean API design
- Premium frontend UX
- Deployment-readiness

Future platform extensions (mobile apps, etc.) will reuse the same core system without duplicating logic.

---

## 🧠 What This Project Does

- Analyzes text and predicts sentiment:
  - Positive
  - Negative
  - Neutral
- Returns a confidence score based on model probability
- Visualizes confidence in a premium, animated UI

---

## 🏗 High-Level Architecture

```
Client (Next.js UI)
        ↓
FastAPI Backend (REST)
        ↓
ML Inference Layer
(TF-IDF + RandomForest)
```

---

## 🛠 Tech Stack

### Frontend
- Next.js (App Router)
- Tailwind CSS
- Responsive, mobile-first design

### Backend
- FastAPI
- Pydantic
- CORS Middleware

### Machine Learning
- Scikit-learn
- TF-IDF Vectorizer
- RandomForest Classifier
- Joblib for model persistence

---

## 📂 Repository Structure

```text
sentiment-analysis/
├── frontend/
│   └── web/
├── backend/
│   └── app/
│       ├── ml/
│       │   ├── inference.py
│       │   └── train_model.py
│       └── main.py
├── runtime.txt
└── README.md
```

---

## 🧠 Model & Inference Strategy

- Trained ML model artifacts (.pkl) are not stored in the Git repository
- Model files are downloaded dynamically at runtime during backend startup
- This keeps the repository lightweight and avoids large binary commits
- Once downloaded, models are reused for all inference requests
- No retraining happens during deployment

This approach reflects real-world industry practices for deploying ML-backed APIs.

---

## 🚀 Current Status

- ML model trained and validated
- API standardized and stable
- Frontend UI polished and synced with API
- Externalized ML model loading implemented
- Ready for cloud deployment

---

## 🚀 Current Status

- ML model trained and integrated
- API standardized and stable
- Frontend UI polished and synced with API
- Ready for cloud deployment

---

## 🔮 Future Scope

- Mobile app delivery using the same backend
- Further ML retraining with larger datasets
- UI enhancements and personalization

---

## 👤 Author

**Suresh Agrawal**  
Java • Python • Full Stack • AI/ML
