"""
===================================================
Script: 04.Ejercicio_4py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-19
Descripción:
    Ejercicio:
    Crear una clase llamada Marino(), con un metodo que sea hablar, 
    en donde muestre un mensaje que diga "Hola...". Luego, crear 
    una clase Pulpo() que herede Marino, pero modificar el mensaje 
    de hablar por "Soy un Pulpo". Por ultimo, crear una clase Foca(), 
    heredada de Marino, pero que tenga un atributo nuevo llamado 
    mensaje y que muestre ese mensaje como parametro.
===================================================
"""

# Clase base Marino
class Marino:
    def hablar(self):
        """Método que imprime un saludo genérico."""
        print("Hola...")


# Clase Pulpo heredada de Marino, sobreescribe el método hablar
class Pulpo(Marino):
    def hablar(self):
        """Método sobrescrito que imprime un mensaje propio del pulpo."""
        print("Soy un pulpo")


# Clase Foca heredada de Marino, agrega el atributo mensaje
class Foca(Marino):
    def hablar(self, mensaje):
        """
        Método sobrescrito que recibe un mensaje como parámetro
        y lo imprime.
        """
        self.mensaje = mensaje
        print(self.mensaje)


# Creación de objetos y ejecución de métodos
marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola, soy una foca")
