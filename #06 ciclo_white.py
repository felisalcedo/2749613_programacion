# Solicitar al usuario el valor de N
N = int(input("Ingrese un número finito de repeticiones (N): "))

# Solicitar al usuario un valor entero para aux1
aux1 = int(input("Ingrese un valor entero para aux1: "))

# Iniciar el ciclo while
contador = 0
while contador < N:
    valor = aux1 ** N
    print(f"Valor en la iteración {contador + 1}: {valor}")
    contador += 1
