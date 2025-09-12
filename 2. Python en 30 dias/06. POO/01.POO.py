"""
===================================================
Script: 01.POO.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-11
Descripción:
    Ejemplo básico de Programación Orientada a Objetos en Python.
    - Clase Gelatina: con atributos sabor, color y tamaño.
    - Clase Persona: con atributos nombre, edad, nacionalidad y sexo.
    - Métodos para imprimir la información de cada objeto.
===================================================
"""

# Primera clase
class Gelatina():
    # Constructor
    def __init__(self, sabor, color, tamanio):
        self.sabor = sabor
        self.color = color
        self.tamanio = tamanio 
    
    def imprimir(self):
        print(f"La gelatina es de {self.sabor}")
        print(f"La gelatina se ve {self.color}")
        print(f"La gelatina es de un tamaño {self.tamanio}\n")


# Segunda clase
class Persona():
    def __init__(self, nombre, nacionalidad, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.sexo = sexo 

    def imprimirPersona(self):
        print(f"Tu nombre es: {self.nombre}")
        print(f"Tu edad es: {self.edad}")
        print(f"Tu sexo es: {self.sexo}")
        print(f"Tu nacionalidad es: {self.nacionalidad}\n")


# Creamos instancias de Gelatina
gel1  = Gelatina("Fresa", "Rojo", "Grande")
gel2 = Gelatina("Mora", "Morado", "Mediana")

gel1.imprimir()
gel2.imprimir()

# Creamos instancia de Persona
persona1 = Persona("Jhon", "Colombiano", 25, "Masculino")
persona1.imprimirPersona()
