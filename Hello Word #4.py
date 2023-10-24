#solicitar el valor de la tension Y la resistencia al usuario
Tension_voltios = float(input("ingrese el valor de la tension en voltios (V): "))
Resistencia_Ohmios = float(input("ingrese el valor de la resistencia en ohmios (Ohm) :" ))

#calcular la corriente utlizando la ley de ohm: I = V / R
corriente_amperios = Tension_voltios / Resistencia_Ohmios 

#mostrar el resultado en el formato requerido 
print("Al conectar un resistor de" ,Resistencia_Ohmios , " Ohm a una fuente de" , Tension_voltios," V , circular una corriente de" ,corriente_amperios, "A.")
