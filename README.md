# 🚲 Bike Sharing Dashboard (Dicoding Data Analysis Project)

## 📌 Deskripsi Project

Project ini merupakan bagian dari submission **Belajar Analisis Data dengan Python** di :contentReference[oaicite:0]{index=0}.

Dashboard ini dibuat menggunakan **Streamlit** untuk melakukan eksplorasi dan visualisasi dataset **Bike Sharing**. Tujuannya adalah untuk memahami pola penggunaan sepeda berdasarkan berbagai faktor seperti waktu, cuaca, musim, dan kondisi lainnya.

## 🌐 Live Demo

🚀 Akses dashboard secara langsung di sini:  
👉 **[Live Demo Bike Sharing Dashboard](https://bikesharingdicoding-rrzevwzyzl9j59fbbt5deh.streamlit.app/)**

---

## 🎯 Tujuan Analisis

Project ini bertujuan untuk menjawab beberapa pertanyaan bisnis:

- Bagaimana pengaruh **musim** terhadap jumlah pengguna sepeda?
- Bagaimana kondisi **cuaca** memengaruhi jumlah penyewaan?
- Kapan waktu (jam) dengan penggunaan sepeda tertinggi?
- Apakah terdapat hubungan antara:
  - suhu dan jumlah pengguna?
  - kelembaban dan jumlah pengguna?
  - kecepatan angin dan jumlah pengguna?
- Bagaimana perbedaan penggunaan sepeda antara:
  - hari kerja vs non-hari kerja
  - hari libur vs hari biasa

---

## 📊 Dataset

Dataset yang digunakan adalah **Bike Sharing Dataset**, yang terdiri dari:

### 1. `day.csv`
Data agregasi harian:
- `temp` → suhu
- `cnt` → jumlah pengguna
- `season` → musim
- `workingday` → hari kerja / tidak

### 2. `hour.csv`
Data per jam:
- `hr` → jam
- `cnt` → jumlah pengguna
- `weathersit` → kondisi cuaca
- `hum` → kelembaban
- `windspeed` → kecepatan angin

---

## 🧰 Tools & Library

- Python
- :contentReference[oaicite:1]{index=1}
- Pandas
- Altair
- Matplotlib
- Seaborn

---

## ⚙️ Fitur Dashboard

### 📌 Sidebar
- Informasi pembuat
- Tampilkan dataset mentah
- Statistik ringkasan
- Deskripsi kondisi cuaca

---

### 📈 Visualisasi Utama

#### 1. Penggunaan Sepeda Berdasarkan Musim
Menampilkan total pengguna pada setiap musim (spring, summer, fall, winter).

#### 2. Penggunaan Sepeda Berdasarkan Cuaca
Menganalisis bagaimana kondisi cuaca memengaruhi jumlah pengguna.

#### 3. Jumlah Pengguna per Jam
Menunjukkan pola penggunaan harian (peak hours).

#### 4. Analisis Korelasi
Scatter plot:
- Suhu vs jumlah pengguna
- Kelembaban vs jumlah pengguna
- Kecepatan angin vs jumlah pengguna

---

### 📊 Analisis Lanjutan

#### 1. Suhu vs Pengguna (Harian)
Melihat hubungan langsung antara suhu dan jumlah penyewaan.

#### 2. Hari Libur vs Non-Libur
Membandingkan total penggunaan sepeda.

#### 3. Hari Kerja vs Non-Hari Kerja
Analisis rata-rata penggunaan sepeda.

#### 4. Distribusi per Jam
Perbandingan pola penggunaan:
- Hari kerja
- Akhir pekan

#### 5. Tren Musiman
Rata-rata penggunaan berdasarkan musim.

#### 6. Tren Tahunan (2011 vs 2012)
Melihat perubahan tren penggunaan sepeda dari waktu ke waktu.

---

## ▶️ Cara Menjalankan Project

### 1. Install Dependency

```bash
pip install streamlit pandas matplotlib seaborn altair
```

---

### 2. Jalankan Dashboard

```bash
streamlit run dashboard.py
```

---

## 📂 Struktur Project

```
.
├── dashboard.py
├── day.csv
├── hour.csv
└── README.md
```

---

## 📈 Insight Utama

- Penggunaan sepeda cenderung meningkat pada musim tertentu (misalnya summer & fall)
- Cuaca buruk menurunkan jumlah pengguna secara signifikan
- Terdapat jam sibuk (peak hours), biasanya pagi & sore
- Suhu memiliki korelasi positif terhadap jumlah pengguna
- Hari kerja menunjukkan pola berbeda dibanding akhir pekan

---

## 🚀 Use Case

Project ini dapat digunakan untuk:
- Data Analysis & Visualization
- Portfolio Data Analyst
- Business Insight untuk transportasi
- Pengambilan keputusan berbasis data

---

## ✨ Highlight

✔ Interactive dashboard  
✔ Insight berbasis data nyata  
✔ Menggunakan Streamlit (web-based)  
✔ Cocok untuk portfolio  

---

## 👤 Author

**Faizal Rizqi Kholily**  
📧 faizalrzqkh@gmail.com  
🔗 Dicoding: https://www.dicoding.com/users/faizalrizqikholily26/

---

## 📌 Catatan

Project ini dibuat sebagai bagian dari submission Dicoding dan bertujuan untuk meningkatkan pemahaman dalam analisis data serta visualisasi menggunakan Python.
