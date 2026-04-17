'''
frase = "Universidad"
print(frase)

frase.upper()
print(frase)

lista = [4, 65, 8, 2, 3, 4, 78, 41, 55]
print(lista)

lista.sort()
print(lista)

print(frase[0])
print(lista[0])

lista[0] = 999

print(frase)
print(lista)

modelo = "Boeing 747"
print(id(modelo))

modelo = modelo + "-800"
print(modelo)
print(id(modelo))

componentes = ["alas", "fuselaje", "motores"]
print(id(componentes))  # Guardamos el ID original

# Modificamos la lista
componentes.append("tren de aterrizaje")
print(componentes)  # ["alas", "fuselaje", "motores", "tren de aterrizaje"]
print(id(componentes))  # Mismo ID, el objeto fue modificado in-place

def agregar_combustible(tanques, litros):
    tanques.append(litros)
    print(f"Combustible actualizado: {tanques}")

combustible_actual = [1000, 1200, 800]  # Lista (objeto mutable)
agregar_combustible(combustible_actual, 500)
print(combustible_actual)  # [1000, 1200, 800, 500] - La lista original fue modificada


# Iterando sobre una lista de sensores de aeronave
sensores = ["temperatura", "presión", "velocidad", "altitud", "combustible"]

for sensor in sensores:
    print(f"Comprobando sensor de {sensor}...")

'''
# Simulando lecturas de altitud cada 10 segundos
altitudes = [0, 100, 500, 1000, 1500, 2000, 2200, 2500]
tiempo = 0
i = 0

while i < len(altitudes):
    print(f"Tiempo: {tiempo}s - Altitud: {altitudes[i]} metros")
    tiempo += 10
    i += 1