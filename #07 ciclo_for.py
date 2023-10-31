# Solicitar al usuario el valor de N
N = int(input("Ingrese un número finito de repeticiones (N): "))

# Solicitar al usuario un valor entero para aux1
aux1 = int(input("Ingrese un valor entero para aux1: "))

# Usar un ciclo for para realizar la operación y mostrar el resultado
for i in range(N):
    valor = aux1 ** N
    print(f"Valor en la iteración {i + 1}: {valor}")
