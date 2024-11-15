import streamlit as st

def show_form():
    with st.form("formulario_propiedad"):
        # Campos para las variables de entrada, usando los nombres de las variables en tu DataFrame
        v2 = st.number_input("Tamaño de la construcción en m² (V-2)", min_value=200, max_value=15670, step=10)
        v3 = st.number_input("Área del lote en m² (V-3)", min_value=60, max_value=5000, step=10)
        v7 = st.number_input("Duración en cuartos de año (V-7)", min_value=2, max_value=23, step=1)
        v8 = st.number_input("Precio por m² (V-8)", min_value=40, max_value=5700, step=10)
        v11 = st.number_input("Valor V-11", min_value=0.0, max_value=100.0, step=0.01)
        v12 = st.number_input("Valor V-12", min_value=0.0, max_value=100.0, step=0.01)
        v13 = st.number_input("Valor V-13", min_value=0.0, max_value=100.0, step=0.01)
        v14 = st.number_input("Valor V-14", min_value=0.92, max_value=6.88, step=0.01)
        v15 = st.number_input("Valor V-15", min_value=0.0, max_value=100.0, step=0.01)
        v16 = st.number_input("Valor V-16", min_value=0.0, max_value=100.0, step=0.01)
        v17 = st.number_input("Valor V-17", min_value=13.6, max_value=319.38, step=0.1)
        v18 = st.number_input("Valor V-18", min_value=0.0, max_value=100.0, step=0.01)
        v19 = st.number_input("Valor V-19", min_value=0.0, max_value=100.0, step=0.01)
        v20 = st.number_input("Valor V-20", min_value=0.0, max_value=100.0, step=0.01)
        v21 = st.number_input("Valor V-21", min_value=0.0, max_value=100.0, step=0.01)
        v22 = st.number_input("Valor V-22", min_value=0.0, max_value=100.0, step=0.01)
        v23 = st.number_input("Valor V-23", min_value=0.0, max_value=100.0, step=0.01)
        v24 = st.number_input("Valor V-24", min_value=0.0, max_value=100.0, step=0.01)
        v25 = st.number_input("Valor V-25", min_value=0.0, max_value=100.0, step=0.01)
        v26 = st.number_input("Valor V-26", min_value=10.06, max_value=222.6, step=0.1)
        v27 = st.number_input("Valor V-27", min_value=0.0, max_value=100.0, step=0.01)
        v28 = st.number_input("Valor V-28", min_value=8436, max_value=50928, step=1)
        v29 = st.number_input("Valor V-29", min_value=0.0, max_value=100.0, step=0.01)
        
        # Botón de envío del formulario
        submitted = st.form_submit_button("Enviar")
        
        if submitted:
            data = {
                "v2": v2,
                "v3": v3,
                "v7": v7,
                "v8": v8,
                "v11": v11,
                "v12": v12,
                "v13": v13,
                "v14": v14,
                "v15": v15,
                "v16": v16,
                "v17": v17,
                "v18": v18,
                "v19": v19,
                "v20": v20,
                "v21": v21,
                "v22": v22,
                "v23": v23,
                "v24": v24,
                "v25": v25,
                "v26": v26,
                "v27": v27,
                "v28": v28,
                "v29": v29
            }

            # Almacenar los datos del formulario y el estado de envío
            st.session_state.form_data = data
            st.session_state.submitted = True
