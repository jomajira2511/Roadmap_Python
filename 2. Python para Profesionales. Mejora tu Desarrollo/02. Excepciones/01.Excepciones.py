"""
===================================================
Script: 01.Excepciones.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-03
Descripción:
    Ejemplo práctico del uso de excepciones en Python.

    El bloque try-except-else-finally permite manejar errores
    de manera controlada, evitando que el programa termine de 
    forma inesperada. 

    Componentes:
    - try: Contiene el código que puede generar un error.
    - except: Captura el error y permite definir una acción.
    - else: Se ejecuta si no ocurre ningún error.
    - finally: Se ejecuta siempre, ocurra o no una excepción.
===================================================
"""

# ===================================================
# Ejemplo: Manejo de excepciones en listas
# ===================================================

# Creamos una lista con 3 elementos
lista = [1, 2, 3]

try:
    # Intentamos acceder a un índice que no existe (índice 4)
    print(lista[4])

except IndexError:
    # Se ejecuta si el error es por índice fuera de rango
    print(" Error: el índice que intentas acceder no existe en la lista.")

else:
    # Solo se ejecuta si no ocurrió ninguna excepción
    print(" No hubo ningún error en el acceso a la lista.")

finally:
    # Siempre se ejecuta, ocurra o no un error
    print(" El script finalizó correctamente.")
