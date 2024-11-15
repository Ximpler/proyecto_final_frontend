import streamlit as st
import plotly.express as px
from utils.pdf_report import generar_pdf

def show_results():
    if "prediction" not in st.session_state:
        st.error("Error: No se ha realizado la predicción.")
        return

    with st.spinner("Cargando resultados..."):
        st.subheader(f"Resultados de la estimación: **${st.session_state.prediction:,.2f}**")
        
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
            st.write("**Desglose de costos**: ")
            st.dataframe(st.session_state.df_costos)
            
        with col2:
            st.write("**Gráfico de costos por componente**: ")
            st.bar_chart(st.session_state.df_costos.set_index("Componentes"))
        
        # Gráfico circular con Plotly
        fig = px.pie(st.session_state.df_costos, values='Costo ($)', names='Componentes', title='Distribución de Costos')
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(plot_bgcolor='lightblue')
        
        with col3:
            st.plotly_chart(fig)

        # Botón para descargar el informe en PDF (por ahora generándolo)
        if st.button("Descargar Informe PDF"):
            pdf_path = generar_pdf(st.session_state)
            st.success(f"Informe PDF generado: {pdf_path}")

        st.button("Volver", on_click=reset_form)

def reset_form():
    st.session_state.submitted = False
    st.session_state.prediction = None
    st.stop()
