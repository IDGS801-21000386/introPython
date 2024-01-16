"""
DICCIONARIOS
"""

miDiccionario = {"Matricula": 21000386, "Nombre": "Erick", "Apellidos": "Rivera Chagoya"}
print(miDiccionario)
print(miDiccionario["Nombre"]) # IMPRIME EL OBJETO NOMBRE
print(type(miDiccionario)) # IDENTIFICA EL TIPO DE DATO DE LA VARIABLE

miDiccionario["Nombre"] = "Saul"
print(miDiccionario)

miDiccionario["correo"] = "saul@gmail.com"
print(miDiccionario)