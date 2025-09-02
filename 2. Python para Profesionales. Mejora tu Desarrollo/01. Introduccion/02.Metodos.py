"""
===================================================
Script: 02.Metodos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-02
Descripción:
    Ejemplo práctico de los diferentes tipos de métodos
    en Programación Orientada a Objetos con Python:

    - Métodos de instancia: requieren una instancia para usarse
      y acceden a variables de instancia.
    - Métodos de clase: pueden llamarse sin instanciar la clase.
      Usan el decorador @classmethod.
    - Métodos estáticos: no dependen de la instancia ni de la clase.
      Usan el decorador @staticmethod.
===================================================
"""

# ===================================================
# Métodos de INSTANCIA
# ===================================================

class Persona():
    edad = 20  #  Variable de clase, compartida por todas las instancias
    
    def __init__(self, nombre, nacionalidad):
        """
        Constructor de la clase Persona.
        """
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def correr(self):
        """
        Método de instancia → requiere crear un objeto
        para poder ser llamado.
        """
        print("Estoy corriendo")


# Uso del método de instancia
print(Persona.edad)  #  Accediendo a la variable de clase
persona1 = Persona("Jhon", "Colombia")  
persona1.correr()  #  Llamando al método de instancia


# ===================================================
# Métodos de CLASE
# ===================================================

class Humano():
    def __init__(self):
        pass

    def despedir(self):
        """
        Método de instancia normal.
        """
        print("Te despido")
    
    @classmethod
    def saludar(cls, nombre):
        """
        Método de clase → no requiere crear un objeto,
        se invoca directamente desde la clase.
        """
        print("Te saludo desde mi método de clase", nombre)


# Uso del método de clase
Humano.saludar("Jhon")  #  Sin necesidad de instanciar la clase


# ===================================================
# Métodos ESTÁTICOS
# ===================================================

class SerVivo():
    def __init__(self):
        pass

    @classmethod
    def correr(cls):
        """
        Método de clase en SerVivo.
        """
        print("Estoy corriendo")
    
    @staticmethod
    def nadar():
        """
        Método estático → no depende ni de la clase ni de la instancia.
        """
        print("Estoy nadando")


# Uso del método estático
Pedro = SerVivo()
Pedro.nadar()  #  Llamado desde una instancia
SerVivo.nadar()  #  También puede llamarse directamente desde la clase
