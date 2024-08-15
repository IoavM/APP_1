import streamlit as st
from PIL import Image

st.title('Primer APP')
st.header('Primera web de interfaces multimodales')
st.write('a')
image = Image.open('perro.jpg')
st.image(image)

texto = st.text_input('Escribe un texto: ')
st.write('El texto escrito es: ', texto)

col1, col2 = st.columns(2)

with col1:
  st.subheader('primera columna')
  st.write('Aprendiendo web')
  resp = st. checkbox('Está chevere el front end')
  if resp:
    st.write('Confirmo')

