import streamlit as st
from PIL import Image
from gtts import gTTS

st.title('Primer APP')
st.header('Primera web de interfaces multimodales')
st.write('a')

# Cargar y mostrar la imagen
image = Image.open('perro.jpg')
st.image(image)

# Entrada de texto
texto = st.text_input('Escribe un texto: ')
st.write('El texto escrito es: ', texto)

# División en columnas
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('Primera columna')
    st.write('Aprendiendo web')
    resp = st.checkbox('¿Está chévere el front end?')
    if resp:
        st.write('Confirmo')

with col2:
    st.subheader('Segunda columna')
    st.write('Pregunta: ¿Te gusta programar?')
    resp2 = st.checkbox('Sí')
    resp3 = st.checkbox('No')
    if resp2:
        st.write('¡Muy bien, así me gusta!')
    if resp3: 
        image2 = Image.open('sticker.jpg')
        st.image(image2)

with col3:
    st.subheader('Esta es la tercera columna')
    modo = st.radio('¿Qué modalidad es la principal en tu interfaz?', ('Visual', 'Auditiva', 'Táctil'))
    if modo == 'Visual':
        st.write('La vista es fundamental para tu interfaz')
    elif modo == 'Auditiva':
        st.write('La audición es fundamental para tu interfaz')
    elif modo == 'Táctil':
        st.write('El tacto es fundamental para tu interfaz')

# Configuración en la barra lateral
with st.sidebar:
    st.subheader('Configura la modalidad')
    mod_radio = st.radio('Escoge la modalidad a usar', ('Visual', 'Auditiva', 'Háptica'))

# Convertir texto a audio
st.subheader('Convierte texto a audio')
text_to_convert = st.text_input('Ingresa tu texto para convertir a audio: ')

if st.button('Generar Audio'):
    if text_to_convert:
        tts = gTTS(text=text_to_convert, lang='es')
        tts.save('audio.mp3')
        audio_file = open('audio.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    else:
        st.write('Por favor ingresa un texto para convertir a audio.')
