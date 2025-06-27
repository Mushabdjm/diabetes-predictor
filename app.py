import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load('model.pkl')

st.title("Prediksi Diabetes")
st.write("Masukkan data pasien:")

# Input
pregnancies = st.number_input("Jumlah Kehamilan", 0, 20)
glucose = st.number_input("Glukosa", 0, 200)
blood_pressure = st.number_input("Tekanan Darah", 0, 150)
skin_thickness = st.number_input("Ketebalan Kulit", 0, 100)
insulin = st.number_input("Insulin", 0, 900)
bmi = st.number_input("BMI", 0.0, 70.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
age = st.number_input("Umur", 1, 100)

if st.button("Prediksi"):
    data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                      insulin, bmi, dpf, age]])
    prediction = model.predict(data)
    result = 'Diabetes' if prediction[0] == 1 else 'Tidak Diabetes'
    st.success(f"Hasil Prediksi: {result}")
