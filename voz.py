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
  resp2 = st.checkbox('Si', key = 'resp2')
  resp3 = st.checkbox('No',key = 'resp3')
  if resp2:
    st.write('Muy bien asi me gusta.')
    if resp3:  # Desactivar "No" si "Sí" está seleccionado
        st.session_state.resp3 = False
  if resp3: 
    image2 = Image.open('sticker.jpg')
    st.image(image2)
    if resp2:
      st.session_state.resp2 = False

with col3:
  st.subheader('Esta es la 3ra columna')
  modo = st.radio('Qué modalidad es la principal dn tu interfaz', ('Visual', 'Auditiva', 'Táctil'))
  if modo == 'visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'Auditiva':
    st.write('La audición es fundamental para tu interfaz')
  if modo == 'Táctil':
    st.write('El tacto es fundamental para tu interfaz')
with st.sidebar:
  st.subheader('Configura la modalidad')
  mod_radio = st.radio('Escoge la modalidad a usar', ('Visual','Auditiva','Háptica'))

