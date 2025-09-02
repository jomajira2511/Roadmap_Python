"""
===================================================
Script: 01.Variables_de_instancia_y_clase.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-02
Descripción:
    Ejemplo práctico del uso de variables de clase y de instancia
    dentro de una clase en Python.
    
    - Variable de clase: pertenece a la clase y es compartida por
    todas las instancias.
    - Variable de instancia: pertenece a cada objeto creado a partir
    de la clase y puede tener valores diferentes en cada uno.
===================================================
"""

# Definición de clase en Python
class Persona():
    edad = 20   #  Variable de CLASE: compartida por todas las instancias
    
    def __init__(self, nombre, nacionalidad):
        """
        Constructor de la clase Persona.
        self → permite acceder a los atributos y métodos propios
        de cada instancia.
        """
        self.nombre = nombre             #  Variable de INSTANCIA: única de cada objeto
        self.nacionalidad = nacionalidad #  Variable de INSTANCIA: única de cada objeto


# Creación de un objeto (instancia) de la clase Persona
persona1 = Persona("Jhon", "Colombia")

# Acceso a las variables de instancia
print(persona1.nombre)  #  Muestra el valor de la variable de instancia "nombre"

# Acceso a la variable de clase
print(persona1.edad)    #  Muestra el valor de la variable de clase "edad"
