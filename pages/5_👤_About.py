"""
About Me Page - Developer Profile & Career Timeline.
"""
import streamlit as st
import config
from utils.helpers import load_css
from components.sidebar import render_sidebar
from components.footer import render_footer

st.set_page_config(
    page_title="About Me | AI Portfolio",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()
render_sidebar()

# Hero Banner
st.markdown(f"""
    <div class="hero-wrapper">
        <div class="hero-content">
            <div class="hero-badge">👤 Professional Profile</div>
            <h1 class="hero-title">{config.DEVELOPER_NAME}</h1>
            <p class="hero-subtitle">
                AI/ML Student, Python Developer, and Machine Learning Enthusiast focused on building production-grade deep learning, NLP, and recommender systems.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Skills Grid
st.markdown("### 💻 Core Technical Competencies")
col_s1, col_s2, col_s3 = st.columns(3, gap="medium")

with col_s1:
    st.markdown("""
        <div style="background: rgba(18, 20, 32, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 1.5rem; height: 100%;">
            <div style="font-size: 1.3rem; margin-bottom: 0.5rem;">🧠 Machine & Deep Learning</div>
            <div style="color: #94a3b8; font-size: 0.85rem; margin-bottom: 1rem;">Neural networks, optimization, and modeling.</div>
            <div>
                <span class="tech-pill">Python</span>
                <span class="tech-pill">Machine Learning</span>
                <span class="tech-pill">Deep Learning</span>
                <span class="tech-pill">TensorFlow / Keras</span>
                <span class="tech-pill">Scikit-Learn</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_s2:
    st.markdown("""
        <div style="background: rgba(18, 20, 32, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 1.5rem; height: 100%;">
            <div style="font-size: 1.3rem; margin-bottom: 0.5rem;">👁️ Vision & NLP</div>
            <div style="color: #94a3b8; font-size: 0.85rem; margin-bottom: 1rem;">Computer vision, explainability, and text mining.</div>
            <div>
                <span class="tech-pill">Computer Vision</span>
                <span class="tech-pill">Grad-CAM (XAI)</span>
                <span class="tech-pill">OpenCV</span>
                <span class="tech-pill">Natural Language Processing</span>
                <span class="tech-pill">spaCy / NLTK</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_s3:
    st.markdown("""
        <div style="background: rgba(18, 20, 32, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 1.5rem; height: 100%;">
            <div style="font-size: 1.3rem; margin-bottom: 0.5rem;">🛠️ Systems & Deployment</div>
            <div style="color: #94a3b8; font-size: 0.85rem; margin-bottom: 1rem;">Full-stack application architecture and web services.</div>
            <div>
                <span class="tech-pill">Recommendation Systems</span>
                <span class="tech-pill">Streamlit</span>
                <span class="tech-pill">Git & GitHub</span>
                <span class="tech-pill">Deployment</span>
                <span class="tech-pill">FastAPI</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='margin-bottom: 2.5rem;'></div>", unsafe_allow_html=True)

# Timeline & Education
col_t1, col_t2 = st.columns(2, gap="large")
with col_t1:
    st.markdown("### ⏳ Project Timeline & Milestones")
    st.markdown("""
        <div style="background: rgba(18, 20, 32, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 1.5rem;">
            <div style="border-left: 2px solid #6366f1; padding-left: 1.25rem; margin-bottom: 1.25rem;">
                <div style="font-weight: 700; color: #f8fafc; font-size: 0.95rem;">Unified AI Portfolio Architecture</div>
                <div style="color: #818cf8; font-size: 0.8rem; margin-bottom: 0.25rem;">2026 • Full Integration</div>
                <div style="color: #94a3b8; font-size: 0.85rem;">Consolidated 3 independent AI services into a monolithic, modular Streamlit dashboard.</div>
            </div>
            <div style="border-left: 2px solid #06b6d4; padding-left: 1.25rem; margin-bottom: 1.25rem;">
                <div style="font-weight: 700; color: #f8fafc; font-size: 0.95rem;">NexusSuggest Hybrid Recommender</div>
                <div style="color: #818cf8; font-size: 0.8rem; margin-bottom: 0.25rem;">Machine Learning Project</div>
                <div style="color: #94a3b8; font-size: 0.85rem;">Engineered collaborative & content-based hybrid recommender with dynamic alpha weighting.</div>
            </div>
            <div style="border-left: 2px solid #10b981; padding-left: 1.25rem; margin-bottom: 1.25rem;">
                <div style="font-weight: 700; color: #f8fafc; font-size: 0.95rem;">ReviewPulse Product Intelligence</div>
                <div style="color: #818cf8; font-size: 0.8rem; margin-bottom: 0.25rem;">NLP Project</div>
                <div style="color: #94a3b8; font-size: 0.85rem;">Built aspect sentiment analyzer and deep sequence models across 15k e-commerce reviews.</div>
            </div>
            <div style="border-left: 2px solid #ec4899; padding-left: 1.25rem;">
                <div style="font-weight: 700; color: #f8fafc; font-size: 0.95rem;">Flora Vision AI Classifier</div>
                <div style="color: #818cf8; font-size: 0.8rem; margin-bottom: 0.25rem;">Computer Vision Project</div>
                <div style="color: #94a3b8; font-size: 0.85rem;">Developed EfficientNetB0 classification engine with Grad-CAM explainability heatmaps.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_t2:
    st.markdown("### 🎓 Education & Background")
    st.markdown(f"""
        <div style="background: rgba(18, 20, 32, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 1.5rem;">
            <div style="margin-bottom: 1.25rem;">
                <div style="font-weight: 700; color: #f8fafc; font-size: 1rem;">Bachelor of Technology / Computer Science</div>
                <div style="color: #818cf8; font-size: 0.82rem; margin-bottom: 0.25rem;">Specialization in Artificial Intelligence & Data Science</div>
                <div style="color: #94a3b8; font-size: 0.85rem;">Focus on Deep Neural Networks, Applied Machine Learning, Natural Language Processing, and Distributed Systems.</div>
            </div>
            <div style="border-top: 1px solid rgba(255,255,255,0.06); padding-top: 1rem;">
                <div style="font-weight: 700; color: #f8fafc; font-size: 0.95rem; margin-bottom: 0.4rem;">🎯 Career Aspirations</div>
                <div style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">
                    Seeking software engineering and machine learning roles where I can architect, train, and deploy high-impact intelligent systems that solve real-world industry problems.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

render_footer()
