import requests

# url de la API
url = "https://makers-challenge.altscore.ai/v1/s1/e8/actions/door"

# Clave de la API
headers = {
    'accept': 'application/json',
    'API-KEY': '64462b944b7e4d458009596b5bc5611e'
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
hacer_solicitud()
