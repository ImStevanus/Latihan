import streamlit as st

# 1. Konfigurasi Halaman (Opsional, agar tampilan di browser lebih bagus)
st.set_page_config(
    page_title="Kalkulator Sederhana",
    page_icon="🧮",
    layout="centered"
)

# 2. Judul Aplikasi
st.title("🧮 Kalkulator Sederhana")
st.write("Aplikasi kalkulator mini untuk operasi matematika dasar.")
st.markdown("---")

# 3. Input Angka (Dibuat berdampingan menggunakan kolom)
mode = st.selectbox('Select a subject:', ['Penjumlahan', 'Pengurangan', 'Perkalian', 'Pembagian'])
st.write('Mode: ', mode)

c1 = st.text_input('Masukkan Angka')
