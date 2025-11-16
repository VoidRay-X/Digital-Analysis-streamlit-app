import streamlit as st
from data_loader import load_data
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

#st.title("📈 Business Overview")
st.markdown("<h1 style='text-align:center;'>📈 Business Overview</h1>", unsafe_allow_html=True)

# ----------------------------
# LOAD DATA
# ----------------------------
website_sessions, website_pageviews, products, orders, order_items, order_item_refunds = load_data()

# slicers
# Convert to datetime
website_sessions['created_at'] = pd.to_datetime(website_sessions['created_at'])
orders['created_at'] = pd.to_datetime(orders['created_at'])
order_items['created_at'] = pd.to_datetime(order_items['created_at'])

# Extract year
website_sessions['year'] = website_sessions['created_at'].dt.year
orders['year'] = orders['created_at'].dt.year
order_items['year']=order_items['created_at'].dt.year

# Get all unique years from both tables
all_years = sorted(pd.concat([website_sessions['year'], orders['year'],order_items['year']]).unique())

# Sidebar multiselect
selected_years = st.sidebar.multiselect("Select Year(s)", all_years)

# Filter tables
if selected_years:  # If user selected at least one year
    sessions_filtered = website_sessions[website_sessions['year'].isin(selected_years)]
    orders_filtered = orders[orders['year'].isin(selected_years)]
    order_items_filtered = order_items[order_items['year'].isin(selected_years)]
else:  # If nothing is selected, show all data
    sessions_filtered = website_sessions
    orders_filtered = orders
    order_items_filtered = order_items

st.write(f"Showing data for: {', '.join(map(str, selected_years)) if selected_years else 'All years'}")


total_session=len(sessions_filtered['website_session_id'])
total_order=len(orders_filtered['order_id'])
total_revenue=round(orders_filtered['price_usd'].sum()/1000000,2)
total_unique_users = orders_filtered['user_id'].nunique()
repeat_customer_ids = orders_filtered['user_id'].value_counts()
repeat_customers = (repeat_customer_ids > 1).sum()
repeat_customers_rate = round((repeat_customers / total_unique_users) * 100,2)
total_quatity=len(order_items_filtered['order_item_id'])
total_cost=round(orders_filtered['cogs_usd'].sum()/1000000,2)
total_profit_margin= round(100*(total_revenue-tota_cost)/total_revenue,2)


col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sessions", total_session)
col2.metric('Total Orders',total_order)
col3.metric('Total Revenue', total_revenue,'M')
col4.metric('Total Customers',total_unique_users)

col1,col2,col3,col4=st.columns(4)
col1.metric('Repeat customers', repeat_customers)
col2.metric('Repeat customer rate(%)', repeat_customers_rate)
col3.metric('Total Order Line',total_quatity)
col4.metric('Total Profit Margin(%)', total_profit_margin)

col1, col2, col3 = st.columns(3)

with col1:
    sess = sessions_filtered.groupby('utm_source')['website_session_id'].count().reset_index()

    total= sess['website_session_id'].sum()
    sess['percentage'] = (sess['website_session_id'] / total) * 100
    
    # --- Pie Chart ---
    #plt.figure(figsize=(7, 7))
    fig, ax = plt.subplots(figsize=(7, 7))
    
    # Create pie chart
    plt.pie(
        sess['percentage'], 
        labels=sess['utm_source'],
        autopct='%1.1f%%',        # show one decimal place
        startangle=90,       # rotate so the first slice starts at the top
        colors=plt.cm.Set2.colors, # use same Set2 palette
        wedgeprops={'edgecolor': 'white'} # cleaner edges
    )
    
    # Add title
    #plt.title('Percentage of Source-wise Traffic volume', fontsize=14)
    #plt.tight_layout()
    
    # Show chart
    #plt.show()
    ax.set_title('Percentage of Source-wise Traffic Volume', fontsize=20)
    plt.tight_layout()
    
    # --- Show in Streamlit ---
    st.pyplot(fig)
