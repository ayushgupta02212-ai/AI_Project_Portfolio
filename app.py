"""
AI Project Portfolio - Master Navigation Router.
"""
import os
import sys
import streamlit as st

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Define explicit multi-page structure
home_page = st.Page("pages/1_🏠_Home.py", title="Home", icon="🏠", default=True)
flora_page = st.Page("pages/2_🌿_FloraVisionAI.py", title="Flora Vision AI", icon="🌿")
reviewpulse_page = st.Page("pages/3_📊_ReviewPulse.py", title="ReviewPulse", icon="📊")
nexussuggest_page = st.Page("pages/4_🎯_NexusSuggest.py", title="NexusSuggest", icon="🎯")
about_page = st.Page("pages/5_👤_About.py", title="About Me", icon="👤")
contact_page = st.Page("pages/6_📞_Contact.py", title="Contact", icon="📞")

pg = st.navigation([home_page, flora_page, reviewpulse_page, nexussuggest_page, about_page, contact_page])
pg.run()
