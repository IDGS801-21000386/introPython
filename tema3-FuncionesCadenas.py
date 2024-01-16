""" FUNCIONES CADENAS """

texto = "Universidad Tecnologica de Leon"
print(texto.upper()) # Pone en mayusculas la cadena
print(texto.lower()) # Pone en minusculas la cadena
print(texto.title()) # Pone mayus en cada palabra de la cadena
print(texto.find("de")) # Busca en la cadena "de"
print(texto.count("e")) # Cuenta las "e" que hay en la cadena

textoNuevo = texto.replace("e", "3") # Remplaza las letras "e" por "3"
print(textoNuevo)