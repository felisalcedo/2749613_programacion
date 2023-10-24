#concepto de listas en python

print ("***************************************************************************************")

# Creación de una lista:

mi_lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
nombres = ("Luisa", "Luna", "Kevin" , "John")
mezcla = [1, "dos", True, 3.14]

print ("****************************************************************************************")


#Acceso a elementos de la lista:

primer_elemento = mi_lista[0]  # Acceder al primer elemento de la lista
ultimo_elemento = nombres[-1]  # Acceder al último elemento de la lista

print ("****************************************************************************************")


#Modificación de elementos de la lista:

mi_lista[1] = 6  # Cambiar el segundo elemento a 6
nombres.append("María")  # Agregar un nuevo nombre al final de la lista
mezcla.remove(True)  # Eliminar el valor True de la lista

print ("****************************************************************************************")


#Longitud de la lista:

longitud = len(mi_lista)  # Obtener la longitud de la lista

print ("*****************************************************************************************")


#Slicing (rebanado) de listas:

sublista = mi_lista[1:4]  # Obtener una sublista desde el índice 1 al 3

print ("*****************************************************************************************")


#Concatenación de listas:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_combinada = lista1 + lista2  # Concatenar dos listas

print ("*****************************************************************************************")


#Iteración a través de una lista:

for elemento in nombres:
    print(elemento)

print ("*****************************************************************************************")


#Verificación de la existencia de un elemento en la lista:

if "Luis" in nombres:
    print("Luis está en la lista de nombres.")

print ("*****************************************************************************************")


#Eliminación de elementos de la lista:

del mi_lista[2] # Eliminar el tercer elemento de la lista

print ("*****************************************************")