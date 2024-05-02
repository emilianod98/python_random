### CHALLENGERS ###

'''
EL FAMOSO "FIZZ BUZZ":

Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de linea entre cada impresión, subtituyendo los siguientes:
- Multiplos de 3 por la palabra "fizz".
- Multiplos de 5 por la palabra "buzz".
- Multiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz()



'''
¿ES UN ANAGRAMA?

Escribe una función que reciba dos palabtas (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
'''

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())
    
print(is_anagram("Amor", "Roma"))



'''
LA SUCESIÓN DE FIBONACCI

Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
- 0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci():
    prev = 0
    curr = 1
    for i in range(1, 51):
        print(i)
        print(prev)
        fib = prev + curr
        prev = curr
        curr = fib

fibonacci()



'''
¿ES UN NÚMERO PRIMO?

Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''

def is_prime():
    for num in range(1, 101):

        if num >= 2:
            is_divisible = False
            for i in range(2, num):
                if num % i == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(num)

print(is_prime())



'''
TEXTO INVERTIDO

Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguajes ¿Que lo hagan de forma automática.

Ejemplo:
    Entrada: Dracula
    Salida: Alucard
'''

def alberre(texto):
    tex_alberre = ""
    for i in range(len(texto)):
        tex_alberre += texto[len(texto) - 1 - i]
    print(tex_alberre)

alberre("alucard")