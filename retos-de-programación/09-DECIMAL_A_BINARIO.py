# DECIMAL A BINARIO
#
#------------------------------------------------------------------
#
# Crea un programa se encargue de transformar un número
# decimal a binario sin utilizar funciones propias del lenguaje que 
# lo hagan directamente.
#
#------------------------------------------------------------------

def decimal_a_binario(num):
    binario = ""
    while num > 0:
        if num % 2 == 0:
            binario = "0" + binario
        else:
            binario = "1" + binario
        num = num // 2  # Decrementar el valor de num dividiéndolo por 2
    return binario

# Ahora llamamos a la función y luego imprimimos el resultado
resultado = decimal_a_binario(44)
print(resultado)