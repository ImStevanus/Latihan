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
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Masukkan angka pertama:", value=0.0, step=1.0)

with col2:
    num2 = st.number_input("Masukkan angka kedua:", value=0.0, step=1.0)

# 4. Pilihan Operasi Matematika
operasi = st.selectbox(
    "Pilih Operasi Matematika:", 
    ["Penjumlahan (+)", "Pengurangan (-)", "Perkalian (×)", "Pembagian (÷)"]
)

st.markdown("---")

# 5. Tombol dan Logika Proses Perhitungan
if st.button("Hitung Hasil", type="primary"):
    hasil = 0.0
    gagal = False
    
    if operasi == "Penjumlahan (+)":
        hasil = num1 + num2
    elif operasi == "Pengurangan (-)":
        hasil = num1 - num2
    elif operasi == "Perkalian (×)":
        hasil = num1 * num2
    elif operasi == "Pembagian (÷)":
        if num2 != 0:
            hasil = num1 / num2
        else:
            gagal = True
            st.error("❌ Error: Tidak bisa membagi angka dengan nol (0)!")
            
    # Menampilkan hasil jika tidak ada error (seperti pembagian dengan nol)
    if not gagal:
        st.success("Perhitungan berhasil!")
        st.metric(label=f"Hasil dari {operasi}", value=f"{hasil}")
