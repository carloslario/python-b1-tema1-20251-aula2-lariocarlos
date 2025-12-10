"""
Enunciado:
Utilizando la librería 'math', implementa una función llamada 
'calculate_angle(angle)'  que reciba como parámetro un número 
correspondiente a un ángulo en grados llamado 'angle' y retorne
como resultado el seno de dicho ángulo redondeado a 2 decimales.

Encontrarás la documentación de la librería 'math' en el 
siguiente enlace: https://docs.python.org/3/library/math.html

En concreto, la función 'sin(x)' de la librería 'math' la 
puedes encontrar en el siguiente enlace:
https://docs.python.org/3/library/math.html#math.sin

Y la función 'radians(x)' de la librería 'math' la puedes
encontrar en el siguiente enlace:
https://docs.python.org/3/library/math.html#math.radians
(te servirá para convertir los grados a radianes)

Recuerda que puedes redondear decimales con la función 
'round(x, n)'


Parámetros:
- angle: Entero correspondiente al valor de un ángulo.

Ejemplo:
    Entrada:
    calculate_angle(270)

    Salida:
    -1
"""

from math import sin, radians

def calculate_angle(angle):
    return sin(radians(angle))

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
#la clavbe es importar la funciones directamente para evitar escribir siempre la libreria de origen (math)
print(calculate_angle(270))
