"""
===================================================
Script: 06.Tuplas.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-08
Descripción:
    Ejemplos prácticos de tuplas en Python.
    Las tuplas son colecciones ordenadas e inmutables, 
    lo que significa que no se pueden modificar después 
    de ser creadas. Pueden contener datos de diferentes tipos.
===================================================
"""

# Declaración de una tupla
Tupla = ("Jhon", 25, "Ingeniero", True)

print("Tupla original:")
print(Tupla, "\n")

# Acceder a elementos de la tupla
print("Primer elemento:", Tupla[0])
print("Último elemento:", Tupla[-1], "\n")

# Longitud de la tupla
print("Número de elementos en la tupla:", len(Tupla), "\n")

# Concatenar tuplas
OtraTupla = ("Python", "Programador")
TuplaConcatenada = Tupla + OtraTupla
print("Tupla concatenada:")
print(TuplaConcatenada, "\n")

# Repetir elementos de la tupla
TuplaRepetida = Tupla * 2
print("Tupla repetida:")
print(TuplaRepetida, "\n")

# Convertir una tupla en lista para modificarla
ListaDesdeTupla = list(Tupla)
ListaDesdeTupla[1] = 30
print("Lista modificada (derivada de tupla):")
print(ListaDesdeTupla, "\n")

# Convertir la lista nuevamente a tupla
TuplaModificada = tuple(ListaDesdeTupla)
print("Tupla modificada:")
print(TuplaModificada, "\n")

# Comprobar si un elemento está en la tupla
print("¿'Jhon' está en la tupla?", "Jhon" in Tupla)
print("¿'Python' está en la tupla?", "Python" in Tupla, "\n")
