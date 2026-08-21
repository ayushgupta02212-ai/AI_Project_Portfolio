"""
Sidebar component for unified portfolio.
"""
import streamlit as st
import config

def render_sidebar():
    """
    Renders custom sidebar header and developer branding.
    """
    with st.sidebar:
        st.markdown(f"""
            <div style="padding: 1rem 0.5rem; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.08); margin-bottom: 1.5rem;">
                <div style="font-size: 2rem; margin-bottom: 0.25rem;">💼</div>
                <div style="font-size: 1.25rem; font-weight: 800; background: linear-gradient(135deg, #6366f1, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                    AI Portfolio
                </div>
                <div style="display: inline-block; padding: 2px 10px; background: rgba(16, 185, 129, 0.15); color: #34d399; border-radius: 9999px; font-size: 0.72rem; font-weight: 700; margin-top: 0.35rem;">
                    ● Unified Hub
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 0.85rem; margin-top: 1rem;">
                <div style="font-size: 0.72rem; text-transform: uppercase; color: #94a3b8; font-weight: 700;">Developer</div>
                <div style="font-weight: 700; color: #f8fafc; font-size: 0.95rem;">{config.DEVELOPER_NAME}</div>
                <div style="font-size: 0.78rem; color: #818cf8;">{config.DEVELOPER_ROLE}</div>
            </div>
        """, unsafe_allow_html=True)
