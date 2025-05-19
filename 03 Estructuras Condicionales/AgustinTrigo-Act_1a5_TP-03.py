#Actividad 1:
edad = int(input("Ingresa tu edad: "))

if edad > 18:
    print("Es mayor de edad.")

#Actividad 2:
nota = int(input("Ingresa tu nota recibida: "))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado")

#Actividad 3:
numPar = int(input("Ingrese un numero par: "))

if numPar % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#Actividad 4:
edadUsuario = int(input("Ingrese su edad: "))

if edadUsuario < 12:
    print("Niño/a")
elif edadUsuario >= 12 and edadUsuario < 18:
    print("Adolecente")
elif edadUsuario >= 18 and edadUsuario < 30:
    print("Adulto/a joven")
elif edadUsuario >= 30:
    print("Adulto/a mayor")


#Actividad 5:
contraseña = input("Ingrese una contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


