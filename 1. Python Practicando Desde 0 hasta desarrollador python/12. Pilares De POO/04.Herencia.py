"""
===================================================
Script: 04.Herencia.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Ejemplo de herencia en Programación Orientada a Objetos (POO) en Python.

    - La herencia permite que una clase hija obtenga métodos y atributos de
        una clase padre, evitando duplicar código.
    - Se pueden sobrescribir métodos o agregar nuevos comportamientos
        en la clase hija.
===================================================
"""

# Clase padre
class Animales:
    def habla(self):
        """
        Método general para todos los animales.
        """
        print("Yo soy un animal")
    
    def descripcion(self):
        """
        Muestra la descripción del animal usando su atributo 'animal'.
        """
        print("Yo soy un {} ".format(self.animal))



# Clase hija: Perro
# Hereda todos los métodos de la clase Animales
class Perro(Animales):
    pass  # No agrega cambios, pero hereda todos los métodos del padre



# Clase hija: Abeja
# Sobrescribe el constructor para agregar atributo 'animal'
class Abeja(Animales):
    def __init__(self, animal):
        # Definimos el atributo 'animal' que usará el método descripcion()
        self.animal = animal


# Ejemplo de uso

# Instancia directa de la clase padre
animal = Animales()
animal.habla()

# Instancia de clase hija que hereda métodos del padre
perro = Perro()
perro.habla()  # Método heredado de Animales

# Instancia de clase hija con constructor propio
abeja = Abeja("abeja")
abeja.descripcion()
