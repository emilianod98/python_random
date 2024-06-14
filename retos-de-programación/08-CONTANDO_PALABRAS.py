# Contando Palabras
#------------------------------------------------------------------
#
# Crea un programa que cuente cuantas veces se repite cada palabra
# y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que
#   lo resuelvan automáticamente.
#
#------------------------------------------------------------------

def contador_palabras(texto):
    texto = texto.lower()
    # Corrigiendo la variable 'palabra' a 'texto' para asegurar que se limpie el texto original
    texto = ''.join(e for e in texto if e.isalnum() or e.isspace())
    texto = texto.split()
    contador = {}
    for palabra in texto:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador

texto = "Si no puedes volar, corre; si no puedes correr, camina; si no puedes caminar, gatea, pero sigue avanzando hacia tu meta"
print(contador_palabras(texto))
