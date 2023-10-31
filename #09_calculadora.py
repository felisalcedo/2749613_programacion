# Solicitar al usuario los valores de A y B
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))

# Menú de selección
print("Seleccione una operación:")
print("1. Suma (A + B)")
print("2. Resta (A - B)")
print("3. Multiplicación (A * B)")
print("4. División (A / B)")
print("5. Potencia (A^B)")
print("6. Raiz (A^(1/B))")
print("7. Suma de potencias (A^B + B^A)")
print("8. Promedio ((A + B) / 2)")
print("9. Comparación entre A y B")

opcion = int(input("Elija una opción (1-9): "))

# Realizar la operación seleccionada
if opcion == 1:
    resultado = A + B
elif opcion == 2:
    resultado = A - B
elif opcion == 3:
    resultado = A * B
elif opcion == 4:
    resultado = A / B
elif opcion == 5:
    resultado = A ** B
elif opcion == 6:
    resultado = A ** (1/B)
elif opcion == 7:
    resultado = A ** B + B ** A
elif opcion == 8:
    resultado = (A + B) / 2
elif opcion == 9:
    if A == B:
        resultado = "A y B son iguales."
    elif A > B:
        resultado = "A es mayor que B."
    else:
        resultado = "B es mayor que A."
else:
    resultado = "Opción no válida."

# Mostrar el resultado
print(f"Resultado: {resultado}")
