import streamlit as st
from datetime import datetime, timedelta 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import mean_absolute_error, mean_squared_error
import os

st.set_page_config(
    page_title="Sales Forecasting Portfolio",
    page_icon="📈",
    layout="wide"
)

# ===== Sidebar Branding =====
st.sidebar.markdown("## 📊 Sales Forecasting App")
st.sidebar.markdown(
    """
    **Portfolio Data Analyst**  
    Time Series Forecasting  
    """
)

st.sidebar.divider()

st.sidebar.info(
    "Gunakan menu di atas untuk berpindah halaman:\n\n"
    "- Profil\n"
    "- Sales Dashboard\n"
    "- Forecasting\n"
    "- Business Insights"
)

# ===== Main Content =====
st.title("📈 Sales Forecasting Dashboard")

st.markdown("""
### Project Overview
Aplikasi ini menampilkan analisis penjualan retail dan prediksi penjualan bulanan menggunakan pendekatan **time series forecasting**.

### Objectives
- Memahami pola penjualan historis
- Menyediakan forecast penjualan
- Mendukung pengambilan keputusan bisnis
""")

