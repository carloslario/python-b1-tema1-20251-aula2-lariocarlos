'''
Enunciado:
Crea una función llamada "count_vowels(text_chain)" que reciba como parámetro
una cadena de texto de tipo string llamada 'text_chain' y retorne el número
de vocales, ya sean mayúsculas o minúsculas, sin tilde que se encuentren en dicha 
cadena de texto.

Parámetros:
- text_chain: Este parámetro admite únicamente strings.

Ejemplo: 
    Entrada:
    count_vowels('Hello world, this is an example.')

    Salida:
    9
'''

def count_vowels(text_chain:str):
    count = 0
    vowel_list = "AEIOUaeiou"
    for n in text_chain:
        if n in vowel_list:
            count += 1
    return count

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# la clave está en crear una lista auxiliar que tenga las vocales e ir comparandola con cada elemento del texto
print(count_vowels("Hello world, this is an example."))
