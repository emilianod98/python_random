# ASPECT RATIO DE UNA IMAGEN.
#
#------------------------------------------------------------------
#
# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
# 
#------------------------------------------------------------------

def invertir_palabras():
    palabra = input("Introduce una palabra o frase: ")
    palabra_invertida = ""
    for i in range(palabra):
        palabra_invertida += palabra[-i-1]
        print(palabra_invertida)

print(invertir_palabras())