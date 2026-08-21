"""
Flora Vision AI - Model Loader and Path Management.
"""
import os
import streamlit as st
import tensorflow as tf

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
TFLITE_MODEL_PATH = os.path.join(PROJECT_DIR, "models", "model.tflite")
KERAS_MODEL_PATH = os.path.join(PROJECT_DIR, "models", "best_model.keras")

CLASS_NAMES = ['Daisy', 'Dandelion', 'Rose', 'Sunflower', 'Tulip']

@st.cache_resource
def load_tflite_interpreter(model_path: str = None):
    """
    Loads and caches the TFLite interpreter for real-time inference.
    """
    if model_path is None:
        model_path = TFLITE_MODEL_PATH
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"TFLite model not found at {model_path}")
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter
