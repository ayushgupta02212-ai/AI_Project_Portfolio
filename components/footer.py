"""
Unified footer component.
"""
import streamlit as st
import config

def render_footer():
    """
    Renders SaaS footer.
    """
    st.markdown(f"""
        <div class="app-footer">
            <div style="margin-bottom: 0.5rem;">
                <a href="{config.DEVELOPER_GITHUB}" target="_blank" style="color: #94a3b8; text-decoration: none; margin: 0 10px;">GitHub</a> •
                <a href="{config.DEVELOPER_LINKEDIN}" target="_blank" style="color: #94a3b8; text-decoration: none; margin: 0 10px;">LinkedIn</a> •
                <a href="mailto:{config.DEVELOPER_EMAIL}" style="color: #94a3b8; text-decoration: none; margin: 0 10px;">Email</a>
            </div>
            <div>© 2026 {config.DEVELOPER_NAME} • Unified AI Project Portfolio • Production Streamlit Hub</div>
        </div>
    """, unsafe_allow_html=True)
