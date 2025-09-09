"""
===================================================
Script: tuplas.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-09
Descripción:
    Ejemplo práctico del uso de tuplas en Python.
    - Declaración de tuplas con diferentes tipos de datos.
    - Acceso a elementos mediante índices.
    - Indexación dentro de una lista almacenada en la tupla.
    - Slicing (subconjuntos de tupla).
    - Uso de métodos propios de las tuplas como:
        - .index() para obtener la posición de un elemento.
        - .count() para contar ocurrencias de un valor.
    - Uso de len() para conocer la longitud de la tupla.
    Nota: Las tuplas son inmutables, por lo que no se pueden modificar 
    sus elementos después de ser creadas.
===================================================
"""

# -------------------------------------------------
# Declaración de una tupla con múltiples tipos de datos
# -------------------------------------------------
tupla = ("Jhon", 10, True, [1, 2, 3], "Matias")
print(tupla)  # Imprime la tupla completa

# -------------------------------------------------
# Acceso por índice
# -------------------------------------------------
print(tupla[0])      # Accede al primer elemento → "Jhon"
print(tupla[3][1])   # Accede a la lista en la posición 3 y luego al índice 1 → 2

# -------------------------------------------------
# Slicing en tuplas
# Devuelve todos los elementos desde el índice 1 hasta el final
# -------------------------------------------------
print(tupla[1:])

# -------------------------------------------------
# Métodos de las tuplas
# -------------------------------------------------
print(tupla.index(10))   # Devuelve el índice del valor "10" → 1
print(tupla.count(10))   # Devuelve cuántas veces aparece "10" → 1

# -------------------------------------------------
# Longitud de la tupla
# -------------------------------------------------
print(len(tupla))  # Devuelve 5 (cantidad de elementos)
