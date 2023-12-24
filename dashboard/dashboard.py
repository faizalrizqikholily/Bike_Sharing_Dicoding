import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

# ==============================
# MUAT DATA
# ==============================
@st.cache(allow_output_mutation=True)
def muat_data():
    data = pd.read_csv("../data/hour.csv")
    return data

data = muat_data()

# ==============================
# JUDUL DASHBOARD
# ==============================
# Set judul halaman
st.title("Bike Share Dashboard")

# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("Informasi:")
st.sidebar.markdown("**• Nama: Faizal Rizqi Kholily**")
st.sidebar.markdown("**• Email: [faizalriziqkholily643@gmail.com](faizalriziqkholily643@gmail.com)**")
st.sidebar.markdown("**• Dicoding: [Faizal Rizqi Kholily](https://www.dicoding.com/users/faizalrizqikholily26/)**")

st.sidebar.title("Dataset Bike Share")
# Tampilkan dataset
if st.sidebar.checkbox("Tampilkan Dataset"):
    st.subheader("Data Mentah")
    st.write(data)

# Tampilkan statistik ringkasan
if st.sidebar.checkbox("Tampilkan Statistik Ringkasan"):
    st.subheader("Statistik Ringkasan")
    st.write(data.describe())

# Tampilkan sumber dataset
st.sidebar.markdown("[Unduh Dataset](https://link-ke-dataset-anda)")

st.sidebar.markdown('**Cuaca:**')
st.sidebar.markdown('1: Cerah, Sedikit awan, Sebagian berawan, Sebagian berawan')
st.sidebar.markdown('2: Kabut + Berawan, Kabut + Awan pecah, Kabut + Sedikit awan, Kabut')
st.sidebar.markdown('3: Salju Ringan, Hujan Ringan + Badai petir + Awan berkeping, Hujan Ringan + Awan berkeping')
st.sidebar.markdown('4: Hujan Lebat + Potongan Es + Badai petir + Kabut, Salju + Kabut')

# ==============================
# VISUALISASI
# ==============================
# buat layout dengan dua kolom
kolom1, kolom2 = st.columns(2)

with kolom1:
    # Jumlah pengguna sepeda berdasarkan musim
    st.subheader("Jumlah Pengguna Sepeda Berdasarkan Musim")

    # Pemetaan dari angka ke label musim
    pemetaan_musim = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
    data["label_musim"] = data["season"].map(pemetaan_musim)

    jumlah_musim = data.groupby("label_musim")["cnt"].sum().reset_index()
    grafik_musim = alt.Chart(jumlah_musim).mark_bar().encode(
        x='label_musim',
        y='cnt'
    )
    st.altair_chart(grafik_musim, use_container_width=True)

with kolom2:
    # Jumlah pengguna sepeda berdasarkan situasi cuaca
    st.subheader("Jumlah Pengguna Sepeda Berdasarkan Situasi Cuaca")

    jumlah_cuaca = data.groupby("weathersit")["cnt"].sum().reset_index()
    grafik_cuaca = alt.Chart(jumlah_cuaca).mark_bar().encode(
        x='weathersit',
        y='cnt'
    )
    st.altair_chart(grafik_cuaca, use_container_width=True)

# Jumlah pengguna sepeda per jam
st.subheader("Jumlah Pengguna Sepeda per Jam")
jumlah_per_jam = data.groupby("hr")["cnt"].sum().reset_index()
grafik_per_jam = alt.Chart(jumlah_per_jam).mark_line().encode(
    x='hr',
    y='cnt'
)
st.altair_chart(grafik_per_jam, use_container_width=True)

# Kelembaban vs. Jumlah Pengguna Sepeda
st.subheader("Kelembaban vs. Jumlah Pengguna Sepeda")
grafik_kelembaban = alt.Chart(data).mark_circle().encode(
    x='hum',
    y='cnt'
)
st.altair_chart(grafik_kelembaban, use_container_width=True)

