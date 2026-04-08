'''
# Tupla vacía
coordenada = ()

# Tupla con elementos
coordenada = (33.9425, -118.4081)  # LAX (Aeropuerto de Los Ángeles)

# Tupla con un solo elemento (requiere coma al final)
rumbo = (270,)  # Sin la coma sería tratado como un entero entre paréntesis

# Tupla sin paréntesis (empaquetado implícito)
avion_info = "Boeing 787", "Dreamliner", 2009, 242

print(f"Cordenadas: {coordenada[0]}")

print(coordenada)

coordenada[1] = -120

print(f"Cordenadas: {coordenada[1]}")

#Las tuplas son inmutables no pueden cambiar, son constantes, cosas que no van a cambiar en el programa

print(coordenada)

fleet_data = [
    ("Airbus A320", 35.80, 37.57, 78000, 871),
    ("Boeing 737-800", 35.79, 39.47, 79010, 853),
    ("Embraer E190", 28.72, 36.24, 51800, 871),
    ("Bombardier CRJ-900", 24.85, 36.40, 38330, 870)
]

# fleet_data[0] = 5

print(fleet_data)

print(fleet_data[2][0])

'''

tupla_lista = (1, 4, [4,5,8])

print(tupla_lista)

tupla_lista[2][0] = 222

print(tupla_lista)

#hola