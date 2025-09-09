"""
===================================================
Script: pilas_colas.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-09
Descripción:
    Ejemplo práctico de estructuras de datos lineales en Python:
    - Uso de listas como colas (FIFO: First In, First Out).
    - Inserción de elementos al final de la cola.
    - Extracción de elementos desde el inicio de la cola.
    Nota: Python no tiene una estructura de datos "cola" nativa,
    pero se puede implementar fácilmente con listas o con la 
    librería "collections.deque" para mayor eficiencia.
===================================================
"""

# -------------------------------------------------
# Definición de una cola (lista que simula el comportamiento FIFO)
# -------------------------------------------------
fila = ["Jhon", "Pedro", "Alejandro", "Sara", "Matias"]
print(fila)  # Estado inicial de la cola

# -------------------------------------------------
# Agregar un elemento al final de la cola
# -------------------------------------------------
fila.append("Andres")
print(fila)  # Ahora "Andres" está al final de la cola

# -------------------------------------------------
# Extraer el primer elemento de la cola
# -------------------------------------------------
i = fila.pop(0)  # Elimina y retorna el primer elemento de la lista (índice 0)
print(fila)  # Estado de la cola después de la extracción
print(i)     # Elemento que fue retirado ("Jhon")
