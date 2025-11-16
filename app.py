import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

# ----------------------------
# HOME / COVER PAGE DESIGN
# ----------------------------
st.markdown("""
<style>
.cover-box {
    padding: 40px;
    background-color: #f8f9fa;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #e0e0e0;
}
.big-title {
    font-size: 48px;
    font-weight: 700;
    color: #333;
}
.sub-title {
    font-size: 20px;
    color: #555;
}
.nav-button {
    display: inline-block;
    background-color: #4CAF50;
    color: white !important;
    padding: 14px 30px;
    border-radius: 8px;
    font-size: 18px;
    margin: 10px;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='cover-box'>
    <div class='big-title'>📊 Digital Analytics Dashboard</div>
    <p class='sub-title'>Welcome! Choose a dashboard below:</p>
    <br>
</div>
""", unsafe_allow_html=True)

# -------- NAVIGATION BUTTONS --------
st.markdown("### 🔽 Navigate to Dashboards")

col1, col2 = st.columns(2)

with col1:
    st.page_link("Page/Business_Overview.py", label="📌 Business Overview", icon="📄")
    st.page_link("Page/Market_Analysis.py", label="📊 Market Analysis", icon="📈")

with col2:
    st.page_link("Page/Product_Analysis.py", label="🛒 Product Analysis", icon="🧪")
    st.page_link("Page/Website_Analysis.py", label="🌐 Website Analysis", icon="💻")

st.info("👉 You can also use the left sidebar to navigate between pages.")
