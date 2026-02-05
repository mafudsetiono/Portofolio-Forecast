import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Performance Dashboard")

# ========= Load Data =========
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, "data", "sample_superstore.csv")
    df = pd.read_csv(data_path, encoding="latin1")
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    return df

df = load_data()

# ========= Sidebar Filter =========
st.sidebar.header("🔎 Filter Data")

date_range = st.sidebar.date_input(
    "Rentang Tanggal Order",
    value=(df["Order Date"].min(), df["Order Date"].max())
)

region_filter = st.sidebar.multiselect(
    "Pilih Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

start_date, end_date = date_range
df_filtered = df[
    (df["Order Date"] >= pd.to_datetime(start_date)) &
    (df["Order Date"] <= pd.to_datetime(end_date)) &
    (df["Region"].isin(region_filter))
]

# ========= KPI =========
col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"${df_filtered['Sales'].sum():,.0f}")
col2.metric("📈 Total Profit", f"${df_filtered['Profit'].sum():,.0f}")
col3.metric("🧾 Total Orders", df_filtered["Order ID"].nunique())
col4.metric("📦 Quantity Sold", df_filtered["Quantity"].sum())

st.divider()

# ========= Monthly Trend =========
monthly_sales = (
    df_filtered
    .set_index("Order Date")
    .resample("M")["Sales"]
    .sum()
    .reset_index()
)

fig_trend = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Monthly Sales Trend"
)

st.plotly_chart(fig_trend, use_container_width=True)

# ========= Tabs =========
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["By Category", "By Region", "By Segment", "By Sub-Category", "By Product Profit", "By Product Sales"])

with tab1:
    cat_sales = df_filtered.groupby("Category")["Sales"].sum().reset_index()
    fig_cat = px.bar(cat_sales, x="Category", y="Sales")
    st.plotly_chart(fig_cat, use_container_width=True)

with tab2:
    reg_sales = df_filtered.groupby("Region")["Sales"].sum().reset_index()
    fig_reg = px.bar(reg_sales, x="Region", y="Sales")
    st.plotly_chart(fig_reg, use_container_width=True)

with tab3:
    seg_sales = df_filtered.groupby("Segment")["Sales"].sum().reset_index()
    fig_seg = px.bar(seg_sales, x="Segment", y="Sales")
    st.plotly_chart(fig_seg, use_container_width=True)

with tab4:
    subcat_sales = df_filtered.groupby("Sub-Category")["Sales"].sum().reset_index()
    fig_subcat = px.bar(subcat_sales, x="Sub-Category", y="Sales")
    st.plotly_chart(fig_subcat, use_container_width=True)

with tab5:
    prod_profit = df_filtered.groupby("Product Name")["Profit"].sum().reset_index().sort_values(by="Profit", ascending=False).head(10)
    fig_prod = px.bar(prod_profit, x="Product Name", y="Profit", title="Top 10 Products by Profit")
    st.plotly_chart(fig_prod, use_container_width=True)

with tab6:
    prod_sales = df_filtered.groupby("Product Name")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False).head(10)
    fig_prod_sales = px.bar(prod_sales, x="Product Name", y="Sales", title="Top 10 Products by Sales")
    st.plotly_chart(fig_prod_sales, use_container_width=True)

# ========= Data Preview =========
with st.expander("📄 Lihat Data"):
    st.dataframe(df_filtered.head(50))
