"""
ReviewPulse Page - Embedded Application.
"""
import os
import sys
import streamlit as st

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

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
