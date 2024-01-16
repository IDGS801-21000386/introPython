""" 
UNA LISTA  ES UNA SECUENCIA DE ELEMENTOS.
SE CREA CON CORCHETES [] 
ES INMUTABLE
"""

# Se pueden usar diferentes tipos de dato
lista1 = ["Erick", 33, 9.5, True, "German", 20.3]
print(lista1)
print(lista1[:]) # IMPRIME TODA LA LISTA
print(lista1[2]) # IMPRIME EL INDICE 2 DE LA LISTA
print(lista1[-1]) # IMPRIME EL -1
print(lista1[0:3]) # IMPRIME DEL INDICE 0 AL 3 (0-1-2) 
print(lista1[3:]) # IMPRIME DEL INDICE 3 HASTA EL FINAL

print("SE AÑARIO VARGAS")
lista1.append("Vargas") # AÑADE AL FINAL A "VARGAS"
print(lista1)

print("INSERT 2 Y NADIA")
lista1.insert(2, "Nadia") # EN EL INDICE 2 PONE A NADIA
print(lista1)

print("EXTEND")
lista1.extend(["uno", 1.1, False]) # AGREGA MAS DE UN VALOR A LA LISTA
print(lista1)

print("REMOVE")
lista1.remove("German") # REMUEVE LO QUE COINCIDA EN LA LISTA
print(lista1)

print("POP")
lista1.pop() # Extrae el ultimo elemento de la lista
print(lista1)

lista2 = ["tres", "cuatro"]
lista3 = lista1 + lista2
print(lista3)
print(lista2 * 4)

lista4 = [2, 1, 5, 4, 3]
print(lista4)

lista4.sort()
print(lista4) # ORDENA ALFABETICAMENTE

del lista4[0] # ELIMINA EL ELEMENTO EN EL INDICE 0
print(lista4)
