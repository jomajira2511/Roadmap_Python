"""
===================================================
Script: 01.For.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-09
Descripción:
    Ejemplo práctico de cómo recorrer (iterar) 
    listas y tuplas en Python utilizando un bucle for.

    Conceptos:
        - Una lista es una colección ordenada y mutable.
        - Una tupla es una colección ordenada e inmutable.
        - El bucle for recorre cada elemento de la colección 
            de forma secuencial.
===================================================
"""

# Lista → permite modificar sus elementos
lista = ["Uno", "Dos", "Tres"]

# Tupla → sus elementos no se pueden modificar
tupla = (1, 2, 3, 4, 5)


for i in lista:
    # Imprime cada elemento de la lista
    print(i)


for i in tupla:
    # Imprime cada elemento de la tupla
    print(i)
