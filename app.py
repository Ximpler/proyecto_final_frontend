import streamlit as st
import plotly.express as px
import pandas as pd
from utils.pdf_report import generar_pdf

# Configuración inicial de la app
st.set_page_config(page_title="Formulario de Propiedad", page_icon="🏠", layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Título de la aplicación
st.title(":blue[Estimación de precio de construcción]")

# Si el usuario no ha enviado el formulario, mostrar el formulario
if "submitted" not in st.session_state:
    st.session_state.submitted = False

def calcular_presupuesto(beds, size, bathrooms):
    precio_base = 500 * size
    costo_camas = 3000 * beds
    costo_banos = 5000 * bathrooms
    presupuesto_total = precio_base + costo_camas + costo_banos

    datos = {
        "Componentes": ["Tamaño", "Camas", "Baños"],
        "Costo ($)": [precio_base, costo_camas, costo_banos]
    }
    df_costos = pd.DataFrame(datos)

    return presupuesto_total, df_costos

# Pestaña principal para el formulario
def show_form():
    with st.form("formulario_propiedad"):
        beds = st.number_input("Número de camas", min_value=1, step=1)
        size = st.number_input("Tamaño de la propiedad (m²)", min_value=10, step=10)
        bathrooms = st.number_input("Número de baños", min_value=1.0, step=0.5, format="%.1f")
        
        # Botón de envío del formulario
        submitted = st.form_submit_button("Enviar")
        
        if submitted:
            st.session_state.beds = beds
            st.session_state.size = size
            st.session_state.bathrooms = bathrooms
            
            # Calcular el presupuesto y guardar los resultados
            st.session_state.presupuesto, st.session_state.df_costos = calcular_presupuesto(beds, size, bathrooms)
            st.session_state.submitted = True
            st.stop()

# Pestaña para mostrar los resultados ingresados y gráficos
def show_results():
    with st.spinner("Cargando resultados..."):
        st.subheader(f"Resultados de la estimación: **${st.session_state.presupuesto:,.2f}**")
        
        c1, c2 = st.columns(2)
        with c1:
            st.write(f"**Camas**: {st.session_state.beds}")
            st.write(f"**Tamaño**: {st.session_state.size} m²")
            st.write(f"**Baños**: {st.session_state.bathrooms}")
            
        with c2:
            image_png_house_path = "img/transparent-house.png"
            st.image(image_png_house_path)

        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("**Desglose de costos**:")
            st.dataframe(st.session_state.df_costos)
            
        with col2:
            st.write("**Gráfico de costos por componente**:")
            st.bar_chart(st.session_state.df_costos.set_index("Componentes"))
        
        # Gráfico circular con Plotly
        fig = px.pie(st.session_state.df_costos, values='Costo ($)', names='Componentes', title='Distribución de Costos')
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(plot_bgcolor='lightblue')
        
        with col3:
            st.plotly_chart(fig)

        # Botón para descargar el informe en PDF (por ahora generandolo)
        if st.button("Descargar Informe PDF"):
            pdf_path = generar_pdf(st.session_state)
            st.success(f"Informe PDF generado: {pdf_path}")

        st.button("Volver", on_click=reset_form)

# Función para reiniciar el formulario
def reset_form():
    st.session_state.submitted = False
    st.stop()

# Mostrar el formulario o los resultados según el estado
if not st.session_state.submitted:
    show_form()
else:
    show_results()
