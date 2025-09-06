"""
===================================================
Script: 02.Generadores.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-05
Descripción:
    Ejemplo práctico del uso de generadores en Python.

    Un generador es una función especial que, en lugar de
    devolver todos los valores de una vez, los produce uno
    por uno utilizando la palabra clave `yield`.

    Esto permite optimizar memoria y trabajar con secuencias
    grandes de manera eficiente.
===================================================
"""

# ===================================================
# Definición de un generador
# ===================================================
def generaPares(limite):
    """
    Generador que devuelve números pares hasta un límite.

    Parámetros:
        limite (int): número máximo de iteraciones.
    
    Retorna:
        int: cada número par en cada paso de la iteración.
    """
    num = 1
    while num < limite:
        yield num * 2  # `yield` devuelve un valor y pausa la ejecución
        num = num + 1


# ===================================================
# Uso del generador
# ===================================================
devuelvePares = generaPares(10)  # Crea el objeto generador

# Se obtienen los valores uno a uno con `next()`
print(next(devuelvePares))  # 2
print(next(devuelvePares))  # 4
print(next(devuelvePares))  # 6
print(next(devuelvePares))  # 8
print(next(devuelvePares))  # 10
print(next(devuelvePares))  # 12
print(next(devuelvePares))  # 14
