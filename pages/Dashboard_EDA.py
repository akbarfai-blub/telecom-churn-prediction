import streamlit as st
import pandas as pd
import plotly.express as px

# Fungsi untuk memuat data
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

# Muat data yang sudah bersih
df_cleaned = load_data('data/clean_churn_data.csv')

st.title("Dashboard Eksplorasi Data (EDA) 📊")
st.write("Beberapa visualisasi kunci dari analisis data eksplorasi yang mendasari pembuatan model.")
st.markdown("---")

# Key Metrics
st.subheader("📌 Key Metrics")
churn_rate = df_cleaned['churn_value'].mean() * 100
st.metric(label="Churn Rate", value=f"{churn_rate:.2f}%")
st.metric(label="Total Customers", value=len(df_cleaned))


# Proporsi Pelanggan Churn vs Stay
st.subheader("Proporsi Pelanggan Churn vs Stay")
churn_counts = df_cleaned['churn_value'].value_counts(normalize=True).mul(100)
fig_pie = px.pie(
    names=churn_counts.index.map({0: "Stay", 1: "Churn"}),
    values=churn_counts.values,
    hole=0.4,
    color=churn_counts.index.map({0: "Stay", 1: "Churn"}),
    color_discrete_map={"Stay": "green", "Churn": "red"}
)
fig_pie.update_traces(textinfo="percent+label")
st.plotly_chart(fig_pie)

# Churn Rate Berdasarkan Tipe Kontrak
st.subheader("Churn Rate Berdasarkan Tipe Kontrak")
churn_by_contract = df_cleaned.groupby('contract')['churn_value'].value_counts(normalize=True).unstack().mul(100)
fig1 = px.bar(churn_by_contract, y=1, title="Churn Rate Berdasarkan Tipe Kontrak", text_auto='.2f')
fig1.update_yaxes(title="Churn Rate (%)")
st.plotly_chart(fig1)

# Churn Rate Berdasarkan Lama Berlangganan
st.subheader("Churn Rate Berdasarkan Lama Berlangganan")
df_cleaned['tenure_group'] = pd.cut(df_cleaned['tenure'], bins=[0, 12, 48, 72], labels=['0-12 Bulan', '13-48 Bulan', '49-72 Bulan'], right=False)
churn_by_tenure = df_cleaned.groupby('tenure_group')['churn_value'].value_counts(normalize=True).unstack().mul(100)
fig2 = px.bar(churn_by_tenure, y=1, title="Churn Rate Berdasarkan Lama Berlangganan", text_auto='.2f')
fig2.update_yaxes(title="Churn Rate (%)")
st.plotly_chart(fig2)

# Churn Rate Berdasarkan Metode Pembayaran
st.subheader("Churn Rate Berdasarkan Metode Pembayaran")
churn_by_payment = df_cleaned.groupby('payment_method')['churn_value'].mean().mul(100).sort_values()
fig3 = px.bar(
    churn_by_payment, 
    x=churn_by_payment.index, 
    y=churn_by_payment.values,
    text=churn_by_payment.values.round(2),
    title="Churn Rate per Payment Method"
)
fig3.update_yaxes(title="Churn Rate (%)")
fig3.update_xaxes(title="Payment Method")
st.plotly_chart(fig3)

# Distribusi Tagihan Bulanan (Monthly Charges)
st.subheader("Distribusi Tagihan Bulanan (Monthly Charges)")
fig4 = px.box(
    df_cleaned, 
    x="churn_value", 
    y="monthly_charges",
    color="churn_value",
    labels={"churn_value": "Churn (1) vs Stay (0)"},
    title="Monthly Charges Distribution by Churn"
)
st.plotly_chart(fig4)

st.subheader("Filter Berdasarkan Tipe Kontrak")
selected_contract = st.selectbox("Pilih Kontrak", df_cleaned['contract'].unique())
filtered_data = df_cleaned[df_cleaned['contract'] == selected_contract]
fig5 = px.histogram(
    filtered_data, 
    x="tenure", 
    color="churn_value", 
    barmode="overlay",
    title=f"Distribusi Tenure untuk Kontrak {selected_contract}"
)
st.plotly_chart(fig5)
