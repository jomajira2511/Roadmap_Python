"""
===================================================
Script: 02.Arrays.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-17
Descripción:
    Ejemplo práctico del uso de listas (arrays) en Python.
    Métodos aplicados:
    - append(): agrega un elemento al final de la lista.
    - extend(): une dos listas.
    - count(): cuenta cuántas veces aparece un elemento.
    - index(): obtiene la posición de un elemento.
    - insert(): inserta un elemento en una posición específica.
    - len(): obtiene la longitud de la lista.
    - remove(): elimina la primera aparición de un elemento.
    - sort(): ordena los elementos de menor a mayor.
    - clear(): elimina todos los elementos de la lista.
===================================================
"""

# ===================================================
# Declaración de listas
# ===================================================
lista = [1, 2, 8, 4, 5]
lista2 = [7, 3, 9, 10]

# ===================================================
# Uso de métodos de listas
# ===================================================

# .append() -> Agrega un elemento al final
lista.append(6)
print("Después de append:", lista)

# .extend() -> Une dos listas
lista.extend(lista2)
print("Después de extend:", lista)

# .count() -> Cuenta cuántas veces aparece un elemento
print("Número de veces que aparece el 1:", lista.count(1))

# .index() -> Retorna el índice de un elemento
print("Posición del número 1:", lista.index(1))

# .insert() -> Inserta un elemento en una posición específica
lista.insert(0, 0)
print("Después de insert en posición 0:", lista)

# len() -> Longitud de la lista
print("Longitud de la lista:", len(lista))

# .remove() -> Elimina la primera aparición de un elemento
lista.remove(1)
print("Después de remove(1):", lista)

# .sort() -> Ordena los elementos de menor a mayor
lista.sort()
print("Después de sort:", lista)

# .clear() -> Vacía completamente la lista
lista.clear()
print("Después de clear:", lista)
