"""
NexusSuggest - Interactive Dashboard UI.
"""
import streamlit as st
import numpy as np
from .recommender import HybridRecommender

@st.cache_resource
def load_and_fit_hybrid_recommender():
    """
    Instantiates and fits the Hybrid Recommender engine.
    """
    recommender = HybridRecommender()
    recommender.fit()
    return recommender

def run():
    """
    Main execution function for NexusSuggest application.
    """
    # Header Banner
    st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(139, 92, 246, 0.2) 0%, rgba(6, 182, 212, 0.2) 100%); padding: 1.75rem 2rem; border-radius: 18px; border: 1px solid rgba(139, 92, 246, 0.3); margin-bottom: 2rem; backdrop-filter: blur(12px);">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.25rem;">
                <span style="font-size: 2.2rem;">🎯</span>
                <h1 style="margin: 0; font-size: 2.3rem; background: linear-gradient(135deg, #a855f7, #38bdf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                    NexusSuggest: Hybrid Intelligence Recommendation Engine
                </h1>
            </div>
            <p style="color: #94a3b8; font-size: 1.05rem; margin-bottom: 0;">
                Collaborative Filtering & Content Similarity Fusion with Cold-Start Fallback Architecture
            </p>
        </div>
    """, unsafe_allow_html=True)

    with st.spinner("Compiling vector similarity spaces and pivoting collaborative matrix..."):
        recommender = load_and_fit_hybrid_recommender()

    tab1, tab2 = st.tabs(["👥 Active User Core", "❄️ New Profile Fallback (Cold-Start)"])

    with tab1:
        col1, col2 = st.columns([1, 2], gap="large")

        with col1:
            st.markdown("### User Query Controls")
            user_id = st.text_input(
                "Active User ID",
                value="user_1",
                help="Enter a valid user ID (e.g. user_1 to user_10000).",
                key="ns_user_id"
            )
            alpha = st.slider(
                "Linear Fusion Balance (α)",
                min_value=0.0,
                max_value=1.0,
                value=0.5,
                step=0.05,
                help="1.0 = 100% User-Based CF | 0.0 = 100% Item-Based CF",
                key="ns_alpha"
            )

            if user_id.strip() in recommender.collaborative.user_to_idx:
                u_idx = recommender.collaborative.user_to_idx[user_id.strip()]
                user_ratings = recommender.collaborative.df_pivot.values[u_idx]
                ratings_count = int(np.sum(~np.isnan(user_ratings)))
                user_mean = float(recommender.collaborative.user_means[u_idx])

                st.markdown("#### User Behavioral Profile")
                st.info(
                    f"**User ID**: `{user_id.strip()}`\n\n"
                    f"**Pivoted Rated Count**: {ratings_count} items\n\n"
                    f"**Historical Rating Mean**: {user_mean:.2f} / 5.0"
                )
            else:
                st.warning(
                    f"User '{user_id.strip()}' does not exist in the training dataset.\n\n"
                    "Submitting this query will automatically trigger the Cold-Start Fallback routing logic."
                )

        with col2:
            st.markdown(f"### Blended Recommendations for `{user_id}`")
            if user_id.strip():
                recs = recommender.get_hybrid_recommendations(user_id.strip(), top_n=10, alpha=alpha)
                if recs:
                    for idx, rec in enumerate(recs):
                        st.markdown(f"""
                            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 1rem 1.25rem; margin-bottom: 0.75rem;">
                                <div style="font-size: 0.75rem; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.25rem;">
                                    Recommendation #{idx+1}
                                </div>
                                <div style="font-size: 1.1rem; font-weight: 600; color: #f8fafc; margin-bottom: 0.4rem;">{rec['title']}</div>
                                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; color: #94a3b8;">
                                    <span>Genre: <span style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; padding: 2px 8px; border-radius: 6px; font-weight: 600;">{rec['genre']}</span></span>
                                    <span>Match Score: <strong style="color: #34d399; font-size: 0.95rem;">{rec['score']:.4f}</strong></span>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No recommendations found.")
            else:
                st.error("Please enter a valid User ID.")

    with tab2:
        col3, col4 = st.columns([1, 2], gap="large")

        with col3:
            st.markdown("### Cold-Start Setup")
            st.caption("Configure interest categories for brand-new users with zero historical interactions.")
            genre = st.selectbox(
                "Primary Interest Category",
                ["AI", "DevOps", "Quantum Computing", "Web Development"],
                key="ns_cold_genre"
            )
            trigger_fallback = st.button("Generate Cold-Start Recommendations", key="btn_cold_trigger", type="primary")

        with col4:
            st.markdown("### Metadata Fallback Recommendation Stack")
            if trigger_fallback or genre:
                recs = recommender.get_hybrid_recommendations("user_99999", top_n=10, preferred_genre=genre)
                if recs:
                    st.success(f"Successfully triggered Content Fallback using category anchor '{genre}'.")
                    for idx, rec in enumerate(recs):
                        st.markdown(f"""
                            <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 1rem 1.25rem; margin-bottom: 0.75rem;">
                                <div style="font-size: 0.75rem; font-weight: 700; color: #a855f7; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.25rem;">
                                    Fallback Recommendation #{idx+1}
                                </div>
                                <div style="font-size: 1.1rem; font-weight: 600; color: #f8fafc; margin-bottom: 0.4rem;">{rec['title']}</div>
                                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 0.85rem; color: #94a3b8;">
                                    <span>Genre: <span style="background: rgba(168, 85, 247, 0.15); color: #c084fc; padding: 2px 8px; border-radius: 6px; font-weight: 600;">{rec['genre']}</span></span>
                                    <span>Similarity: <strong style="color: #34d399; font-size: 0.95rem;">{rec['score']:.4f}</strong></span>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    st.info("No recommendations found.")
