"""
Metrics component displaying animated KPI cards.
"""
import streamlit as st

def render_metrics():
    """
    Renders the KPI statistics grid.
    """
    st.markdown("""
        <div class="metrics-grid">
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 0.25rem;">🚀</div>
                <div class="metric-val">3</div>
                <div class="metric-lbl">AI Projects</div>
            </div>
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 0.25rem;">🧠</div>
                <div class="metric-val">Core ML</div>
                <div class="metric-lbl">Machine Learning</div>
            </div>
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 0.25rem;">👁️</div>
                <div class="metric-val">EfficientNet</div>
                <div class="metric-lbl">Computer Vision</div>
            </div>
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 0.25rem;">💬</div>
                <div class="metric-val">ABSA NLP</div>
                <div class="metric-lbl">Natural Language</div>
            </div>
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 0.25rem;">🎯</div>
                <div class="metric-val">Hybrid</div>
                <div class="metric-lbl">Recommendation</div>
            </div>
            <div class="metric-card">
                <div style="font-size: 1.5rem; margin-bottom: 0.25rem;">🛡️</div>
                <div class="metric-val">100%</div>
                <div class="metric-lbl">Production Ready</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
