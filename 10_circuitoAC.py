import cmath

# Solicitar al usuario el tipo de circuito (serie o paralelo)
tipo_circuito = input("Elija el tipo de circuito (S para serie, P para paralelo): ")

# Solicitar los datos del usuario
Vrms = float(input("Valor RMS (Vrms): "))
f = float(input("Frecuencia en Hz (f): "))
R = float(input("Resistencia en Ohmios (R): "))
L = float(input("Inductancia en Henrios (L): "))
C = float(input("Capacitancia en Faradios (C): "))

# Calcular la impedancia en función del tipo de circuito
if tipo_circuito == "S" or tipo_circuito == "s":  # Circuito en serie
    Z_R = R
    Z_L = complex(0, 2 * cmath.pi * f * L)
    Z_C = 1 / (complex(0, 2 * cmath.pi * f * C))
    Z_total = Z_R + Z_L + Z_C
else:  # Circuito en paralelo
    Y_R = 1 / R
    Y_L = complex(0, -1 / (2 * cmath.pi * f * L))
    Y_C = 2j * cmath.pi * f * C
    Y_total = Y_R + Y_L + Y_C
    Z_total = 1 / Y_total

# Calcular la corriente total
I_total = Vrms / Z_total

# Calcular las potencias
S = Vrms *(I_total)
P = S.real
Q = S.imag
FP = P / abs(S)

# Mostrar los resultados
print(f"Impedancia Total (Z) = {abs(Z_total):.2f} Ohmios ∠ {cmath.phase(Z_total):.2f} radianes")
print(f"Corriente Total (I) = {abs(I_total):.2f} Amperios ∠ {cmath.phase(I_total):.2f} radianes")
print(f"Potencia Activa (P) = {P:.2f} Watts")
print(f"Potencia Aparente (S) = {abs(S):.2f} VA")
print(f"Potencia Reactiva (Q) = {Q:.2f} VAR")
print(f"Factor de Potencia (FP) = {FP:.2f}")
