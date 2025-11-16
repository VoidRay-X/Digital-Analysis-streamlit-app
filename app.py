import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Home", layout="wide")

st.title("🏠 Home Page")



st.write("### Welcome to the Digital Analytics Dashboard")
st.write("Use the left sidebar to open the other dashboards.")

st.write("### Dataset Preview")
st.dataframe(df.head())





