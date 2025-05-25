import random
#Actividad 1:
print("Actividad 1:")
for i in range(0,101):
    print(i)

#Actividad 2:
print("Actividad 2:")
numero = input("Ingrese un numero entero: ")
print(f"Digitos: {len(numero)}\n")

#Actividad 3:
print("Actividad 3:")
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

acumulador = 0

for i in range(num1, num2+1):
    acumulador += i

print(f"Total acumulado entre ambos numeros: {acumulador}\n")

#Actividad 4:
print("Actividad 4:")
userInput = ""
acumulador = 0

while userInput != 0:
    userInput = int(input("Ingrese el numero a sumar o 0 para salir: "))
    acumulador += userInput

print(f"Total sumado: {acumulador}\n")

#Actividad 5:
print("Actividad 5:")

aleatorio = random.randint(0,9)
intentos = 0
respuesta = ""

while aleatorio != respuesta:
    intentos += 1
    respuesta = int(input("Intenta adivinar el numero entre 0 y 9: "))

print(f"Adivinaste! {aleatorio} = {respuesta} en {intentos} intentos.\n")

#Actividad 6:
print("Actividad 6:")
for i in range(0,100+1,2):
    print(i)


#Actividad 7:
print("Actividad 7:")
numero = int(input("Ingrese un numero: "))
acumulador = 0
if numero > 0:
    for i in range(0,numero+1):
        acumulador += i
    print(f"Total sumado: {acumulador}\n")
else:
    print("Debe ingresar un numero entero positivo.")

#Actividad 8:
print("Actividad 8:")
#Variable para crontolar el limite:
limite = 5
par = 0
impar = 0
positivo = 0
negativo = 0

for i in range(0, limite):
    userInput = int(input("Ingrese un numero: "))

    if(userInput > 0):
        positivo += 1
    elif(userInput < 0):
        negativo += 1
    
    if(userInput % 2 == 0):
        par += 1
    elif(userInput % 2 != 0):
        impar += 1

print(f"Resultados: \nPares: {par}\nImpares: {impar}\nPositivos: {positivo}\nNegativos {negativo}\n")

#Actividad 9:
print("Actividad 9:")
limite = 5
acumulador = 0


for i in range(0,limite):
    userInput = int(input("Ingrese un numero: "))
    acumulador += userInput

promedio = acumulador / limite

print(f"Promedio: {promedio}\n")

#Actividad 10:
print("Actividad 10:")
userInput = input("Ingrese un numero: ")
nuevoNum = ""

for i in range(len(userInput)-1,-1,-1):
    nuevoNum += userInput[i]

print(f"{userInput} -> {nuevoNum}")