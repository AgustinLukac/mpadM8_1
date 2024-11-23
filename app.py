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
    st.write("Preparando el video, espera un momento...")

    # Pausa de 3 segundos
    time.sleep(3)

    # URL del video de YouTube
    video_url = "https://www.youtube.com/watch?v=l91cnF-rrRI"  # Reemplaza con la URL de tu video

    # Mostrar el video en Streamlit
    st.video(video_url)