"""
Flora Vision AI - Image Preprocessing and Inference Pipeline.
"""
from typing import Tuple, Dict, Any
import numpy as np
import tensorflow as tf
from PIL import Image
from .model import load_tflite_interpreter, CLASS_NAMES

def preprocess_image(image: Image.Image, target_size: Tuple[int, int] = (224, 224)) -> np.ndarray:
    """
    Resizes and transforms an RGB PIL image into an input tensor.
    """
    img_resized = image.resize(target_size)
    img_array = tf.keras.utils.img_to_array(img_resized)
    input_data = np.expand_dims(img_array, axis=0).astype(np.float32)
    return input_data

def predict_flower(image: Image.Image) -> Dict[str, Any]:
    """
    Runs TFLite inference on the uploaded PIL image and returns predictions with confidence.
    """
    interpreter = load_tflite_interpreter()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    target_size = (input_details[0]['shape'][1], input_details[0]['shape'][2])
    input_data = preprocess_image(image, target_size)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    predictions = interpreter.get_tensor(output_details[0]['index'])[0]

    pred_idx = int(np.argmax(predictions))
    pred_label = CLASS_NAMES[pred_idx]
    confidence = float(predictions[pred_idx])

    confidence_scores = {CLASS_NAMES[i]: float(predictions[i]) for i in range(len(CLASS_NAMES))}

    return {
        "label": pred_label,
        "confidence": confidence,
        "confidence_scores": confidence_scores,
        "raw_predictions": predictions
    }
