# 📊 Advanced Churn Prediction & Strategy

<p align="center">
  <img src="https://github.com/user-attachments/assets/41296e12-3c61-431b-9e18-4d2b3b3f3558" width="80%">
</p>

Sebuah aplikasi web interaktif berbasis **Streamlit + Plotly** untuk menganalisis dan memprediksi _customer churn_ pada perusahaan telekomunikasi fiktif.  
Proyek ini tidak hanya membangun model machine learning, tapi juga menghasilkan **insight bisnis dan rekomendasi strategi retensi** yang bisa ditindaklanjuti.

---

### 🔗 Live Demo

**[Coba Aplikasi Churn Prediction di Sini!](https://telecom-churn-prediction-btdyjjaiuzjb7uhe6ot3ed.streamlit.app/)**

---

### 📝 Latar Belakang Proyek

Dalam industri telekomunikasi, kehilangan pelanggan (_churn_) adalah tantangan besar yang langsung berdampak pada pendapatan.

Proyek ini bertujuan menjawab pertanyaan fundamental:

**Siapa pelanggan yang paling berisiko churn, faktor apa yang mendorong churn, dan strategi apa yang paling efektif untuk meningkatkan retensi?**

Proyek ini mencakup pipeline lengkap dari **EDA → Modeling → Interpretasi → Deployment.**

---

### ✨ Fitur Utama Aplikasi

- **👤 Prediksi Individual:** Masukkan data 1 pelanggan → prediksi risiko churn secara real-time.
- **📂 Prediksi Batch:** Upload file CSV → prediksi churn massal dengan probabilitas.
- **📊 Dashboard EDA:** Visualisasi churn berdasarkan kontrak, tenure, dll.
- **🎯 Confidence Badge:** Probabilitas churn ditampilkan jelas → meningkatkan transparansi & trust.

---

### 💡 Insight Kunci

1. **Kontrak bulanan** → risiko churn paling tinggi.
2. **Masa kritis pelanggan baru (0–12 bulan)** → periode paling rawan churn.
3. **High Value Customer** → perlu strategi retensi khusus (loyalty, referral, family plan).
4. **Recall Model 87%** → lebih baik mendeteksi hampir semua churn, walau ada false positive.
5. **Model valid** (ROC-AUC > 0.91) & konsisten dengan EDA → bisa dipercaya sebagai dasar strategi bisnis.

---

### 🛠️ Teknologi yang Digunakan

- **Bahasa:** Python
- **Analisis Data:** Pandas, Scikit-learn
- **Modeling:** Logistic Regression (Balanced Class Weight)
- **Visualisasi:** Plotly Express, Matplotlib, Seaborn
- **Interpretasi Model:** SHAP (SHapley Additive exPlanations)
- **Deployment:** Streamlit

---
