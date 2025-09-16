"""
===================================================
Script: 02.Herencia_multiple.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-16
Descripción:
    Ejemplo de herencia múltiple en Python.
    - Clase1: Define un método propio.
    - Clase2: Define un método propio.
    - Clase3: Hereda de Clase1 y Clase2, 
            accediendo a sus métodos y añadiendo uno propio.
===================================================
"""

# ===================================================
# Clase1: define un método
# ===================================================
class Clase1:
    def metodo1(self):
        print("Hola, soy el método de la Clase 1.")


# ===================================================
# Clase2: define un método
# ===================================================
class Clase2:
    def metodo2(self):
        print("Soy el método de la Clase 2.")


# ===================================================
# Clase3: hereda de Clase1 y Clase2
# ===================================================
class Clase3(Clase1, Clase2):
    def metodo3(self):
        print("Soy el método de la Clase 3 (heredo de Clase1 y Clase2).")


# ===================================================
# Bloque principal de ejecución
# ===================================================

c = Clase3()
c.metodo1()  # Heredado de Clase1
c.metodo2()  # Heredado de Clase2
c.metodo3()  # Propio de Clase3
