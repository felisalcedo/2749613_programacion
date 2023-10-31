import math

def calcular_area_cuadrado(lado):
    return lado ** 2

def calcular_area_triangulo(lado):
    return (math.sqrt(3) / 4) * lado ** 2

def calcular_area_pentagono(lado):
    apotema = lado / (2 * math.tan(math.pi / 5))
    return (5 * lado * apotema) / 2

def calcular_area_hexagono(lado):
    apotema = lado / (2 * math.tan(math.pi / 6))
    return (6 * lado * apotema) / 2

def calcular_area_circulo(lado):
    radio = lado
    return math.pi * radio ** 2

opciones = {
    1: calcular_area_cuadrado,
    2: calcular_area_triangulo,
    3: calcular_area_pentagono,
    4: calcular_area_hexagono,
    5: calcular_area_circulo
}

print("Seleccione una opción:")
print("1. Calcular el área de un cuadrado")
print("2. Calcular el área de un triángulo equilátero")
print("3. Calcular el área de un pentágono regular")
print("4. Calcular el área de un hexágono regular")
print("5. Calcular el área de un círculo (radio)")

opcion = int(input("Elija una opción (1-5): "))
lado = float(input("Ingrese el valor del lado o radio: "))

if opcion in opciones:
    area = opciones[opcion](lado)
    print(f"El área del polígono es: {area}")
else:
    print("Opción no válida. Se calculará el área como la de un círculo.")
    area = calcular_area_circulo(lado)
    print(f"El área del círculo es: {area}")
