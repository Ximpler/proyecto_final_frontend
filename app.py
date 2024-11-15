import streamlit as st
from formulario import show_form
from api import obtener_prediccion
from utils.pdf_report import generar_pdf
import plotly.express as px

# Configuración inicial de la app
st.set_page_config(page_title="Formulario de Propiedad", page_icon="🏠", layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Título de la aplicación
st.title(":blue[Estimación de precio de construcción]")

# Mostrar el formulario o los resultados según el estado
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Pestaña para mostrar los resultados ingresados y gráficos
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
    #st.session_state.df_costos = prediction['df_costos']  # Si tienes el desglose de costos en la respuesta

    # Mostrar el desglose de costos y gráficos
    col1, col2, col3 = st.columns(3)
    #with col1:
        #st.write("**Desglose de costos**:")
        #st.dataframe(st.session_state.df_costos)
    #with col2:
        
        #st.write("**Gráfico de costos por componente**:")
        #st.bar_chart(st.session_state.df_costos.set_index("Componentes"))
    #with col3:
        #fig = px.pie(st.session_state.df_costos, values='Costo ($)', names='Componentes', title='Distribución de Costos')
        #st.plotly_chart(fig)

    # Botón para descargar el informe en PDF
    if st.button("Descargar Informe PDF"):
        pdf_path = generar_pdf(st.session_state)
        st.success(f"Informe PDF generado: {pdf_path}")

    # Botón para reiniciar
    st.button("Volver", on_click=reset_form)

# Función para reiniciar el formulario
def reset_form():
    st.session_state.submitted = False
    st.session_state.prediction = None
    st.stop()

# Mostrar el formulario o los resultados según el estado
if st.session_state.submitted:
    show_results()
else:
    show_form()
