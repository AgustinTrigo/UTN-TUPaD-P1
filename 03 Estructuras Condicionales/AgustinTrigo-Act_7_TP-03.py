#Actividad 7
cadena = input("Ingrese una palabra o frase: ")
ultimaLetra = cadena[len(cadena)-1]
vocales = ["a", "e", "i", "o", "u"]
coincidencia = False

for i in vocales:
    if ultimaLetra == i:
        print(f"{cadena}!")
        coincidencia = True
        break

if not coincidencia:
    print(cadena)


""" if ultimaLetra == "a" or ultimaLetra == "e" or ultimaLetra == "i" or ultimaLetra == "o" or ultimaLetra == "u":
    print(f"{cadena}!")
else:
    print(cadena)
       """