import joblib
import re
import os

# ---------------- PATH SETUP ----------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "sentiment_model.pkl")
VECT_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

# ---------------- LOAD MODEL ----------------

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECT_PATH)

# ---------------- TEXT CLEANING ----------------

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+|#\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text.strip()

# ---------------- INFERENCE ----------------

def predict_sentiment(text: str) -> dict:
    try:
        cleaned = clean_text(text)
        vec = vectorizer.transform([cleaned])

        probs = model.predict_proba(vec)[0]
        classes = model.classes_

        max_prob = float(probs.max())
        predicted_class = classes[probs.argmax()]

        # Neutral confidence threshold
        if max_prob < 0.65:
            sentiment = "Neutral"
        else:
            sentiment = predicted_class

        return {
            "sentiment": sentiment,
            "confidence": round(max_prob, 2)
        }

    except Exception:
        return {
            "sentiment": "Error",
            "confidence": 0.0
        }
