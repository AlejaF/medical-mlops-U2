import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from predictor import predecir_estado
import pytest


def test_enfermedad_terminal():

    resultado = predecir_estado(
        42,
        142,
        10
    )

    assert resultado == "ENFERMEDAD TERMINAL"


@pytest.mark.parametrize(
    "temperatura,frecuencia,nivel,esperado",
    [

        (36,80,1,"NO ENFERMO"),

        (37.5,95,4,"ENFERMEDAD LEVE"),

        (39,110,8,"ENFERMEDAD AGUDA"),

        (38.5,90,3,"ENFERMEDAD CRÓNICA"),

        (42,142,10,"ENFERMEDAD TERMINAL")

    ]
)
def test_todas_las_categorias(
    temperatura,
    frecuencia,
    nivel,
    esperado
):

    resultado = predecir_estado(
        temperatura,
        frecuencia,
        nivel
    )

    assert resultado == esperado