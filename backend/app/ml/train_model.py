import pandas as pd
import re
import joblib
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# ---------------- PATH SETUP ----------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "Twitter_Sentiments.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "sentiment_model.pkl")
VECT_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

# DATA_PATH = "ml/data/Twitter_Sentiments.csv"
# MODEL_PATH = "ml/models/sentiment_model.pkl"
# VECT_PATH = "ml/models/vectorizer.pkl"

# ---------------- TEXT CLEANING ----------------

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+|#\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text.strip()


# ---------------- TRAINING PIPELINE ----------------

def main():
    print("📥 Loading dataset...")
    df = pd.read_csv(DATA_PATH)

    # ---- STANDARDIZE COLUMN NAMES (VERY IMPORTANT) ----
    df = df.rename(columns={
        "text": "tweet",
        "sentence": "tweet",
        "review": "tweet",
        "content": "tweet",
        "sentiment": "label"
    })

    # ---- SAFETY CHECK ----
    if "tweet" not in df.columns or "label" not in df.columns:
        raise ValueError(
            f"Dataset must contain text & label columns. Found columns: {df.columns}"
        )

    # ---- CLEAN TEXT ----
    print("🧹 Cleaning text...")
    df["tweet"] = df["tweet"].astype(str).apply(clean_text)

    X = df["tweet"]
    y = df["label"].astype(str).str.capitalize()   # positive → Positive

    # ---- TF-IDF VECTORIZATION ----
    print("🔢 Vectorizing text (TF-IDF)...")
    vectorizer = TfidfVectorizer(
        max_features=30000,
        ngram_range=(1, 2)
    )
    X_vec = vectorizer.fit_transform(X)

    # ---- TRAIN / TEST SPLIT ----
    X_train, X_test, y_train, y_test = train_test_split(
        X_vec, y, test_size=0.2, random_state=42
    )

    # ---- MODEL TRAINING ----
    print("🤖 Training Random Forest model...")
    model = RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    # ---- SAVE MODEL ----
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECT_PATH)

    print("✅ Model & Vectorizer saved successfully.")


# ---------------- ENTRY POINT ----------------

if __name__ == "__main__":
    main()