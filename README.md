# 🩺 Prediksi Diabetes dengan Machine Learning dan Streamlit

Aplikasi web interaktif untuk memprediksi kemungkinan seseorang menderita diabetes berdasarkan data medis sederhana. Dibuat menggunakan **Python**, **Scikit-Learn**, dan **Streamlit**.

## 🚀 Demo Aplikasi
🌐 Coba aplikasinya secara langsung: [Klik di sini](https://your-username-diabetes-predictor.streamlit.app/)  
*(Link akan aktif setelah deploy ke Streamlit Cloud)*

---

## 📊 Dataset
Menggunakan dataset **Pima Indians Diabetes Database** dari [Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database), dengan fitur:
- Jumlah kehamilan
- Glukosa
- Tekanan darah
- Ketebalan kulit
- Insulin
- BMI
- Diabetes Pedigree Function
- Umur

---

## ⚙️ Cara Menjalankan Aplikasi Lokal

1. Clone repo:
```bash
git clone https://github.com/your-username/diabetes-predictor.git
cd diabetes-predictor
pip install -r requirements.txt
python train_model.py
streamlit run app.py

---

🧠 Model ML yang Digunakan
Algoritma: Random Forest Classifier

Framework: Scikit-Learn

Model disimpan dalam file model.pkl

📦 Deployment
Aplikasi ini dideploy menggunakan Streamlit Cloud, cukup dengan meng-upload:

app.py

model.pkl

requirements.txt

diabetes.csv

🧑‍💻 Kontributor
👤 Mushab DJM
