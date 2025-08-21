# pages/5_📊_EDA.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ===============================
# CONFIG
# ===============================
st.set_page_config(page_title="Exploratory Data Analysis", layout="wide")
st.title("📊 Exploratory Data Analysis (EDA)")

# Load cleaned dataset
df = pd.read_csv("data/Food_Delivery_Times_final.csv")

# Palettes
cat_palette = sns.color_palette("Set2")      # kategori
num_palette = sns.color_palette("viridis")   # numerik

# ===============================
# TABS
# ===============================
tab1, tab2, tab3 = st.tabs(["📌 Univariate Analysis", "🔗 Bivariate Analysis", "🌐 Multivariate Analysis"])

# ===============================
# TAB 1 - UNIVARIATE
# ===============================
with tab1:
    st.subheader("📌 Univariate Analysis")

    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots(figsize=(6,4))
        sns.countplot(x='weather', data=df, palette=cat_palette, ax=ax)
        ax.set_title('Distribusi Data of Weather')
        for container in ax.containers:
            ax.bar_label(container, fmt='%d')
        st.pyplot(fig)
        st.caption("👉 Cuaca cerah mendominasi pesanan, cuaca ekstrem jarang terjadi.")

    with col2:
        fig, ax = plt.subplots(figsize=(6,4))
        sns.countplot(x='traffic_level', data=df, palette=cat_palette, ax=ax)
        ax.set_title('Distribusi Traffic Condition')
        for container in ax.containers:
            ax.bar_label(container, fmt='%d')
        st.pyplot(fig)
        st.caption("👉 Sebagian besar pengiriman dilakukan saat lalu lintas normal hingga padat.")

    col3, col4 = st.columns(2)
    with col3:
        fig, ax = plt.subplots(figsize=(6,4))
        sns.countplot(x='time_of_day', data=df, palette=cat_palette, ax=ax)
        ax.set_title('Distribution of Deliveries by Time of Day')
        for container in ax.containers:
            ax.bar_label(container, fmt='%d')
        st.pyplot(fig)
        st.caption("👉 Pengiriman lebih banyak terjadi pada jam makan siang dan sore hari.")

    with col4:
        fig, ax = plt.subplots(figsize=(6,4))
        sns.countplot(x='vehicle_type', data=df, palette=cat_palette, ax=ax)
        ax.set_title('Distribution of Deliveries by Vehicle Type')
        for container in ax.containers:
            ax.bar_label(container, fmt='%d')
        st.pyplot(fig)
        st.caption("👉 Motor merupakan kendaraan dominan untuk pengiriman.")

    # Numeric distributions
    st.subheader("Distribusi Fitur Numerik")
    col5, col6 = st.columns(2)
    with col5:
        fig, ax = plt.subplots(figsize=(6,4))
        sns.histplot(df['distance_km'], bins=20, kde=True, color=num_palette[-2], ax=ax)
        ax.set_title('Distribution of Delivery Distance')
        st.pyplot(fig)
        st.caption("👉 Sebagian besar pengiriman berada di bawah 10 km.")

    with col6:
        fig, ax = plt.subplots(figsize=(6,4))
        sns.histplot(df['preparation_time_min'], bins=20, kde=True, color=num_palette[-3], ax=ax)
        ax.set_title('Distribution of Preparation Time')
        st.pyplot(fig)
        st.caption("👉 Waktu persiapan makanan umumnya di bawah 40 menit.")

    col7, col8 = st.columns(2)
    with col7:
        fig, ax = plt.subplots(figsize=(6,4))
        sns.histplot(df['courier_experience_yrs'], bins=20, kde=True, color=num_palette[-4], ax=ax)
        ax.set_title('Distribution of Courier Experience')
        st.pyplot(fig)
        st.caption("👉 Mayoritas kurir memiliki pengalaman di bawah 10 tahun.")

    with col8:
        fig, ax = plt.subplots(figsize=(6,4))
        sns.histplot(df['delivery_time_min'], bins=20, kde=True, color=num_palette[-1], ax=ax)
        ax.set_title('Distribution of Delivery Time')
        st.pyplot(fig)
        st.caption("👉 Waktu pengiriman terbanyak berada di rentang 20–60 menit.")

# ===============================
# TAB 2 - BIVARIATE
# ===============================
with tab2:
    st.subheader("🔗 Bivariate Analysis")

    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots(figsize=(8,6))
        sns.boxplot(x='weather', y='delivery_time_min', hue='traffic_level', data=df, palette=cat_palette, ax=ax)
        ax.set_title("Delivery Time by Weather and Traffic Level")
        st.pyplot(fig)
        st.caption("👉 Waktu pengiriman cenderung meningkat pada cuaca buruk & lalu lintas padat.")

    with col2:
        grouped = df.groupby(['vehicle_type', 'time_of_day'])['delivery_time_min'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(8,6))
        sns.barplot(x='vehicle_type', y='delivery_time_min', hue='time_of_day', data=grouped, palette=cat_palette, ax=ax)
        ax.set_title("Average Delivery Time by Vehicle Type and Time of Day")
        for container in ax.containers:
            ax.bar_label(container, fmt='%.1f')
        st.pyplot(fig)
        st.caption("👉 Mobil relatif lebih lama dibanding motor, terutama di jam sibuk.")

# ===============================
# TAB 3 - MULTIVARIATE
# ===============================
with tab3:
    st.subheader("🌐 Multivariate Analysis")

    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots(figsize=(8,6))
        corr_matrix = df.corr(numeric_only=True)
        sns.heatmap(corr_matrix, annot=True, cmap='viridis', fmt=".2f", ax=ax)
        ax.set_title("Correlation Heatmap (Numerical Features)")
        st.pyplot(fig)
        st.caption("👉 Jarak memiliki korelasi moderat dengan waktu pengiriman.")

    with col2:
        fig = sns.pairplot(df[['distance_km','preparation_time_min','courier_experience_yrs','delivery_time_min']],
                           diag_kind='kde', palette=num_palette)
        fig.fig.suptitle("Pairplot of Numerical Features", y=1.02)
        st.pyplot(fig)
        st.caption("👉 Terlihat hubungan linier antara jarak dan waktu pengiriman.")

    # Scatter advanced
    st.subheader("Scatter Plot with Multiple Dimensions")
    fig, ax = plt.subplots(figsize=(8,6))
    sns.scatterplot(x='distance_km', y='delivery_time_min', hue='traffic_level', 
                    size='courier_experience_yrs', data=df, palette=cat_palette, alpha=0.7, ax=ax)
    ax.set_title("Delivery Time vs Distance (colored by Traffic Level, sized by Experience)")
    st.pyplot(fig)
    st.caption("👉 Semakin jauh jarak, waktu pengiriman meningkat; lalu lintas padat makin memperlama pengiriman.")
