# ¿ES UN ANAGRAMA?
#
#------------------------------------------------------------------
#
# Enunciado: Escribe una función que reciba dos palabras (String) 
# y retorne verdadero o falso (Boolean) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las 
# letras de otra palabra inicial.
#
# A) NO hace falta comprobar que ambas palabras existan.
# B) Dos palabras exactamente iguales no son anagrama.
#
#------------------------------------------------------------------

from collections import Counter

is_anagram = lambda w1, w2: Counter(w1.lower()) == Counter(w2.lower())

print(is_anagram("roma", "amor"))

#def is_anagram(w1, w2):
#### Convertir ambas palabras a minúsculas para hacer la comparación de forma insensible a mayúsculas y minúsculas
#    w1 = w1.lower()
#    w2 = w2.lower()
#   
#### Si las palabras tienen la misma longitud, son anagramas potenciales
#    if len(w1) != len(w2):
#        return False
#
#### Usar un diccionario para contar la frecuencia de cada letra en ambas palabras
#    letter_count = {}
#    for char in w1:
#        letter_count[char] = letter_count.get(char, 0) + 1
#    for char in w2:
#        letter_count[char] = letter_count.get(char, 0) - 1
#    
#### Si todas las frecuencias son cero, entonces las palabras son anagramas
#    return all(count == 0 for count in letter_count.values())