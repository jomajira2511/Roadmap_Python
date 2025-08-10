"""
===================================================
Script: 09.Metodos_especiales.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Ejemplo práctico del uso de constructores (__init__),
    destructores (__del__) y representación en cadena (__str__)
    en Programación Orientada a Objetos (POO) con Python.

    Objetivos:
    - Comprender cómo inicializar atributos al crear un objeto.
    - Implementar un método para mostrar la representación textual del objeto.
    - Observar el ciclo de vida de un objeto: creación y destrucción.
===================================================
"""


# Clase con constructor, destructor y método __str__
class FabricaTelefono():
    def __init__(self, marca, color):
        """
        Constructor de la clase. 
        Se ejecuta automáticamente al instanciar un nuevo objeto.

        Parámetros:
            marca (str): Marca del teléfono.
            color (str): Color del teléfono.
        """
        self.marca = marca
        self.color = color
        print("El objeto {} ha sido creado".format(self.marca))

    def __str__(self):
        """
        Método especial que devuelve la representación en cadena del objeto.
        Se ejecuta automáticamente cuando se usa print() sobre la instancia.
        """
        return "El objeto es {} ".format(self.marca)

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta cuando el objeto es eliminado de la memoria.
        """
        print("El objeto {} ha sido destruido".format(self.marca))



# Creación de un objeto e interacción con sus métodos
telefono = FabricaTelefono("Motorola", "Negro")  
# Mensaje del constructor: "El objeto Motorola ha sido creado"

# Acceso y visualización de atributos de instancia
print(telefono.marca, telefono.color)  # Resultado: Motorola Negro

# Llamada implícita a __str__ mediante print()
print(telefono)  # Resultado: "El objeto es Motorola"
