import joblib
import re
import os

# ==================================================
# PATH SETUP
# ==================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

MODEL_PATH = os.path.join(MODEL_DIR, "sentiment_model.pkl")
VECT_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")

# ==================================================
# LOAD MODEL (ON STARTUP)
# ==================================================

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECT_PATH)
    print("✅ ML model loaded successfully")
except Exception as e:
    print("❌ Failed to load ML model:", e)
    model = None
    vectorizer = None

# ==================================================
# TEXT CLEANING (TRAINING-COMPATIBLE)
# ==================================================

def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+|#\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text.strip()

# ==================================================
# INFERENCE
# ==================================================

def predict_sentiment(text: str) -> dict:
    if model is None or vectorizer is None:
        return {
            "sentiment": "Error",
            "confidence": 0.0
        }

    try:
        cleaned = clean_text(text)
        vec = vectorizer.transform([cleaned])

        probs = model.predict_proba(vec)[0]
        classes = model.classes_

        max_prob = float(probs.max())
        predicted_class = classes[probs.argmax()]

        sentiment = "Neutral" if max_prob < 0.65 else predicted_class

        return {
            "sentiment": sentiment,
            "confidence": round(max_prob, 2)
        }

    except Exception as e:
        print("❌ Inference error:", e)
        return {
            "sentiment": "Error",
            "confidence": 0.0
        }
