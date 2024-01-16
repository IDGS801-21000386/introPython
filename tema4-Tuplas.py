""" LAS TUPLAS SON INMUTABLES"""

# UNA VEZ CREADA LA TUPLA NO SE PUEDE MODIFICA

tupla = ("uno", "dos", "tres")
print(tupla)

tuplasVariosDatos = (12, True, 23.5, "El gato", 12 + 4)
print(tuplasVariosDatos)

tuplasConTuplas = (1, 2, 3, 4, (1, 2, 3))
print(tuplasConTuplas)

print(tuplasVariosDatos[3])
print(tuplasVariosDatos[-2])
print(tuplasVariosDatos[0:2])

a,b,c = tupla
print(a)
print(b)
print(c)

tuplaNueva = tupla + tuplasVariosDatos
print("TUPLA NUEVA")
print(tuplaNueva)
