# ÁREA DE UN POLÍGONO
#
#------------------------------------------------------------------
#
# Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) 
# que sea capaz de calcular y retornar el área de un polígono.
# A) La función recibirá por parámetro sólo UN polígono a la vez.
# B) Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# C) Imprime el cálculo del área de un polígono de cada tipo.
#
#------------------------------------------------------------------
triangulo = lambda a, b : a * b / 2
cuadrado = lambda a : a * a
rectangulo = lambda a, b : a * b
#------------------------------------------------------------------

def calcular_area_poligono(poligono):
    if isinstance(poligono, tuple):
        tipo = poligono[0]
        if tipo == 'Triangulo':
            area = lambda a, b: a * b / 2
            print(f"El área del triángulo es: {area(*poligono[1:])}")
        elif tipo == 'Cuadrado':
            area = lambda a: a * a
            print(f"El área del cuadrado es: {area(poligono[1])}")
        elif tipo == 'Rectangulo':
            area = lambda a, b: a * b
            print(f"El área del rectángulo es: {area(*poligono[1:])}")
        else:
            print("Tipo de polígono no soportado")
    else:
        print("Formato de polígono no válido")

# Ejemplo de uso:
calcular_area_poligono(('Triangulo', 5, 3))
calcular_area_poligono(('Cuadrado', 4))
calcular_area_poligono(('Rectangulo', 6, 2))
