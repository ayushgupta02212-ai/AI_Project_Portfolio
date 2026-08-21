"""
ReviewPulse - Sentiment Analysis Model Loader and Inference Engine.
"""
import os
import pickle
from typing import Dict, Any
import streamlit as st
from .preprocessing import clean_review_text

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
TFIDF_PATH = os.path.join(PROJECT_DIR, "models", "tfidf_vectorizer.pkl")
NB_PATH = os.path.join(PROJECT_DIR, "models", "naive_bayes_model.pkl")

SENTIMENT_LABELS = ['negative', 'neutral', 'positive']

@st.cache_resource
def load_sentiment_models():
    """
    Loads and caches TF-IDF vectorizer and Naive Bayes model.
    """
    if not os.path.exists(TFIDF_PATH) or not os.path.exists(NB_PATH):
        raise FileNotFoundError(f"Model binaries missing in {os.path.join(PROJECT_DIR, 'models')}")

    with open(TFIDF_PATH, "rb") as f:
        tfidf = pickle.load(f)
    with open(NB_PATH, "rb") as f:
        nb = pickle.load(f)
    return tfidf, nb

def predict_sentiment(raw_text: str) -> Dict[str, Any]:
    """
    Cleans raw review text, applies TF-IDF vectorization, and predicts sentiment category and class probabilities.
    """
    tfidf, nb_model = load_sentiment_models()
    cleaned = clean_review_text(raw_text)
    features = tfidf.transform([cleaned])

    pred_idx = int(nb_model.predict(features)[0])
    pred_probs = nb_model.predict_proba(features)[0]

    sentiment = SENTIMENT_LABELS[pred_idx]
    confidence = float(pred_probs[pred_idx]) * 100

    probabilities = {
        'negative': float(pred_probs[0]),
        'neutral': float(pred_probs[1]),
        'positive': float(pred_probs[2])
    }

    return {
        "sentiment": sentiment,
        "confidence": confidence,
        "probabilities": probabilities,
        "cleaned_text": cleaned
    }
