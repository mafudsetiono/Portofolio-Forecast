import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

st.set_page_config(
    page_title="Forecasting",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📈 Sales Forecasting")
st.caption("Prediksi penjualan berbasis Time Series untuk mendukung keputusan bisnis")
st.markdown("""
Halaman ini menampilkan **prediksi penjualan** menggunakan
model **Prophet Time Series** yang telah dilatih sebelumnya
pada level **bulanan** dan **mingguan**.
""")

# =========================
# NEW: Forecast Level
# =========================
level = st.radio(
    "Pilih Level Forecast:",
    ["Bulanan", "Mingguan"],
    horizontal=True
)

# =========================
# Load Model (Dynamic)
# =========================
@st.cache_resource
def load_model(level):
    base_dir = os.path.dirname(os.path.dirname(__file__))

    if level == "Bulanan":
        model_path = os.path.join(base_dir, "model", "prophet_sales_model.pkl")
        freq = "M"
        max_horizon = 12
        horizon_label = "bulan"
    else:
        model_path = os.path.join(base_dir, "model", "prophet_sales_weekly.pkl")
        freq = "W"
        max_horizon = 24
        horizon_label = "minggu"

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    return model, freq, max_horizon, horizon_label


model, freq, max_horizon, horizon_label = load_model(level)

# =========================
# Forecast Setting
# =========================
with st.container():
    st.subheader("🔧 Forecast Configuration")
    st.caption("Atur level dan horizon prediksi sesuai kebutuhan bisnis")

    level = st.radio(
        "Level Forecast",
        ["Bulanan", "Mingguan"],
        horizontal=True
    )

    horizon = st.slider(
        f"Forecast Horizon ({horizon_label} ke depan)",
        min_value=3,
        max_value=max_horizon,
        value=12 if level == "Bulanan" else 8,
        step=1
    )

# =========================
# Generate Forecast
# =========================
future = model.make_future_dataframe(periods=horizon, freq=freq)
forecast = model.predict(future)

# =========================
# Forecast Plot
# =========================
st.subheader("📊 Actual vs Forecast")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=forecast["ds"],
    y=forecast["yhat"],
    name="Forecast",
    line=dict(color="orange")
))

fig.add_trace(go.Scatter(
    x=forecast["ds"],
    y=forecast["yhat_upper"],
    line=dict(width=0),
    showlegend=False
))

fig.add_trace(go.Scatter(
    x=forecast["ds"],
    y=forecast["yhat_lower"],
    fill="tonexty",
    fillcolor="rgba(255,165,0,0.25)",
    line=dict(width=0),
    name="Confidence Interval"
))

fig.update_layout(
    xaxis_title="Tanggal",
    yaxis_title="Penjualan",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# Evaluation (MAE & RMSE)
# =========================

# ambil data actual dari model history
history = model.history[["ds", "y"]].copy()

# ambil forecast yang overlap dengan history
eval_df = forecast.merge(history, on="ds", how="inner")

# hitung metric
mae = mean_absolute_error(eval_df["y"], eval_df["yhat"])
rmse = np.sqrt(mean_squared_error(eval_df["y"], eval_df["yhat"]))

st.subheader("📏 Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label=f"MAE ({level})",
        value=f"{mae:,.0f}"
    )

with col2:
    st.metric(
        label=f"RMSE ({level})",
        value=f"{rmse:,.0f}"
    )

# =========================
# Forecast Table
# =========================
st.subheader("📄 Forecast Table")

forecast_table = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(horizon)
forecast_table.columns = ["Tanggal", "Prediksi", "Batas Bawah", "Batas Atas"]

st.dataframe(forecast_table, use_container_width=True)

st.download_button(
    label="⬇️ Download Forecast (CSV)",
    data=forecast_table.to_csv(index=False),
    file_name=f"sales_forecast_{level.lower()}.csv",
    mime="text/csv"
)


# =========================
# Business Insight
# =========================
st.subheader("🧠 Forecast Insight")

trend_direction = (
    "meningkat"
    if forecast_table["Prediksi"].iloc[-1] > forecast_table["Prediksi"].iloc[0]
    else "menurun"
)

st.info(f"""
📌 **Insight Otomatis ({level})**  
- Prediksi penjualan menunjukkan tren **{trend_direction}** dalam {horizon} {horizon_label} ke depan.  
- Forecast **mingguan** cocok untuk keputusan operasional jangka pendek.  
- Forecast **bulanan** lebih sesuai untuk perencanaan strategis dan target bisnis.  
- Confidence interval membantu manajemen mengantisipasi risiko permintaan.
""")

st.caption("Model: Prophet Time Series • Evaluasi: MAE & RMSE • Data: Superstore Sales")