"""
===================================================
Script: 05.Ejercicio_5.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-19
Descripción:
    Ejercicio:
    Crear un programa con tres clases Universidad, con atributos 
    nombre (Donde se almacena el nombre de la Universidad). Otra 
    llamada Carerra, con los atributos especialidad (En donde me guarda 
    la especialidad de un estudiante). Una ultima llamada Estudiante, 
    que tenga como atributos su nombre y edad. El programa debe imprimir 
    la especialidad, edad, nombre y universidad de dicho estudiante con 
    un objeto llamado persona.
===================================================
"""

# Clase Universidad con atributo Nombre
class Universidad:
    def __init__(self, Nombre):
        """Inicializa el nombre de la universidad."""
        self.Nombre = Nombre


# Clase Carrera con atributo especialidad
class Carrera:
    def carrera(self, especialidad):
        """Asigna la especialidad del estudiante."""
        self.especialidad = especialidad


# Clase Estudiante que hereda de Universidad y Carrera
class Estudiante(Universidad, Carrera):
    def datos(self, nombre, edad):
        """
        Método que recibe los datos del estudiante y muestra
        su nombre, edad, especialidad y universidad.
        """
        self.nombre = nombre
        self.edad = edad
        print("Mi nombre es: {}, tengo {} años, mi especialidad es {}, "
                "y estudio en la universidad {}"
                .format(self.nombre, self.edad, self.especialidad, self.Nombre))


# Creación de un objeto de tipo Estudiante
persona = Estudiante("Andes")
persona.carrera("Sistemas")
persona.datos("Juan", 25)
