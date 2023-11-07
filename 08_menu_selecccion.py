def calcular_area_poligono(lado, lados ):
    pi = 3.1416
    area = 0
    if lados==1 or lados==2:
        print("error...")
    elif lados == 3:  # Triángulo equilátero
        area = (lado * 2 * (3 ** 0.5)) / 4
    elif lados == 4:  # Cuadrado
        area = lado ** 2
    elif lados == 5:  # Pentágono
        apotema = lado / (2 * (5 ** 0.5))
        area = (5 * lado * apotema) / 2
    elif lados == 6:  # Hexágono
        area = (3 * (3 * 0.5) * (lado * 2)) / 2
    elif lados == 8:  # Octágono
        apotema = lado / (2 * (2 ** 0.5))
        area = 8 * lado * apotema / 2
    else:  # Default: Círculo
        area = pi * (lado ** 2)
    
    return area

while True:
    print("Escriba el numero de lados del poligono:")
    print("1. Calcular el area de un triángulo equilátero")
    print("2. Calcular el area de un cuadrado")
    print("3. Calcular el area de un pentágono")
    print("4. Calcular el area de un hexágono")
    print("5. Calcular el area de un octágono")
    print("6. Calcular el area de un círculo")
    print("7. Salir")
    
    opcion = int(input("Elija una opción: "))

    if opcion == 7:
        print("ciao:)""*********************************************************")
        break

    lado = float(input("Ingrese la longitud del lado (o radio en caso de círculo): "))
    
    area = calcular_area_poligono(lado, opcion)
    
    print(f"El área del polígono es: {area}""******************************")