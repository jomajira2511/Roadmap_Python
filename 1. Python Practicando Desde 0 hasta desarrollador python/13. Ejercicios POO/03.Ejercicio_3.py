"""
===================================================
Script: 03.Ejercicio_3.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-18
Descripción:
    Ejercicio:
    Crear una clase Fabrica que tenga los atributos de Llantas, 
    Color y Precio; luego crear dos clases mas que hereden de 
    Fabrica, las cuales son Moto y Carro. Crear metodos que 
    muestren la cantidad de llantas, color y precio de ambos 
    transportes. Por ultimo, crear objetos para cada clase y 
    mostrar por pantalla los atributos de cada uno.
===================================================
"""

# Clase base que representa la Fábrica de vehículos
class Fabrica:
    def __init__(self, llantas, color, precio):
        """
        Constructor de la clase Fabrica.
        Inicializa los atributos comunes para cualquier vehículo.
        """
        self.llantas = llantas
        self.color = color
        self.precio = precio
    

# Clase Carro que hereda de Fabrica
class Carro(Fabrica):
    def datos(self):
        """Muestra los datos del carro: llantas, color y precio."""
        print("La cantidad de llantas es de:", self.llantas)
        print("El color del carro es:", self.color)
        print("El precio del carro es:", self.precio)


# Clase Moto que hereda de Fabrica
class Moto(Fabrica):
    def datos(self):
        """Muestra los datos de la moto: llantas, color y precio."""
        print("La cantidad de llantas es de:", self.llantas)
        print("El color de la moto es:", self.color)
        print("El precio de la moto es:", self.precio)


# Creación de objetos de las clases derivadas
moto = Moto(2, "Negro", 2000)
moto.datos()

print("-" * 40)  # Separador visual

carro = Carro(4, "Azul", 4000)
carro.datos()
