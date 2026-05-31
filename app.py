import streamlit as st

st.set_page_config(
    page_title="EcoGrid AI",
    page_icon="🌍",
    layout="wide"
)

# Load CSS
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🌍 EcoGrid AI</h1>
    <h3>AI-Powered Sustainability Intelligence Platform</h3>
    <p>Building Smarter & Greener Communities</p>
</div>
""", unsafe_allow_html=True)

st.write("## Welcome")