# Kecepatan Angin vs. Jumlah Pengguna Sepeda
st.subheader("Kecepatan Angin vs. Jumlah Pengguna Sepeda")
grafik_kecepatan_angin = alt.Chart(data).mark_circle().encode(
    x='windspeed',
    y='cnt'
)
st.altair_chart(grafik_kecepatan_angin, use_container_width=True)

# Suhu vs. Jumlah Pengguna Sepeda
st.subheader("Suhu vs. Jumlah Pengguna Sepeda")
grafik_suhu = alt.Chart(data).mark_circle().encode(
    x='temp',
    y='cnt'
)
st.altair_chart(grafik_suhu, use_container_width=True)

# Tampilkan sumber data dan deskripsi
st.sidebar.title("Tentang")
st.sidebar.info("Dashboard ini menampilkan visualisasi untuk sekumpulan data Bike Share. "
                "Dataset ini mengandung informasi mengenai penyewaan sepeda berdasarkan berbagai variabel seperti musim, suhu, kelembaban, dan faktor lainnya.")

                        
# Load day.csv dataset
day_data = pd.read_csv('../data/day.csv')

# Load hour.csv dataset
hour_data = pd.read_csv('../data/hour.csv')

# 1. Hubungan antara Suhu dan Jumlah Pengguna Sepeda pada Hari-hari Tertentu
st.title('Hubungan antara Suhu dan Jumlah Pengguna Sepeda pada Hari-hari Tertentu')
scatter_fig = alt.Chart(day_data).mark_circle().encode(
    x='temp',
    y='cnt',
    tooltip=['temp', 'cnt']
).properties(
    width=600,
    height=400
)
st.altair_chart(scatter_fig, use_container_width=True)

# 2. Perbedaan Penggunaan Sepeda pada Hari Libur dan Bukan Hari Libur
st.title('Perbedaan Penggunaan Sepeda pada Hari Libur dan Bukan Hari Libur')
boxplot_fig = alt.Chart(hour_data.groupby('dteday')['cnt'].sum().reset_index()).mark_boxplot().encode(
    x='holiday:N',
    y='cnt:Q'
).properties(
    width=600,
    height=400
)
st.altair_chart(boxplot_fig, use_container_width=True)

# 3. Pola Penggunaan Sepeda pada Hari Kerja dan Bukan Hari Kerja
st.title('Pola Penggunaan Sepeda pada Hari Kerja dan Bukan Hari Kerja')
barplot_fig = alt.Chart(day_data).mark_bar().encode(
    x='workingday:N',
    y='mean(cnt):Q',
    color='workingday:N'
).properties(
    width=400,
    height=300
)
st.altair_chart(barplot_fig, use_container_width=True)

# 4. Distribusi Jumlah Pengguna Sepeda pada Jam Tertentu (Hari Kerja vs. Akhir Pekan)
st.title('Distribusi Jumlah Pengguna Sepeda pada Jam Tertentu (Hari Kerja vs. Akhir Pekan)')
boxplot_hr_fig = alt.Chart(hour_data).mark_boxplot().encode(
    x='hr:N',
    y='cnt:Q',
    color='workingday:N'
).properties(
    width=600,
    height=400
)
st.altair_chart(boxplot_hr_fig, use_container_width=True)

# 5. Tren Penggunaan Sepeda Berdasarkan Musim
st.title('Tren Penggunaan Sepeda Berdasarkan Musim')
barplot_season_fig = alt.Chart(day_data).mark_bar().encode(
    x='season:N',
    y='mean(cnt):Q',
    color='season:N'
).properties(
    width=400,
    height=300
)
st.altair_chart(barplot_season_fig, use_container_width=True)

# 5 (lanjutan). Perubahan Tren Penggunaan Sepeda dari Tahun 2011 ke 2012
st.title('Perubahan Tren Penggunaan Sepeda dari Tahun 2011 ke 2012')
lineplot_year_fig = alt.Chart(hour_data.groupby(['yr', 'mnth'])['cnt'].mean().reset_index()).mark_line().encode(
    x='mnth:N',
    y='mean(cnt):Q',
    color='yr:N'
).properties(
    width=600,
    height=400
)
st.altair_chart(lineplot_year_fig, use_container_width=True)
