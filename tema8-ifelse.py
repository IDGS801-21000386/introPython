"""
OPERADORES IF ELSE
"""

print("Suma de numeros")
num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
# print(f"La suma es: {num1 + num2}")
print("La suma {} + {} = {}".format(num1, num2, num1 + num2))

if num1 > num2:
    print("El num1: {} es mayor que num2: {}".format(num1,num2))
else:
    print("El num1: {} es menor que num2: {}".format(num1,num2))    

print("<--------------- PEDIR UNA EDAD ---------------------->")
edad = int(input("Ingresa tu edad: "))

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    