from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.linear_model import LinearRegression

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="EcoGrid AI Dashboard",
    page_icon="🌍",
    layout="wide"
)
# ---------------- LOAD CSS ---------------- #

with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: #00FFAA;
    text-align: center;
}

.stMetric {
    background-color: #1C1F26;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
}

div.stButton > button {
    background-color: #00FFAA;
    color: black;
    border-radius: 10px;
    border: none;
    padding: 10px;
    font-weight: bold;
}

.block-container {
    max-width: 1200px;
    margin: auto;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.title("🌍 EcoGrid AI")
st.subheader("AI-Powered Sustainability Intelligence Platform for Schools")

st.markdown("---")

# ---------------- SIDEBAR ---------------- #

st.sidebar.header("🏫 School Information")

school_name = st.sidebar.text_input(
    "School Name",
    "Green Future School"
)

electricity = st.sidebar.slider(
    "Monthly Electricity Usage (kWh)",
    0,
    5000,
    1200
)

solar = st.sidebar.selectbox(
    "Solar Energy Installed?",
    ["No", "Yes"]
)

students = st.sidebar.slider(
    "Number of Students",
    50,
    5000,
    1000
)

building_size = st.sidebar.slider(
    "Campus Size (sq ft)",
    1000,
    100000,
    20000
)



# ---------------- CALCULATIONS ---------------- #

carbon = electricity * 0.4

score = max(0, 100 - (electricity // 50))

if solar == "Yes":
    score += 15

score = min(score, 100)

# ---------------- DASHBOARD ---------------- #

st.write("## 📊 School Sustainability Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "⚡ Electricity Usage",
        f"{electricity} kWh"
    )

with col2:
    st.metric(
        "🌫 Estimated CO₂ Emissions",
        f"{carbon:.1f} kg"
    )

with col3:
    st.metric(
        "🌱 Sustainability Score",
        f"{score}/100"
    )

# ---------------- PROGRESS ---------------- #

st.write("## 🌍 Sustainability Progress")

st.progress(score / 100)

st.markdown("---")

# ---------------- AI RECOMMENDATIONS ---------------- #

st.write("## 🤖 AI Sustainability Recommendations")

if electricity > 3000:

    st.warning("⚠️ High energy consumption detected.")

    st.info("""
    💡 AI Suggestions:
    - Optimize air conditioning schedules
    - Install smart lighting systems
    - Increase renewable energy usage
    - Conduct energy efficiency audits
    """)

elif electricity > 1500:

    st.info("""
    🔋 Moderate energy usage detected.

    Recommendations:
    - Encourage energy-saving awareness programs
    - Optimize lab and computer usage schedules
    """)

else:

    st.success("✅ Excellent sustainability performance!")

if solar == "No":

    st.info(
        "☀️ Installing solar panels can significantly reduce operational costs and carbon emissions."
    )

# ---------------- ENERGY BREAKDOWN ---------------- #

st.write("## 📊 School Energy Breakdown")

energy_data = pd.DataFrame({
    "Category": [
        "Air Conditioning",
        "Lighting",
        "Computers",
        "Laboratories",
        "Others"
    ],
    "Usage": [40, 20, 20, 10, 10]
})

pie_fig = px.pie(
    energy_data,
    names="Category",
    values="Usage",
    title="School Energy Consumption Distribution",
    hole=0.4
)

pie_fig.update_layout(
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    font_color="white"
)

st.plotly_chart(pie_fig, use_container_width=True)

# ---------------- MONTHLY TREND ---------------- #

st.write("## 📈 Monthly Energy Trend")

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

usage_values = [900, 1000, 1100, 1200, 1250, electricity]

trend_df = pd.DataFrame({
    "Month": months,
    "Energy Usage": usage_values
})

line_fig = px.line(
    trend_df,
    x="Month",
    y="Energy Usage",
    markers=True,
    title="Monthly School Energy Usage"
)

line_fig.update_layout(
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
    font_color="white"
)

st.plotly_chart(line_fig, use_container_width=True)

# ---------------- AI PREDICTION ---------------- #

st.write("## 🤖 AI Future Energy Prediction")

x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

y = np.array([900, 1000, 1100, 1200, 1250, electricity])

model = LinearRegression()

model.fit(x, y)

future_month = np.array([[7]])

prediction = model.predict(future_month)

st.success(
    f"🔮 Predicted Next Month Energy Usage: {prediction[0]:.1f} kWh"
)

if prediction[0] > 2500:

    st.warning("⚠️ AI predicts increasing future energy demand.")

else:

    st.info("✅ AI predicts stable sustainable energy usage.")

# ---------------- SOLAR SAVINGS ---------------- #

st.write("## ☀️ Solar Energy Savings Estimator")

solar_savings = electricity * 0.35

co2_reduction = carbon * 0.4

col4, col5 = st.columns(2)

with col4:
    st.metric(
        "💰 Potential Energy Savings",
        f"{solar_savings:.1f} kWh"
    )

with col5:
    st.metric(
        "🌿 Potential CO₂ Reduction",
        f"{co2_reduction:.1f} kg"
    )


# ---------------- ECO BADGE ---------------- #

st.write("## 🥇 Eco Achievement Badge")

if score >= 85:

    st.success("🥇 Net-Zero Champion")

elif score >= 70:

    st.info("🥈 Green Campus Leader")

else:

    st.warning("🥉 Sustainability Starter")

# ---------------- GLOBAL IMPACT ---------------- #

st.write("## 🌎 Global School Impact Simulator")

schools = st.slider(
    "Number of Schools Using EcoGrid AI",
    1,
    5000,
    500
)

global_reduction = schools * 3.2

st.success(
    f"🌱 If {schools} schools adopt EcoGrid AI, estimated annual CO₂ reduction could reach {global_reduction:.0f} tons."
)

# ---------------- SDGs ---------------- #

st.write("## 🎯 Sustainable Development Goals Supported")

st.markdown("""
✅ SDG 4 → Quality Education  
✅ SDG 7 → Affordable & Clean Energy  
✅ SDG 11 → Sustainable Cities & Communities  
✅ SDG 12 → Responsible Consumption  
✅ SDG 13 → Climate Action  
""")

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.caption(
    "🌍 EcoGrid AI | Empowering Schools Towards a Sustainable & Net-Zero Future"
)
# ---------------- SUSTAINABILITY REPORT ---------------- #

st.write("## 📄 AI Sustainability Report")

report = f"""
====================================================
            ECOGRID AI SUSTAINABILITY REPORT
====================================================

🏫 School Name:
{school_name}

----------------------------------------------------

⚡ Monthly Electricity Usage:
{electricity} kWh

🌫 Estimated CO₂ Emissions:
{carbon:.1f} kg

🌱 Sustainability Score:
{score}/100

☀️ Solar Energy Installed:
{solar}

👨‍🎓 Number of Students:
{students}

🏢 Campus Size:
{building_size} sq ft

----------------------------------------------------

🤖 AI ENERGY PREDICTION

Predicted Next Month Usage:
{prediction[0]:.1f} kWh

----------------------------------------------------

💡 AI SUSTAINABILITY RECOMMENDATIONS

"""

# ---------------- AI RECOMMENDATIONS ---------------- #

if electricity > 3000:

    report += """
- Optimize air conditioning schedules
- Install smart lighting systems
- Increase renewable energy usage
- Conduct energy efficiency audits
"""

elif electricity > 1500:

    report += """
- Encourage energy-saving awareness programs
- Optimize computer lab schedules
- Improve energy monitoring systems
"""

else:

    report += """
- Excellent sustainability performance
- Maintain current energy optimization practices
"""

# ---------------- SDG IMPACT ---------------- #

report += """

----------------------------------------------------

🎯 SDGs SUPPORTED

✅ SDG 4  -> Quality Education
✅ SDG 7  -> Affordable & Clean Energy
✅ SDG 11 -> Sustainable Cities & Communities
✅ SDG 12 -> Responsible Consumption
✅ SDG 13 -> Climate Action

----------------------------------------------------

🌍 EcoGrid AI
Empowering Schools Towards a Sustainable Future

====================================================
"""

# ---------------- DOWNLOAD BUTTON ---------------- #

st.download_button(
    label="📥 Download Sustainability Report",
    data=report,
    file_name="EcoGridAI_Report.txt",
    mime="text/plain"
)

