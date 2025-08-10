"""
===================================================
Script: 02.Metodos_y_atributos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Ejemplo de uso de atributos y métodos en una clase de Python:
        - Definición de atributos de clase (propiedades comunes a todos los objetos).
        - Definición de métodos de instancia (funcionalidades que pueden ejecutar los objetos).
        - Creación e interacción con objetos de la clase.
===================================================
"""

# Definición de la clase
class FabricaTelefonos:
    # Atributos de clase (propiedades comunes para todos los objetos)
    marca = "Motorola"
    color = "Rojo"
    memoria_ram = 32
    almacenamiento = 256

    # Método de instancia que recibe un argumento y retorna un mensaje
    def llamar(self, mensaje):
        return mensaje
    
    # Método de instancia que imprime una acción
    def escuchar_musica(self):
        print("Estás escuchando música")


# Creación de un objeto (instancia) de la clase
telefono = FabricaTelefonos()

# Acceso a los atributos del objeto
telefono.marca
telefono.color
telefono.memoria_ram
telefono.almacenamiento

# Uso de métodos del objeto
print(telefono.llamar("Hola, ¿cómo vas?"))
telefono.escuchar_musica()
