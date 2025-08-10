"""
===================================================
Script: 03.Funciones_Matematicas.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-09
Descripción:
    Demostración de funciones matemáticas y generación de números aleatorios en Python.

    - Uso de la librería math:
        * math.sqrt(): Raíz cuadrada.
        * math.isqrt(): Raíz cuadrada con resultado entero.
        * math.sin(): Seno.
        * math.cos(): Coseno.
        * math.tan(): Tangente.
        * math.factorial(): Factorial.
        * pow(): Potencias.

    - Uso de la librería random:
        * random.randint(): Generación de valores enteros aleatorios en un rango específico.
===================================================
"""


# Funciones matematicas 
# Estan integrados en una libreria 
# Para usar librerias se debe de importar 

# Importamos libreria math -> para usar funciones matematicas
import math 

# Importamos libreria random -> Permite generar valores aleatorios
import random

# .pow() -> Funcion para elevar un numero a una potencia (Numero , Potencia a elevar)
print (pow(10 , 10))

# .sqrt() -> Funcion que permite obtener la raiz cuadrada de un numero
print(math.sqrt(64))  # Nos da el resultado en float
print(math.isqrt(64))  # Nos da el resultado en int

# .sin() -> Funcion que permite encontrar un seno de un numero 
print(math.sin(90)) 

# .cos() -> Funcion que permite encontrar el coseno de un numero
print(math.cos(90))

# .tan() -> Funcion que permite encontrar la tangente de un numero
print(math.tan(90))

# .fact() -> Funcion para encontrar el factorial de un numero 
print(math.factorial(90)) 

# .random -> Proporciona valores aleatorio
print(random.randint(1 , 100 ))   # Entrega valores entre 1 y 100 
