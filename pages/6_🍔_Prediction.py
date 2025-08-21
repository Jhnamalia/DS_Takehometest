# pages/6_🍔_Prediction.py
import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# ===============================
# CONFIG
# ===============================
st.set_page_config(page_title="🍔 Modelling & Prediction", layout="wide")
st.markdown("<h1 style='text-align: center;'>🍔 Delivery Time Prediction</h1>", unsafe_allow_html=True)
st.markdown("---")

# ===============================
# LOAD MODEL
# ===============================
model = joblib.load("data/best_xgb_model.joblib")  # pipeline (preprocessor + XGBRegressor)

# ===============================
# FORM INPUT
# ===============================
st.subheader("🔮 Masukkan Data untuk Prediksi")

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        traffic_level = st.selectbox("🚦 Traffic Level", ["Low", "Medium", "High"])
        courier_experience_category = st.selectbox("👨‍✈️ Courier Experience Category", ["Beginner", "Intermediate", "Expert"])
        weather = st.selectbox("🌤️ Weather", ["Sunny", "Rainy", "Cloudy"])

    with col2:
        time_of_day = st.selectbox("⏰ Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
        vehicle_type = st.selectbox("🚗 Vehicle Type", ["Motorcycle", "Car", "Bicycle"])
        distance_km = st.number_input("📍 Distance (km)", min_value=0.1, max_value=50.0, value=7.5, step=0.1)

    with col3:
        preparation_time_min = st.number_input("🍳 Preparation Time (min)", min_value=1, max_value=120, value=15, step=1)
        courier_experience_yrs = st.number_input("📆 Courier Experience (yrs)", min_value=0, max_value=20, value=5, step=1)

# Derived feature
distance_per_experience = distance_km / (courier_experience_yrs + 1)

# ===============================
# PREDICTION
# ===============================
st.markdown("---")
if st.button("🚀 Predict Delivery Time", use_container_width=True):
    # Buat DataFrame input
    input_data = pd.DataFrame([{
        "traffic_level": traffic_level,
        "courier_experience_category": courier_experience_category,
        "weather": weather,
        "time_of_day": time_of_day,
        "vehicle_type": vehicle_type,
        "distance_km": distance_km,
        "preparation_time_min": preparation_time_min,
        "courier_experience_yrs": courier_experience_yrs,
        "distance_per_experience": distance_per_experience
    }])

    # Sesuaikan kolom dengan urutan training
    input_data = input_data[model.feature_names_in_]

    # Prediksi pakai model pipeline
    prediction = model.predict(input_data)[0]

    # ===============================
    # HASIL TAMPILAN KEREN
    # ===============================
    st.markdown(
        f"""
        <div style="
            padding: 20px;
            border-radius: 15px;
            background: linear-gradient(135deg, #FFDEE9, #B5FFFC);
            text-align: center;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
        ">
            <h2>📦 Estimated Delivery Time</h2>
            <h1 style="color:#FF5733;">{prediction:.2f} minutes</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ===============================
    # GAUGE CHART (tanpa delta)
    # ===============================
    fig = go.Figure(go.Indicator(
        mode="gauge+number",   # ⬅️ delta dihapus
        value=prediction,
        title={'text': "Delivery Speed"},
        gauge={
            'axis': {'range': [0, 60]},
            'bar': {'color': "black"},
            'steps': [
                {'range': [0, 20], 'color': "lightgreen"},
                {'range': [20, 40], 'color': "yellow"},
                {'range': [40, 60], 'color': "tomato"}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 4},
                'thickness': 0.75,
                'value': prediction
            }
        }
    ))

    fig.update_layout(width=500, height=300, margin=dict(l=30, r=30, t=50, b=20))
    st.plotly_chart(fig, use_container_width=True)

    # ===============================
    # CATEGORY TEXT
    # ===============================
    if prediction <= 20:
        st.success("🚀 Fast Delivery – Great performance!")
    elif prediction <= 40:
        st.warning("⚠️ Normal Delivery – Within expected range.")
    else:
        st.error("🐌 Slow Delivery – Might need optimization.")