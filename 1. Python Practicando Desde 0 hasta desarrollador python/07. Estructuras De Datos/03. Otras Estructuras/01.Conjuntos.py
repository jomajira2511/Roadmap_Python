"""
===================================================
Script: 09.Metodos_Conjuntos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-08
Descripción:
    Ejemplos prácticos del uso de conjuntos (set) en Python.
    Un conjunto:
        - No permite valores repetidos
        - No garantiza un orden específico
        - Es útil para operaciones matemáticas de conjuntos
    Métodos usados:
        - .add() para agregar elementos
        - .remove() y .discard() para eliminar elementos
        - .pop() para eliminar un elemento aleatorio
        - .update() para agregar múltiples elementos
        - .clear() para vaciar el conjunto
===================================================
"""


# Creación de un conjunto con llaves {}
Conjunto = {1, 2, 3, 4, 5}

# Creación de conjunto usando set() con tupla
Conjunto2 = set((1, 2, 3, 4, 5))

# Creación de conjunto usando set() con lista
Conjunto3 = set([1, 2, 3, 4, 5])

# Mostrar los conjuntos iniciales
print("Conjunto 1:", Conjunto)
print("Conjunto 2:", Conjunto2)
print("Conjunto 3:", Conjunto3)


# ==========================
# Métodos con conjuntos
# ==========================

# Conjunto inicial de números
ConjuntoNumeros = {1, 2, 3, 4, 5, 6}
print("\nConjunto original:", ConjuntoNumeros)

# .add() → Agregar un elemento (si ya existe, no lo duplica)
ConjuntoNumeros.add(20)
print("\nDespués de .add(20):", ConjuntoNumeros)

# .remove() → Eliminar un elemento (da error si no existe)
ConjuntoNumeros.remove(1)
print("\nDespués de .remove(1):", ConjuntoNumeros)

# .discard() → Eliminar un elemento (no da error si no existe)
ConjuntoNumeros.discard(20)
print("\nDespués de .discard(20):", ConjuntoNumeros)

# .pop() → Elimina un elemento aleatorio
elemento_eliminado = ConjuntoNumeros.pop()
print("\nElemento eliminado con .pop():", elemento_eliminado)
print("Después de .pop():", ConjuntoNumeros)

# .update() → Agregar múltiples elementos (no se repiten)
ConjuntoNumeros.update([33, 32, 44, 22])
print("\nDespués de .update([33, 32, 44, 22]):", ConjuntoNumeros)

# .clear() → Vaciar el conjunto
ConjuntoNumeros.clear()
print("\nDespués de .clear():", ConjuntoNumeros)
