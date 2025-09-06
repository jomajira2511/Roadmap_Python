"""
===================================================
Script: 03.Decoradores.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-06
Descripción:
    Ejemplo introductorio al uso de decoradores en Python.

    Los decoradores permiten modificar o extender el 
    comportamiento de una función sin alterar su código
    original. Se implementan mediante funciones que reciben
    como argumento otra función y devuelven una nueva función.

    En este script:
    - Se define un decorador básico que envuelve una función.
    - Se utiliza la sintaxis @decorador para aplicarlo a 
      una función común.
===================================================
"""

# ===================================================
# Definición de un decorador básico
# ===================================================
def decorador(funcionComun):
    """
    Recibe una función como parámetro y devuelve otra función
    (funcionDecorada) que puede modificar su comportamiento.
    """
    def funcionDecorada(*args, **kwargs):
        # Antes de ejecutar la lógica de la función decorada
        print("✨ Mi primer decorador ✨")
        # Aquí se podría llamar a la función original si se desea:
        # return funcionComun(*args, **kwargs)
    return funcionDecorada


# ===================================================
# Aplicación del decorador a una función
# ===================================================
@decorador
def funcionComun():
    """
    Función original, que sería envuelta por el decorador.
    """
    print("Mi función común")


# ===================================================
# Ejecución del script
# ===================================================
funcionComun()
