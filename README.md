

# Debemos crear una carpeta llamada "gemini-api"
# Al entrar creamos una carpeta llamada "prueba_entorno", donde verificaremos si el entorno virtual esta activo. Para ello debemos hacer lo siguiente: 
                                          - Abrir Visual Studio
                                          - Seleccionamos la carpeta creada "gemini-api"
                                          - ctrl+ñ = Para abrir la terminal de Visual Studio
                                          - En la terminal ponemos el siguiente comando: "python -m venv venv"
                                            Este comando creará una carpeta llamada venv dentro de tu proyecto. Esta carpeta contendrá todos los paquetes que instalemos.
                                          - Para activar el entorno = ".\venv\Scripts\Activate"
                                          - Para que Visual Studio reconozca el entorno debemos hacer lo siguiente: 
                                                          * Presiona Ctrl + Shift + P para abrir la paleta de comandos.
                                                          *Escribe "Python: Select Interpreter".
                                                          *Selecciona la opción que apunta a tu carpeta del entorno virtual (debería
                                                           decir algo como ./venv/Scripts/python.exe ).

# Instalación de librería: "pip install requests"
# Crear un archivo llamado prueba_entorno.py en la carpeta gemini-api y pega el siguiente código

import requests
import sys
import os
def verificar_configuracion():
print("--- Verificación de Entorno Virtual ---")
# Comprobar si estamos dentro de un entorno virtual
if hasattr(sys, 'real_prefix') or (sys.base_prefix != sys.prefix):
 print("✅ Estado: Entorno Virtual ACTIVO.")
else:
 print("❌ Estado: Entorno Virtual NO detectado. Por favor, actívalo.")
# Mostrar la ruta del ejecutable de Python que se está usando
print(f"📍 Ruta de Python: {sys.executable}")
# Simular una pequeña petición de red para verificar conexión
try:
 response = requests.get("<https://www.google.com>")
 if response.status_code == 200:
 print("🌐 Conexión a internet: OK (Google es alcanzable).")
except Exception as e:
 print(f"⚠️ Error de conexión: {e}")
if name == "main":
verificar_configuracion()

Para saber si esta corriendo correctamente debemos ver el siguiente mensaje:
<img width="729" height="121" alt="image" src="https://github.com/user-attachments/assets/f02a8ec3-a9eb-455b-8d19-9c40ca344325" />




