import streamlit as st
import pandas as pd
import joblib

# Fungsi untuk memuat model
@st.cache_resource
def load_model(path):
    return joblib.load(path)

# Muat model pipeline
model_pipeline = load_model('model/churn_model_pipeline.pkl')

st.title("Prediksi Churn Massal (Batch Prediction) 📂")
st.write("Unggah file CSV berisi data pelanggan untuk mendapatkan prediksi churn untuk setiap baris.")
st.markdown("---")

uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

if uploaded_file is not None:
    # Baca file yang diunggah
    input_df_batch = pd.read_csv(uploaded_file)
    st.write("**Data yang Diunggah:**")
    st.dataframe(input_df_batch)

    # Lakukan prediksi
    predictions = model_pipeline.predict(input_df_batch)
    prediction_probas = model_pipeline.predict_proba(input_df_batch)[:, 1]

    # Tambahkan hasil prediksi ke DataFrame
    results_df = input_df_batch.copy()
    results_df['Prediksi Churn'] = ['Churn' if pred == 1 else 'Stay' for pred in predictions]
    results_df['Probabilitas Churn (%)'] = [f"{proba*100:.2f}" for proba in prediction_probas]
    
    st.write("**Hasil Prediksi:**")
    st.dataframe(results_df)

    # Opsi untuk mengunduh hasil
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(results_df)
    st.download_button(
        label="Unduh Hasil sebagai CSV",
        data=csv,
        file_name='hasil_prediksi_churn.csv',
        mime='text/csv',
    )