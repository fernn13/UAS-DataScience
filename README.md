# 📘 Deteksi Serangan BHP Flooding pada OBS Network Menggunakan Deep Learning

## 👤 Informasi
- **Nama**: Istya Yulia Amesti
- **Program Studi**: Teknologi Informasi
- **Institusi**: Politeknik Negeri Madiun
- **Repository**: [Isi link GitHub jika ada]
- **Video**: [Isi link jika ada]

---

## 1. 🎯 Ringkasan Proyek
Proyek ini bertujuan untuk mendeteksi serangan **Burst Header Packet (BHP) Flooding**
pada jaringan **Optical Burst Switching (OBS)** menggunakan pendekatan Machine Learning
dan Deep Learning.

Tahapan utama:
- Data preparation dan preprocessing
- Membangun 3 model (Baseline, Advanced ML, Deep Learning)
- Evaluasi performa model
- Menentukan model terbaik

---

## 2. 📄 Problem & Goals

### Problem Statements
- Bagaimana mendeteksi serangan BHP Flooding pada jaringan OBS?
- Model apa yang memberikan performa terbaik?

### Goals
- Melakukan preprocessing dataset OBS
- Membangun dan membandingkan beberapa model klasifikasi
- Menentukan model dengan performa terbaik

---

## 3. 📁 Struktur Folder

```
project/
│
├── data/ # Dataset (tidak di-commit)
├── notebooks/
│ └── ML_Project.ipynb
├── src/
│ └── preprocess.py
├── models/
│ └── model_cnn.h5
├── images/
│ └── confusion_matrix_cnn.png
├── requirements.txt
├── .gitignore
└── README.md

```

---

## 4. 📊 Dataset
- **Sumber**: UCI Machine Learning Repository
- **Nama Dataset**: BHP Flooding Attack on OBS Network
- **Format**: ARFF
- **Tipe Data**: Multiclass Classification

---

## 5. 🔧 Data Preparation
- Konversi data ARFF ke DataFrame
- Encoding fitur kategorikal
- Normalisasi fitur (StandardScaler)
- Pembagian data train dan test

---

## 6. 🤖 Modeling
- **Baseline Model**: Model sederhana sebagai pembanding
- **Advanced ML Model**: Random Forest
- **Deep Learning Model**: CNN 1D menggunakan TensorFlow/Keras

---

## 7. 🧪 Evaluation
Metrik evaluasi yang digunakan:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 8. 🏁 Kesimpulan
Model CNN memberikan performa terbaik dalam mendeteksi serangan BHP Flooding
berdasarkan metrik evaluasi yang digunakan.

---

## 9. 🔮 Future Work
- Penambahan data
- Hyperparameter tuning
- Eksperimen arsitektur deep learning lain
- Deployment sistem

---

## 10. 🔁 Reproducibility
Install dependency:
pip install -r requirements.txt
Jalankan notebook:
notebooks/ML_Project.ipynb

