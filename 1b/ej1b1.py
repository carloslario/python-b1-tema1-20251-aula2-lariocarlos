"""
Enunciado:
Implementar la función 'obtain_max(list_numbers)' que recibe 
como parámetro una lista no vacía de números enteros y devuelve
el número mayor de la lista.

Recuerda que en Python existe la función llamada 'max'

Parámetros:
- list_numbers: Lista de números enteros

Ejemplo:
    Entrada:
    obtain_max([1, 45, 87, 21, 0, 23, 28])

    Salida:
    87
"""

def obtain_max(list_numbers):
    maximum = max(list_numbers)    
    return maximum

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
#la clave es la funcion max
print(obtain_max([1, 45, 87, 21, 0, 23, 28]))