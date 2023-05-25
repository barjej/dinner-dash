import streamlit as st

st.set_page_config(
    page_title='Mari Belajar Streamlit',
    layout='wide'
)

st.write("Hello World!")

"Hello Worlddd"

"**hello**"

ini_tombol = st.button("Tekan")

saya_setuju = st.checkbox("Centang jika setuju")

if saya_setuju :
    "aku belajar lebih giat"
else :
    "Belajar dongg"

buah_favorit = st.radio(
    "Pilih buah favorit",
    ["Apel","Mangga","Jeruk"]
)

if buah_favorit == "Apel":
    "ewh sukanya sama apel"
elif buah_favorit == "Mangga":
    "siapa yang nyuruh pilih mangga?"
elif buah_favorit == "Jeruk":
    "dasar gak punya pendirian, malah pilih jeruk"

selectbox = st.selectbox(
    "Pilih buah favorit",
    ["Apel","Mangga","Jeruk"]
)

selectbox

multiselekan = st.multiselect(
    'pilih pilih aja'
    ,['Apel','Mangga','Jeruk']
)
multiselekan

multiselekan[2]

parameter_alpha = st.slider(
    "Insert value",
    min_value=0.0,
    max_value=1.0,
    step=0.1,
    value=0.5
)

parameter_alpha

ukuran_baju = st.select_slider(
    "ukuran baju",
    ["S","M","L","XL","XXL"]
)