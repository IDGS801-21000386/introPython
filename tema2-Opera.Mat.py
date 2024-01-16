""" OPERADOR MATH """

num1 = 20
num2 = 4
print("La suma es: ", (num1 + num2))
print("La resta es: ", (num1 - num2))
print("La multiplicacion es: ", (num1 * num2))
print("La division es: ", (num1 / num2))
print("La division exacta  es: ", (num1 // num2)) # No regresa decimales
print("La potencia es: ", (num1 ** num2)) 

# Concatenacion en python
texto1 = "Hola"
texto2 = "Mundo"
textoFinal = texto1 + " " + texto2
# textoFinal = f"{texto1} {texto2}"
print(textoFinal)
print(f"{texto1} {texto2}")

print("El saludo es: %s %s" %(texto1, "texto2")) # Sustituye los valores del %s por las variables
saludoFinal = "Saludo {} {}".format(texto1, texto2) # Remplasa los {} por las variables
print(saludoFinal)

saludoFinal2 = "Saludo 2: {y} {x}".format(x = texto1, y = texto2) # Remplasa los {} por las variables
print(saludoFinal2)
