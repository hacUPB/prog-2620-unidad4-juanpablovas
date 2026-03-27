# La trasposición de una matriz es una operacion que cambia 
# las filas de una matriz por sus columnas y viceversa

import random

def generar_matriz(filas, columnas):
    return [[random.randint(1, 50) for j in range(columnas)] for i in range(filas)]

# esto es lo que define la trasposición para una matriz
def transpuesta(m):
    filas = len(m)
    columnas = len(m[0])
    
    return [[m[i][j] for i in range(filas)] for j in range(columnas)]

filas = 3
columnas = 4

# Generar matriz
matriz = generar_matriz(filas, columnas)

print("Matriz original:")
for fila in matriz:
    print(fila)

# Calcular transpuesta
t = transpuesta(matriz)

print("\nMatriz transpuesta:")
for fila in t:
    print(fila)
