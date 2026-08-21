"""
Contact Page - Professional Connections & Direct Messaging.
"""
import os
import sys
import streamlit as st

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import config
from utils.helpers import load_css
from components.sidebar import render_sidebar
from components.footer import render_footer

st.set_page_config(
    page_title="Contact | AI Portfolio",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
render_sidebar()

# Hero Banner
st.markdown("""
    <div class="hero-wrapper">
        <div class="hero-content">
            <div class="hero-badge">📞 Get in Touch</div>
            <h1 class="hero-title">Connect & Collaborate</h1>
            <p class="hero-subtitle">
                Reach out for full-time AI/ML opportunities, internships, technical discussions, or open-source collaborations.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Contact Cards Grid
st.markdown("### 🌐 Contact Channels")
col_c1, col_c2, col_c3, col_c4 = st.columns(4, gap="medium")

with col_c1:
    st.markdown(f"""
        <div style="background: rgba(18, 20, 32, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 1.5rem; text-align: center; margin-bottom: 0.5rem;">
            <div style="font-size: 2.2rem; margin-bottom: 0.5rem;">✉️</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #f8fafc; margin-bottom: 0.25rem;">Email</div>
            <div style="font-size: 0.82rem; color: #94a3b8;">{config.DEVELOPER_EMAIL}</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Send Email", url=f"mailto:{config.DEVELOPER_EMAIL}", use_container_width=True, type="primary")

with col_c2:
    st.markdown(f"""
        <div style="background: rgba(18, 20, 32, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 1.5rem; text-align: center; margin-bottom: 0.5rem;">
            <div style="font-size: 2.2rem; margin-bottom: 0.5rem;">💻</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #f8fafc; margin-bottom: 0.25rem;">GitHub</div>
            <div style="font-size: 0.82rem; color: #94a3b8;">Open-Source Code</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("View GitHub", url=config.DEVELOPER_GITHUB, use_container_width=True)

with col_c3:
    st.markdown(f"""
        <div style="background: rgba(18, 20, 32, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 1.5rem; text-align: center; margin-bottom: 0.5rem;">
            <div style="font-size: 2.2rem; margin-bottom: 0.5rem;">💼</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #f8fafc; margin-bottom: 0.25rem;">LinkedIn</div>
            <div style="font-size: 0.82rem; color: #94a3b8;">Professional Profile</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("Connect", url=config.DEVELOPER_LINKEDIN, use_container_width=True)

with col_c4:
    st.markdown(f"""
        <div style="background: rgba(18, 20, 32, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 1.5rem; text-align: center; margin-bottom: 0.5rem;">
            <div style="font-size: 2.2rem; margin-bottom: 0.5rem;">📄</div>
            <div style="font-size: 1.1rem; font-weight: 700; color: #f8fafc; margin-bottom: 0.25rem;">Resume</div>
            <div style="font-size: 0.82rem; color: #94a3b8;">Curriculum Vitae</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("View Resume", url=config.DEVELOPER_GITHUB, use_container_width=True)

st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)

# Message Form
col_f1, col_f2 = st.columns([1.5, 1], gap="large")
with col_f1:
    st.markdown("### 💬 Direct Message Terminal")
    name = st.text_input("Full Name", placeholder="e.g. Recruiter / Collaborator Name")
    email = st.text_input("Email Address", placeholder="e.g. yourname@company.com")
    message = st.text_area("Message / Opportunity Details", placeholder="Share your message or job opportunity description...", height=120)
    if st.button("Send Inquiry 🚀", type="primary", use_container_width=True):
        if name and email and message:
            st.success(f"Thank you, {name}! Your message has been logged. You can also reach out via email at {config.DEVELOPER_EMAIL}.")
        else:
            st.error("Please fill in all fields before sending.")

with col_f2:
    st.markdown("### 📍 Location & Availability")
    st.markdown(f"""
        <div style="background: rgba(18, 20, 32, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 1.5rem;">
            <div style="margin-bottom: 1rem;">
                <div style="color: #818cf8; font-size: 0.78rem; font-weight: 700; text-transform: uppercase;">Status</div>
                <div style="color: #34d399; font-weight: 700;">🟢 Open to Opportunities</div>
            </div>
            <div style="margin-bottom: 1rem;">
                <div style="color: #818cf8; font-size: 0.78rem; font-weight: 700; text-transform: uppercase;">Role Specialization</div>
                <div style="color: #f8fafc; font-weight: 600;">{config.DEVELOPER_ROLE}</div>
            </div>
            <div>
                <div style="color: #818cf8; font-size: 0.78rem; font-weight: 700; text-transform: uppercase;">Timezone</div>
                <div style="color: #cbd5e1;">IST (UTC+5:30) • Remote / Hybrid Ready</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

render_footer()
