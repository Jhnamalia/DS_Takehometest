import streamlit as st

st.set_page_config(page_title="Food Delivery Project", layout="wide")

# ===============================
# HEADER
# ===============================
st.title("🍔 Food Delivery Time Prediction Project")

st.markdown("""
Selamat datang di aplikasi **Food Delivery Time Prediction**! 🚴  
Proyek ini dirancang untuk **menganalisis dan memprediksi waktu pengiriman makanan** 
berdasarkan berbagai faktor seperti jarak, cuaca, jenis kendaraan, dan kondisi lalu lintas.
""")

st.markdown("---")

# ===============================
# FLOW / PIPELINE
# ===============================
st.subheader("🔎 Alur Analisis")

dot = """
    digraph {
        rankdir=LR
        graph [size="12,6", fontsize=16, fontname="Arial"]
        node [shape=box, style="rounded,filled", color="#EAECEE", fontname="Arial", fontsize=9, fillcolor="#EAECEE"];
        edge [penwidth=2]

        A [label="👤 About Me"]
        B [label="📄 Overview Project"]
        C [label="📊 Data Understanding"]
        D [label="🧹 Data Preparation"]
        E [label="📈 EDA & Insight"]
        F [label="🤖 Prediction Model"]
        G [label="💡 Business Recommendation"]
        H [label="📱 Contact"]

        A -> B -> C -> D -> E -> F -> G -> H
    }
"""

st.graphviz_chart(dot, use_container_width=True)


st.markdown("---")

# ===============================
# MANFAAT
# ===============================
st.subheader("🚀 Manfaat Project")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background: linear-gradient(135deg,#A1FFCE,#FAFFD1);
                padding:20px; border-radius:15px; box-shadow:2px 2px 8px rgba(0,0,0,0.1);">
        <h3>🎯 Estimasi Akurat</h3>
        <p>Memperkirakan waktu pengiriman dengan lebih tepat.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg,#F6D365,#FDA085);
                padding:20px; border-radius:15px; box-shadow:2px 2px 8px rgba(0,0,0,0.1);">
        <h3>🚴 Efisiensi Operasional</h3>
        <p>Membantu kurir & restoran mengelola waktu lebih efektif.</p>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div style="background: linear-gradient(135deg,#C9FFBF,#FFAFBD);
                padding:20px; border-radius:15px; box-shadow:2px 2px 8px rgba(0,0,0,0.1);">
        <h3>😊 Kepuasan Pelanggan</h3>
        <p>Mengurangi keluhan & meningkatkan loyalitas customer.</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="background: linear-gradient(135deg,#84fab0,#8fd3f4);
                padding:20px; border-radius:15px; box-shadow:2px 2px 8px rgba(0,0,0,0.1);">
        <h3>📊 Insight Bisnis</h3>
        <p>Memberikan rekomendasi strategis berbasis data.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ===============================
# FOOTER
# ===============================
st.info("👉 Gunakan **sidebar** untuk mulai menjelajahi tiap bagian analisis.")
