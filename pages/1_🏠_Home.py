"""
Home Page - Master Showcase & Unified AI Launcher.
"""
import streamlit as st
import config
from utils.helpers import load_css, render_hero
from components.metrics import render_metrics
from components.cards import render_project_cards
from components.sidebar import render_sidebar
from components.footer import render_footer

st.set_page_config(
    page_title="Home | AI & Machine Learning Portfolio",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
render_sidebar()

# Hero Section
render_hero(
    title=config.APP_TITLE,
    subtitle=config.APP_SUBTITLE,
    badge="🚀 Unified AI Application Hub"
)

# Statistics Cards
render_metrics()

# Project Cards Section
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 1.5rem;">
        <div>
            <h2 style="font-size: 1.85rem; color: #f8fafc; margin-bottom: 0.25rem;">Featured AI Applications</h2>
            <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 0;">Explore and launch fully interactive production AI models.</p>
        </div>
        <div style="font-size: 0.85rem; color: #818cf8; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">
            3 Active Services
        </div>
    </div>
""", unsafe_allow_html=True)

render_project_cards()

render_footer()
