import streamlit as st
from PIL import Image

st.title('Primer APP')
st.header('Primera web de interfaces multimodales')
st.write('a')
image = Image.open('perro.jpg')
st.image(image)

texto = st.text_input('Escribe un texto: ', 'Mi texto es ')

