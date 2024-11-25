import streamlit as st
from utils.upload_json import load_json

# Variables
ppf_vars = ['PPF-V-2', 'PPF-V-3','PPF-V-4','PPF-V-5', 'PPF-V-6' , 'PPF-V-7', 'PPF-V-8']
evi1_vars = ['EVI1-V-11', 'EVI1-V-12', 'EVI1-V-13', 'EVI1-V-14', 'EVI1-V-15', 'EVI1-V-16', 'EVI1-V-17', 'EVI1-V-18', 'EVI1-V-19', 'EVI1-V-20', 'EVI1-V-21', 'EVI1-V-22', 'EVI1-V-23', 'EVI1-V-24', 'EVI1-V-25', 'EVI1-V-26', 'EVI1-V-27', 'EVI1-V-28', 'EVI1-V-29']
evi2_vars = ['EVI2-V-11', 'EVI2-V-12', 'EVI2-V-13', 'EVI2-V-14', 'EVI2-V-15', 'EVI2-V-16', 'EVI2-V-17', 'EVI2-V-18', 'EVI2-V-19', 'EVI2-V-20', 'EVI2-V-21', 'EVI2-V-22', 'EVI2-V-23', 'EVI2-V-24', 'EVI2-V-25', 'EVI2-V-26', 'EVI2-V-27', 'EVI2-V-28', 'EVI2-V-29']
evi3_vars = ['EVI3-V-11', 'EVI3-V-12', 'EVI3-V-13', 'EVI3-V-14', 'EVI3-V-15', 'EVI3-V-16', 'EVI3-V-17', 'EVI3-V-18', 'EVI3-V-19', 'EVI3-V-20', 'EVI3-V-21', 'EVI3-V-22', 'EVI3-V-23', 'EVI3-V-24', 'EVI3-V-25', 'EVI3-V-26', 'EVI3-V-27', 'EVI3-V-28', 'EVI3-V-29']
evi4_vars = ['EVI4-V-11', 'EVI4-V-12', 'EVI4-V-13', 'EVI4-V-14', 'EVI4-V-15', 'EVI4-V-16', 'EVI4-V-17', 'EVI4-V-18', 'EVI4-V-19', 'EVI4-V-20', 'EVI4-V-21', 'EVI4-V-22', 'EVI4-V-23', 'EVI4-V-24', 'EVI4-V-25', 'EVI4-V-26', 'EVI4-V-27', 'EVI4-V-28', 'EVI4-V-29']
evi5_vars = ['EIV5-V-11', 'EIV5-V-12', 'EIV5-V-13', 'EIV5-V-14', 'EIV5-V-15', 'EIV5-V-16', 'EIV5-V-17', 'EIV5-V-18', 'EIV5-V-19', 'EIV5-V-20', 'EIV5-V-21', 'EIV5-V-22', 'EIV5-V-23', 'EIV5-V-24', 'EIV5-V-25', 'EIV5-V-26', 'EIV5-V-27', 'EIV5-V-28', 'EIV5-V-29']

