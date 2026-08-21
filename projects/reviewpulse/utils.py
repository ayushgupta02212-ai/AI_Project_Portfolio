"""
ReviewPulse - Dataset and Aspect Analytics Utilities.
"""
import os
import pandas as pd
import streamlit as st

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESSED_REVIEWS_PATH = os.path.join(PROJECT_DIR, "data", "processed_reviews.csv")
ASPECT_INSIGHTS_PATH = os.path.join(PROJECT_DIR, "data", "aspect_insights.csv")

@st.cache_data
def load_reviewpulse_data():
    """
    Loads and caches the processed reviews and aspect insights datasets.
    """
    if not os.path.exists(PROCESSED_REVIEWS_PATH) or not os.path.exists(ASPECT_INSIGHTS_PATH):
        raise FileNotFoundError(f"ReviewPulse data files missing in {os.path.join(PROJECT_DIR, 'data')}")

    df_reviews = pd.read_csv(PROCESSED_REVIEWS_PATH)
    df_aspects = pd.read_csv(ASPECT_INSIGHTS_PATH)
    return df_reviews, df_aspects
