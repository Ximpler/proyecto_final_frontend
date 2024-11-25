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
    # 'Seleccione una opción': {
    #     'evi1_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
    #     'evi2_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
    #     'evi3_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
    #     'evi4_vars':[7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
    #     'eiv5_vars': [7196,51.3,56.13,5.97,249110.7,2562.3,52.8,217,10445.6,15,733.8,815.5,1755,8002,60.74,54.26,2978.26,41407,601988.1],
    # },
    'Evento 1': {
        'evi1_vars': [7100, 51.5, 57.8, 6.0, 240500.4, 2520.0, 53.5, 220, 10500.6, 15, 740.0, 820.3, 1750, 8005, 61.0, 54.5, 2920.0, 41250, 601000.0],
        'evi2_vars': [7250, 50.8, 56.5, 5.8, 250300.0, 2600.5, 51.0, 210, 10350.4, 14, 710.0, 815.6, 1725, 7900, 60.0, 53.0, 2890.0, 41500, 605000.0],
        'evi3_vars': [7300, 51.0, 57.0, 6.1, 247000.6, 2550.3, 54.0, 225, 10480.3, 16, 735.0, 818.2, 1740, 7950, 61.5, 54.2, 2910.0, 42000, 607000.0],
        'evi4_vars': [7450, 52.2, 58.0, 6.2, 245800.8, 2580.4, 52.0, 205, 10300.5, 15, 725.0, 810.5, 1730, 8000, 62.0, 55.0, 2940.0, 42500, 610000.0],
        'eiv5_vars': [7500, 50.3, 59.0, 6.0, 255000.0, 2405.0, 59.0, 235, 10050.0, 17, 715.0, 825.3, 1760, 8350, 63.0, 57.0, 2980.0, 43500, 625000.0]
    },
    'Evento 2': {
        'evi1_vars': [7543, 49.8, 60.2, 6.5, 300450.3, 2005.7, 62.1, 310, 9982.6, 18, 875.6, 745.2, 1854, 9003, 70.15, 58.32, 3100.5, 45500, 642135.4],
        'evi2_vars': [7021, 53.6, 52.7, 5.2, 229800.0, 2700.4, 49.3, 150, 10230.4, 13, 689.4, 865.7, 1680, 7800, 59.84, 52.42, 2850.3, 40010, 585000.0],
        'evi3_vars': [7200, 50.1, 58.9, 6.8, 254000.7, 2500.6, 55.5, 230, 10800.1, 14, 700.5, 810.0, 1700, 7950, 62.35, 53.67, 2900.0, 41000, 600050.3],
        'evi4_vars': [7350, 52.0, 57.5, 6.3, 243210.5, 2600.8, 50.2, 215, 10620.5, 17, 750.0, 825.4, 1800, 8100, 61.0, 55.0, 2950.0, 42000, 605000.0],
        'eiv5_vars': [7600, 50.5, 59.8, 5.9, 260000.0, 2400.2, 58.0, 250, 10100.0, 16, 720.0, 835.3, 1775, 8300, 64.0, 56.0, 2990.0, 43000, 620000.0]
    },
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
                #print(f"Valor inicial: {value}, Tipo: {type(value)}")
                #print(f"Min: {min_value}, Max: {max_value}, Step: {step}")
                #print("____________________________LOG___________________")
                
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
        
        st.write(f"Opción seleccionada: **{evento_seleccionado}**")        
        # Si cambia el evento, refresca la página
        if st.session_state.evento_seleccionado != evento_seleccionado:
            st.session_state.evento_seleccionado = evento_seleccionado
            print("------------selecciono el evento:", evento_seleccionado)
            st.rerun()
    
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
                     # Renombrar las claves para que coincidan con el formato requerido
                    data = {}

                    # PPF-V variables
                    data.update({
                        "PPF-V-2": ppf_inputs['PPF-V-2'],
                        "PPF-V-3": ppf_inputs['PPF-V-3'],
                        "PPF-V-4": ppf_inputs['PPF-V-4'],
                        "PPF-V-5": ppf_inputs['PPF-V-5'],
                        "PPF-V-6": ppf_inputs['PPF-V-6'],
                        "PPF-V-7": ppf_inputs['PPF-V-7'],
                        "PPF-V-8": ppf_inputs['PPF-V-8']
                    })

                    # Función para renombrar claves eliminando la repetición del prefijo
                    def rename_keys(input_data, prefix):
                        renamed_data = {}
                        for key, value in input_data.items():
                            # Eliminar el prefijo repetido y mantener solo la parte relevante
                            new_key = key.replace(f'{prefix}-{prefix}-', f'{prefix}-')
                            renamed_data[new_key] = value
                        return renamed_data

                    # Renombrar las claves de EVI1, EVI2, EVI3, EVI4, EVI5
                    data.update(rename_keys(evi1_inputs, 'EVI1'))
                    data.update(rename_keys(evi2_inputs, 'EVI2'))
                    data.update(rename_keys(evi3_inputs, 'EVI3'))
                    data.update(rename_keys(evi4_inputs, 'EVI4'))
                    data.update(rename_keys(evi5_inputs, 'EVI5'))


                    # Almacenar los datos del formulario y el estado de envío
                    st.session_state.form_data = data
                    st.session_state.submitted = True


    