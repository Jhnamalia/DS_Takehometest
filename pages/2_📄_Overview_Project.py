import streamlit as st

st.set_page_config(page_title="Project Overview", layout="wide")

st.title("📊 Project Overview")

# ===============================
# BUSINESS UNDERSTANDING
# ===============================
st.subheader("🏢 Business Understanding")
st.markdown(
    """
    <div style="background-color:#FDF6EC; padding:15px; border-radius:10px; box-shadow:1px 1px 8px rgba(0,0,0,0.1);">
    Dalam industri food delivery, ketepatan waktu pengiriman sangat berpengaruh terhadap:
    <ul>
        <li>✅ Kepuasan pelanggan</li>
        <li>✅ Daya saing bisnis</li>
        <li>✅ Repeat order yang lebih tinggi</li>
    </ul>
    Sebaliknya, keterlambatan bisa menurunkan customer loyalty dan berdampak pada pendapatan 🚴‍♂️💨
    </div>
    """,
    unsafe_allow_html=True
)

# ===============================
# BACKGROUND
# ===============================
st.subheader("📌 Latar Belakang")
st.markdown(
    """
    <div style="background-color:#E8F8F5; padding:15px; border-radius:10px; box-shadow:1px 1px 8px rgba(0,0,0,0.1);">
    Dengan meningkatnya jumlah pengguna aplikasi food delivery 📱, perusahaan menghadapi tantangan:
    <ul>
        <li>Menjamin makanan sampai tepat waktu walau ada faktor cuaca, jarak, lalu lintas, atau waktu pemesanan.</li>
        <li>Prediksi waktu pengiriman penting agar:
            <ul>
                <li>🛵 Operasional driver lebih optimal</li>
                <li>⏱ Estimasi waktu pengiriman lebih akurat</li>
                <li>📉 Risiko keluhan pelanggan berkurang</li>
            </ul>
        </li>
    </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# ===============================
# PROJECT GOALS
# ===============================
st.subheader("🎯 Tujuan Project")
st.markdown(
    """
    <div style="background-color:#FEF9E7; padding:15px; border-radius:10px; box-shadow:1px 1px 8px rgba(0,0,0,0.1);">
    <ol>
        <li>🔹 Membangun model prediksi untuk memperkirakan waktu pengiriman makanan.</li>
        <li>🔹 Mengidentifikasi faktor-faktor utama yang mempengaruhi lama pengiriman.</li>
        <li>🔹 Mendukung strategi bisnis untuk meningkatkan efisiensi operasional.</li>
        <li>🔹 Memberikan rekomendasi berbasis data untuk meningkatkan kepuasan pelanggan.</li>
    </ol>
    </div>
    """,
    unsafe_allow_html=True
)

# ===============================
# KEY BUSINESS QUESTIONS
# ===============================
st.subheader("❓ Key Business Questions")
st.markdown(
    """
    <div style="background-color:#FDEDEC; padding:15px; border-radius:10px; box-shadow:1px 1px 8px rgba(0,0,0,0.1);">
    <ul>
        <li>❓ Apa faktor utama yang memengaruhi lama pengiriman makanan?</li>
        <li>❓ Bagaimana cara meminimalisir keterlambatan pengiriman?</li>
        <li>❓ Apakah estimasi model prediksi bisa meningkatkan akurasi estimasi waktu pelanggan?</li>
        <li>❓ Bagaimana hasil analisis ini bisa membantu pengambilan keputusan strategis?</li>
    </ul>
    </div>
    """,
    unsafe_allow_html=True
)
