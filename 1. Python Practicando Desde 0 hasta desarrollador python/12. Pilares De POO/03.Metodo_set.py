"""
===================================================
Script: 12.Set.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Ejemplo de encapsulamiento en Programación Orientada a Objetos (POO)
    usando decoradores @property (getter) y @atributo.setter (setter).

    - Getter: Permite acceder a un atributo protegido de forma controlada.
    - Setter: Permite modificar el valor del atributo protegido de forma segura.
===================================================
"""

# Clase con encapsulamiento usando @property y @setter
class A():
    def __init__(self):
        # Atributos protegidos (por convención: un solo guion bajo "_")
        self._cuenta = 0
        self._contador = 0  

    # Getter para _cuenta
    @property
    def cuenta(self):
        """
        Devuelve el valor actual de _cuenta.
        """
        return self._cuenta
    
    # Setter para _cuenta
    @cuenta.setter
    def cuenta(self, cuenta):
        """
        Permite modificar el valor de _cuenta de forma controlada.
        """
        self._cuenta = cuenta
    
    # Getter para _contador
    @property
    def contador(self):
        """
        Devuelve el valor actual de _contador.
        """
        return self._contador



# Ejemplo de uso de la clase
a = A()

# Acceder a los atributos a través de getters
print(a.cuenta)    # Salida: 0
print(a.contador)  # Salida: 0

# Modificar un atributo usando el setter
a.cuenta = 10
print(a.cuenta)    # Salida: 10
