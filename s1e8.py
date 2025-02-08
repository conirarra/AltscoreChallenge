import requests
import time
from datetime import datetime, timedelta

# url de la API
url = "https://makers-challenge.altscore.ai/v1/s1/e8/actions/door"

# Clave de la API
headers = {
    'accept': 'application/json',
    'API-KEY': '64462b944b7e4d458009596b5bc5611e',
}


# Función para hacer la solicitud y revelar detalles
def hacer_solicitud():
    response = requests.post(url, headers=headers)

    # Mostrar el código de estado HTTP
    print(f"Estado HTTP: {response.status_code}")

    # Mostrar los encabezados de la respuesta
    print("Encabezados de la respuesta:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    # Mostrar el cuerpo de la respuesta (por si hay más pistas)
    print("Cuerpo de la respuesta:")
    try:
        print(response.json())  # Intentamos parsear como JSON
    except ValueError:
        print(response.text)  # Si no es JSON, mostramos el texto

# Ejecutar la función
#hacer_solicitud()

# se encontro que se debe setear la cookie en "set-cookie: gryffindor="QWx0d2FydHM=""
# se seguira con el ejercicio

# session = requests.Session()
# session.cookies.set('gryffindor', 'Y29udGludWFtZW50ZQ==')

# Las cookies revelaron un mensaje encriptado en base64:
# "Altwarts revela cómo la magia surge mediante perseverancia, precisión y esmero al enfrentar desafíos. 
# Cada detalle importa; auténtica destreza se refleja con dedicación para mejorar continuamente"

# response = session.post(url, headers=headers)

# print(f"Estado HTTP: {response.status_code}")
    
# # Mostrar los encabezados de la respuesta
# print("Encabezados de la respuesta:")
# for key, value in response.headers.items():
#     print(f"{key}: {value}")

# # Mostrar el cuerpo de la respuesta
# print("Cuerpo de la respuesta:")
# try:
#     print(response.json())  # Intentamos parsear como JSON
# except ValueError:
#     print(response.text)  # Si no es JSON, mostramos el texto

url_solution = "https://makers-challenge.altscore.ai/v1/s1/e8/solution"

# Se envía el mensaje desencriptado
response = requests.post(url_solution, headers=headers, json={"hidden_message": "Altwarts revela cómo la magia surge mediante perseverancia, precisión y esmero al enfrentar desafíos. Cada detalle importa; auténtica destreza se refleja con dedicación para mejorar continuamente"})

# Mostrar respuesta
print(f"Estado HTTP: {response.status_code}")
print("Encabezados de la respuesta:")
for key, value in response.headers.items():
    print(f"{key}: {value}")
print("Cuerpo de la respuesta:")
try:
    print(response.json())  # Intentamos parsear como JSON
except ValueError:
    print(response.text)

# Respuesta correcta