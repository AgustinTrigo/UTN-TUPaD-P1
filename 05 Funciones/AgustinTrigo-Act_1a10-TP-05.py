#Actividad 1
lista = list(range(0,101,4))
print(lista)

#Actividad 2

lista = ["A", "B", "C", "D", "E"]

print(lista)
print(f"Penultimo elemento: {lista[-2]}")


#Actividad 3

listaVacia = []

listaVacia.append("Hola")
listaVacia.append("Que")
listaVacia.append("Tal?")

print(listaVacia)


#Actividad 4

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#Actividad 5

""" 
Segun el codigo dado:

numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

Primero crea una variable "numeros" a la que se le asigna una lista de 5 elementos.
Luego llama al metodo "remove" y dentro de este utiliza la funcion "max" 
y le pasa como parametro la lista anteriormente creada.
El metodo remove quita de la lista el numero mas grande en este caso 22.
Y por ultimo imprime la lista la cual sería: [8,15,3,7]

"""

#Actividad 6

lista = list(range(10,31,5))
print(lista[0:2])

#Actividad 7

autos = ["sedan", "polo", "suran", "gol"] 
autos[1] = "golf"
autos[2] = "siroko"
print(autos)

#Actividad 8

dobles = []

for i in range(5,16,5):
    dobles.append(i*2)

print(dobles)

#Actividad 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

#Actividad 10

lista_anidada = [15,True,[25.5,57.9,30.6],False]
print(lista_anidada)