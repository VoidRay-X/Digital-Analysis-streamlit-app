import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Home", layout="wide")

st.title("🏠 Home Page")

# ------------------------------
# LOAD DATA FROM GOOGLE DRIVE
# ------------------------------
url_sessions = "https://drive.google.com/uc?export=download&id=1ycYab0CgibgaGxopEiZFOCE13mGTm77x"
url_pageviews = "https://drive.google.com/uc?export=download&id=1Ruc6Q622uJoeDR_pVhKI5hU2rlgTlicy"
url_products = "https://drive.google.com/uc?export=download&id=1F13iyzdpDmy6j_w_eYaFRmVDfyy3jV0R"
url_orders = "https://drive.google.com/uc?export=download&id=1csibm0W8Ewphbu3OEaayqbiLQka9qlrm"
url_order_items = "https://drive.google.com/uc?export=download&id=163b-CGyWRafz-1ZRT0XNepi70MyRzg7O"
url_order_items_refunds = "https://drive.google.com/uc?export=download&id=1di14Gd4eNh5norDomih8G7Gw57Kz358L"

website_sessions = pd.read_csv(url_sessions)
website_pageviews = pd.read_csv(url_pageviews)
products = pd.read_csv(url_products)
orders = pd.read_csv(url_orders)
order_items = pd.read_csv(url_order_items)
order_item_refunds = pd.read_csv(url_order_items_refunds)

st.write("### Welcome to the Digital Analytics Dashboard")
st.write("Use the left sidebar to open the other dashboards.")

st.write("### Dataset Preview")
st.dataframe(df.head())





