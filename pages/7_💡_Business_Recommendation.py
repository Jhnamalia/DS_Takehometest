# pages/7_💡_Business_Recommendation.py
import streamlit as st

# ===============================
# CONFIG
# ===============================
st.set_page_config(page_title="💡 Business Recommendation", layout="wide")
st.title("💡 Business Recommendation")

st.markdown("""
Berdasarkan hasil **EDA** dan **Model Prediksi Waktu Pengiriman**, berikut adalah rekomendasi strategis
untuk meningkatkan **efisiensi operasional** dan **kepuasan pelanggan**. 🚀
""")

st.markdown("---")

# ===============================
# KPI CARDS (Visual)
# ===============================
st.subheader("📊 Key Performance Indicators (KPI)")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #A1FFCE, #FAFFD1);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <h3>⏱️ Avg Delivery Time</h3>
            <h1 style="color:#333;">32 min</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #F6D365, #FDA085);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <h3>✅ SLA ≤ 30 min</h3>
            <h1 style="color:#333;">72%</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div style="
            background: linear-gradient(135deg, #C9FFBF, #FFAFBD);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
            <h3>💙 Est. Customer Satisfaction</h3>
            <h1 style="color:#333;">89%</h1>
        </div>
        """,
        unsafe_allow_html=True
    )


# ===============================
# REKOMENDASI STRATEGIS
# ===============================
st.subheader("📌 Rekomendasi Utama")

with st.expander("🚴 Optimasi Operasional Driver"):
    st.write("- Gunakan model prediksi untuk mengatur alokasi kurir secara **dinamis** berdasarkan jarak, cuaca, dan traffic.")
    st.write("- Prioritaskan **motor** untuk area padat karena lebih efisien dibanding mobil.")

with st.expander("🍽️ Perencanaan Waktu Restoran"):
    st.write("- Berikan notifikasi kepada restoran dengan estimasi waktu pengiriman → agar **sinkronisasi preparation & pickup** lebih baik.")
    st.write("- Dorong restoran untuk menjaga waktu persiapan di bawah **30 menit**.")

with st.expander("💙 Customer Experience"):
    st.write("- Tampilkan estimasi waktu pengiriman **real-time** di aplikasi pelanggan.")
    st.write("- Gunakan kategori (Fast / Normal / Slow Delivery) agar pelanggan lebih mudah memahami estimasi.")

with st.expander("🎁 Strategi Insentif Kurir"):
    st.write("- Berikan **bonus/insentif** kepada kurir berpengalaman dengan performa cepat.")
    st.write("- Sediakan program pelatihan untuk kurir baru agar lebih efisien.")

with st.expander("🌦️ Manajemen Cuaca & Traffic"):
    st.write("- Siapkan sistem harga dinamis (*surge pricing*) saat hujan/traffic padat untuk menjaga ketersediaan kurir.")
    st.write("- Tambahkan buffer waktu estimasi agar pelanggan tetap puas meski ada delay karena faktor eksternal.")

# ===============================
# PENUTUP
# ===============================
st.success("""
🚀 Dengan menerapkan rekomendasi ini, perusahaan siap untuk:
- ✅ Meningkatkan akurasi estimasi pengiriman  
- ✅ Mengurangi keluhan pelanggan  
- ✅ Mengoptimalkan efisiensi operasional kurir  
- ✅ Menjaga kepuasan & loyalitas pelanggan dalam jangka panjang  
""")
