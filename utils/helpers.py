"""
Shared UI and Styling Helpers.
"""
import os
import streamlit as st

def load_css():
    """
    Injects custom style.css into the active Streamlit page.
    """
    css_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "styles", "style.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def render_hero(title: str, subtitle: str, badge: str = "⚡ Production-Ready AI"):
    """
    Renders gradient hero banner.
    """
    badge_html = f'<div class="hero-badge">{badge}</div>' if badge else ''
    st.markdown(f"""
        <div class="hero-wrapper">
            <div class="hero-content">
                {badge_html}
                <h1 class="hero-title">{title}</h1>
                <p class="hero-subtitle">{subtitle}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
