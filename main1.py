import streamlit as st

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="Kalkulator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Kalkulator Bjir")
st.write("Kamu bisa menambah atau menghapus input angka!")
st.markdown("---")

# 2. Inisialisasi Session State (Memori Aplikasi)
# Kita mulai dengan minimal 2 input angka default
if 'jumlah_angka' not in st.session_state:
    st.session_state.jumlah_angka = 2

# 3. Pilihan Operasi Matematika
mode = st.selectbox('Pilih mode operasi:', ['(+) Penjumlahan', '(-) Pengurangan', '(x) Perkalian', '(/) Pembagian'])
st.write('Mode saat ini: ', mode)

st.markdown("### 🔢 Masukkan Angka")

# 4. Loop untuk Membuat Input Angka Secara Dinamis
daftar_angka = []
for i in range(st.session_state.jumlah_angka):
    # Membuat input field dinamis: Angka 1, Angka 2, Angka 3, dst.
    angka = st.number_input(f'Masukkan Angka {i+1}', value=0.0, key=f'angka_{i}')
    daftar_angka.append(angka)

# 5. Tombol untuk Menambah / Mengurangi Jumlah Input (Loop Controller)
kolom1, kolom2 = st.columns(2)

with kolom1:
    if st.button("➕ Tambah Angka"):
        st.session_state.jumlah_angka += 1
        st.rerun()  # Memaksa streamlit menggambar ulang layar dengan input baru

with kolom2:
    # Batasi agar input tidak bisa kurang dari 2 angka
    if st.session_state.jumlah_angka > 2:
        if st.button("❌ Kurangi Angka"):
            st.session_state.jumlah_angka -= 1
            st.rerun()

st.markdown("---")

# 6. Logika Perhitungan Berdasarkan Daftar Angka
if st.button('🖩 Hitung Hasil'):
    # Ambil angka pertama sebagai dasar perhitungan
    hasil = daftar_angka[0]
    string_proses = f"{daftar_angka[0]}"
    
    error_pembagian = False

    # Lakukan loop untuk menghitung angka ke-2 hingga angka terakhir
    for angka_berikutnya in daftar_angka[1:]:
        
        if mode == 'Penjumlahan (+)':
            hasil += angka_berikutnya
            string_proses += f" + {angka_berikutnya}"
            
        elif mode == 'Pengurangan (-)':
            hasil -= angka_berikutnya
            string_proses += f" - {angka_berikutnya}"
            
        elif mode == 'Perkalian (x)':
            hasil *= angka_berikutnya
            string_proses += f" x {angka_berikutnya}"
            
        elif mode == 'Pembagian (/)':
            if angka_berikutnya == 0:
                error_pembagian = True
                break
            hasil /= angka_berikutnya
            string_proses += f" / {angka_berikutnya}"

    # Tampilkan Hasil
    if error_pembagian:
        st.error("Error: Tidak bisa melakukan pembagian dengan angka nol (0)!")
    else:
        st.success(f"Hasil: {string_proses} = **{hasil}**")
