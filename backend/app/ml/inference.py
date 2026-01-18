import joblib
import re
import os
import urllib.request

# ---------------- PATH SETUP ----------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

MODEL_PATH = os.path.join(MODEL_DIR, "sentiment_model.pkl")
VECT_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")

# ---------------- EXTERNAL MODEL URLS ----------------

MODEL_URL = "https://drive.google.com/uc?id=1s2k-GfcM8JkzMEkDx5V4JSB_sAqgrwbZ"
VECT_URL = "https://drive.google.com/uc?id=16ne-gRCSOBiJJ0GzUDQcCW6rGS2mPhhs"

# ---------------- DOWNLOAD IF MISSING ----------------

def download_if_missing():
    os.makedirs(MODEL_DIR, exist_ok=True)

    if not os.path.exists(MODEL_PATH):
        print("⬇️ Downloading sentiment model...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

    if not os.path.exists(VECT_PATH):
        print("⬇️ Downloading vectorizer...")
        urllib.request.urlretrieve(VECT_URL, VECT_PATH)


download_if_missing()

# ---------------- LOAD MODEL ----------------

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECT_PATH)

# ---------------- TEXT CLEANING ----------------

def clean_text(text: str) -> str:
    text = str(text).lower()
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

        # Neutral confidence threshold (same as before)
        if max_prob < 0.65:
            sentiment = "Neutral"
        else:
            sentiment = predicted_class

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
