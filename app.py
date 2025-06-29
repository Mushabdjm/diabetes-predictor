import streamlit as st
import numpy as np
import joblib
import time
import random

# Load model
model = joblib.load('model.pkl')

# --- SETUP STREAMLIT PAGE ---
st.set_page_config(page_title="Prediksi Diabetes", page_icon="🩺", layout="centered")

# --- CSS STYLE: Background, Glass Effect, Font Color ---
st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF; /* Latar belakang putih */
        color: #4E342E; /* Teks utama coklat gelap */
    }

    .block-container {
        backdrop-filter: blur(10px);
        background-color: rgba(165, 214, 167, 0.7); /* Aksen hijau daun */
        border-radius: 15px;
        padding: 2rem 2rem 1rem 2rem;
    }

    h1, h3, p, label, .stButton>button {
        color: #4E342E; /* Teks utama coklat gelap */
    }

    .stButton>button {
        background-color: #FFEB3B; /* Tombol kuning emas */
        color: #212121; /* Teks tombol hitam */
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }

    .stButton>button:hover {
        background-color: #FBC02D; /* Tombol kuning tua saat hover */
    }

    .result-card {
        background-color: rgba(255, 255, 255, 0.7); /* Kartu hasil putih transparan */
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ccc;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- LOGO / HEADER ---
st.image("logo.png", width=120)
st.title("🩺 Prediksi Diabetes")
st.markdown("Masukkan data pasien untuk memprediksi kemungkinan risiko diabetes.")

# --- FORM INPUT (2 COLUMNS) ---
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Jumlah Kehamilan", min_value=0, max_value=20, value=0)
    glucose = st.number_input("Glukosa", min_value=50, max_value=200, value=120)
    blood_pressure = st.number_input("Tekanan Darah", min_value=40, max_value=140, value=80)
    skin_thickness = st.number_input("Ketebalan Kulit", min_value=10, max_value=100, value=30)

with col2:
    insulin = st.number_input("Insulin", min_value=0, max_value=900, value=100)
    bmi = st.number_input("BMI", min_value=10.0, max_value=70.0, value=28.0)
    dpf = st.number_input("DPF", min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input("Umur", min_value=10, max_value=100, value=35)

# --- VALIDASI RINGAN ---
if glucose < 50:
    st.warning("⚠️ Nilai glukosa sangat rendah. Apakah benar?")
if bmi < 10:
    st.warning("⚠️ BMI sangat rendah, harap periksa kembali input.")

# --- TOMBOL PREDIKSI ---
if st.button("🔍 Prediksi"):
    with st.spinner("Memproses data..."):
        time.sleep(2)  # Simulasi loading
        data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                          insulin, bmi, dpf, age]])
        prediction = model.predict(data)
        result = '⚠️ Pasien berisiko Diabetes' if prediction[0] == 1 else '✅ Pasien tidak berisiko Diabetes'
        
        # Kalimat template berdasarkan hasil prediksi
        if prediction[0] == 1:
            messages = [
                "Kami sarankan untuk berkonsultasi dengan dokter untuk langkah selanjutnya.",
                "Perubahan gaya hidup mungkin diperlukan. Pertimbangkan untuk mengatur pola makan dan olahraga.",
                "Penting untuk memantau kesehatan Anda secara rutin.",
                "Jangan ragu untuk mencari dukungan dari ahli gizi atau profesional kesehatan.",
                "Menjaga pola makan yang sehat dan aktif dapat membantu mengelola risiko diabetes."
            ]
        else:
            messages = [
                "Tetap jaga pola hidup sehat!",
                "Lanjutkan dengan rutinitas sehat Anda.",
                "Anda berada di jalur yang baik, teruskan gaya hidup sehat ini.",
                "Tetap waspada dan lakukan pemeriksaan kesehatan secara berkala.",
                "Menjaga berat badan yang sehat dan berolahraga secara teratur sangat penting."
            ]

        # Pilih pesan acak
        advice_message = random.choice(messages)

        # KARTU HASIL PREDIKSI
        st.markdown(f"""
        <div class='result-card'>
            <h3>Hasil Prediksi:</h3>
            <p style='font-size:24px; font-weight:bold;'>{result}</p>
            <p style='font-size:16px; color:#555;'>{advice_message}</p>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<hr style="border: 0.5px solid #ccc" />
<div style='text-align: center; font-size: 13px; color: black;'>
    Dibuat dengan semangat oleh Mushab Dzul dan Zidan Nugraha
</div>
""", unsafe_allow_html=True)
