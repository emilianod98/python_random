# LA SUCESIÓN DE FIBONACCI
#
#------------------------------------------------------------------
#
# Enunciado: Escribe un programa que imprima los 50 primeros números 
# de la sucesión de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en la que 
# el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...
#
#------------------------------------------------------------------
fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

n = 1
while fibonacci(n) <= 50:
    print(fibonacci(n))
    n += 1
#------------------------------------------------------------------
# def fibonacci():
#    y = 0
#    z = 1
#    for x in range(1,51):
#        x = y + z
#        print(x)
#        y = z
#        z = x
#
# fibonacci()