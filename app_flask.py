from flask import Flask, request, jsonify
from predictor import predecir_estado

app = Flask(__name__)

@app.route('/predecir', methods=['POST'])
def predecir():
    data = request.get_json()

    temperatura = data.get('temperatura')
    frecuencia_cardiaca = data.get('frecuencia_cardiaca')
    nivel_dolor = data.get('nivel_dolor')

    resultado = predecir_estado(
        temperatura,
        frecuencia_cardiaca,
        nivel_dolor
    )

    return jsonify({
        'estado': resultado
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)