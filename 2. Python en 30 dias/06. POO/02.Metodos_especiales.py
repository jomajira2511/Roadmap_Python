"""
===================================================
Script: 02.Metodos_Especiales.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-11
Descripción:
    Ejemplo del uso de métodos especiales en clases de Python.
    - __init__: Constructor que inicializa los atributos.
    - __del__: Destructor que elimina la instancia.
    - __str__: Representación en forma de cadena del objeto.
===================================================
"""

# ===================================================
# Clase Coche
# Representa un automóvil con marca, kilometraje y año.
# ===================================================
class Coche:
    def __init__(self, marca, km, anio):
        """
        Constructor de la clase Coche.
        Parámetros:
            marca (str): Marca del vehículo.
            km (int): Kilometraje recorrido.
            anio (int): Año de fabricación.
        """
        self.marca = marca
        self.km = km
        self.anio = anio
        print(f"Se ha creado el vehículo {self.marca}")

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta automáticamente al eliminar la instancia.
        """
        print(f"Se ha vendido el auto {self.marca}")

    def __str__(self):
        """
        Representación en cadena del objeto.
        Retorna una descripción amigable del coche.
        """
        return "El auto es un {}, tiene {} KM y es del año {}".format(
            self.marca, self.km, self.anio
        )


# ===================================================
# Bloque principal de ejecución
# ===================================================

# Creación de un objeto Coche
MiCoche = Coche("Audi", 200, 1993)

# Llamada implícita a __str__ al imprimir el objeto
print(str(MiCoche))

# Eliminación manual de la instancia (invoca __del__)
del MiCoche




