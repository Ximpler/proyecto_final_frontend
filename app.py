import streamlit as st
from formulario import show_form
from informe import show_results  

# Configuración inicial de la app
st.set_page_config(page_title="Formulario de Propiedad", page_icon="🏠", layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Título de la aplicación
st.title(":blue[Estimación de precio de construcción]")

# Mostrar el formulario o los resultados según el estado
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Mostrar el formulario o los resultados según el estado
if st.session_state.submitted:
    show_results()
else:
    show_form()
