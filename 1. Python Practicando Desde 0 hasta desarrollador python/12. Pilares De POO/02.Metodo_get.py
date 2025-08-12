"""
===================================================
Script: 02.Metodo_get.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Ejemplo de uso del decorador @property en Python para implementar getters.
    El decorador @property permite acceder a un método como si fuera un atributo.
    Esto ayuda a proteger atributos internos y controlar su acceso.
===================================================
"""


# Clase con atributos "protegidos" y getters usando @property

class A():
    def __init__(self):
        # Atributos protegidos (por convención se usa un guion bajo "_")
        self._cuenta = 0
        self._contador = 0  

    @property
    def cuenta(self):
        """
        Getter para _cuenta.
        Permite obtener el valor de _cuenta como si fuera un atributo normal.
        """
        return self._cuenta
    
    @property
    def contador(self):
        """
        Getter para _contador.
        """
        return self._contador



# Ejemplo de uso de la clase
a = A()

# Accediendo a los atributos a través de los getters (como si fueran públicos)
print(a.cuenta)    # Salida: 0
print(a.contador)  # Salida: 0
