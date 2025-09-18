"""
===================================================
Script: 04.Conjuntos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-17
Descripción:
    Ejemplo práctico del uso de conjuntos en Python.
    Métodos aplicados:
    - add(): agrega un elemento al conjunto.
    - discard(): elimina un elemento sin generar error si no existe.
    - copy(): crea una copia del conjunto.
    - union(): une dos conjuntos.
    - intersection(): devuelve elementos en común.
    - difference(): devuelve elementos diferentes.
    - symmetric_difference(): devuelve elementos que no se repiten en ambos.
    - issubset(): verifica si un conjunto está contenido en otro.
    - issuperset(): verifica si un conjunto contiene a otro.
    - isdisjoint(): verifica si no hay elementos en común.
    - clear(): elimina todos los elementos del conjunto.
===================================================
"""

# ===================================================
# Declaración de conjuntos
# ===================================================
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Conjunto A:", A)
print("Conjunto B:", B)

# ===================================================
# Métodos básicos
# ===================================================

# .add()
A.add(10)
print("\nA después de agregar 10:", A)

# .discard()
A.discard(2)
print("A después de descartar 2:", A)

# .copy()
C = A.copy()
print("Copia del conjunto A:", C)

# ===================================================
# Operaciones entre conjuntos
# ===================================================

# .union()
print("\nUnión de A y B:", A.union(B))

# .intersection()
print("Intersección de A y B:", A.intersection(B))

# .difference()
print("Diferencia A - B:", A.difference(B))
print("Diferencia B - A:", B.difference(A))

# .symmetric_difference()
print("Diferencia simétrica (elementos no comunes):", A.symmetric_difference(B))

# ===================================================
# Métodos de comparación
# ===================================================

X = {1, 2, 3}
Y = {1, 2, 3, 4, 5}

print("\nX:", X)
print("Y:", Y)
print("¿X es subconjunto de Y? ->", X.issubset(Y))
print("¿Y es superconjunto de X? ->", Y.issuperset(X))
print("¿X y B no tienen elementos en común? ->", X.isdisjoint(B))

# ===================================================
# Métodos para limpieza
# ===================================================

B.clear()
print("\nB después de .clear():", B)
