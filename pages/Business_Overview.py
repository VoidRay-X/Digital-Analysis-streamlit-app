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



sess = website_sessions.groupby('utm_source')['website_session_id'].count().reset_index()

total= sess['website_session_id'].sum()
sess['percentage'] = (sess['website_session_id'] / total) * 100

# --- Pie Chart ---
plt.figure(figsize=(7, 7))

# Create pie chart
plt.pie(
    sess['percentage'], 
    labels=sess['utm_source'],
    autopct='%1.1f%%',        # show one decimal place
    startangle=90,            # rotate so the first slice starts at the top
    colors=plt.cm.Set2.colors, # use same Set2 palette
    wedgeprops={'edgecolor': 'white'} # cleaner edges
)

# Add title
plt.title('Percentage of Source-wise Traffic volume', fontsize=14)
plt.tight_layout()

# Show chart
plt.show()
