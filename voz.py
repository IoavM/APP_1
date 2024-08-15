import streamlit as st
from PIL import Image

st.title('Primer APP')
st.header('Primera web de interfaces multimodales')
st.write('a')
image = Image.open('perro.jpg')
st.image(image)

texto = st.text_input('Escribe un texto: ')
st.write('El texto escrito es: ', texto)

col1, col2,col3 = st.columns(3)

with col1:
  st.subheader('primera columna')
  st.write('Aprendiendo web')
  resp = st. checkbox('Está chevere el front end')
  if resp:
    st.write('Confirmo')
with col2:
  st.subheader('Segunda columna')
  st.write('Pregunta ¿Te gusta programar?')
  resp2 = st.checkbox('Si')
  resp3 = st.checkbox('No')
  if resp2:
    st.write('Muy bien aspi me gusta.')
  if resp3: 
    image2 = Image.open()


  

