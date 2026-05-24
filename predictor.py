def predecir_estado(temperatura, frecuencia_cardiaca, nivel_dolor):

    if temperatura <37 and frecuencia_cardiaca <90 and nivel_dolor<=2:
        return "NO ENFERMO"

    elif temperatura <38 and frecuencia_cardiaca <100 and nivel_dolor<=5:
        return "ENFERMEDAD LEVE"

    elif (
        temperatura >=38 and temperatura <41
        and frecuencia_cardiaca >=100 and frecuencia_cardiaca <140
        and nivel_dolor >=6 and nivel_dolor <9
    ):
        return "ENFERMEDAD AGUDA"

    elif temperatura >=41 and frecuencia_cardiaca >=140 and nivel_dolor >=9:
        return "ENFERMEDAD TERMINAL"

    else:
        return "ENFERMEDAD CRÓNICA"