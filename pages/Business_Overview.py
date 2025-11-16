import streamlit as st
from data_loader import load_data
import plotly.express as px

st.title("📈 Business Overview")

# ----------------------------
# LOAD DATA
# ----------------------------
website_sessions, website_pageviews, products, orders, order_items, order_item_refunds = load_data()

total_session=len(website_sessions['website_session_id'])

col1, = st.columns(1)
col1.metric("Total Sessions", total_session)
