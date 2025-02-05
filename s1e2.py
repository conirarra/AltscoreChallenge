import requests

# URLs de la API
url_get = "https://makers-challenge.altscore.ai/v1/s1/e2/resources/stars"
url_post = "https://makers-challenge.altscore.ai/v1/s1/e2/solution"

# Clave de la API
headers = {
    'accept': 'application/json',
    'API-KEY': '64462b944b7e4d458009596b5bc5611e'
}

# Función para obtener las estrellas de una página específica
def obtener_estrellas(pagina):
    url = f"{url_get}?page={pagina}&sort-by=resonance&sort-direction=desc"

    # Note que habia más de una página para las estrellas, por lo que se tuvo que hacer un loop para obtener todas las estrellas

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener los datos de la página {pagina}: {response.status_code}")
        return None

# Función para calcular el promedio de resonancia de todas las estrellas
def calcular_promedio_resonancia():
    ids_vistos = set()  # Conjunto para asegurar que no repetimos IDs
    resonancias = []

    # Recorrer todas las páginas
    for pagina in range(1, 35): 
        data = obtener_estrellas(pagina)
        
        if data:
            for estrella in data:
                estrella_id = estrella['id']
                
                # Verificar si ya hemos visto esta estrella
                if estrella_id not in ids_vistos:
                    ids_vistos.add(estrella_id)
                    resonancias.append(estrella['resonance'])
        
    # Calcular el promedio de resonancia
    if resonancias:
        promedio = sum(resonancias) / len(resonancias)
        return promedio
    else:
        return 0

def enviar_resonancia_promedio(promedio):
    """Envía la resonancia promedio calculada a la API."""
    payload = {"average_resonance": str(int(promedio))}
    response = requests.post(url_post, json=payload, headers=headers)

    if response.status_code == 200:
        print("Resonancia promedio enviada correctamente:", response.text)
    else:
        print("Error al enviar la resonancia promedio:", response.status_code, response.text)

# Calcular el promedio
promedio_resonancia = calcular_promedio_resonancia()

# Postear el promedio
enviar_resonancia_promedio(promedio_resonancia)
