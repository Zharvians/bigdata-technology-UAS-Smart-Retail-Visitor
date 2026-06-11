### Smart Retail Visitor Prediction System

## Final Test – Big Data Technology

Sistem Big Data untuk memonitor jumlah pengunjung pusat perbelanjaan dan memprediksi lonjakan pengunjung menggunakan PySpark, Parquet, Machine Learning, dan Streamlit Dashboard.

---

##  👨‍🏫 Dosen Pembimbing
[![GitHub - Muhayat Lab](https://img.shields.io/badge/GitHub-Muhayat--Lab-181717?logo=github&style=for-the-badge)](https://github.com/muhayat-lab)

##  👨‍💻 Developer
[![GitHub - Zharvian](https://img.shields.io/badge/GitHub-Zharvians-007ACC?logo=github&style=for-the-badge)](https://github.com/Zharvians)

**Nama:** Muhammad Ade Ramadhani  
**NPM:** 230104040213  
**Kelas:** TI23A  

---

## 🧠 Deskripsi Proyek

Smart Retail Visitor Prediction System merupakan implementasi pipeline Big Data yang digunakan untuk:

- Menghasilkan data pengunjung secara otomatis
- Mengolah data menggunakan PySpark
- Menyimpan data dalam format Parquet
- Memprediksi jumlah pengunjung menggunakan Machine Learning
- Menampilkan visualisasi interaktif menggunakan Streamlit

Studi kasus yang digunakan adalah pusat perbelanjaan yang memiliki beberapa zona pengunjung.

Zona yang dimonitor:
- FoodCourt
- FashionArea
- Cinema

---

## ✨ Fitur Utama

- 📊 Generate Visitor Data
- ⚡ Spark Data Processing
- 📦 Parquet Storage
- 🤖 Linear Regression Prediction
- 📈 Plotly Visualization
-  🎛 Interactive Streamlit Dashboard
- 🕒 Peak Hour Analysis
- 🌊 Modern Ocean Theme Dashboard
---

## 🛠 Teknologi yang Digunakan
```bash
- Python
- PySpark
- Pandas
- Parquet
- Streamlit
- Plotly
- Scikit-Learn
- Joblib
- Linear Regression

```

---

## 🔄 Big Data Pipeline

```bash
Visitor Tracking

↓

Spark Aggregation

↓

Parquet Storage

↓

Machine Learning

↓

Streamlit Dashboard
```

---

## 📂 Struktur Folder

```bash

uas-tbg-230104040213
│
├── data
│   └── visitor_data.csv
│
├── dashboard
│   └── app.py
│
├── models
│   └── visitor_prediction.pkl
│
├── output
│   ├── visitor_detail
│   ├── visitor_total
│   ├── visitor_time
│   └── ml_visitor
│
├── scripts
│   ├── generate_data.py
│   ├── spark_processing.py
│   └── train_model.py
│
└── README.md

```
---

## 📊 Dataset
```bash

| Field         | Tipe     |
| ------------- | -------- |
| timestamp     | datetime |
| zone          | string   |
| visitor_count | integer  |

Zona:

- FoodCourt
- FashionArea
- Cinema

Jumlah data:

- 180 menit
- 540 record
- Visitor random 10–500

```
---

## ⚡ Spark Transformation

```bash
Transformasi yang dilakukan:

1. Total Pengunjung Tiap Zona

Menghitung total visitor pada setiap zona.

2. Tren Pengunjung Tiap 15 Menit

Mengelompokkan visitor berdasarkan interval waktu.

3. Dataset Machine Learning

Membuat dataset prediksi berdasarkan jam kunjungan.
```
---

## 📦 Output Parquet
Folder output:

```bash

output/
│
├── visitor_detail
├── visitor_total
├── visitor_time
└── ml_visitor

```
---

## 📜 Lisensi
```bash
Proyek ini dibuat untuk keperluan akademik
Final Test – Technology Big Data

Dilarang menggunakan untuk kepentingan komersial.
© 2025 — 230104040213. Seluruh hak dilindungi.

```
---





