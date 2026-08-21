"""
ReviewPulse - Text Preprocessing and Normalization Pipeline with NLTK & Built-in Fallback.
"""
import string
import streamlit as st

# Built-in English stop words list for standalone execution
FALLBACK_STOPWORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at",
    "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could",
    "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for",
    "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
    "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm",
    "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't",
    "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours",
    "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so",
    "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
    "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until",
    "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when",
    "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would",
    "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"
}

@st.cache_resource
def get_nltk_resources():
    """
    Attempts to initialize NLTK resources with graceful fallback to built-ins.
    """
    try:
        import nltk
        from nltk.corpus import stopwords
        from nltk.stem import WordNetLemmatizer
        from nltk.tokenize import word_tokenize

        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
        nltk.download('omw-1.4', quiet=True)

        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        return stop_words, lemmatizer, word_tokenize
    except Exception:
        return FALLBACK_STOPWORDS, None, None

def clean_review_text(text: str) -> str:
    """
    Lowercases, removes punctuation, tokenizes, filters stopwords, and lemmatizes text.
    """
    if not text or not isinstance(text, str):
        return ""

    stop_words, lemmatizer, tokenizer = get_nltk_resources()
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    if tokenizer is not None:
        tokens = tokenizer(text)
    else:
        tokens = text.split()

    if lemmatizer is not None:
        cleaned_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    else:
        cleaned_tokens = [token for token in tokens if token not in stop_words]

    return " ".join(cleaned_tokens)
