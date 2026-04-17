import random
# Importe la libreria random para tener números aleatorios para obtener matrices aleatorias.

def determinante3x3(m):
    a = m[0][0]
    b = m[0][1]
    c = m[0][2]
    d = m[1][0]
    e = m[1][1]
    f = m[1][2]
    g = m[2][0]
    h = m[2][1]
    i = m[2][2]

    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

    return det

print("Hola!!! Bienvenido a la calculadora de determinantes de matrices")
print("La matriz aleatoria dada es: ")
print("")

filas = 3
columnas = 3

matriz = [[random.randint(1,50) for j in range(columnas)] for i in range(filas)]

for fila in matriz:
    print(fila)


determinante = determinante3x3(matriz)
print("")
print(f"el determinante de la matriz es: {determinante}")



