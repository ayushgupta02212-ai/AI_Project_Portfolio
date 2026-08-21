# 🚀 AI & Machine Learning Portfolio

A unified, production-ready SaaS-style multi-page **Streamlit** dashboard consolidating three state-of-the-art AI applications into one monolithic deployment.

---

## 🌟 Included Applications

1. **🌿 Flora Vision AI**: Deep learning image classifier leveraging transfer learning (EfficientNetB0) and Grad-CAM explainable AI heatmaps.
2. **📊 ReviewPulse**: Natural Language Processing customer intelligence pipeline combining TF-IDF, Naive Bayes, and fine-grained aspect-based sentiment extraction.
3. **🎯 NexusSuggest**: Hybrid intelligence recommender engine fusing collaborative filtering (user & item correlation) with content-based cosine similarity and cold-start fallback handlers.

---

## 📁 Directory Structure

```
AI_Project_Portfolio/
│
├── app.py                     # Root application entry point
├── config.py                  # Metadata & developer contact configuration
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
│
├── pages/
│   ├── 1_🏠_Home.py          # Landing page with metrics & application cards
│   ├── 2_🌿_FloraVisionAI.py  # Embedded Flora Vision AI application
│   ├── 3_📊_ReviewPulse.py    # Embedded ReviewPulse NLP intelligence
│   ├── 4_🎯_NexusSuggest.py   # Embedded NexusSuggest recommendation system
│   ├── 5_👤_About.py          # Developer profile, skills & timeline
│   └── 6_📞_Contact.py        # Professional contact channels & inquiry form
│
├── projects/
│   ├── flora/                 # Flora Vision AI modular subpackage
│   ├── reviewpulse/           # ReviewPulse modular subpackage
│   └── nexussuggest/          # NexusSuggest modular subpackage
│
├── components/                # Reusable UI cards, metrics, sidebar & footer
├── styles/                    # Dark glassmorphic theme stylesheet
└── utils/                     # Helper utilities
```

---

## 🚀 Running Locally

```bash
cd AI_Project_Portfolio
pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ Deploying to Streamlit Community Cloud

1. Push this repository to GitHub.
2. Visit [share.streamlit.io](https://share.streamlit.io/).
3. Connect your GitHub repository and set **Main file path** to `app.py`.
4. Click **Deploy!**
