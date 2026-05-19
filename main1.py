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

num1 = st.number_input('Masukkan Angka 1', value=0)
num2 = st.number_input('Masukkan Angka 2', value=0)
tambah_angka = st.checkbox('Tambah angka ke-3 (Opsional)')

if tambah_angka:
    num3 = st.number_input('Masukkan Angka 3', value=0.0)
else:
    num3 = None

if st.button('Hitung Hasil'):
    if mode == 'Penjumlahan':
        hasil = num1 + num2
        st.success(f'Hasil dari {num1} + {num2} = **{hasil}**')
        
    elif mode == 'Pengurangan':
        hasil = num1 - num2
        st.success(f'Hasil dari {num1} - {num2} = **{hasil}**')
        
    elif mode == 'Perkalian':
        hasil = num1 * num2
        st.success(f'Hasil dari {num1} x {num2} = **{hasil}**')
        
    elif mode == 'Pembagian':
        if num2 == 0:
            st.error('Error: Tidak bisa membagi angka dengan nol (0)!')
        else:
            hasil = num1 / num2
            st.success(f'Hasil dari {num1} / {num2} = **{hasil}**')
