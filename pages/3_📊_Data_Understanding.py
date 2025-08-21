import streamlit as st
import pandas as pd
import plotly.express as px

# Judul halaman
st.title("📊 Data Understanding")

st.markdown("""
Dataset **Food Delivery Time Prediction** ini dirancang untuk memprediksi waktu pengiriman makanan berdasarkan berbagai faktor yang memengaruhi, seperti **jarak, cuaca, kondisi lalu lintas, waktu pemesanan, jenis kendaraan, hingga pengalaman kurir**.  

Dataset ini sangat relevan untuk **praktisi machine learning** yang tertarik pada bidang **logistik dan operations research**, karena mencakup aspek nyata dari proses pengiriman makanan. 🍔🚴‍♂️
""")

# Load dataset
df = pd.read_csv("data/Food_Delivery_Times_final.csv")

# 1. Ringkasan Dataset
st.subheader("📌 Ringkasan Dataset")
st.markdown(f"""
- Jumlah baris: **{df.shape[0]:,}**
- Jumlah kolom: **{df.shape[1]:,}**
""")

# 2. Struktur Kolom
st.subheader("📂 Struktur Kolom & Tipe Data")
st.dataframe(df.dtypes.reset_index().rename(columns={"index": "Nama Kolom", 0: "Tipe Data"}))

# 3. Kategori Fitur
st.subheader("📋 Kategori Fitur")
st.markdown("""
- **Informasi Order**: `order_id`  
- **Kondisi Pengiriman**: `distance_km`, `weather`, `traffic_level`, `time_of_day`  
- **Kendaraan & Kurir**: `vehicle_type`, `courier_experience_yrs`, `courier_experience_category`, `distance_per_experience`  
- **Restoran**: `preparation_time_min`  
- **Target (Y)**: `delivery_time_min` (lama waktu pengiriman dalam menit)  
""")

# 4. Contoh Data
st.subheader("🔍 Contoh Data")
st.dataframe(df.sample(5, random_state=42))

# 5. Visualisasi Distribusi Target Variable
st.subheader("📈 Distribusi Waktu Pengiriman (Target)")
fig = px.histogram(df, x="delivery_time_min", nbins=30, 
                   title="Distribusi Lama Waktu Pengiriman (menit)",
                   labels={"delivery_time_min": "Delivery Time (minutes)"})
st.plotly_chart(fig, use_container_width=True)

# 6. Informasi tambahan
st.info("Dataset ini berisi **1.000 baris** dan **11 kolom** yang mencakup informasi pesanan, kondisi pengiriman, kurir, serta variabel target yaitu **delivery_time_min**.")