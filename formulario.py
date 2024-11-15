import streamlit as st

def show_form():
    with st.form("formulario_propiedad"):
        
        # Variables
        ppf_vars = ['PPF-V-2', 'PPF-V-3','PPF-V-4','PPF-V-5', 'PPF-V-6' , 'PPF-V-7', 'PPF-V-8']
        evi1_vars = ['EVI1-V-11', 'EVI1-V-12', 'EVI1-V-13', 'EVI1-V-14', 'EVI1-V-15', 'EVI1-V-16', 'EVI1-V-17', 'EVI1-V-18', 'EVI1-V-19', 'EVI1-V-20', 'EVI1-V-21', 'EVI1-V-22', 'EVI1-V-23', 'EVI1-V-24', 'EVI1-V-25', 'EVI1-V-26', 'EVI1-V-27', 'EVI1-V-28', 'EVI1-V-29']
        evi2_vars = ['EVI2-V-11', 'EVI2-V-12', 'EVI2-V-13', 'EVI2-V-14', 'EVI2-V-15', 'EVI2-V-16', 'EVI2-V-17', 'EVI2-V-18', 'EVI2-V-19', 'EVI2-V-20', 'EVI2-V-21', 'EVI2-V-22', 'EVI2-V-23', 'EVI2-V-24', 'EVI2-V-25', 'EVI2-V-26', 'EVI2-V-27', 'EVI2-V-28', 'EVI2-V-29']
        evi3_vars = ['EVI3-V-11', 'EVI3-V-12', 'EVI3-V-13', 'EVI3-V-14', 'EVI3-V-15', 'EVI3-V-16', 'EVI3-V-17', 'EVI3-V-18', 'EVI3-V-19', 'EVI3-V-20', 'EVI3-V-21', 'EVI3-V-22', 'EVI3-V-23', 'EVI3-V-24', 'EVI3-V-25', 'EVI3-V-26', 'EVI3-V-27', 'EVI3-V-28', 'EVI3-V-29']
        evi4_vars = ['EVI4-V-11', 'EVI4-V-12', 'EVI4-V-13', 'EVI4-V-14', 'EVI4-V-15', 'EVI4-V-16', 'EVI4-V-17', 'EVI4-V-18', 'EVI4-V-19', 'EVI4-V-20', 'EVI4-V-21', 'EVI4-V-22', 'EVI4-V-23', 'EVI4-V-24', 'EVI4-V-25', 'EVI4-V-26', 'EVI4-V-27', 'EVI4-V-28', 'EVI4-V-29']
        evi5_vars = ['EIV5-V-11', 'EIV5-V-12', 'EIV5-V-13', 'EIV5-V-14', 'EIV5-V-15', 'EIV5-V-16', 'EIV5-V-17', 'EIV5-V-18', 'EIV5-V-19', 'EIV5-V-20', 'EIV5-V-21', 'EIV5-V-22', 'EIV5-V-23', 'EIV5-V-24', 'EIV5-V-25', 'EIV5-V-26', 'EIV5-V-27', 'EIV5-V-28', 'EIV5-V-29']

        eventos = {
            'Evento 1': {
                'evi1_vars': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],
                'evi2_vars': [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],
                'evi3_vars': [12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142, 152, 162, 172, 182, 192],
                'evi4_vars': [13, 23, 33, 43, 53, 63, 73, 83, 93, 103, 113, 123, 133, 143, 153, 163, 173, 183, 193],
                'evi5_vars': [18, 28, 38, 48, 58, 68, 78, 88, 98, 108, 118, 128, 138, 148, 158, 168, 178, 188, 198],
            },
            'Evento 2': {
                'evi1_vars': [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],
                'evi2_vars': [25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205],
                'evi3_vars': [22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122, 132, 142, 152, 162, 172, 182, 192, 202],
                'evi4_vars': [23, 33, 43, 53, 63, 73, 83, 93, 103, 113, 123, 133, 143, 153, 163, 173, 183, 193, 203],
                'evi5_vars': [28, 38, 48, 58, 68, 78, 88, 98, 108, 118, 128, 138, 148, 158, 168, 178, 188, 198, 208],
            }
        }

        # Formulario de entrada
        st.title("Formulario de Variables")
        evi_inputs = {}

        # Ingreso de PPF-V- variables (normal input)
        # PPF-V variables
        ppf_inputs = {}

        # PPF-V-2 input
        ppf_inputs['PPF-V-2'] = st.number_input('Total floor area of the building in square meters.', value=0.0, min_value=0.0)

        # PPF-V-3 input
        ppf_inputs['PPF-V-3'] = st.number_input('Lot area in square meters.', value=0.0, min_value=0.0)
        
        # PPF-V-4 input
        ppf_inputs['PPF-V-4'] = st.number_input('Lot area in square meters.', value=0.0, min_value=0.0)
        
        # PPF-V-5 input
        ppf_inputs['PPF-V-5'] = st.number_input('Preliminary estimated construction cost based on the prices at the beginning of the project.', value=0.0, min_value=0.0)
        
        # PPF-V-6 input
        ppf_inputs['PPF-V-6'] = st.number_input('Equivalent preliminary estimated construction cost based on the prices at the beginning of the project in a selected base year.', value=0.0, min_value=0.0)

        # PPF-V-7 input
        ppf_inputs['PPF-V-7'] = st.number_input('Duration of construction in time resolution (e.g., quarters).', value=0, min_value=0)

        # PPF-V-8 input
        ppf_inputs['PPF-V-8'] = st.number_input('Price per unit (per m2) at the beginning of the project in Iranian Rial (IRRm).', value=0.0, min_value=0.0)
            
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

        # Usar radio para un comportamiento de switch
        evento_seleccionado = st.selectbox("Seleccione el evento", list(eventos.keys()))


        with st.container():
            with st.expander("EIV1 Variables"):
                evi1_inputs = {}
                for i, var in enumerate(evi1_vars):
                    v = var.split("EVI1-")[1]
                    min_value = ranges[v]['Rango min']
                    max_value = ranges[v]['Rango max']
                    step = ranges[v]['Paso']
                    
                    if evento_seleccionado:
                        value = eventos[evento_seleccionado]['evi1_vars'][i]
                    else:
                        value = min_value
                    evi1_inputs[var] = st.slider(f'{evi_descriptions[v]}', min_value=min_value, max_value=max_value, step=step, key=var)

            with st.expander("EIV2 Variables"):
                evi2_inputs = {}
                for i, var in enumerate(evi2_vars): 
                    v = var.split("EVI2-")[1]
                    min_value = ranges[v]['Rango min']
                    max_value = ranges[v]['Rango max']
                    step = ranges[v]['Paso']
                    if evento_seleccionado:
                        value = eventos[evento_seleccionado]['evi2_vars'][i]
                    else:
                        value = min_value
                    evi2_inputs[var] = st.slider(f'{evi_descriptions[v]}', min_value=min_value, max_value=max_value, step=step, key=var)

            with st.expander("EIV3 Variables"):
                evi3_inputs = {}
                for i, var in enumerate(evi3_vars): 
                    v = var.split("EVI3-")[1]
                    min_value = ranges[v]['Rango min']
                    max_value = ranges[v]['Rango max']
                    step = ranges[v]['Paso']
                    if evento_seleccionado:
                        value = eventos[evento_seleccionado]['evi3_vars'][i]
                    else:
                        value = min_value
                    evi3_inputs[var] = st.slider(f'{evi_descriptions[v]}', min_value=min_value, max_value=max_value, step=step, key=var)

            with st.expander("EIV4 Variables"):
                evi4_inputs = {}
                for i, var in enumerate(evi4_vars): 
                    v = var.split("EVI4-")[1]
                    min_value = ranges[v]['Rango min']
                    max_value = ranges[v]['Rango max']
                    step = ranges[v]['Paso']
                    if evento_seleccionado:
                        value = eventos[evento_seleccionado]['evi5_vars'][i]
                    else:
                        value = min_value
                    evi4_inputs[var] = st.slider(f'{evi_descriptions[v]}', min_value=min_value, max_value=max_value, step=step, key=var)


            with st.expander("EIV5 Variables"):
                evi5_inputs = {}
                for i, var in enumerate(evi5_vars):  # Cambia según las variables reales
                    v = var.split("EIV5-")[1]
                    min_value = ranges[v]['Rango min']
                    max_value = ranges[v]['Rango max']
                    step = ranges[v]['Paso']
                    if evento_seleccionado:
                        value = eventos[evento_seleccionado]['evi5_vars'][i]
                    else:
                        value = min_value
                    evi5_inputs[var] = st.slider(f'{evi_descriptions[v]}', min_value=min_value, max_value=max_value, step=step, key=var)


       
        # Botón de envío del formulario
        submitted = st.form_submit_button("Enviar")
        
        if submitted:
            data = {
                "ppf_inputs": ppf_inputs,
                "evi1_inputs": evi1_inputs,
                # Add the other input sets for EVI2, EVI3, EVI4, EIV5 here
            }

            # Almacenar los datos del formulario y el estado de envío
            st.session_state.form_data = data
            st.session_state.submitted = True
