"""
===================================================
Script: 01.Declarar_funciones.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-10
Descripción:
    Ejemplo de declaración y uso de funciones en Python:
    - Una función es un bloque de código reutilizable.
    - Se define con la palabra reservada 'def'.
    - Puede recibir parámetros, retornar valores y encapsular lógica.
    - Las variables dentro de una función tienen alcance local
    (solo existen dentro de ella).
===================================================
"""

# -------------------------------------------------
# Definición de función sin parámetros
# -------------------------------------------------
def saludar():
    """Imprime un saludo simple en consola."""
    print("HOLA MUNDO ")

# Llamada de la función
saludar()


# -------------------------------------------------
# Función para realizar una suma
# -------------------------------------------------
def sumar():
    """Ejemplo de suma dentro de una función."""
    i = 10  # Variable local
    m = 4   # Variable local
    print("El resultado de la suma es:", i + m)

# Llamada de la función
sumar()


# -------------------------------------------------
# Función para realizar una resta
# -------------------------------------------------
def restar():
    """Ejemplo de resta dentro de una función."""
    m = 10
    n = 5
    print("El resultado de la resta es:", m - n)

# Llamada de la función
restar()
