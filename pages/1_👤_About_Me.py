import streamlit as st
from PIL import Image

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(page_title="About Me - Jihan Amalia", layout="wide")

# ===============================
# HEADER
# ===============================
st.title("👩‍💻 About Me")

# ===============================
# PROFILE SECTION
# ===============================
col1, col2 = st.columns([1, 2])

with col1:
    image = Image.open("images/jihan_amalia.jpg")
    st.image(image, caption="Jihan Amalia", use_container_width=True)

with col2:
    st.markdown(
        """
        ### Halo! 👋 Saya **Jihan Amalia**
        Saya seorang **Data Analyst** dengan minat besar di bidang **Data Science, Business Intelligence, dan Machine Learning**.  
        Passion saya adalah mengubah data menjadi **cerita & insight** yang bermakna untuk membantu bisnis mengambil keputusan strategis. 🚀
        """
    )

    st.success(
        """
        🔬 **About Project:**  
        **🍔 Food Delivery Time Prediction**  
        Mencakup *Business Understanding → Data Understanding → Data Preparation → EDA → Modelling → Business Recommendation*  
        Divisualisasikan melalui **Streamlit Dashboard** yang interaktif.
        """
    )

st.markdown("---")

# ===============================
# SKILLS
# ===============================
st.subheader("🛠️ Keahlian Utama")
st.markdown(
    """
    - 🧹 **Data Cleaning & Preprocessing**  
    - 📊 **Exploratory Data Analysis (EDA)**  
    - 📈 **Data Visualization** (Matplotlib, Plotly, Tableau, Power BI)  
    - 🤖 **Machine Learning** (Supervised & Unsupervised)  
    - 🖥️ **Dashboard Development** (Streamlit, Tableau, Power BI)  
    """
)

# ===============================
# EDUCATION
# ===============================
st.subheader("🎓 Pendidikan")
edu_col1, edu_col2 = st.columns(2)

with edu_col1:
    st.info("🎯 **Full-Stack Data Analyst & Data Science Bootcamp** – Dibimbing.id")
with edu_col2:
    st.info("🐟 **Budidaya Perairan** – Universitas Jenderal Soedirman")

# ===============================
# MOTTO
# ===============================
st.subheader("💡 Motto")
st.warning(
    "“Committed to use my technical and analytical skills to provide valuable insights and data-driven solutions, and adapt quickly to industry changes.”"
)

# ===============================
# RESOURCES
# ===============================
st.markdown("---")
st.subheader("🔗 Project Resources")
st.markdown(
    """
    - 📄 **Project Slide Deck** → [Food Delivery Time Prediction](https://drive.google.com/drive/folders/1ozbu6NxpJpzdxsO9cMOWpijmqrU5LgsB?usp=drive_link)  
    - 🍔 **Dataset Source** → [Food Delivery Time Prediction – Kaggle](https://www.kaggle.com/datasets/denkuznetz/food-delivery-time-prediction)  
    """
)
