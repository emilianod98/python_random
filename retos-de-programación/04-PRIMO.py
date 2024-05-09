# ¿ES UN NÚMERO PRIMO?
#
#------------------------------------------------------------------
#
# Enunciado: Escribe un programa que se encargue de comprobar si un 
# número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.
#
#------------------------------------------------------------------
prime = lambda: [i for i in range(2, 101) if all(i % j != 0 for j in range(2, i))]
print(prime())
#------------------------------------------------------------------

# def isprime():
#    lista_isprime = []
#    for i in range(1, 101):
#        if i > 1:
#            for j in range(2, i):
#                if (i % j) == 0:
#                    break
#            else:
#                lista_isprime.append(i)
#    return lista_isprime

# print(isprime())