import os
from google import genai
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el Cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)


# 3. Llamada directa al servicio de modelos
try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="""Actualiza el nombre Ing. Leandro por Ing. Alejandro y 
        el cargo Consultor por Estudiamte en el siguiente texto:

        'Alejandro es un estudiante de ing de sistemas el cual va en 7 semestre
         y esta ampliando su conocimiento acerca de todos los temas relacionados con ing de sistemas.'
        """
    )
except Exception as e:
    print(f"❌ Ocurrió un error en la conexión: {e}")

# 4. Imprimir la respuesta
if response:
    print("✅ Respuesta del modelo:")
    print(response.text)