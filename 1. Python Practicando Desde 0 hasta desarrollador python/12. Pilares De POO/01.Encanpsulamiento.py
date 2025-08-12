"""
===================================================
Script: 01.Encapsulamiento.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Ejemplo práctico de encapsulamiento en Programación Orientada a Objetos (POO) en Python.
    Se muestra la diferencia entre atributos públicos y privados en clases.

    Objetivos:
    - Entender cómo limitar el acceso a los atributos de una clase.
    - Diferenciar entre atributos accesibles desde fuera y protegidos/privados.
===================================================
"""

# ===================================================
# Clase con atributo público
# ===================================================
class A():
    def __init__(self):
        # Atributo público: puede accederse y modificarse desde fuera de la clase
        self.contador = 0

    def incrementar(self):
        """Incrementa el contador en 1."""
        self.contador += 1

    def cuenta(self):
        """Devuelve el valor actual del contador."""
        return self.contador


# Clase con atributo privado (encapsulado)
class B():
    def __init__(self):
        # Atributo privado: solo debe ser accesible desde dentro de la clase
        # Python lo simula usando doble guion bajo (__), lo que activa *name mangling*
        self._contador = 0

    def incrementar(self):
        """Incrementa el contador en 1."""
        self._contador += 1

    def cuenta(self):
        """Devuelve el valor actual del contador."""
        return self._contador



# Prueba de funcionamiento de ambas clases

print("-------------OBJETO 1----------------")
a = A()
print(a.cuenta())      # 0
a.incrementar()
print(a.cuenta())      # 1

print("---------------OBJETO 2-----------------")
b = B()
print(b.cuenta())      # 0
b.incrementar()
print(b.cuenta())      # 1
