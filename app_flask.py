import json
from datetime import datetime
from flask import Flask, request, jsonify
from predictor import predecir_estado
from collections import Counter

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

    # Guardar historial
    registro = {

        "fecha": str(datetime.now()),
        "estado": resultado

    }

    with open(
        "historial.txt",
        "a"
    ) as f:

        f.write(
            json.dumps(registro) + "\n"
        )

    return jsonify({

        'estado': resultado

    })


@app.route('/reporte', methods=['GET'])
def reporte():

    try:

        with open(
            "historial.txt",
            "r"
        ) as f:

            lineas=f.readlines()

        datos=[]

        for linea in lineas:

            linea=linea.strip()

            if linea:

                datos.append(
                    json.loads(linea)
                )

    except FileNotFoundError:

        datos=[]

    categorias=[

        x["estado"]

        for x in datos

    ]

    conteo=Counter(categorias)

    ultimas=datos[-5:]

    ultima_fecha=(

        datos[-1]["fecha"]

        if datos

        else "Sin datos"

    )

    return jsonify({

        "total_por_categoria":dict(conteo),

        "ultimas_5_predicciones":ultimas,

        "fecha_ultima_prediccion":ultima_fecha

    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)