eventos = {
    'Seleccione una opción': {
        'evi1_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
        'evi2_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
        'evi3_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
        'evi4_vars':[7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
        'eiv5_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
    },
    'Evento 1': {
        'evi1_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
        'evi2_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
        'evi3_vars':[7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
        'evi4_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
        'eiv5_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
    },
    'Evento 2': {
        'evi1_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
        'evi2_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
        'evi3_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
        'evi4_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
        'eiv5_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1]
    }
}

evi_descriptions = {
        'V-11': 'Number of building permits issued.',
        'V-12': 'Building services index (BSI) for a preselected base year.',
        'V-13': 'Wholesale price index (WPI) of building materials for the base year.',
        'V-14': 'Total floor areas of building permits issued by the city/municipality.',
        'V-15': 'Cumulative liquidity in IRRm.',
        'V-16': 'Private sector investment in new buildings in IRRm.',
        'V-17': 'Land price index for the base year.',
        'V-18': 'Number of loans extended by banks in a time resolution.',
        'V-19': 'Amount of loans extended by banks in IRRm.',
        'V-20': 'Interest rate for loans in percentage.',
        'V-21': 'Average construction cost of buildings by private sector at the time of completion in IRRm per m2.',
        'V-22': 'Average construction cost of buildings by private sector at the beginning of construction in IRRm per m2.',
        'V-23': 'Official exchange rate with respect to dollars in IRRm.',
        'V-24': 'Nonofficial (street market) exchange rate with respect to dollars in IRRm.',
        'V-25': 'Consumer price index (CPI) for the base year.',
        'V-26': 'CPI of housing, water, fuel & power in the base year.',
        'V-27': 'Stock market index.',
        'V-28': 'Population of the city.',
        'V-29': 'Gold price per ounce in IRRm.'
    }

ranges = {
    'V-11': {'Rango max': 8000, 'Rango min': 1000, 'Paso': 1},
    'V-12': {'Rango max': 274.0, 'Rango min': 10.0, 'Paso': 0.01},
    'V-13': {'Rango max': 225.0, 'Rango min': 3.91, 'Paso': 0.01},
    'V-14': {'Rango max': 6.88, 'Rango min': 0.92, 'Paso': 0.01},
    'V-15': {'Rango max': 2171922.8, 'Rango min': 27231.21, 'Paso': 0.01},
    'V-16': {'Rango max': 18690.9, 'Rango min': 287.2, 'Paso': 0.01},
    'V-17': {'Rango max': 319.38, 'Rango min': 9.85, 'Paso': 0.01},
    'V-18': {'Rango max': 432.4, 'Rango min': 14.15, 'Paso': 0.01},
    'V-19': {'Rango max': 73143.5, 'Rango min': 152.6, 'Paso': 0.01},
    'V-20': {'Rango max': 20, 'Rango min': 5, 'Paso': 1},
    'V-21': {'Rango max': 4188.65, 'Rango min': 165.1, 'Paso': 0.01},
    'V-22': {'Rango max': 4741.56, 'Rango min': 152.25, 'Paso':0.01},
    'V-23': {'Rango max': 9967.33, 'Rango min': 1439.0, 'Paso': 0.01},
    'V-24': {'Rango max': 10099.3, 'Rango min': 1450.0, 'Paso': 0.01},
    'V-25': {'Rango max': 204.7, 'Rango min': 9.73, 'Paso': 0.01},
    'V-26': {'Rango max': 222.6, 'Rango min': 8.34, 'Paso': 0.01},
    'V-27': {'Rango max': 13596.37, 'Rango min': 354.55, 'Paso':0.01},
    'V-28': {'Rango max': 2000000, 'Rango min': 8000, 'Paso': 1},
    'V-29': {'Rango max': 2606321.0, 'Rango min': 121857.2, 'Paso': 0.01}
}

# Define una función modular para generar sliders
def generar_sliders(titulo, variables, eventos, evento_seleccionado, ranges, descriptions, prefix):
        """
        Crea un conjunto de sliders para las variables de un evento específico.
        """
        with st.expander(titulo):
            inputs = {}
            for i, var in enumerate(variables):
                var_key = var.split(f"{prefix}-")[1]
                min_value = ranges[var_key]['Rango min']
                max_value = ranges[var_key]['Rango max']
                step = ranges[var_key]['Paso']
                
                # Obtener el valor inicial del evento
                value = eventos[evento_seleccionado][f'{prefix.lower()}_vars'][i]

                # Log para depurar
                print(f"Valor inicial: {value}, Tipo: {type(value)}")
                print(f"Min: {min_value}, Max: {max_value}, Step: {step}")
                print("____________________________LOG___________________")
                
                # Convertir `value` al tipo de `min_value`
                if isinstance(min_value, int):
                    value = int(value)  # Convertir a entero si `min_value` es entero
                elif isinstance(min_value, float):
                    value = float(value)  # Convertir a flotante si `min_value` es flotante

                # Asegurarse de que el valor esté dentro del rango
                if not (min_value <= value <= max_value):
                    value = min_value

                # Agregar el slider
                inputs[var] = st.slider(
                    f'{descriptions[var_key]}',
                    min_value=min_value,
                    max_value=max_value,
                    value=value,
                    step=step,
                    key=var
                )
            return inputs

    

def show_form():
    with st.form("formulario_propiedad"):
        
        # Formulario de entrada
        st.title("Formulario de Variables")
        evi_inputs = {}

        # Ingreso de PPF-V- variables (normal input)
        # PPF-V variables
        ppf_inputs = {}
        
        uploaded_file = st.file_uploader("Arrastra y suelta un archivo JSON aquí", type="json")
        

        # PPF-V-2 input
        ppf_inputs['PPF-V-2'] = st.number_input('Total floor area of the building in square meters.', value=0.0, min_value=0.0)

        # PPF-V-3 input
        ppf_inputs['PPF-V-3'] = st.number_input('Lot area in square meters.', value=0.0, min_value=0.0)
        
        # PPF-V-4 input
        ppf_inputs['PPF-V-4'] = st.number_input('Total preliminary estimated construction cost based on the prices at the beginning of the project', value=0.0, min_value=0.0)
        
        # PPF-V-5 input
        ppf_inputs['PPF-V-5'] = st.number_input('Preliminary estimated construction cost based on the prices at the beginning of the project.', value=0.0, min_value=0.0)
        
        # PPF-V-6 input
        ppf_inputs['PPF-V-6'] = st.number_input('Equivalent preliminary estimated construction cost based on the prices at the beginning of the project in a selected base year.', value=0.0, min_value=0.0)

        # PPF-V-7 input
        ppf_inputs['PPF-V-7'] = st.number_input('Duration of construction in time resolution (e.g., quarters).', value=0, min_value=0)

        # PPF-V-8 input
        ppf_inputs['PPF-V-8'] = st.number_input('Price per unit (per m2) at the beginning of the project in Iranian Rial (IRRm).', value=0.0, min_value=0.0)

        # Guardar el evento seleccionado previamente en session_state
        if "evento_seleccionado" not in st.session_state:
            st.session_state.evento_seleccionado = None

        # Detectar el cambio en el evento seleccionado
        evento_seleccionado = st.selectbox("Seleccione el evento", list(eventos.keys()))

        # Si cambia el evento, refresca la página
        if st.session_state.evento_seleccionado != evento_seleccionado:
            st.session_state.evento_seleccionado = evento_seleccionado
            print("------------selecciono el evento:", evento_seleccionado)
            #st.rerun()
    
        with st.container():
            evi1_inputs = generar_sliders(
                "EIV1 Variables", evi1_vars, eventos, evento_seleccionado, ranges, evi_descriptions, "EVI1"
            )
            evi2_inputs = generar_sliders(
                "EIV2 Variables", evi2_vars, eventos, evento_seleccionado, ranges, evi_descriptions, "EVI2"
            )
            evi3_inputs = generar_sliders(
                "EIV3 Variables", evi3_vars, eventos, evento_seleccionado, ranges, evi_descriptions, "EVI3"
            )
            evi4_inputs = generar_sliders(
                "EIV4 Variables", evi4_vars, eventos, evento_seleccionado, ranges, evi_descriptions, "EVI4"
            )
            evi5_inputs = generar_sliders(
                "EIV5 Variables", evi5_vars, eventos, evento_seleccionado, ranges, evi_descriptions, "EIV5"
            )

            # Botón de envío del formulario
            submitted = st.form_submit_button("Enviar")
            
            if submitted:
                if uploaded_file:
                    st.success("Archivo cargado con éxito.")
                    data = load_json(uploaded_file)
                    st.session_state.form_data = data
                    st.session_state.submitted = True
                else:
                    data = {
                        "ppf_inputs": ppf_inputs,
                        "evi1_inputs": evi1_inputs,
                        # Add the other input sets for EVI2, EVI3, EVI4, EIV5 here
                    }

                    # Almacenar los datos del formulario y el estado de envío
                    st.session_state.form_data = data
                    st.session_state.submitted = True


    