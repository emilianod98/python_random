# El Famoso "FIZZ BUZZ"
#------------------------------------------------------------------
#
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# Múltiplos de 3 por la palabra "fizz".
# Múltiplos de 5 por la palabra "buzz".
# Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#
#-------------------------------------------------------------------
fizz_buzz = lambda x: "FIZZBUZZ" if x % 3 == 0 and x % 5 == 0 else "Fizz" if x % 3 == 0 else "BUZZ" if x % 5 == 0 else x
result = list(map(fizz_buzz, range(1, 101)))

print(result)