import streamlit as st
import time

#Título de la app
st.title("Hola desde strealit cloud")

#Boton para mostrar el mensaje

if st.button("Mostrar mensaje"):
    st.write("Ignacio te clava SANTANDER CRISTIAN CON SUS BUBIS creo que con silviolin te pasa")
    st.write("Ingnacio TEnes cara de contra puto")

    st.title("Van a hablar el recontra puto")
    # Mensaje inicial antes de la pausa
    # Ruta del archivo de audio
    audio_file_path = "audio/1.aac"

    # Abrir el archivo de audio y reproducirlo
    with open(audio_file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/aac")
    st.write("Preparando el video, espera un momento...")

    # Pausa de 3 segundos
    time.sleep(3)

    # URL del video de YouTube
    video_url = "https://www.youtube.com/watch?v=l91cnF-rrRI"  # Reemplaza con la URL de tu video

    # Mostrar el video en Streamlit
    st.video(video_url)