import streamlit as st
import math

# Set layout halaman agar lebih rapi dan pas di tengah
st.set_page_config(page_title="Kalkulator Grid", page_icon="🔢", layout="centered")

# Menggunakan CSS kustom agar tampilan tombol lebih padat dan mirip kalkulator fisik
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 60px;
        font-size: 20px !important;
        font-weight: 500;
        margin-bottom: -10px;
    }
    .display-box {
        background-color: #f0f4f9;
        padding: 20px;
        border-radius: 5px;
        text-align: right;
        font-size: 40px;
        font-weight: bold;
        font-family: monospace;
        margin-bottom: 20px;
        border: 1px solid #dcdcdc;
        color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

# Inisialisasi session state untuk menyimpan data input/angka
if 'display' not in st.session_state:
    st.session_state.display = "0"
if 'stored_value' not in st.session_state:
    st.session_state.stored_value = 0.0
if 'operator' not in st.session_state:
    st.session_state.operator = None
if 'reset_on_next_click' not in st.session_state:
    st.session_state.reset_on_next_click = False

# Fungsi logika ketika tombol ditekan
def press_number(num):
    if st.session_state.reset_on_next_click:
        st.session_state.display = str(num)
        st.session_state.reset_on_next_click = False
    else:
        if st.session_state.display == "0":
            st.session_state.display = str(num)
        else:
            st.session_state.display += str(num)

def press_operator(op):
    try:
        st.session_state.stored_value = float(st.session_state.display)
        st.session_state.operator = op
        st.session_state.reset_on_next_click = True
    except:
        st.session_state.display = "Error"

def calculate():
    if st.session_state.operator:
        try:
            current_value = float(st.session_state.display)
            if st.session_state.operator == "+":
                res = st.session_state.stored_value + current_value
            elif st.session_state.operator == "-":
                res = st.session_state.stored_value - current_value
            elif st.session_state.operator == "×":
                res = st.session_state.stored_value * current_value
            elif st.session_state.operator == "÷":
                res = st.session_state.stored_value / current_value if current_value != 0 else "Error"
            
            # Format hasil agar tidak banyak angka 0 di belakang koma jika bilangan bulat
            if isinstance(res, float) and res.is_integer():
                res = int(res)
                
            st.session_state.display = str(res)
        except Exception:
            st.session_state.display = "Error"
            
        st.session_state.operator = None
        st.session_state.reset_on_next_click = True

def clear_all():
    st.session_state.display = "0"
    st.session_state.stored_value = 0.0
    st.session_state.operator = None

def clear_entry():
    st.session_state.display = "0"

def backspace():
    if len(st.session_state.display) > 1:
        st.session_state.display = st.session_state.display[:-1]
    else:
        st.session_state.display = "0"

# --- TAMPILAN UTAMA ---
st.title("🔢 Standard Calculator")

# Kotak Layar Tampilan Angka
st.markdown(f'<div class="display-box">{st.session_state.display}</div>', unsafe_allow_html=True)

# Membuat Grid Tombol (Sesuai Layout Gambar)
# Baris 1
row1 = st.columns(4)
if row1[0].button("%"): 
    try:
        st.session_state.display = str(float(st.session_state.display) / 100)
    except:
        st.session_state.display = "Error"
if row1[1].button("CE"): clear_entry()
if row1[2].button("C"): clear_all()
if row1[3].button("⌫"): backspace()

# Baris 2
row2 = st.columns(4)
if row2[0].button("¹/x"): 
    try:
        val = float(st.session_state.display)
        st.session_state.display = str(1/val) if val != 0 else "Error"
    except:
        st.session_state.display = "Error"
if row2[1].button("x²"): 
    try:
        st.session_state.display = str(float(st.session_state.display) ** 2)
    except:
        st.session_state.display = "Error"
if row2[2].button("²√x"): 
    try:
        val = float(st.session_state.display)
        st.session_state.display = str(math.sqrt(val)) if val >= 0 else "Error"
    except:
        st.session_state.display = "Error"
if row2[3].button("÷"): press_operator("÷")

# Baris 3
row3 = st.columns(4)
if row3[0].button("7"): press_number(7)
if row3[1].button("8"): press_number(8)
if row3[2].button("9"): press_number(9)
if row3[3].button("×"): press_operator("×")

# Baris 4
row4 = st.columns(4)
if row4[0].button("4"): press_number(4)
if row4[1].button("5"): press_number(5)
if row4[2].button("6"): press_number(6)
if row4[3].button("-"): press_operator("-")

# Baris 5
row5 = st.columns(4)
if row5[0].button("1"): press_number(1)
if row5[1].button("2"): press_number(2)
if row5[2].button("3"): press_number(3)
if row5[3].button("+"): press_operator("+")

# Baris 6
row6 = st.columns(4)
if row6[0].button("+/-"): 
    try:
        if st.session_state.display != "0":
            st.session_state.display = str(-float(st.session_state.display))
    except:
        st.session_state.display = "Error"
if row6[1].button("0"): press_number(0)
if row6[2].button("."): 
    if "." not in st.session_state.display:
        st.session_state.display += "."
if row6[3].button("=", type="primary"): calculate()
