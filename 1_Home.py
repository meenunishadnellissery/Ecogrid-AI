import streamlit as st

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Home | EcoGrid AI",
    page_icon="🌍",
    layout="wide"
)

# ---------------- LOAD CSS ---------------- #

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- HERO ---------------- #

st.markdown("""
<div class="hero">
    <h1>🌍 EcoGrid AI</h1>
    <h3>AI-Powered Sustainability Intelligence</h3>
    <p>Empowering schools and communities toward net-zero energy systems.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- IMPACT CARDS ---------------- #

st.write("## 📈 Global Impact")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h2>120+</h2>
        <p>Schools Connected</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h2>25%</h2>
        <p>Energy Reduction</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h2>18 Tons</h2>
        <p>CO₂ Saved</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h2>92%</h2>
        <p>AI Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------- ABOUT ---------------- #

st.write("## 🤖 About EcoGrid AI")

st.markdown("""
<p>
EcoGrid AI is a sustainability intelligence platform that helps schools and communities reduce energy waste using Artificial Intelligence.
</p>
""", unsafe_allow_html=True)

# ---------------- SDGs ---------------- #

st.write("## 🎯 Sustainable Development Goals")

sdg1, sdg2, sdg3, sdg4 = st.columns(4)

with sdg1:
    st.success("SDG 7")

with sdg2:
    st.info("SDG 11")

with sdg3:
    st.warning("SDG 12")

with sdg4:
    st.error("SDG 13")

# ---------------- HOW IT WORKS ---------------- #

st.write("## ⚙️ How It Works")

step1, step2, step3 = st.columns(3)

with step1:
    st.markdown("""
    <div class="metric-card">
    <h3>1️⃣ Data Collection</h3>
    <p>Smart energy monitoring</p>
    </div>
    """, unsafe_allow_html=True)

with step2:
    st.markdown("""
    <div class="metric-card">
    <h3>2️⃣ AI Analysis</h3>
    <p>Predictive sustainability analytics</p>
    </div>
    """, unsafe_allow_html=True)

with step3:
    st.markdown("""
    <div class="metric-card">
    <h3>3️⃣ Optimization</h3>
    <p>Intelligent eco recommendations</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.caption("🌍 EcoGrid AI | Building a Smarter & Greener Future")