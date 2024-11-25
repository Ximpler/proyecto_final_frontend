import streamlit as st
from utils.api import obtener_prediccion

def show_results():
    if "form_data" not in st.session_state:
        st.error("No se han recibido datos del formulario.")
        return

    # Recuperar los datos del formulario desde session_state
    data = st.session_state.form_data

    # Hacer la solicitud a la API
    prediction = obtener_prediccion(data)

    if "error" in prediction:
        st.error(prediction["error"])
        return

    # Mostrar resultados
    st.subheader(f"Resultados de la estimación: **${prediction['data']:,.2f}**")
    st.session_state.prediction = prediction['data']

    # Botón para reiniciar
    st.button("Volver", on_click=reset_form)

# Función para reiniciar el formulario
def reset_form():
    st.session_state.submitted = False
    st.session_state.prediction = None
    st.rerun()
