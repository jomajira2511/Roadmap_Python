"""
===================================================
Script: 03.Encapsulamiento.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-16
Descripción:
    Ejemplo de encapsulamiento en Programación Orientada a Objetos.
    - Se encapsula el atributo `marca` con doble guion bajo (__marca).
    - Solo se puede definir al crear el objeto (constructor).
    - Métodos para interactuar con el objeto:
        * arrancar(): indica si el auto está encendido o apagado.
        * __str__(): representación del objeto en forma de cadena.
===================================================
"""

# ===================================================
# Clase Coche
# Representa un automóvil con marca, kilometraje y año.
# Demuestra el uso de encapsulamiento.
# ===================================================
class Coche:
    def __init__(self, marca, km, anio):
        """
        Constructor de la clase Coche.
        Parámetros:
            marca (str): Marca del vehículo (encapsulada).
            km (int): Kilometraje recorrido.
            anio (int): Año de fabricación.
        """
        self.__marca = marca   # Atributo privado (encapsulado)
        self.km = km
        self.anio = anio
        print(f"Se ha creado el vehículo {self.__marca}")

    def arrancar(self, arrancamos):
        """
        Método que simula el encendido del vehículo.
        Parámetros:
            arrancamos (bool): True si se quiere encender, False si se apaga.
        Retorna:
            str: Mensaje con el estado del vehículo.
        """
        self.enmarcha = arrancamos
        if self.enmarcha:
            return "El auto está encendido"
        else:
            return "El auto está apagado"

    def __str__(self):
        """
        Representación en cadena del objeto.
        Retorna una descripción del coche.
        """
        return "El auto es un {}, tiene {} KM y es del año {}".format(
            self.__marca, self.km, self.anio
        )


# ===================================================
# Bloque principal de ejecución
# ===================================================

# Primera instancia
MiCoche = Coche("Audi", 200, 1993)
print(str(MiCoche))
print(MiCoche.arrancar(True))

print()

# Segunda instancia
MiCoche2 = Coche("BMW", 222, 1990)

# Intento de modificar la marca desde fuera
# Esto no afecta el valor encapsulado (__marca)
MiCoche2.marca = "Ciclomotor"  
print(str(MiCoche2))

# ===================================================
# NOTA:
# El encapsulamiento con __ (doble guion bajo) en Python
# hace que el atributo sea "privado" y no se pueda modificar
# directamente desde fuera de la clase.
# ===================================================
