# 📝 Plantilla de Autoevaluación: Gestión de Mantenimiento de Flota Aeronáutica ✈️

**Instrucciones para los estudiantes:**
1. Hagan una copia de este archivo y guárdenlo en la raíz de su repositorio con el nombre `AUTOEVALUACION.md`.
2. Lean cuidadosamente cada criterio de la rúbrica.
3. En el apartado **Nota Esperada**, asignen una calificación numérica (de 0.0 a 5.0) que consideren justa para su trabajo en ese criterio.
4. En el apartado **Justificación**, expliquen con sus propias palabras por qué merecen esa nota. Sean críticos y honestos.
5. En el apartado **Evidencia**, inserten pantallazos de la ejecución de la consola, imágenes de su diagrama o bloques de código (usando la sintaxis de Markdown con \`\`\`) que respalden su justificación.
6. Al final, calculen su nota definitiva esperada según los porcentajes.

---

## 👥 1. Información del Equipo

* **Miembro 1:** Juan Pablo Vásquez Muñoz - 000584530

---

## 📊 2. Evaluación por Criterios

### Criterio 1: Diagrama y Lógica (Valor: 20%)
* **Nota Esperada (0.0 - 5.0):** **5.0**

* **Justificación:** 
  > Se elaboraron dos diagramas. El primero representa el flujo de almacenamiento de datos, utilizando estructuras tipo diccionario, y se presenta como un diagrama de memoria. El segundo diagrama ilustra el proceso de ingreso de datos por parte del usuario (técnico de mantenimiento) y el comportamiento del programa según las acciones que este realiza. Con base en lo anterior, considero que el trabajo cumple con los criterios establecidos para una calificación de 5.0. 
  
* **Evidencia:**

Diagrama memoria.

  ![Diagrama Memoria](../Imagenes/Memoria.drawio.png)

Diagrama de bloques - código.

![Diagrama de bloques](../Imagenes/EsquemaReto.drawio.png)


### Criterio 2: Uso de Estructuras (Listas y Diccionarios) (Valor: 30%)
* **Nota Esperada (0.0 - 5.0):** **5.0**

* **Justificación:**
  > Se empleó un diccionario principal denominado flota, en el cual se almacenan las aeronaves. A su vez, cada aeronave se representa como un diccionario interno que contiene sus datos mediante pares clave-valor. Los componentes de cada aeronave se gestionan a través de otro diccionario, donde se registra el nombre del componente y sus horas de operación. Considero que este apartado merece una calificación de 5.0, debido al uso adecuado de los diccionarios, la correcta aplicación de sus métodos y la integración de estos con conocimientos previamente adquiridos.

* **Evidencia:**
  ![Eviencia de diccionarios](../Imagenes/Evidenciadiccionarios.png)
  
  ```python
  # Reemplaza esto con tu fragmento de código real
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
  # ... código de inserción de datos ...

### Criterio 3: Cumplimiento de Restricciones Técnicas (Valor: 20%)
* **Nota Esperada (0.0 - 5.0):** **5.0**

* **Justificación:**
    > Considero que en este criterio merezco una calificación de 5.0, ya que hago un uso adecuado de las estructuras de control for y while. Además, no utilizo librerías externas ni funciones avanzadas, y evito el uso de comprensiones de listas, cumpliendo así con los requisitos establecidos.

* **Evidencia:** 
![Eviencia de cumplimientos](../Imagenes/evidencia%202.png)


### Criterio 4: Funcionalidad del Código (Valor: 15%)
* **Nota Esperada (0.0 - 5.0):** [Escribe tu nota aquí]
* **Justificación:**
    > Considero que mi calificación en este criterio es 5.0, ya que el programa valida correctamente los datos ingresados por el usuario, no presenta errores durante su ejecución y genera un reporte final de mantenimiento. Además, ofrece una interacción clara y amigable con el usuario (técnico).

* **Evidencia:** 

![Eviencia de funcionalidad](../Imagenes/evidencia%203.png)


### Criterio 5: Preparación para Sustentación (Valor: 15%)

* **Nivel de Confianza (Bajo / Medio / Alto):** **Alto**
* **Justificación:**
    > Comprendo no solo el código, sino también el proceso de diseño de las estructuras de datos de acuerdo con los requerimientos planteados. Además, elaboro una base previa mediante diagramas, lo que me permite tener mayor claridad en el desarrollo e implementación del código.

* **Evidencia de preparación: 
    > Desarrollé el código teniendo claridad sobre cómo debían almacenarse los datos y cuáles eran los requerimientos planteados. Durante el proceso, me formulé constantemente preguntas como “¿por qué lo hago?” y “¿cómo lo hago?”, lo que me permitió fortalecer y afianzar los conocimientos adquiridos en la unidad.

### 📈 3. Cálculo de Nota Definitiva Esperada
Multipliquen la nota asignada en cada criterio por su porcentaje respectivo y sumen los resultados para obtener su nota final esperada.

|Criterio	|Nota |Asignada	|Peso	|Subtotal |(Nota * Peso) |
|---|---|---|---|---|---|
|1. Diagrama y Lógica	|[Nota]	|20% |(0.2)	|5.0| 1|
|2. Uso de Estructuras	|[Nota]	|30% |(0.3)	|5.0|1.5|
|3. Cumplimiento Restricciones|	[Nota]	|20% |(0.2)	|5.0|1|
|4. Funcionalidad	|[Nota]	|15% |(0.15)	|5.0|0.75|
|5. Sustentación (Estimado)|	[Nota]|	15%| (0.15)|5.0|0.75|

NOTA FINAL ESPERADA		100%	**[5]**

✨ ""La educación es para el carácter, no solo para la mente"." ✨