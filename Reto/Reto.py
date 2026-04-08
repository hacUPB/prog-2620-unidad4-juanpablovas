flota = {}

print("Bienvenido al registro tecnico de mantenimiento de Avianca")
print("¿Qué vamos a hacer el día de hoy?")
print("1) registrar aeronaves")
print("2) registrar componentes")
print("3) Consultar una aeronave")
opcion = int(input("Selecciona la opción de la tarea a realizar: "))

if opcion == 1:
    flota["aeronave"] = input("Agrega la el nombre de la aeronave")
    print(flota)
    pass
elif opcion == 2:
    pass
elif opcion == 3:
    pass 
else:
    pass
