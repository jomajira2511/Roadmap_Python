"""
===================================================
Script: 02.Bucle_while.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-08
Descripción:
    Ejemplo del uso del bucle while en Python.
    El programa recorre una lista de lenguajes de
    programación utilizando un contador manual.
    Se incrementa la variable de control hasta que
    deja de cumplirse la condición establecida.
===================================================
"""

# -----------------------------------------
# Lista de lenguajes de programación
# -----------------------------------------
lenguajes = ["Python", "Java", "Ruby", "C++", "Cobol"]

# -----------------------------------------
# Variable de control para el bucle while
# -----------------------------------------
a = 0

# -----------------------------------------
# Bucle while
# Se repite mientras la condición (a < len(lenguajes))
# sea verdadera. En cada iteración se imprime el
# lenguaje correspondiente y se incrementa 'a'.
# -----------------------------------------
while a < len(lenguajes):
    print(lenguajes[a])
    a += 1  # Incrementa en 1 la variable de control
