import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('model.pkl')

# --- HEADER ---
st.set_page_config(page_title="Prediksi Diabetes", page_icon="🩺")
st.title("🩺 Prediksi Diabetes")
st.markdown("""
Aplikasi ini digunakan untuk memprediksi risiko diabetes berdasarkan data medis sederhana.  
Silakan masukkan informasi pasien pada form di bawah ini.
""")

# --- FORM INPUT DENGAN 2 KOLOM ---
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Jumlah Kehamilan", min_value=0, max_value=20, value=2)
    glucose = st.number_input("Glukosa", min_value=50, max_value=200, value=120)
    blood_pressure = st.number_input("Tekanan Darah", min_value=40, max_value=140, value=80)
    skin_thickness = st.number_input("Ketebalan Kulit", min_value=10, max_value=100, value=25)

with col2:
    insulin = st.number_input("Insulin", min_value=0, max_value=900, value=100)
    bmi = st.number_input("BMI", min_value=10.0, max_value=70.0, value=28.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input("Umur", min_value=10, max_value=100, value=35)

# --- VALIDASI NILAI EKSTREM ---
if glucose < 50:
    st.warning("⚠️ Nilai glukosa sangat rendah. Apakah benar?")
if bmi < 10:
    st.warning("⚠️ BMI sangat rendah, harap periksa kembali input.")

# --- PREDIKSI ---
if st.button("🔍 Prediksi"):
    data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                      insulin, bmi, dpf, age]])
    prediction = model.predict(data)
    result = '⚠️ Pasien berisiko Diabetes' if prediction[0] == 1 else '✅ Pasien tidak berisiko Diabetes'

    st.markdown(f"""
    <div style='background-color:#f0f0f5;padding:20px;border-radius:10px'>
        <h3 style='color:#0000'>Hasil Prediksi:</h3>
        <p style='font-size:20px'>{result}</p>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<hr style="border: 0.5px solid #ccc" />
<div style='text-align: center; font-size: 14px; color: gray;'>
    Dibuat dengan ❤️ oleh Mushab DJM • Powered by Streamlit
</div>
""", unsafe_allow_html=True)
