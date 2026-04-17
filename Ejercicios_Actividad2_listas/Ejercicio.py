
'''
lista = []

# Crear un programa para llenar esa lista con 10 datos diferentes
for caracter in range(1,11):
    caracter = input("Agrega algo: ")
    lista.append(caracter)
    print(lista)

lista = []
caracter = 1

# Crear un programa para llenar esa lista con 3 datos diferentes
for i in range(1,4):
    lista.append(caracter)
    i += 1
    caracter = (caracter + 1) * 4
    print(lista)


# Datos de vuelo para un avión comercial
tiempo = [0, 10, 20, 30, 40, 50, 60]  # segundos
altitud = [0, 100, 500, 1000, 1500, 2000, 2200]  # metros
velocidad = [0, 50, 100, 150, 200, 250, 300]  # km/h
estado = ["despegue", "ascenso inicial", "ascenso", "ascenso", "ascenso", "nivelación", "crucero"]

# Imprimir informe de despegue
print("INFORME DE DESPEGUE:")
for t, a, v, est in zip(tiempo, altitud, velocidad, estado): #Zip toma cada uno de los elementos de la lista y lo copia en cada variable
    print(f"T+{t}s: Altitud={a}m, Velocidad={v}km/h, Fase={est}")

'''

import random

lista = []

for i in range(0,10):
    lista.append(random.randint(-100,1))

print(lista)

i=0
may = lista[0]
while i < 9:
    if may < lista[i + 1]:
        may = lista[i + 1]
    i += 1

print(may)

mayor = max(lista)
print(f"El mayor es {mayor}")

minin = lista[0]
while i < 9:
    if minin > lista[i + 1]:
        minin = lista[i + 1]
    i += 1

print(minin)
menor = min(lista)
print(f"El menor es {menor}")



