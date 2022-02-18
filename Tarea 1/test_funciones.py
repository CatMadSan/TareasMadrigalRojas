# Instituto Tecnologico de Costa Rica
# Por Fabricio Rojas y Catalina Madrigal
# Última modificación: 18 de febrero de 2022, 16:33

# Definicion de funcion string_work
# entrada esperada --> variable tipo str
# salida --> variable tipo str
# error si entrada no es del tipo esperado --> AssertionError: 187
# error si entrada presenta un caracter no perteneciente
# al alfabeto --> AssertionError: 923
# Note que el llamado de esta función requiere
# de la libreria string

def string_work(texto):
    assert type(texto) == str, 187  # Se verifica que el input es tipo str
    assert texto.isalpha(), 923  # Se verifica que el input tiene solo
    # caracteres pertenecientes al abecedario
    textoNuevo = texto.swapcase()  # Realiza el cambio de MÁY a min y viceversa
    return textoNuevo


def num_to_str(x):  # La función recibe un número entre 0 y 99
    assert type(x) == int, "13"  # La función valida que el tipo de variable
    # sea un número. Si no lo es, devuelve el código de error "13".
    assert x >= 0, "15"  # La función valida que sea un número positivo.
    # Si no lo es, devuelve el código de error "15".
    assert x <= 99, "18"  # La función valida que sea un número menor a 99.
    # Si no lo es, devuelve el código de error "18".
    unidades = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco",
                6: "seis", 7: "siete", 8: "ocho", 9: "nueve"}
    # Se crea un diccionario con las unidades.
    decimales = {0: "cero_", 1: "dieci", 2: "veinti", 3: "treinta_y_",
                 4: "cuarenta_y_", 5: "cincuenta_y_", 6: "sesenta_y_",
                 7: "setenta_y_", 8: "ochenta_y_", 9: "noventa_y_"}
    # Se crea un diccionario con las decenas.
    especiales = {0: "cero", 10: "diez", 11: "once", 12: "doce", 13: "trece",
                  14: "catorce", 15: "quince", 20: "veinte", 30: "treinta",
                  40: "cuarenta", 50: "cincuenta", 60: "sesenta",
                  70: "setenta", 80: "ochenta", 90: "noventa"}
    # Se crea un diccionario con los números especiales.
    num = especiales.get(x)
    if num:  # La función valida si el número está
        # en el diccionario de números especiales.
        return especiales[x]  # Si está en el diccionario de
        # números especiales, devuelve el nombre del número en ese diccionario.
    else:  # Si no está en el diccionario de números especiales,devuelve
        # la concatenación del nombre de las decenas
        # con el nombre de las unidades.
        uni = x % 10
        dec = x//10
        return decimales[dec]+unidades[uni]
    if type(x) == int:
        if 0 <= x <= 99:
            unidades = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco",
                        6: "seis", 7: "siete", 8: "ocho", 9: "nueve"}
            # Se crea un diccionario con las unidades.
            decimales = {0: "cero_", 1: "dieci", 2: "veinti", 3: "treinta_y_",
                         4: "cuarenta_y_", 5: "cincuenta_y_", 6: "sesenta_y_",
                         7: "setenta_y_", 8: "ochenta_y_", 9: "noventa_y_"}
            # Se crea un diccionario con las decenas.
            especiales = {0: "cero", 10: "diez", 11: "once", 12: "doce",
                          13: "trece", 14: "catorce", 15: "quince",
                          20: "veinte", 30: "treinta", 40: "cuarenta",
                          50: "cincuenta", 60: "sesenta", 70: "setenta",
                          80: "ochenta", 90: "noventa"}
            # Se crea un diccionario con los números especiales.
            num = especiales.get(x)
            if num:  # La función valida si el número está
                # en el diccionario de números especiales.
                return especiales[x]  # Si está en el diccionario de
                # números especiales, devuelve el nombre
                # del número en ese diccionario.
            else:  # Si no está en el diccionario de números especiales,
                # devuelve la concatenación del nombre de las decenas
                # con el nombre de las unidades.
                uni = x % 10
                dec = x//10
                return decimales[dec]+unidades[uni]
        else:
            return 46
            # código de error para números negativos
            # o mayores que 99
    else:
        return 72
        # código de error para datos distintos
        # a un número entero
