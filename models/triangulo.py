# Funciones para calcular el área de un triágulo
def calcular_area(base, altura):
    return (base * altura) / 2

# Funciones para calcular el perímetro de un triángulo
def calcular_perimetro(base, lado1, lado2):
    return base + lado1 + lado2

# Funcion de alto nivel que utiliza las funciones anteriores
def calcular_triangulo(base, altura, lado1, lado2):
    area = calcular_area(base, altura)
    perimetro = calcular_perimetro(base, lado1, lado2)
    return area, perimetro