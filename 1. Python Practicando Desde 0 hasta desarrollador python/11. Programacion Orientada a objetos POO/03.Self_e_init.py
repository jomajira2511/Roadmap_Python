"""
===================================================
Script: 08.Clases_y_Constructores.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Ejemplos prácticos de Programación Orientada a Objetos (POO) en Python.
    Se muestran dos conceptos clave:
    
    1. Modificación de atributos de clase mediante un método.
    2. Uso del método constructor (__init__) para inicializar atributos de instancia.

    Objetivos:
    - Diferenciar entre atributos de clase y atributos de instancia.
    - Comprender cómo y cuándo usar self para modificar valores de un objeto.
    - Aprender a inicializar objetos con valores personalizados.
===================================================
"""


# Ejemplo 1: Atributos de clase y modificación con un método

class FabricaTelefonos():
    marca = "Samsung"  # Atributo de clase: compartido por todas las instancias

    def ElaborarHuawei(self):
        """
        Método que cambia el atributo 'marca' del objeto actual a 'Huawei'.
        Al usar 'self', el cambio solo afecta a esa instancia.
        """
        self.marca = "Huawei" 

# Creación de un objeto a partir de la clase FabricaTelefonos
telefono = FabricaTelefonos()

# Imprime la marca inicial (atributo de clase por defecto)
print(telefono.marca)  # Resultado: Samsung

# Llamado al método para cambiar la marca
telefono.ElaborarHuawei()  # Aquí se ejecuta el cambio de marca

# Imprime la marca después del cambio (afecta solo a este objeto)
print(telefono.marca)  # Resultado: Huawei



# Ejemplo 2: Uso de constructor (__init__) y atributos de instancia
class FabricaTelefono():
    def __init__(self, marca, color):
        """
        Constructor de la clase.
        
        Parámetros:
            marca (str): Marca del teléfono.
            color (str): Color del teléfono.
        
        Se ejecuta automáticamente al crear una nueva instancia,
        asignando los valores recibidos a los atributos del objeto.
        """
        self.marca = marca    # Atributo de instancia: propio de cada objeto
        self.color = color    # Atributo de instancia: propio de cada objeto

# Creación de un objeto con valores personalizados
telefono = FabricaTelefono("Motorola", "Negro")

# Acceso y visualización de un atributo de instancia
print(telefono.marca , telefono.color)  # Resultado: Motorola Negro
