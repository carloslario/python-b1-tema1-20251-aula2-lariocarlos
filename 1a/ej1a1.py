'''
Enunciado:
Implementa la función 'fibonacci(fibonacci_number)' que contenga el algoritmo
de Fibonacci y reciba como parámetro un valor numérico entero llamado 
'fibonacci_number'  y devuelva el valor de la serie Fibonacci en esa posición.
Asimismo, si el valor no es numérico, o es menor a cero, se debe lanzar 
una excepción ValueError("mensaje"), la cual puede incluir un mensaje que debería 
corresponder con el tipo de error durante la validación.

Parámetros:
- fibonacci_number: Número entero positivo mayor a 0 que representa la
posición en la serie Fibonacci.

Ejemplo:
    Entrada:
    fibonacci(10)

    Salida:
    55
'''

def fibonacci(fibonacci_number):
    if not isinstance(fibonacci_number, int):
        raise ValueError("Number must be integer.")
    elif fibonacci_number < 0:
        raise ValueError("Number must be greater than 0.")
    else:
        a, b = 0, 1
    for i in range(fibonacci_number):
        a, b = b, a + b
    return a

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
#este codigo devuelve la operacion de fibonacci de la posicion indicada
# la cadena de fibonacci consiste en suma 0+1= 1 ; 1+1=2 ; 2+3=5 ; 3+5=8 ; 5+8=13 ; 8+13 = 21  
print(fibonacci(8))
