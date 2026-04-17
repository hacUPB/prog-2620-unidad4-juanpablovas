


def analizar_eficiencia(distancias, combustible_consumido):
    eficiencia_tramos = []
    for a, b in zip(distancias, combustible_consumido):
        eficiencia = a/b
        eficiencia_tramos.append(eficiencia)

    ef_max = max(eficiencia_tramos)
    ef_min = min(eficiencia_tramos)
    
    prom = 0
    sum = 0

    for c in eficiencia_tramos:
        sum = sum + c

    
    prom = sum/len(eficiencia_tramos)
    
    msg = print(f"El tramo mas eficiente es {ef_max} y el menos {ef_min} y el promedio es {prom}")

    return msg


    
tramos_distancia = [800, 1200, 1000, 750] # km
tramos_combustible = [2400, 3000, 2800, 2000] #L

resultado = analizar_eficiencia(tramos_distancia, tramos_combustible)
print(resultado)