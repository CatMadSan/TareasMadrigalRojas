import string
from test_funciones import *
for i in string.ascii_letters:  # string.ascii_letters es una constante
    # que contiene todos los caracteres ascii del abecedario
    print(i + " => " + string_work(i))  # Entonces, para cada uno,
    # lo imprime antes y despues de que se le aplique la string_work
assert string_work(99) == 187  # Comprueba código de error
#  Para error de tipo de entrada incorrecta
assert string_work("a@jd") == 923  # Comprueba código de error
# Para error de caracter no alfabético.

for i in range(0, 100):  # se hace un recorrido
    # de los números del 0 al 99
    print(num_to_str(i))  # se devuelve el nombre
    # de los números del 0 al 99
assert num_to_str("a") == 72  # Comprueba el código de error
# Para tipo de entrada incorrecta (string).
assert num_to_str(-1) == 46  # Comprueba el código de error
# Para entrada negativa.
assert num_to_str(100) == 46  # Comprueba el código de error
# Para entrada mayor que 99,
assert num_to_str(4.4) == 72  # Comprueba el código de error
# Para tipo de entrada incorrecta (decimal).
asdñlfjañsdlfjañlsdkjfñalskdjfñalksdjfñlakjsdf
