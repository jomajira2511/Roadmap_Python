"""
===================================================
Script: 02.Excepciones_multiples.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-11
Descripción:
    Ejemplo de manejo de múltiples excepciones en Python.
    - Se solicita un valor por teclado.
    - Se fuerza un error de división por cero.
    - Se capturan excepciones específicas como ValueError.
    - Se usa Exception para atrapar cualquier otro error y
    mostrar el nombre del error sin detener el programa.
===================================================
"""

try:
    c = int(input("Ingresa un valor: "))  # Pedimos un dato por teclado
    c / 0  # Forzamos un error de división por cero

except ValueError:
    print("No puedes ingresar texto cuando se espera un número.")

except Exception as e:  # Le asignamos un nombre al error
    print("Se produjo una excepción:", type(e).__name__)
