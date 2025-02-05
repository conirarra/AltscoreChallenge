import requests

url_post = "https://makers-challenge.altscore.ai/v1/s1/e4/solution"

headers = {
    'accept': 'application/json',
    'API-KEY': '64462b944b7e4d458009596b5bc5611e'
}

payload = {
    "username": "Not all those who wander",
    "password": "are lost"
}

response = requests.post(url_post, json=payload, headers=headers)

if response.status_code == 200:
    print("Credenciales enviadas correctamente:", response.text)
else:
    print("Error al enviar las credenciales:", response.status_code, response.text)

