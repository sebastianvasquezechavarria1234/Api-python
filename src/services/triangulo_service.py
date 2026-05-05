# Funciones para calcular el área de un triágulo
def calcular_area(base: float, altura: float) -> float:
    return (base * altura) / 2

# Funciones para calcular el perímetro de un triángulo
def calcular_perimetro(base: float, lado1: float, lado2: float) -> float:
    return base + lado1 + lado2

# Funcion de alto nivel que utiliza las funciones anteriores
def calcular_triangulo(base: float, altura: float, lado1: float, lado2: float) -> tuple[float, float]:
    area = calcular_area(base, altura)
    perimetro = calcular_perimetro(base, lado1, lado2)
    return area, perimetro