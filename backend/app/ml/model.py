from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dummy training data (simple but effective)
texts = [
    "I love this product",
    "This is amazing",
    "Very happy with the service",
    "I hate this",
    "This is terrible",
    "Very bad experience",
    "It is okay",
    "Nothing special",
    "Average experience"
]

labels = [
    "Positive", "Positive", "Positive",
    "Negative", "Negative", "Negative",
    "Neutral", "Neutral", "Neutral"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)


def predict_sentiment(text: str) -> str:
    vector = vectorizer.transform([text])
    return model.predict(vector)[0]
