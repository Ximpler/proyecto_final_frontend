import requests
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
API_URL = os.getenv("API_URL")


# Función para formatear los datos antes de enviarlos a la API
def formatear_datos(ppf_inputs, evi1_inputs):
    """
    Formatea los datos de entrada para la API.

    Args:
        ppf_inputs (dict): Datos relacionados con PPF.
        evi1_inputs (dict): Datos relacionados con EVI1.

    Returns:
        dict: Datos combinados y formateados.
    """
    # Combina los datos de PPF y EVI1 en un solo diccionario
    datos_combinados = {**ppf_inputs, **evi1_inputs}
    return datos_combinados

# Función para llamar a la API con los datos formateados
def obtener_prediccion(data):
    """
    Llama a la API para obtener la predicción basada en los datos proporcionados.

    Args:
        data (dict): Los datos a enviar a la API.

    Returns:
        dict: La respuesta de la API o un error.
    """
    try:
        print(data)
        response = requests.post(API_URL, json=data)
        print(data)
        if response.status_code == 200:
            print("Llamada a la API exitosa!")
            return response.json()
        else:
            return {"error": "Error en la predicción: " + response.json().get('error')}
    except Exception as e:
        return {"error": f"Error al conectarse a la API: {str(e)}"}