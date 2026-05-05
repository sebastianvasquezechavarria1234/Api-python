import pytest
from src.services.triangulo_service import calcular_area, calcular_perimetro, calcular_triangulo

def test_calcular_area():
    assert calcular_area(10, 5) == 25.0
    assert calcular_area(7, 3) == 10.5

def test_calcular_perimetro():
    assert calcular_perimetro(3, 4, 5) == 12.0
    assert calcular_perimetro(10, 10, 10) == 30.0

def test_calcular_triangulo():
    area, perimetro = calcular_triangulo(10, 5, 10, 10)
    assert area == 25.0
    assert perimetro == 30.0

def test_triangle_logic_integration():
    # Test with standard values
    base, altura, l1, l2 = 3, 4, 4, 5
    area, perimetro = calcular_triangulo(base, altura, l1, l2)
    assert area == 6.0
    assert perimetro == 12.0
