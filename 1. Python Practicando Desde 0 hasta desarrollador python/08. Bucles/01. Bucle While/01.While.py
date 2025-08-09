"""
===================================================
Script: 01.While.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-09
Descripción:
    Ejemplo práctico del uso del bucle `while` en Python.
    Un bucle `while` ejecuta un bloque de código de forma repetitiva 
    mientras se cumpla una condición booleana.
    En este caso, usamos un contador para evitar un loop infinito.
===================================================
"""

# ==========================
# Ejemplo de bucle while
# ==========================

i= 0 # Contador o iterador para poder usar el bucle while

while i < 10:  #Condicion del while -> mientras 1 sea menor que 10, al llegar a 10 rompe la condicion y sale del bucle 
    print("Esta es la iteracion #{}".format(i)) #Accion que se repetira 
    i +=1  #Sumamos +1 cada vez que el bucle itera, para evitar loops infinitos 

