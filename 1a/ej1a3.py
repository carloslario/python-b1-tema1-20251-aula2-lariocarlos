'''
Enunciado:
Implementa una función llamada "invert_text(text_chain)" que reciba como
parámetro una cadena de texto de tipo string llamada 'text_chain' y devuelva
el texto invertido.

Parámetros:
- text_chain: Este parámetro solo admite strings.

Ejemplo:
    Entrada:
    invert_text('Hello world!')

    Salida:
    !dlrow olleH


'''

def invert_text(text_chain:str):
    return text_chain[::-1]

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# es sencillo utilizando las propiedades de slicing de cadenas de texto o listas
print(invert_text("Hello world!"))
