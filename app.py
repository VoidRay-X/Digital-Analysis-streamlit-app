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
    background-color: #4CAF50;
    color: white;
    padding: 14px 30px;
    border-radius: 8px;
    font-size: 18px;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='cover-box'>
    <div class='big-title'>📊 Digital Analytics Dashboard</div>
    <p class='sub-title'>Welcome! Use the left sidebar to navigate between pages.</p>
    <br>
    <a href="/?page=Overview" target="_self" class="nav-button">Go to Overview</a>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

st.info("👉 Use the left sidebar to open Overview, Marketing, Website, and Product dashboards.")
