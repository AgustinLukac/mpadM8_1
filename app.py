import streamlit as st

#Título de la app
st.title("Hola desde strealit cloud")

#Boton para mostrar el mensaje

if st.button("Mostrar mensaje"):
    st.write("Ignacio te clava SANTANDER CRISTIAN CON SUS BUBIS creo que con silviolin te pasa")
    st.write("Ingnacio TEnes cara de contra puto")

    st.title("Incrustar un video de YouTube en Streamlit")

    # URL del video de YouTube
    video_url = "https://www.youtube.com/watch?v=l91cnF-rrRI"  # Reemplaza con la URL de tu video

    # Mostrar el video en Streamlit
    st.video(video_url)