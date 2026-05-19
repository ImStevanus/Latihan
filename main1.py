%%writefile app.py
import streamlit as st

# Mengatur judul halaman aplikasi
st.title("🧮 Kalkulator Sederhana")
st.write("Aplikasi kalkulator mini buatanmu sendiri.")

# Membuat dua kolom untuk input angka agar tampilan lebih rapi
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Masukkan angka pertama:", value=0.0)

with col2:
    num2 = st.number_input("Masukkan angka kedua:", value=0.0)

# Membuat dropdown untuk memilih operasi matematika
operasi = st.selectbox("Pilih Operasi Matematika:", ["Penjumlahan (+)", "Pengurangan (-)", "Perkalian (×)", "Pembagian (÷)"])

# Tombol untuk menghitung
if st.button("Hitung Hasil"):
    hasil = 0
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
            st.error("Error: Tidak bisa membagi angka dengan nol (0)!")
            
    # Menampilkan hasil jika tidak ada error pembagian nol
    if not gagal:
        st.success(#f"Hasil dari {operasi} adalah:")
        st.metric(label="Hasil Akhir", value=f"{hasil}")
