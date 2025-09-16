"""
===================================================
Script: 01.Herencia.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-16
Descripción:
    Ejemplo de herencia en Programación Orientada a Objetos.
    - Clase base: Persona
    - Clase derivada: Empleado (hereda de Persona)
    - Métodos para imprimir datos personales y laborales.
===================================================
"""

# ===================================================
# Clase base: Persona
# ===================================================
class Persona: 
    def __init__(self, nombre, edad, apellido, sexo):
        """
        Constructor de Persona.
        Parámetros:
            nombre (str): Nombre de la persona.
            edad (int): Edad de la persona.
            apellido (str): Apellido de la persona.
            sexo (str): Sexo de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.sexo = sexo
    
    def datosPersonales(self):
        """Imprime los datos básicos de la persona."""
        print(f"El nombre de la persona es: {self.nombre}")
        print(f"El apellido de {self.nombre} es: {self.apellido}")
        print(f"La edad de {self.nombre} es: {self.edad}")
        print(f"El sexo de {self.nombre} es: {self.sexo}")


# ===================================================
# Clase derivada: Empleado
# Hereda de Persona y añade características laborales
# ===================================================
class Empleado(Persona):   
    def datosEmpleados(self, vacaciones, salario):
        """
        Imprime los datos laborales del empleado.
        Parámetros:
            vacaciones (int): Días de vacaciones asignados.
            salario (float): Salario del empleado.
        """
        print(f"Sus días de vacaciones son: {vacaciones}")
        print(f"Su salario es: {salario}")


# ===================================================
# Bloque principal de ejecución
# ===================================================

# Instancia de Persona
miPersona = Persona("Pedro", 23, "Suarez", "Masculino")
miPersona.datosPersonales()

print()  # Separador visual

# Instancia de Empleado
miEmpleado = Empleado("Maria", 22, "Torres", "Femenino")
miEmpleado.datosPersonales()      # Método heredado de Persona
miEmpleado.datosEmpleados(30, 12000)  # Método propio de Empleado
