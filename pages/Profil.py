import streamlit as st

st.set_page_config(
    page_title="Profil",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# HEADER SECTION
# =========================
st.title("👤 Profil")

st.caption("Data Analyst | Time Series & Business Insight")

st.divider()

# =========================
# MAIN PROFILE SECTION
# =========================
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "assets/Foto Nonformal.png",
        width=220,
        caption="Mafud Satrio Setiono"
    )

with col2:
    st.subheader("Halo, saya Mafud 👋")

    st.markdown("""
Saya **Mafud Satrio Setiono**, seorang **Data Enthusiast** yang berfokus pada
**Data Engineering, Data Analysis, Data Scientist, dan Business Insight**.

Saya memiliki latar belakang **Teknik Informatika** dan pengalaman mengerjakan
berbagai proyek analisis data menggunakan **Python, SQL**, serta tools visualisasi
seperti **Tableau dan Power BI**.

Saya tertarik membangun solusi berbasis data yang **tidak hanya akurat secara teknis,
tetapi juga relevan untuk pengambilan keputusan bisnis**.
""")

# =========================
# SKILLS SECTION
# =========================
st.divider()
st.subheader("🛠️ Skills & Tools")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
**📊 Data & BI Tools**
- Tableau  
- Power BI  
- Excel  
- Git & GitHub
""")

with col2:
    st.markdown("""
**💻 Programming & Database**
- Python  
- PostgreSQL  
- MySQL
""")

with col3:
    st.markdown("""
**🤝 Soft Skills**
- Problem Solving  
- Critical Thinking  
- Communication  
- Teamwork  
- Time Management
- Adaptability
- Growth Mindset
""")

# =========================
# VALUE SECTION
# =========================
st.divider()
st.subheader("💡 What I Bring")

st.markdown("""
- Mampu menerjemahkan data menjadi **insight yang actionable**
- Terbiasa bekerja dengan **data historis & time series**
- Fokus pada **impact bisnis**, bukan hanya model
- Memiliki **rasa ingin tahu yang tinggi** dan selalu berusaha belajar hal baru
- Memiliki **etika kerja yang kuat** dan selalu berusaha memberikan yang terbaik
""")

# =========================
# CONTACT SECTION
# =========================
st.divider()
st.subheader("📬 Contact & Links")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
📧 **Email**  
riosetiono23@gmail.com
""")

with col2:
    st.markdown("""
🔗 **LinkedIn**  
[linkedin.com/in/mafud-satrio-setiono](https://www.linkedin.com/in/mafud-satrio-setiono-5950a7266/)
""")

st.caption("Terbuka untuk peluang Data Analyst / Data Scientist 🚀")
