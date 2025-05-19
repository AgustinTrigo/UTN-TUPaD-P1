nombre = input("Ingresa tu nombre: ")
opcion = int(input("Ingresa la opcion: \n1) Nombre en mayuscula \n2) Nombre en minúsculas \n3) Primera letra en mayúscula : "))

if opcion == 1:
    print(str.upper(nombre))
elif opcion == 2:
    print(str.lower(nombre))
elif opcion == 3:
    print(str.title(nombre))
else:
    print("Indique una opcion.")