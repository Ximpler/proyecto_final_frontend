import requests
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
API_URL = os.getenv("API_URL")

def obtener_prediccion(data):
    try:
        response = requests.post(API_URL, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Error en la predicción: " + response.json().get('error')}
    except Exception as e:
        return {"error": f"Error al conectarse a la API: {str(e)}"}