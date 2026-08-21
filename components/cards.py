"""
Project Cards component for dashboard showcase with native in-app navigation.
"""
import streamlit as st

def render_project_cards():
    """
    Renders 3 project cards in a responsive columns grid with in-app page switching.
    """
    col1, col2, col3 = st.columns(3, gap="medium")

    # Card 1: Flora Vision AI
    with col1:
        st.markdown("""
            <div class="project-card-wrapper">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🌿</div>
                <div style="font-size: 1.4rem; font-weight: 700; color: #f8fafc; margin-bottom: 0.4rem;">
                    Flora Vision AI
                </div>
                <div style="color: #94a3b8; font-size: 0.9rem; line-height: 1.5; min-height: 55px; margin-bottom: 1rem;">
                    Deep learning powered plant and flower recognition with Grad-CAM visualization.
                </div>
                <div>
                    <span class="tech-pill">EfficientNetB0</span>
                    <span class="tech-pill">TFLite</span>
                    <span class="tech-pill">Grad-CAM</span>
                    <span class="tech-pill">OpenCV</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Launch Application", key="btn_launch_flora", type="primary", use_container_width=True):
            st.switch_page("pages/2_🌿_FloraVisionAI.py")

        with st.expander("📖 Learn More"):
            st.markdown("""
                - **Accuracy**: 91.4% test accuracy across 5 distinct species.
                - **Explainability**: Saliency heatmaps highlighting petal and pistil features.
                - **Inference**: Sub-second lightweight CPU inference.
            """)

    # Card 2: ReviewPulse
    with col2:
        st.markdown("""
            <div class="project-card-wrapper">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
                <div style="font-size: 1.4rem; font-weight: 700; color: #f8fafc; margin-bottom: 0.4rem;">
                    ReviewPulse
                </div>
                <div style="color: #94a3b8; font-size: 0.9rem; line-height: 1.5; min-height: 55px; margin-bottom: 1rem;">
                    Advanced sentiment analysis platform for customer reviews using Natural Language Processing.
                </div>
                <div>
                    <span class="tech-pill">TF-IDF</span>
                    <span class="tech-pill">Naive Bayes</span>
                    <span class="tech-pill">spaCy ABSA</span>
                    <span class="tech-pill">Word2Vec</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Launch Application", key="btn_launch_reviewpulse", type="primary", use_container_width=True):
            st.switch_page("pages/3_📊_ReviewPulse.py")

        with st.expander("📖 Learn More"):
            st.markdown("""
                - **Dataset Volume**: 15,000 processed e-commerce customer reviews.
                - **ABSA Engine**: Aspect extraction for Battery, Screen, Camera, and Price.
                - **Compression**: 48.37% text compression via lemmatization and stopword removal.
            """)

    # Card 3: NexusSuggest
    with col3:
        st.markdown("""
            <div class="project-card-wrapper">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">🎯</div>
                <div style="font-size: 1.4rem; font-weight: 700; color: #f8fafc; margin-bottom: 0.4rem;">
                    NexusSuggest
                </div>
                <div style="color: #94a3b8; font-size: 0.9rem; line-height: 1.5; min-height: 55px; margin-bottom: 1rem;">
                    Machine learning recommendation system providing intelligent personalized suggestions.
                </div>
                <div>
                    <span class="tech-pill">Hybrid Fusion</span>
                    <span class="tech-pill">Collaborative Filtering</span>
                    <span class="tech-pill">Cold-Start</span>
                    <span class="tech-pill">Cosine Sim</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Launch Application", key="btn_launch_nexussuggest", type="primary", use_container_width=True):
            st.switch_page("pages/4_🎯_NexusSuggest.py")

        with st.expander("📖 Learn More"):
            st.markdown("""
                - **Hybrid Fusion**: Real-time linear fusion slider (α) balancing exploration vs exploitation.
                - **Cold-Start Handler**: Content-based fallback routing for zero-interaction profiles.
                - **Scale**: 10,000 user profiles across 5,000 catalog items.
            """)
