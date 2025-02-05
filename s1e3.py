import requests
import base64

# URLs de la API
url_base_swapi = "https://swapi.dev/api/people/"
url_base_oracle = "https://makers-challenge.altscore.ai/v1/s1/e3/resources/oracle-rolodex"
url_post = "https://makers-challenge.altscore.ai/v1/s1/e3/solution" 

# Clave de la API
headers = {
    'accept': 'application/json',
    'API-KEY': '64462b944b7e4d458009596b5bc5611e'
}

# Lista para almacenar los nombres de los personajes
personajes = []
total_personajes = 0

# Diccionario para almacenar las respuestas del Oráculo
respuestas_por_personaje = {}

# Iniciar con la primera página de SWAPI
pagina = 1

# Función para decodificar las respuestas del Oráculo
def decode_base64(data):
    decoded_data = base64.b64decode(data).decode('utf-8')
    return decoded_data

# Obtener los nombres de todos los personajes de SWAPI
while url_base_swapi:
    response = requests.get(url_base_swapi)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extraer el nombre de cada personaje en la página actual
        for personaje in data['results']:
            nombre = personaje['name']
            homeworld = personaje['homeworld']  # Guardamos el homeworld
            
            # Agregamos el nombre y el homeworld al listado
            personajes.append({'nombre': nombre, 'homeworld': homeworld})
            
        total_personajes += len(data['results'])
        
        # Verificar si hay más páginas de resultados
        url_base_swapi = data['next']
        pagina += 1
    else:
        print(f"Error en la solicitud de SWAPI. Status code: {response.status_code}")
        break

print(f"Total de personajes en la API de SWAPI: {total_personajes}")

# Realizar una solicitud al Oráculo por cada personaje	
for personaje in personajes:
    # Parámetros de la consulta (nombre del personaje)
    nombre_personaje = personaje['nombre']
    params = {'name': nombre_personaje}

    response = requests.get(url_base_oracle, params=params, headers=headers)
    
    if response.status_code == 200:
        # Guardar la respuesta en el diccionario con el nombre del personaje como clave
        respuestas_por_personaje[nombre_personaje] = response.json()
    else:
        print(f"Error en la solicitud para {personaje}. Status code: {response.status_code}")

decoded_responses = {
    key: {
        k: decode_base64(v)  # Decodificamos las respuestas del Oráculo
        for k, v in value.items()
    }
    for key, value in respuestas_por_personaje.items()
}

personajes_info = {}

# Vemos si son del lado oscuro o del lado de la luz

for character, notes in decoded_responses.items():
    # Inicializamos la información del personaje
    afiliacion = 'Light Side' if 'Light Side' in notes['oracle_notes'] else 'Dark Side'
    
    # Añadimos la información al diccionario
    personajes_info[character] = {
        'afiliacion': afiliacion,
        'planeta': None  # Este campo se rellenará más adelante
    }

# Obtenemos el nombre del planeta de cada personaje
for personaje in personajes:
    homeworld_url = personaje['homeworld']
    response = requests.get(homeworld_url)
    
    if response.status_code == 200:
        homeworld_data = response.json()
        homeworld_name = homeworld_data['name']
        personajes_info[personaje['nombre']]['planeta'] = homeworld_name
    else:
        print(f"Error al obtener el planeta para {personaje}. Status code: {response.status_code}")

# Contamos cuantos personajes hay en cada planeta y sus afiliaciones

conteo_planetas_afiliacion = {}

for character, info in personajes_info.items():
    planeta = info['planeta']
    afiliacion = info['afiliacion']
    
    if planeta:
        # Inicializamos el diccionario para el planeta si no existe
        if planeta not in conteo_planetas_afiliacion:
            conteo_planetas_afiliacion[planeta] = {'Light Force': 0, 'Dark Force': 0}
        
        # Contamos las afiliaciones de los personajes por planeta
        if afiliacion == 'Light Side':
            conteo_planetas_afiliacion[planeta]['Light Force'] += 1
        elif afiliacion == 'Dark Side':
            conteo_planetas_afiliacion[planeta]['Dark Force'] += 1

# Diccionario para calcular el valor único (IBF) por planeta
resultado_ibf = {}

for planeta, conteo in conteo_planetas_afiliacion.items():
    light_force = conteo['Light Force']
    dark_force = conteo['Dark Force']
    
    # Calcular la resta de personajes Light Force y Dark Force
    diferencia = light_force - dark_force
    
    # Calcular el total de personajes en el planeta
    total_personajes_planeta = light_force + dark_force
    
    # Si el total de personajes es mayor que 0, calculamos el IBF
    if total_personajes_planeta > 0:
        ibf = diferencia / total_personajes_planeta
    else:
        ibf = 0  # Si no hay personajes, asignamos 0
    
    # Guardamos el valor del IBF para el planeta
    resultado_ibf[planeta] = ibf

# Funcion para postear el planeta con IBF = 0
def enviar_post(planeta):
    data = {"planet": planeta}
    # Realizamos la solicitud POST
    response = requests.post(url_post, json=data, headers=headers)
    
    if response.status_code == 200:
        print(f"Datos enviados exitosamente: {planeta}")
        print(response.json())
    else:
        print(f"Error al enviar los datos. Status code: {response.status_code}")

planeta_ibf_0 = None
for planeta, ibf in resultado_ibf.items():
    if ibf == 0:
        planeta_ibf_0 = planeta
        break  # Salir del bucle cuando encontramos el primer planeta con IBF = 0

if planeta_ibf_0:
    print(f"El planeta con IBF = 0 es: {planeta_ibf_0}")
    enviar_post(planeta_ibf_0)

