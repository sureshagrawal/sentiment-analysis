import joblib
import re
import os

# -------- PATH SETUP (SAME AS train_model.py) --------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "sentiment_model.pkl")
VECT_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")


# -------- LOAD MODEL & VECTORIZER --------

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECT_PATH)


# -------- TEXT CLEANING (SAME LOGIC) --------

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+|#\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text.strip()


# -------- INFERENCE FUNCTION --------

def predict_sentiment(text: str):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])

    probs = model.predict_proba(vec)[0]
    classes = model.classes_

    max_prob = max(probs)
    predicted_class = classes[probs.argmax()]

    # Neutral threshold logic
    if max_prob < 0.65:
        final_sentiment = "Neutral"
    else:
        final_sentiment = predicted_class

    return {
        "sentiment": final_sentiment,
        "confidence": round(float(max_prob), 2)
    }

