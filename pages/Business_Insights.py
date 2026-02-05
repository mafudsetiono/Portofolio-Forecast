import streamlit as st

st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Business Insights & Recommendations")

st.markdown("""
Halaman ini merangkum **temuan utama** dari analisis data dan hasil forecasting,
serta menerjemahkannya menjadi **insight bisnis yang dapat ditindaklanjuti**.
""")

st.divider()

# =========================
# Executive Summary
# =========================
st.header("📌 Executive Summary")
st.write("Forecast ini membantu bisnis memprediksi permintaan ke depan sehingga perencanaan stok dan strategi penjualan bisa dilakukan lebih awal. Dengan forecast mingguan dan bulanan, perusahaan bisa mengelola operasional jangka pendek sekaligus perencanaan strategis, serta mengurangi risiko overstock atau kehilangan peluang penjualan.")
st.markdown("""
- Penjualan menunjukkan **tren peningkatan yang konsisten** dari waktu ke waktu.
- Terdapat **pola musiman yang kuat**, terutama pada periode akhir tahun.
- Model **Prophet Time Series** memberikan performa terbaik dibandingkan baseline dan model machine learning lainnya.
""")

# =========================
# Key Insights
# =========================
st.header("🔍 Key Business Insights")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Sales Trend")
    st.markdown("""
    - Penjualan cenderung **meningkat setiap tahun**.
    - Fluktuasi bulanan masih terjadi, namun tidak mengubah arah tren jangka panjang.
    """)

with col2:
    st.subheader("🔁 Seasonality")
    st.markdown("""
    - Penjualan mencapai puncak pada **Q4 (Sep–Des)**.
    - Periode awal tahun relatif lebih rendah.
    """)

# =========================
# Forecast Interpretation
# =========================
st.header("🔮 Forecast Interpretation")

st.markdown("""
Berdasarkan hasil forecasting:
- Penjualan diproyeksikan **tetap tumbuh** dalam beberapa bulan ke depan.
- Rentang *confidence interval* menunjukkan adanya ketidakpastian, namun tren utama tetap positif.
- Model lebih konservatif pada lonjakan ekstrem, sehingga cocok untuk **perencanaan stok yang aman**.
""")

# =========================
# Business Recommendations
# =========================
st.header("🎯 Business Recommendations")

st.markdown("""
**1️⃣ Inventory Planning**
- Tingkatkan stok menjelang periode **Q4**.
- Kurangi risiko overstock di awal tahun dengan strategi *just-in-time*.

**2️⃣ Sales & Marketing Strategy**
- Fokuskan kampanye promosi pada bulan dengan performa tinggi.
- Gunakan forecast sebagai dasar penentuan target penjualan bulanan.

**3️⃣ Data-Driven Decision**
- Gunakan dashboard ini sebagai alat monitoring rutin.
- Perbarui model secara berkala untuk menjaga akurasi prediksi.
""")

# =========================
# Limitations & Next Steps
# =========================
st.header("⚠️ Limitations & Next Steps")

st.markdown("""
**Limitations**
- Forecast dibuat berdasarkan data historis tanpa mempertimbangkan faktor eksternal (promo besar, kondisi ekonomi, dll).
- Model menggunakan pendekatan univariate (hanya data penjualan).

**Next Steps**
- Menambahkan variabel eksternal (promo, diskon, hari libur).
- Mengembangkan forecast per kategori atau per region.
- Integrasi dengan sistem inventory untuk automasi keputusan stok.
""")

st.success("Insight ini diharapkan dapat membantu pengambilan keputusan bisnis yang lebih terarah dan berbasis data.")
