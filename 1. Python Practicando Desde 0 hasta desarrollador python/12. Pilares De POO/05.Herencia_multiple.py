"""
===================================================
Script: 08.Herencia_Multiple.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-13
Descripción:
    Ejemplo de herencia múltiple en Python, donde una clase 
    hija hereda métodos de más de una clase padre.
    Se muestra cómo funciona el acceso a los métodos y 
    el orden de resolución de métodos (MRO).
===================================================
"""

# Definición de la primera clase padre
class A():
    def primera(self):
        return "Esta es la clase A"
    

# Definición de la segunda clase padre
class B():
    def segunda(self):
        return "Esta es la clase B"
    

# Clase hija que hereda de A y B
class C(A, B):  
    """
    Hereda de ambas clases (A y B) 
    lo que permite acceder a sus métodos sin reescribirlos.
    """
    pass


# Crear un objeto de la clase C
c = C()

# Llamar a los métodos heredados de ambas clases
print(c.primera())  # Método heredado de A
print(c.segunda())  # Método heredado de B
