'''
Crea un diccionario llamado vuelo que contenga la siguiente
información inicial

# Ejercicio1
vuelo = {
    "aerolinea" : "Avianca",
    "vuelo" : "AV123",
    "origen" : "BOG",
    "destino" : "MDE"
}

# Ejercicio2: Extraer el valor destino

ciudad_llegada = vuelo["destino"]
print(ciudad_llegada)
print("")

# Ejercicio3: Modificación del valor existente

vuelo["destino"] = "CLO"

print(vuelo)
print("")

# Ejercicio4: Agregar un nuevo par clave-valor

vuelo["estado"] = "En el aire"

print(vuelo)
print("")

# Ejercicio5: Uso del metodo .get()
if "piloto" in vuelo:
    print(f"El piloto se llama {vuelo["piloto"]}")
else:
    print("Piloto no asignado")

# Ejercicio6: 
del vuelo["vuelo"]
print(vuelo)
'''

flota = {
    "N123AA": {
        "modelo": "Boeing 787-9",
        "año": 2018,
        "horas_vuelo": 12500,
        "ciclos": 1350,
        "estado": "En servicio",
        "base": "DFW",
        "proxima_revision": "2023-07-15"
    },
    "N456AA": {
        "modelo": "Boeing 777-300ER",
        "año": 2014,
        "horas_vuelo": 26800,
        "ciclos": 2940,
        "estado": "En mantenimiento",
        "base": "MIA",
        "proxima_revision": "2023-03-30"
    }
}
print("Vamos a ingresar una nueva aeronave a la flota!!!")
matricula = input("Ingresa la matricula: ")
mod = input("Ingresa el modelo: ")
año = input("Ingresa el año: ")
horas = input("Ingresa el numero de horas de vuelo: ")


flota[matricula] = {
    "modelo": mod,
    "año": año,
    "horas_vuelo": horas,
}

print(flota[matricula])



