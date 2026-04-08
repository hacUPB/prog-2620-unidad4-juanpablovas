# Gestión de Mantenimiento de Flota Aeronautica

## Contexto
Una aerolínea regional necesita un prototipo de sistema básico para gestionar las horas de vuelo de sus aeronaves y el inventario de piezas críticas sometidas a mantenimiento. Como ingenieros aeronáuticos, su misión es diseñar un algoritmo en Python que permita registrar y consultar esta información utilizando las estructuras de datos vistas en clase (Listas y Diccionarios).

![Imagen de Mantenimiento](../Imagenes/mantenimiento-aeronautico.jpg)

## Descripción de la Tarea

Deben crear un programa interactivo por consola que permita a los técnicos de mantenimiento realizar las siguientes acciones:

1. **Registro de Aeronaves:** El programa debe permitir al usuario ingresar datos de al menos 3 aeronaves. Cada aeronave debe tener:
    - Matrícula (ej. HK-4532)
    - Modelo (ej. A320, ATR72)
    - Horas de vuelo acumuladas

2. **Registro de Componentes:** Por cada aeronave, se deben poder registrar componentes críticos (ej. Motor izquierdo, Tren de aterrizaje, Alabes del compresor) junto con sus horas de uso actuales y el límite de horas permitidas antes del mantenimiento.

3. **Almacenamiento de Datos:** Toda la información recolectada desde el teclado (`input()`) debe almacenarse de forma estructurada en **listas** y **diccionarios**.

4. **Consulta de Mantenimiento:** El sistema debe recorrer los datos almacenados y mostrar un reporte en pantalla de qué componentes de qué aeronaves han superado su límite de horas y requieren mantenimiento inmediato.

## Planteamiento

    #Menu

    definir flota de aeronaves

    Flota = {
        Aeronave = {info[], item1, item2, item3, ..., itemN}
        .
        .
        .
    }

    Bienvenido al registro tecnico de mantenimiento
    ¿Qué vamos a hacer el día de hoy?
    1) registrar aeronaves
    2) Registrar componentes
    3) Consultar una aeronave

    si se escoge la primera opción
        Se entra en el diccionario de la flota
        Se agrega un item al diccionario
        Se solicita la matricula, el modelo 
        Se solicita horas de vuelo y ciclos
        Guardar en flota

    Si se escoge la segunda opcion
        Preguntar con otro menu que aeronave desea registro de componentes
        Se entra en el diccionario de la aeronave
            Pregunta: deseas añadir o modificar
            Si es añadir: agregar al diccionario
            Si es modificar, modificar el diccionario

    Si se escoge la tercera opción
        Se realiza una busqueda de la flota


            





