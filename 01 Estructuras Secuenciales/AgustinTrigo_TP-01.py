#Actividad 1:
print("Hola Mundo!")

#Actividad 2:
nombre = input("Por favor ingresa tu nombre: ")
print(f"Hola {nombre}!")

#Actividad 3:
nombre = input("Por favor ingresa tu nombre: ")
apellido = input("Ahora ingresa tu apellido: ")
edad = input("Que edad tenes?: ")
residencia = input("Cual es tu lugar de residencia?: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Actividad 4:
radio = int(input("Por favor ingrese el radio del circulo: "))
pi = 3.14159
diametro = radio * 2
area = pi * radio ** 2
perimetro = pi * diametro

print(f"Si el radio del circulo es: {radio}. El area es: {area}, y el perimetro: {perimetro}.")

#Actividad 5:

segundos = int(input("Por favor escriba la cantidad de segundos que quieras convertir a horas: "))
horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas} horas.")

#Actividad 6
numero = int(input("Por favor ingrese un numero para mostrar su tabla: "))

print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#Actividad 7
numA = int(input("Ingrese un numero entero distinto de 0: "))
numB = int(input("Ingrese otro numero distinto de 0: "))

print(f"Suma: {numA} + {numB} = {numA + numB}")
print(f"Resta: {numA} - {numB} = {numA - numB}")
print(f"Multiplicación: {numA} * {numB} = {numA * numB}")
print(f"División: {numA} / {numB} = {numA / numB}")

#Actividad 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso: "))

imc = peso / (altura ** 2)

print(f"Su indice de masa corporal (IMC) es el siguiente: {imc}.")

#Actividad 9
celsius = int(input("ingresa la temperatura en grados celcius: "))
fahrenheit = ((9/5) * celsius) + 32

print(f"El equivalente de {celsius} grados celcius en grados Fahrenheit es: {fahrenheit}")

#Actividad 10
numA = int(input("Por favor ingrese un numero: "))
numB = int(input("Por favor otro numero: "))
numC = int(input("Por favor otro numero "))

promedio = (numA + numB + numC) / 3

print(f"Promedio: {promedio}")

