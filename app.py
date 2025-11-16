import streamlit as st
from data_loader import load_data

st.set_page_config(page_title="Home", layout="wide")

st.title("🏠 Welcome to the Digital Analytics Dashboard")
st.write("Use the left sidebar to navigate to different dashboards.")

# Load the data
website_sessions, website_pageviews, products, orders, order_items, order_item_refunds = load_data()

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Sessions", len(website_sessions))
col2.metric("Total Pageviews", len(website_pageviews))
col3.metric("Total Products", len(products))

st.write("---")

st.subheader("📊 Quick Snapshot")
st.write("Explore detailed dashboards using the menu on the left.")
