"""
===================================================
Script: 02.Operadores_logicos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-08
Descripción:
    Ejemplo práctico del uso de los operadores lógicos 
    en Python. 

    Los operadores lógicos permiten combinar condiciones
    booleanas y retornan True o False según la evaluación.

    Operadores cubiertos en este script:
    - NOT (not): invierte el valor lógico.
    - AND (and): retorna True solo si ambas condiciones se cumplen.
    - OR (or): retorna True si al menos una condición se cumple.
===================================================
"""

# ===================================================
# Operador NOT
# Invierte el valor lógico. 
# Si es True → False, si es False → True.
# ===================================================
print(not False)   # True

# ===================================================
# Operador AND
# Retorna True únicamente cuando ambas condiciones son True.
# ===================================================
print(False and True)  # False

# ===================================================
# Operador OR
# Retorna True si al menos una de las condiciones es True.
# ===================================================
print(False or True)  # True

# ===================================================
# Ejemplo práctico con cadenas
# Se evalúan dos condiciones unidas con "and":
# 1. Que la longitud de la palabra sea menor que 8.
# 2. Que el primer carácter sea la letra "P".
# Ambas deben cumplirse para que el resultado sea True.
# ===================================================
a = "Python"
b = len(a)
print(b < 8 and a[0] == "P")  # True

