"""
Flora Vision AI Page - Embedded Application.
"""
import streamlit as st
from utils.helpers import load_css
from components.sidebar import render_sidebar
from components.footer import render_footer
from projects.flora.ui import run

st.set_page_config(
    page_title="Flora Vision AI | AI Portfolio",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
render_sidebar()

# Run the project module
run()

render_footer()
