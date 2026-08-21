"""
Flora Vision AI - Grad-CAM (Gradient-weighted Class Activation Mapping) Utilities.
"""
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from .model import KERAS_MODEL_PATH

def generate_gradcam(
    img_path: str,
    output_path: str,
    model_path: str = KERAS_MODEL_PATH,
    last_conv_layer_name: str = "top_activation"
) -> str:
    """
    Computes the Grad-CAM heatmap and overlays it onto the target image.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Keras model file not found at: {model_path}")
        
    model = tf.keras.models.load_model(model_path)
    
    # Extract base model layer
    base_model = None
    for layer in model.layers:
        if isinstance(layer, tf.keras.Model) or layer.name == "efficientnetb0":
            base_model = layer
            break
            
    if base_model is None:
        raise ValueError("EfficientNetB0 base model layer not found in loaded model.")
        
    # Extract head layers
    head_layers = []
    base_model_found = False
    for layer in model.layers:
        if layer == base_model:
            base_model_found = True
            continue
        if base_model_found:
            head_layers.append(layer)
            
    last_conv_layer = base_model.get_layer(last_conv_layer_name)
    base_grad_model = tf.keras.models.Model(
        inputs=base_model.inputs,
        outputs=[last_conv_layer.output, base_model.output]
    )
    
    # Preprocess image
    img_size = (224, 224)
    img_for_pred = tf.keras.utils.load_img(img_path, target_size=img_size)
    img_array = tf.keras.utils.img_to_array(img_for_pred)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Compute gradients
    with tf.GradientTape() as tape:
        conv_outputs, base_outputs = base_grad_model(img_array)
        x = base_outputs
        for layer in head_layers:
            x = layer(x, training=False)
        preds = x
        pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]
        
    grads = tape.gradient(class_channel, conv_outputs)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
    
    conv_outputs = conv_outputs[0]
    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)
    heatmap = tf.maximum(heatmap, 0) / (tf.math.reduce_max(heatmap) + 1e-10)
    heatmap = heatmap.numpy()
    
    # Overlay heatmap on original image
    orig_img = tf.keras.utils.load_img(img_path)
    orig_img = tf.keras.utils.img_to_array(orig_img)
    
    heatmap_resized = tf.image.resize(
        heatmap[..., tf.newaxis],
        (orig_img.shape[0], orig_img.shape[1])
    ).numpy().squeeze()
    
    heatmap_resized = np.uint8(255 * heatmap_resized)
    colormap = plt.colormaps["jet"]
    colormap_colors = colormap(np.arange(256))[:, :3]
    colorized_heatmap = colormap_colors[heatmap_resized]
    colorized_heatmap = np.uint8(255 * colorized_heatmap)
    
    superimposed_img = colorized_heatmap * 0.4 + orig_img * 0.6
    superimposed_img = np.clip(superimposed_img, 0, 255).astype(np.uint8)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    tf.keras.utils.save_img(output_path, superimposed_img)
    return output_path
