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
mode = st.selectbox('Pilih mode :', ['Penjumlahan', 'Pengurangan', 'Perkalian', 'Pembagian'])
st.write('Mode: ', mode)

c1 = st.number_input('Masukkan Angka 1', value=0)
c2 = st.number_input('Masukkan Angka 2', value=0)

if st.button('Hitung Hasil'):
    if operasi == 'Penjumlahan (+)':
        hasil = num1 + num2
        st.success(f'Hasil dari {num1} + {num2} = **{hasil}**')
        
    elif operasi == 'Pengurangan (-)':
        hasil = num1 - num2
        st.success(f'Hasil dari {num1} - {num2} = **{hasil}**')
        
    elif operasi == 'Perkalian (x)':
        hasil = num1 * num2
        st.success(f'Hasil dari {num1} x {num2} = **{hasil}**')
        
    elif operasi == 'Pembagian (/)':
        if num2 == 0:
            st.error('Error: Tidak bisa membagi angka dengan nol (0)!')
        else:
            hasil = num1 / num2
            st.success(f'Hasil dari {num1} / {num2} = **{hasil}**')
