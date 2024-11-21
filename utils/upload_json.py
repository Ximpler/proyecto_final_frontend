import json
from utils.api import obtener_prediccion

# Función para cargar el archivo JSON
def load_json(file):
    try:
        data = json.load(file)
        return data
    except Exception as e:
        st.error(f"Error al cargar el archivo JSON: {e}")
        return None
    
def process_data_json_2_api(data):
    return obtener_prediccion(data)