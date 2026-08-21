"""
ReviewPulse - Interactive Dashboard UI.
"""
import streamlit as st
import pandas as pd
import altair as alt

from .sentiment import predict_sentiment, load_sentiment_models
from .utils import load_reviewpulse_data

def run():
    """
    Main execution function for ReviewPulse application.
    """
    # Header Banner
    st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(6, 182, 212, 0.2) 0%, rgba(59, 130, 246, 0.2) 100%); padding: 1.75rem 2rem; border-radius: 18px; border: 1px solid rgba(6, 182, 212, 0.3); margin-bottom: 2rem; backdrop-filter: blur(12px);">
            <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.25rem;">
                <span style="font-size: 2.2rem;">📊</span>
                <h1 style="margin: 0; font-size: 2.3rem; background: linear-gradient(135deg, #06b6d4, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                    ReviewPulse: Product Intelligence Dashboard
                </h1>
            </div>
            <p style="color: #94a3b8; font-size: 1.05rem; margin-bottom: 0;">
                Real-time Review Analysis & Aspect-Based Sentiment Insights using Natural Language Processing
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Load data and check models
    try:
        df_reviews, df_aspects = load_reviewpulse_data()
        load_sentiment_models()
        models_ready = True
    except Exception as e:
        st.error(f"Error loading ReviewPulse resources: {e}")
        return

    tab_dashboard, tab_prediction = st.tabs(["📈 Sentiment & Product Insights", "🔮 Real-Time Sentiment Predictor"])

    with tab_dashboard:
        st.subheader("Key Operational Metrics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("""
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-top: 4px solid #3b82f6; border-radius: 14px; padding: 1.25rem; text-align: center;">
                    <div style="font-size: 1.8rem; font-weight: 700; color: #f8fafc;">15,000</div>
                    <div style="font-size: 0.75rem; text-transform: uppercase; color: #94a3b8; font-weight: 600; letter-spacing: 0.05em;">Total Reviews Analyzed</div>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-top: 4px solid #06b6d4; border-radius: 14px; padding: 1.25rem; text-align: center;">
                    <div style="font-size: 1.8rem; font-weight: 700; color: #f8fafc;">67.7 words</div>
                    <div style="font-size: 0.75rem; text-transform: uppercase; color: #94a3b8; font-weight: 600; letter-spacing: 0.05em;">Avg. Length (Raw)</div>
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-top: 4px solid #10b981; border-radius: 14px; padding: 1.25rem; text-align: center;">
                    <div style="font-size: 1.8rem; font-weight: 700; color: #f8fafc;">34.9 words</div>
                    <div style="font-size: 0.75rem; text-transform: uppercase; color: #94a3b8; font-weight: 600; letter-spacing: 0.05em;">Avg. Length (Cleaned)</div>
                </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown("""
                <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-top: 4px solid #8b5cf6; border-radius: 14px; padding: 1.25rem; text-align: center;">
                    <div style="font-size: 1.8rem; font-weight: 700; color: #f8fafc;">48.37%</div>
                    <div style="font-size: 0.75rem; text-transform: uppercase; color: #94a3b8; font-weight: 600; letter-spacing: 0.05em;">Vocabulary Compression</div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='margin-bottom: 2rem;'></div>", unsafe_allow_html=True)
        col_left, col_right = st.columns([1, 1.4], gap="large")

        with col_left:
            st.subheader("Dataset Sentiment Balance")
            sentiment_counts = df_reviews['sentiment'].value_counts().reset_index()
            sentiment_counts.columns = ['Sentiment', 'Reviews']

            chart = alt.Chart(sentiment_counts).mark_bar(cornerRadiusTopLeft=8, cornerRadiusTopRight=8).encode(
                x=alt.X('Sentiment:N', sort=['positive', 'neutral', 'negative']),
                y=alt.Y('Reviews:Q', title="Count"),
                color=alt.Color('Sentiment:N', scale=alt.Scale(
                    domain=['positive', 'neutral', 'negative'],
                    range=['#10b981', '#94a3b8', '#f43f5e']
                ), legend=None)
            ).properties(height=300)
            st.altair_chart(chart, use_container_width=True)

        with col_right:
            st.subheader("Aspect Sentiment Extraction Analysis")
            df_aspects_melted = pd.melt(
                df_aspects,
                id_vars=['aspect'],
                value_vars=['positive', 'negative'],
                var_name='Sentiment',
                value_name='Mentions'
            )
            aspect_chart = alt.Chart(df_aspects_melted).mark_bar().encode(
                x=alt.X('Sentiment:N', title=None, sort=['positive', 'negative']),
                y=alt.Y('Mentions:Q', title="Mentions"),
                color=alt.Color('Sentiment:N', scale=alt.Scale(
                    domain=['positive', 'negative'],
                    range=['#10b981', '#f43f5e']
                ), legend=None),
                column=alt.Column('aspect:N', title=None, header=alt.Header(labelFontSize=13, labelColor='#cbd5e1'))
            ).properties(width=75, height=300).configure_facet(spacing=8)
            st.altair_chart(aspect_chart, use_container_width=True)

        st.subheader("Granular Aspect Insights Detail Table")
        df_aspects_calc = df_aspects.copy()
        df_aspects_calc['total_mentions'] = df_aspects_calc['positive'] + df_aspects_calc['negative']
        df_aspects_calc['pos_ratio_pct'] = (df_aspects_calc['positive'] / df_aspects_calc['total_mentions'] * 100).round(1)
        df_aspects_display = df_aspects_calc.sort_values(by='total_mentions', ascending=False)

        st.dataframe(
            df_aspects_display.rename(columns={
                'aspect': 'Product Feature',
                'positive': 'Positive Mentions',
                'negative': 'Negative Mentions',
                'total_mentions': 'Total Mentions',
                'pos_ratio_pct': 'Approval Ratio (%)'
            }),
            use_container_width=True,
            hide_index=True
        )

    with tab_prediction:
        st.subheader("Real-Time Review Analysis Terminal")
        st.markdown("Enter customer review text below to classify its sentiment polarity and confidence breakdown.")

        review_input = st.text_area(
            "Review Text Input",
            value="This cell phone has a beautiful, bright screen and the battery life lasts for days! Highly recommended.",
            height=130,
            key="rp_review_input"
        )

        if st.button("Predict Sentiment 🔮", key="btn_rp_predict", type="primary", use_container_width=True):
            if not review_input.strip():
                st.warning("Please enter review text to analyze.")
            else:
                with st.spinner("Tokenizing, lemmatizing, and classifying review text..."):
                    res = predict_sentiment(review_input)

                sentiment = res["sentiment"]
                confidence = res["confidence"]
                probs = res["probabilities"]

                color_map = {
                    "positive": ("#10b981", "rgba(16, 185, 129, 0.15)"),
                    "negative": ("#f43f5e", "rgba(244, 63, 94, 0.15)"),
                    "neutral": ("#94a3b8", "rgba(148, 163, 184, 0.15)")
                }
                border_color, bg_color = color_map.get(sentiment, ("#94a3b8", "rgba(255,255,255,0.05)"))

                st.markdown(f"""
                    <div style="background: {bg_color}; border: 2px solid {border_color}; border-radius: 14px; padding: 1.5rem; text-align: center; margin: 1.5rem 0;">
                        <div style="font-size: 1.8rem; font-weight: 800; text-transform: uppercase; color: {border_color}; margin-bottom: 0.25rem;">
                            {sentiment} Sentiment
                        </div>
                        <div style="font-size: 1.05rem; color: #cbd5e1;">Confidence: <strong>{confidence:.2f}%</strong></div>
                    </div>
                """, unsafe_allow_html=True)

                st.markdown("#### Confidence Breakdown per Sentiment Class")
                col_p1, col_p2, col_p3 = st.columns(3)
                with col_p1:
                    st.metric("🟢 Positive Probability", f"{probs['positive']*100:.2f}%")
                with col_p2:
                    st.metric("🟡 Neutral Probability", f"{probs['neutral']*100:.2f}%")
                with col_p3:
                    st.metric("🔴 Negative Probability", f"{probs['negative']*100:.2f}%")

                with st.expander("🔍 Cleaned & Lemmatized Text"):
                    st.code(res["cleaned_text"], language="text")
