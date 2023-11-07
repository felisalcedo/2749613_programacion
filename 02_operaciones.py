#Primer programa que escribes en un nuevo lenguaje 
print ("**********************************************************************************************") 
print ("Hello, Word!")

#Comentario 
print ("El texto en pantalla sirve de interacion con el usuario de un programa") 
print ("Es presindible, sin embargo una adecuada interfraz permite claridad en la")
print ("Ejecucion")





print ("*************************************************************************************************************************")



#Autores
print ("Autores : Sixto Felipe Salcedo Melo")
print ("Luna Gisell Puentes Montengro")
print ("# de Ficha : 2749613")
print ("18 de octubre del 2023") 
print ("Diseño e integracion de automastismos mecatronicos") 

print ("*************************************************************************************************************************")
#operaciones numericas

a = int (input("numero1 "))
b = int (input ("numero2 "))

suma = a+b
resta = a-b
multiplicacion = a*b
division = a/b
modulo = a%b
potencia = a**b


#operaciones booleanas 
booleano1 = True
booleano2 = False


and_result = booleano1 and booleano2
or_result = booleano1 or booleano2
not_result = not booleano1



#mostrar los resultados 
print("operaciones numericas:")
print("suma:", a, "+", b , "=", suma)
print("resta:", a , "-", b , "=", resta)
print("multiplicacion:", a , "*", b , "=", multiplicacion)
print("division:", a, "/" , b , "=", division)
print("modulo:", a , "%", b , "=", modulo)
print("potencia:", a , "**", b , "=", potencia)


print("\nOperaciones booleanas:")
print("AND:", booleano1,"AND", booleano2, "=", and_result)
print("OR:", booleano1,"OR", booleano2, "=", or_result)
print("NOT:", "NOT", booleano1, "=", not_result)
