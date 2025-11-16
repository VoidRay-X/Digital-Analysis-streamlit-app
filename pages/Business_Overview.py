import streamlit as st
from data_loader import load_data
import plotly.express as px

#st.title("📈 Business Overview")
st.markdown("<h1 style='text-align:center;'>📈 Business Overview</h1>", unsafe_allow_html=True)

# ----------------------------
# LOAD DATA
# ----------------------------
website_sessions, website_pageviews, products, orders, order_items, order_item_refunds = load_data()

total_session=len(website_sessions['website_session_id'])
total_order=len(orders['order_id'])
total_revenue=round(orders['price_usd'].sum()/1000000,2)

col1, col2, col3 = st.columns(3)
col1.metric("Total Sessions", total_session)
col2.metric('Total Orders',total_order)
col3.metric('Total Revenue', total_revenue,'M')
#col1, col2=st.columns(2)
#col1.metric('Total Revenue', total_revenue)
