import streamlit as st
from data_loader import load_data
import plotly.express as px

st.title("📈 Business Overview")

# ----------------------------
# LOAD DATA
# ----------------------------
website_sessions, website_pageviews, products, orders, order_items, order_item_refunds = load_data()

total_session=len(website_sessions['website_session_id'])
total_order=len(orders['order_id'])

col1, col2 = st.columns(2)
col1.metric("Total Sessions", total_session)
col2.metric('Total Orders',total_order)
