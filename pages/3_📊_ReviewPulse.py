"""
ReviewPulse Page - Embedded Application.
"""
import streamlit as st
from utils.helpers import load_css
from components.sidebar import render_sidebar
from components.footer import render_footer
from projects.reviewpulse.ui import run

st.set_page_config(
    page_title="ReviewPulse | AI Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
render_sidebar()

# Run the project module
run()

render_footer()
