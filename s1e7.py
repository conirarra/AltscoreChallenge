import requests
from flask import Flask, jsonify, make_response
import random

# URLs de la API
url_post = "https://makers-challenge.altscore.ai/v1/s1/e7/solution"

# Clave de la API
headers = {
    'accept': 'application/json',
    'API-KEY': '64462b944b7e4d458009596b5bc5611e'
}

# Abrimos una pagina web
app = Flask(__name__)

# Tabla de códigos de reparación por sistema
repair_codes = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Primera llamada
@app.route('/status', methods=['GET'])
def status():
    # Definir los sistemas posibles y elegir uno aleatoriamente para simular un daño
    systems = ["navigation", "communications", "life_support", "engines", "deflector_shield"]
    damaged_system = random.choice(systems)
    return jsonify({"damaged_system": damaged_system})

@app.route('/repair-bay', methods=['GET'])
def repair_bay():
    # Obtener el sistema dañado, este debe estar presente en una variable global o en algún estado
    # Por simplificación, simula un sistema dañado ya que GET /status se ejecuta aleatoriamente
    damaged_system = "engines"  # Este valor se puede modificar según la lógica o el estado compartido
    
    if damaged_system not in repair_codes:
        return jsonify({"error": "Invalid system"}), 400
    
    repair_code = repair_codes[damaged_system]
    
    # Generar una página HTML con el código de reparación
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">{repair_code}</div>
    </body>
    </html>
    '''
    return make_response(html_content, 200)

@app.route('/teapot', methods=['POST'])
def teapot():
    # Simular la respuesta de teapot (418 I'm a teapot)
    return make_response("I'm a teapot", 418)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
