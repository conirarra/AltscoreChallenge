import requests

url_post = "https://makers-challenge.altscore.ai/v1/s1/e5/actions/perform-turn"

headers = {
    'accept': 'application/json',
    'API-KEY': '64462b944b7e4d458009596b5bc5611e'
}

payload = {
    "action": "radar",
    "attack_position": None
}

response = requests.post(url_post, json=payload, headers=headers)

if response.status_code == 200:
    print("Accion Enviada:", response.text)
else:
    print("Error al enviar las credenciales:", response.status_code, response.text)



# Code made for problem 5, time limit reached because it said I already started the challenge and couldnt try again
# (probably did when i was trying all the documentation and just pressing buttons randomly on the website)
# Oops