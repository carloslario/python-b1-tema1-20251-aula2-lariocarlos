'''
Enunciado:
Crea una función 'sum_odd_numbers(list_numbers)' que reciba como 
parámetro una lista de números positivos enteros llamada 'list_numbers'
y devuelva la suma de los números impares encontrados en la lista.
Considerar que 'list_numbers' debe contener valores numéricos enteros mayores
o iguales a '0', en caso contrario se debe mostrar un error tipo 'ValueError'.

El error lo puedes mostrar con la siguiente instrucción:    
raise ValueError("MENSAJE DE ERROR")

Parámetros:
- list_numbers: Lista de números enteros positivos.

Ejemplo:
    Entrada:
    sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

    Salida:
    30

'''

def sum_odd_numbers(list_numbers):
    sum=0
    for n in list_numbers:
        if not isinstance(n, int):
            raise ValueError("Number in list must be integer.")
        elif n < 0:
            raise ValueError("Number must be greater or equal than 0.")
        if n%2 != 0:
            sum +=n
    return sum

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# se trata de sumar los numeros impares revisando que no haya problemas 
print(sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100]))
