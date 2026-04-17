'''
# Lista de componentes con sus masas (kg) y posiciones (m)
componentes = ["motor izquierdo", "motor derecho", "fuselaje", "ala izquierda", "ala derecha", "cola"]
masas = [1200, 1200, 5000, 800, 800, 600]
posiciones_x = [2, 2, 0, -2, 2, -6]

# Cálculo del centro de masa en eje X sin list comprehensions
masa_total = 0
momento_total = 0


for i in range(len(masas)):
    masa_total += masas[i]
    momento_total += masas[i] * posiciones_x[i]

for m, p in zip(masas, posiciones_x):
    masa_total += m
    momento_total += m*p

centro_masa_x = momento_total / masa_total

print(f"Centro de masa en eje X: {centro_masa_x:.2f} m") #:.f quiere decir que solo me de dos números decimales


from random import randint

lista = []

for i in range(100):
    dato = randint(1,9)
    lista.append(dato)

print(lista)

ocho = lista.count(8)
print(f"El número 8 se repite {ocho} veces")

-----------------------------------------------


#venta de vehiculos vendidos

from random import randint

meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
lista = []

for i in range(12):
    dato = randint(20,80)
    lista.append(dato)

print(lista)

mayor = max(lista)
posicion = lista.index(mayor)
mes = meses[posicion]
repet = lista.count(mayor)

if repet > 1:
    lista_meses = []
    for i in range(len(lista)):
        if lista[i] == mayor:
            lista_meses.append(i)
    print("Ventas mayores en:")
    for mes in lista_meses:
        print(f" {meses[mes]}")
    print(f"Se vendieron {mayor}")
else:
    print(f"El mes que se vendieron más autos fue {mes}")
    print(f"Se vendieron {mayor}")
----------------------------------
'''
from random import randint

lista = [110, 119, 30, 241, 234, 204, 105, 107, 101, 63, 181, "Falla"]

lista.insert(13, "Falla")
lista.remove(110)
lista.pop(3)

print(lista)


