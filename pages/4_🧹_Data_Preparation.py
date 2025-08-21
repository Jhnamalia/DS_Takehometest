# pages/4_🧹_Data_Preparation.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Preparation", layout="wide")
st.title("🧹 Data Preparation")

# Load dataset
df_raw = pd.read_csv("data/Food_Delivery_Times.csv")   # dataset ori
df_clean = pd.read_csv("data/Food_Delivery_Times_final.csv") # dataset clean

# ---- Step 1: Missing Value ----
with st.expander("1️⃣ Missing Value"):
    st.write("📍 Pada dataset **original**, terdapat missing value di beberapa kolom:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Original Dataset**")
        st.dataframe(df_raw.isnull().sum())
    with col2:
        st.markdown("**Clean Dataset**")
        st.dataframe(df_clean.isnull().sum())

    st.success("👉 Setelah dilakukan cleaning, **tidak ada lagi missing value** ✅")

# ---- Step 2: Duplicate ----
with st.expander("2️⃣ Duplicate Data"):
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Jumlah baris sebelum dibersihkan", df_raw.shape[0])
    with col2:
        st.metric("Jumlah baris setelah dibersihkan", df_clean.shape[0])

    st.info("👉 Tidak ditemukan duplikat data.")

# ---- Step 3: Outlier ----
with st.expander("3️⃣ Outlier Analysis"):
    st.markdown("""
    📍 Analisis outlier dilakukan pada kolom **`delivery_time_min`**.  
    - **Sebelum dibersihkan:** terdapat **6 outlier**.  
    - **Setelah dibersihkan:** tidak ada lagi outlier.
    """)

    # Buat 2 plot side by side
    fig, axes = plt.subplots(1, 2, figsize=(12,5))

    # Boxplot sebelum cleaning
    sns.boxplot(y=df_raw['Delivery_Time_min'], color="salmon", ax=axes[0])
    axes[0].set_title("Before Cleaning (Raw Dataset)", fontsize=12, weight="bold")
    axes[0].set_ylabel("Delivery Time (min)")
    axes[0].grid(axis="y", linestyle="--", alpha=0.6)

    # Boxplot sesudah cleaning
    sns.boxplot(y=df_clean['delivery_time_min'], color="skyblue", ax=axes[1])
    axes[1].set_title("After Cleaning (Clean Dataset)", fontsize=12, weight="bold")
    axes[1].set_ylabel("")
    axes[1].grid(axis="y", linestyle="--", alpha=0.6)

    st.pyplot(fig)

# ---- Step 4: Feature Engineering ----
with st.expander("4️⃣ Feature Engineering"):
    st.markdown("""
    Pada tahap ini ditambahkan **dua kolom baru** hasil rekayasa fitur:
    - ✨ **`courier_experience_category`** → kategori pengalaman kurir (Baru, Menengah, Berpengalaman).
    - 📏 **`distance_per_experience`** → rasio jarak tempuh terhadap pengalaman kurir (km per tahun).
    """)

    st.dataframe(
        df_clean[['courier_experience_yrs', 'courier_experience_category', 
                  'distance_km', 'distance_per_experience']].head()
    )

    st.success("👉 Fitur tambahan ini akan membantu dalam analisis dan pemodelan selanjutnya 🚀")