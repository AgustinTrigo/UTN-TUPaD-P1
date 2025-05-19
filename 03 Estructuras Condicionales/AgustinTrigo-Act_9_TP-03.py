magnitud = int(input("De que magnitud es el terremoto?: "))

if magnitud < 3:
    print("Según la escala de Richter: Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Según la escala de Richter: Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Según la escala de Richter: Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Según la escala de Richter: Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Según la escala de Richter: Muy fuerte")
elif magnitud >= 7:
    print("Según la escala de Richter: Extremo")