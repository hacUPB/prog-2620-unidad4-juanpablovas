flota = {}

def registro_aeronave(flota):
    matricula = input("\nAgrega la matricula de la aeronave: ")
    Modelo = input("Ingresa el modelo de la aeronave: ")
    HorasAcumuladas = input("Ingresa las horas de vuelo acumuladas: ")
        
    if matricula in flota:
        print("\nLa aeronave ya está registrada")

    else:
        flota[matricula] = {
            "Modelo" : Modelo,
            "HorasAcumuladas" : HorasAcumuladas,
        }
        print("\nAeronave registrada") 

def registro_componente(flota):
    if len(flota) == 0:
        print("\nNo hay aeronaves registradas")

    else:
        print("\nAeronaves registradas:")
        for matricula in flota:
            print(f"- {matricula}")
        
        matricula = input("Selecciona la matrícula: ")

        if matricula in flota:
            componente = input("Nombre del componente: ")
            horas = int(input("Horas del componente: "))

            if "Componentes" not in flota[matricula]:
                flota[matricula]["Componentes"] = {}

            flota[matricula]["Componentes"][componente] = {
                "Horas" : horas
                }
            
            print("Componente agregado correctamente")

        else:
            print("Matricula no encontrada")

def modificar_componente(flota):
    print("\nDeseas: ")
    print("1) Modificar. ")
    print("2) Eliminar Componentes. ")
    opcion1 = int(input("\nIngresa la opción: "))

    if opcion1 == 1:
        if len(flota) == 0:
            print("\nNo hay aeronaves registradas")
        else:
            print("\nAeronaves registradas:")
            for matricula in flota:
                print(f"- {matricula}")
            matricula = input("\nSeleciona la matricula: ")
            
            if matricula in flota:
                if "Componentes" in flota[matricula]:
                    print("\nComponentes:")
                    for comp in flota[matricula]["Componentes"]:
                        print(f"- {comp}")
                    
                    componente = input("\n¿Qué componente deseas modificar?: ")

                    if componente in flota[matricula]["Componentes"]:
                        nueva_hora = input("\nIngresa las nuevas horas del componente: ")
                        flota[matricula]["Componentes"][componente]["Horas"] = nueva_hora
                        print("Componente actualizado correctamente")
                    else:
                        print("Componente no encontrado")
                else:
                    print("Esta aeronave no tiene componentes")
            else:
                print("Matricula no encontrada")

    if opcion1 == 2:
        if len(flota) == 0:
            print("\nNo hay aeronaves registradas")
        else:
            print("\nAeronaves registradas:")
            for matricula in flota:
                print(f"- {matricula}")

            matricula = input("\nSeleciona la matricula: ")

            if matricula in flota:
                if "Componentes" in flota[matricula]:

                    print("\nComponentes:")
                    for comp in flota[matricula]["Componentes"]:
                        print(f"- {comp}")
                    
                    componente_eliminar = input("\n¿Qué componente deseas eliminar: ")

                    if componente_eliminar in flota[matricula]["Componentes"]:
                        del flota[matricula]["Componentes"][componente_eliminar]
                        print("\nComponente eliminado correctamente")
                    else:
                        print("\nComponente no encontrado")
                else:
                    print("\nComponente no encontrado")
            else:
                print("\nMatricula no encontrada")

def consultar_aeronave(flota):
    if len(flota) == 0:
        print("\nNo hay aeronaves registradas")

    else:
        print("\nAeronaves registradas")
        for matricula in flota:
            print(f"- {matricula}")

        matricula_consulta = input("Selecciona la matrícula: ")

        if matricula_consulta in flota:
            datos = flota[matricula_consulta]

            print("\nMatrícula:", matricula)
            print("Modelo:", datos["Modelo"])
            print("Horas:", datos["HorasAcumuladas"])

            alerta = False

            if "Componentes" in datos:
                print("Componentes:")
                for nombre, info in datos["Componentes"].items():
                    horas = info["Horas"]
                    print(f"- {nombre} | Horas: {info['Horas']}")

                    if horas >= 10000:
                        alerta = True
                        print(f"{nombre} requiere mantenimiento")
                
                if alerta:
                    print("\nALERTA: Esta aeronave requiere revisión")
            else:
                print("\nNo tiene componentes registrados")
        else:
            print("Matricula no encontrada")

print("\nBienvenido al registro tecnico de mantenimiento de Avianca")

while True:
    print("\nSelecciona la opcion correspondiente")
    print("1) Registrar aeronave")
    print("2) Registrar componente")
    print("3) Modificar componente")
    print("4) Consultar aeronave")
    print("5) Salir")
    opcion = int(input("\nSelecciona la opción de la tarea a realizar: "))

    if opcion == 1:
        registro_aeronave(flota)
    
    elif opcion == 2:
        registro_componente(flota)

    elif opcion == 3:
        modificar_componente(flota)

    elif opcion == 4:
        consultar_aeronave(flota)

    elif opcion == 5:
        print("Saliendo...")
        break
