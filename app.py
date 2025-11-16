import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Home",
    layout="wide",
)

# ----------------------------
# CSS for Home Page
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
.nav-buttons {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
    margin-top: 20px;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    padding: 14px 30px;
    border-radius: 8px;
    font-size: 18px;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Home / Cover Page
# ----------------------------
st.markdown("""
<div class='cover-box'>
    <div class='big-title'>📊 Digital Analytics Dashboard</div>
    <p class='sub-title'>Welcome! Use the buttons below or the sidebar to navigate between pages.</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# Navigation Buttons
# ----------------------------
# ----------------------------
# Navigation Buttons
# ----------------------------
st.markdown("<div class='nav-buttons'>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------
# Additional Info
# ----------------------------
st.info("👉 Use the left sidebar to open Overview, Marketing, Website, and Product dashboards.")
