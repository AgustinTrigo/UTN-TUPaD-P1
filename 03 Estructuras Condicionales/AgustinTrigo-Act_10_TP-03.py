hemisferio = input("Indique \"N\" si se encuentra en el hemisferio norte o \"S\" en el hemisferio sur : ")
mes = int(input("Indique el mes en el que se encuentra: "))
dia = int(input("Y ahora el día: "))



if mes == 12 or mes <= 3:
    if mes == 12 and dia > 20:
        if(hemisferio == "N"):
            print("Invierno")
        elif(hemisferio == "S"):
            print("Verano")
    elif mes == 3 and dia <= 21:
        if(hemisferio == "N"):
            print("Invierno")
        elif(hemisferio == "S"):
            print("Verano")
    elif mes != 3 and mes != 12:
        if(hemisferio == "N"):
            print("Invierno")
        elif(hemisferio == "S"):
            print("Verano")

if mes == 3 or (mes > 3 and mes <= 6):
    if mes == 3 and dia > 20:
        if(hemisferio == "N"):
            print("Primavera")
        elif(hemisferio == "S"):
            print("Otoño")
    elif mes == 6 and dia <= 21:
        if(hemisferio == "N"):
            print("Primavera")
        elif(hemisferio == "S"):
            print("Otoño")
    elif mes != 3 and mes != 6:
        if(hemisferio == "N"):
            print("entro aca1")
            print("Primavera")
        elif(hemisferio == "S"):
            print("Otoño")

if mes == 6 or (mes > 6 and mes <= 9):
    if mes == 6 and dia > 20:
        if(hemisferio == "N"):
            print("Verano")
        elif(hemisferio == "S"):
            print("Invierno")
    elif mes == 9 and dia <= 21:
        if(hemisferio == "N"):
            print("Verano")
        elif(hemisferio == "S"):
            print("Invierno")
    elif mes != 6 and mes != 9:
        if(hemisferio == "N"):
            print("Verano")
        elif(hemisferio == "S"):
            print("Invierno")

if mes == 9 or (mes > 9 and mes <= 12):
    if mes == 9 and dia > 20:
        if(hemisferio == "N"):
            print("Otoño")
        elif(hemisferio == "S"):
            print("Primavera")
    elif mes == 12 and dia <= 21:
        if(hemisferio == "N"):
            print("Primavera")
        elif(hemisferio == "S"):
            print("Otoño")
    elif mes != 9 and mes != 12:
        if(hemisferio == "N"):
            print("Otoño")
        elif(hemisferio == "S"):
            print("Primavera")

        

