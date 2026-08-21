"""
Flora Vision AI - Interactive Dashboard UI.
"""
import os
import tempfile
import streamlit as st
from PIL import Image

from .model import CLASS_NAMES, KERAS_MODEL_PATH, TFLITE_MODEL_PATH
from .inference import predict_flower
from .utils import generate_gradcam

def run():
    """
    Main execution function for Flora Vision AI dashboard.
    """
    # Top Section Header
    st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.2) 0%, rgba(59, 130, 246, 0.2) 100%); padding: 1.75rem 2rem; border-radius: 18px; border: 1px solid rgba(16, 185, 129, 0.3); margin-bottom: 2rem; backdrop-filter: blur(12px);">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.25rem;">
                <span style="font-size: 2.2rem;">🌸</span>
                <h1 style="margin: 0; font-size: 2.3rem; background: linear-gradient(135deg, #34d399, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                    FloraVision Flower Classifier
                </h1>
            </div>
            <p style="color: #94a3b8; font-size: 1.05rem; margin-bottom: 0;">
                Deep Learning Model Inference (EfficientNetB0) with Grad-CAM Explainable AI Saliency Heatmaps
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Check if TFLite model exists
    if not os.path.exists(TFLITE_MODEL_PATH):
        st.error(f"🚨 TFLite model binary not found at `{TFLITE_MODEL_PATH}`.")
        return

    # Image Uploader
    uploaded_file = st.file_uploader("Upload Flower Image (.jpg, .jpeg, .png)", type=["jpg", "jpeg", "png"], key="flora_file_uploader")

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.markdown("### 🖼️ Input Image")
            st.image(image, use_container_width=True, caption="Uploaded Floral Sample")

        with col2:
            st.markdown("### ⚡ Real-Time AI Inference")
            
            with st.spinner("Executing TFLite convolutional tensor inference..."):
                result = predict_flower(image)

            pred_label = result["label"]
            confidence = result["confidence"]
            scores = result["confidence_scores"]

            st.metric(
                label="Predicted Species",
                value=pred_label,
                delta=f"{confidence * 100:.2f}% Confidence"
            )
            st.success(f"Classification result: **{pred_label}** with **{confidence * 100:.2f}%** certainty.")

            # Styled Confidence Bars
            st.markdown("""
                <div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 1.25rem; margin-top: 1rem;">
                    <h4 style="margin-top: 0; margin-bottom: 1rem; color: #f8fafc; font-size: 1.05rem;">Species Confidence Distribution</h4>
            """, unsafe_allow_html=True)

            for name, score in scores.items():
                score_pct = score * 100
                st.markdown(f"""
                    <div style="margin-bottom: 12px;">
                        <div style="display: flex; justify-content: space-between; font-size: 0.88rem; margin-bottom: 3px; color: #cbd5e1;">
                            <span>{name}</span>
                            <span style="font-weight: 700; color: #34d399;">{score_pct:.1f}%</span>
                        </div>
                        <div style="background: rgba(255, 255, 255, 0.08); border-radius: 6px; height: 10px; overflow: hidden;">
                            <div style="width: {score_pct}%; background: linear-gradient(90deg, #10b981 0%, #3b82f6 100%); height: 100%; border-radius: 6px;"></div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        # Grad-CAM Section
        st.markdown("---")
        st.markdown("### 🔍 Model Explainability & Interpretability (Grad-CAM)")
        st.markdown("Grad-CAM (Gradient-weighted Class Activation Mapping) extracts spatial activations from the final convolutional layer to visualize the discriminative features driving the classification.")

        if st.button("Generate Grad-CAM Heatmap Overlay", key="btn_grad_cam", type="primary"):
            with st.spinner("Extracting layer gradients and generating activation heatmap..."):
                if not os.path.exists(KERAS_MODEL_PATH):
                    st.warning("⚠️ Keras model (`best_model.keras`) is required to generate Grad-CAM gradients.")
                else:
                    temp_dir = tempfile.mkdtemp()
                    temp_img_path = os.path.join(temp_dir, "input_image.jpg")
                    output_heatmap_path = os.path.join(temp_dir, "grad_cam_output.png")
                    image.save(temp_img_path)

                    try:
                        generate_gradcam(
                            img_path=temp_img_path,
                            output_path=output_heatmap_path,
                            model_path=KERAS_MODEL_PATH,
                            last_conv_layer_name="top_activation"
                        )
                        st.image(
                            output_heatmap_path,
                            caption=f"Grad-CAM Heatmap overlay for predicted category '{pred_label}'",
                            use_container_width=True
                        )
                        st.info("🟢 The thermal red/yellow regions above highlight the highest neural activation features (e.g. petals, pistil, texture) that influenced the prediction.")
                    except Exception as e:
                        st.error(f"Error computing Grad-CAM: {e}")
                    finally:
                        if os.path.exists(temp_img_path):
                            os.remove(temp_img_path)
                        if os.path.exists(output_heatmap_path):
                            os.remove(output_heatmap_path)
                        if os.path.exists(temp_dir):
                            os.rmdir(temp_dir)
    else:
        st.info("💡 Upload a flower image (.jpg, .jpeg, or .png) above to trigger real-time AI classification.")
        st.markdown("""
            <div style="text-align: center; padding: 3.5rem 2rem; border: 2px dashed rgba(255,255,255,0.12); border-radius: 16px; background: rgba(255,255,255,0.01); margin-top: 1rem;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🌸 🌼 🌹 🌻 🌷</div>
                <h3 style="color: #cbd5e1; margin-bottom: 0.35rem;">Supported Flower Species</h3>
                <p style="color: #94a3b8; font-size: 0.92rem; max-width: 500px; margin: 0 auto;">
                    Daisy, Dandelion, Rose, Sunflower, Tulip. The system achieves 91.4% test accuracy using fine-tuned EfficientNetB0 representations.
                </p>
            </div>
        """, unsafe_allow_html=True)
