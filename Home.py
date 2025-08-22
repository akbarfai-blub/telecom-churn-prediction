import streamlit as st

st.set_page_config(
    page_title="Home: Prediksi Churn",
    layout="wide"
)

st.title("Advanced Churn Prediction & Strategy 🚀")
st.markdown("---")
st.subheader("Selamat Datang di Project Analisis dan Prediksi Customer Churn")

st.markdown("""
Aplikasi ini adalah implementasi dari proyek Data Science untuk memprediksi *customer churn* di sebuah perusahaan telekomunikasi fiktif. 
Proyek ini mencakup analisis data eksplorasi (EDA), pengembangan model *machine learning*, dan interpretasi model untuk menghasilkan rekomendasi bisnis yang dapat ditindaklanjuti.

**Gunakan menu di sidebar untuk menavigasi ke halaman lain:**
- **Dashboard EDA:** Lihat beberapa visualisasi kunci dari analisis data eksplorasi.
- **Prediksi Batch:** Unggah file CSV berisi data beberapa pelanggan untuk mendapatkan prediksi massal.
- **Prediksi Individual:** Masukkan data satu pelanggan untuk melihat prediksi churn-nya secara *real-time*.
""")