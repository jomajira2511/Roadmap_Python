"""
===================================================
Módulo: Paquetes2.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-21
Descripción:
    Este módulo define funciones matemáticas básicas
    (Multiplicar y dividir) que serán
    utilizadas en otros scripts de la calculadora.
===================================================
"""

# ===================================================
# Funciones matemáticas básicas
# ===================================================



def multiplicacion(op1, op2):
    """Devuelve la multiplicación de dos números"""
    print(f"El resultado de la multiplicación es : {op1 * op2}")


def dividir(op1, op2):
    """Devuelve la división de dos números, con manejo de error por división entre cero"""
    try:
        print(f"El resultado de la división es : {op1 / op2}")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
