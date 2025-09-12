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

# ===================================================
# Clase Gelatina
# Representa un postre con atributos básicos.
# ===================================================
class Gelatina:
    def __init__(self, sabor, color, tamanio):
        """
        Constructor de Gelatina.
        Parámetros:
            sabor (str): Sabor de la gelatina.
            color (str): Color de la gelatina.
            tamanio (str): Tamaño de la gelatina.
        """
        self.sabor = sabor
        self.color = color
        self.tamanio = tamanio 
    
    def imprimir(self):
        """
        Imprime en consola las características de la gelatina.
        """
        print(f"La gelatina es de {self.sabor}")
        print(f"La gelatina se ve {self.color}")
        print(f"La gelatina es de un tamaño {self.tamanio}\n")


# ===================================================
# Clase Persona
# Representa a una persona con datos básicos.
# ===================================================
class Persona:
    def __init__(self, nombre, edad, nacionalidad, sexo):
        """
        Constructor de Persona.
        Parámetros:
            nombre (str): Nombre de la persona.
            edad (int): Edad de la persona.
            nacionalidad (str): Nacionalidad de la persona.
            sexo (str): Sexo de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.sexo = sexo 

    def imprimirPersona(self):
        """
        Imprime en consola los datos de la persona.
        """
        print(f"Tu nombre es: {self.nombre}")
        print(f"Tu edad es: {self.edad}")
        print(f"Tu sexo es: {self.sexo}")
        print(f"Tu nacionalidad es: {self.nacionalidad}\n")


# ===================================================
# Bloque principal de ejecución
# Se crean instancias y se llaman a los métodos.
# ===================================================

# Instancias de Gelatina
gel1  = Gelatina("Fresa", "Rojo", "Grande")
gel2 = Gelatina("Mora", "Morado", "Mediana")

gel1.imprimir()
gel2.imprimir()

# Instancia de Persona
#  OJO: El orden de los parámetros debe coincidir con el constructor.
#         (nombre, edad, nacionalidad, sexo)
persona1 = Persona("Jhon", 25, "Colombiano", "Masculino")
persona1.imprimirPersona()
