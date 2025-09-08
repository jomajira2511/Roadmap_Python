"""
===================================================
Script: 01.Operadores_relacionales.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-08
Descripción:
    Ejemplo práctico del uso de los operadores relacionales
    en Python. 

    Los operadores relacionales permiten comparar valores y 
    siempre retornan un resultado booleano (`True` o `False`).

    Operadores cubiertos en este script:
    - Igualdad (==)
    - Diferente (!=)
    - Menor que (<)
    - Mayor que (>)
    - Menor o igual (<=)
    - Mayor o igual (>=)
===================================================
"""

# ===================================================
# Operador de comparación (==)
# Retorna True si ambos valores son exactamente iguales.
# ===================================================
a = "Raul" == "raul"  
print(a)  # False, porque distingue mayúsculas de minúsculas

# ===================================================
# Operador "diferente que" (!=)
# Retorna True si los valores comparados no son iguales.
# ===================================================
b = 10 != 20
print(b)  # True

# ===================================================
# Operador "menor que" (<)
# Retorna True si el valor de la izquierda es menor que el de la derecha.
# ===================================================
c = 10 < 5
print(c)  # False

# ===================================================
# Operador "mayor que" (>)
# Retorna True si el valor de la izquierda es mayor que el de la derecha.
# ===================================================
d = 10 > 5
print(d)  # True

# ===================================================
# Operador "menor o igual que" (<=)
# Retorna True si el valor de la izquierda es menor o igual al de la derecha.
# ===================================================
e = 10 <= 20
print(e)  # True

# ===================================================
# Operador "mayor o igual que" (>=)
# Retorna True si el valor de la izquierda es mayor o igual al de la derecha.
# ===================================================
f = 10 >= 30
print(f)  # False
