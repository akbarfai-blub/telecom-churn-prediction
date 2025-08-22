import streamlit as st
import pandas as pd
import joblib

# Fungsi untuk memuat model
@st.cache_resource
def load_model(path):
    return joblib.load(path)

# Muat model pipeline
# Pastikan path ini benar sesuai struktur folder Anda
try:
    model_pipeline = load_model('model/churn_model_pipeline.pkl')
except FileNotFoundError:
    st.error("File model 'churn_model_pipeline.pkl' tidak ditemukan. Pastikan file berada di dalam folder 'model/'.")
    st.stop()


st.title("Prediksi Churn untuk Pelanggan Individual 👤")
st.write("Masukkan data pelanggan di bawah ini untuk melihat prediksi churn-nya.")
st.markdown("---")

# Membuat form input
with st.form(key='prediction_form'):
    st.subheader("Informasi Pelanggan:")
    
    # Input utama berdasarkan feature importance
    col1, col2 = st.columns(2)
    with col1:
        contract = st.selectbox('Tipe Kontrak', ('Month-to-month', 'One year', 'Two year'))
        tenure = st.slider('Lama Berlangganan (Bulan)', 0, 72, 12)
        number_of_dependents = st.slider('Jumlah Tanggungan', 0, 10, 0)
        
    with col2:
        internet_service = st.selectbox('Tipe Layanan Internet', ('DSL', 'Fiber optic', 'No'))
        monthly_charges = st.slider('Tagihan Bulanan ($)', 18.0, 120.0, 70.0)
        number_of_referrals = st.slider('Jumlah Rujukan', 0, 15, 0)
        
    payment_method = st.selectbox('Metode Pembayaran', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))

    submit_button = st.form_submit_button(label='Prediksi')

# Logika setelah tombol ditekan
if submit_button:
    # Membuat DataFrame dari input
    
    # Buat dictionary dari input pengguna
    user_data = {
        'contract': contract,
        'tenure': tenure,
        'internet_service': internet_service,
        'monthly_charges': monthly_charges,
        'payment_method': payment_method,
        'number_of_dependents': number_of_dependents,
        'number_of_referrals': number_of_referrals
    }
    
    # Buat dictionary berisi nilai default untuk semua kolom lain yang dibutuhkan pipeline
    # Nilai-nilai ini bisa berupa nilai yang paling umum (modus) dari analisis EDA.
    default_features = {
        'gender': 'Female', 'age': 40, 'senior_citizen': 'No', 'partner': 'No',
        'dependents': 'No', 'phone_service': 'Yes', 'online_security': 'No',
        'online_backup': 'No', 'device_protection': 'No', 'premium_tech_support': 'No',
        'streaming_tv': 'No', 'streaming_movies': 'No', 'streaming_music': 'No',
        'internet_type': 'Fiber Optic', 'paperless_billing': 'Yes',
        'avg_monthly_long_distance_charges': 0.0, 'total_charges': 0.0, # Akan di-handle oleh imputer jika kosong
        'total_refunds': 0.0, 'total_extra_data_charges': 0,
        'total_long_distance_charges': 0.0, 'total_revenue': 0.0,
        'multiple_lines': 'No', 'avg_monthly_gb_download': 0, 'unlimited_data': 'Yes',
        'offer': 'No Offer', 'referred_a_friend': 'No', 'num_additional_services': 0
    }
    
    # Gabungkan input pengguna dengan nilai default
    final_data = {**default_features, **user_data}
    input_df = pd.DataFrame(final_data, index=[0])
    
    # Lakukan prediksi
    prediction = model_pipeline.predict(input_df)
    prediction_proba = model_pipeline.predict_proba(input_df)

    prob_churn = prediction_proba[0][1] * 100
    prob_stay = prediction_proba[0][0] * 100

    st.subheader("Hasil Prediksi:")

    # Badge visual (Confidence Level)
    confidence = max(prob_churn, prob_stay)
    if confidence >= 80:
        badge_color = "🟢 Sangat Yakin"
    elif confidence >= 60:
        badge_color = "🟡 Cukup Yakin"
    else:
        badge_color = "🔴 Rendah"

    if prediction[0] == 1:
        st.error(f"Pelanggan ini **BERISIKO TINGGI** untuk Churn.")
    else:
        st.success(f"Pelanggan ini **cenderung akan Tetap Tinggal** (Stay).")

    st.markdown(f"**Confidence Level:** {badge_color} ({confidence:.2f}%)")

    st.write(f"**Probabilitas Churn:** {prob_churn:.2f}%")
    st.write(f"**Probabilitas Stay:** {prob_stay:.2f}%")