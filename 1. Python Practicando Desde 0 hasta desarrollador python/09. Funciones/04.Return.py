"""
===================================================
Script: 04.Return.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-09
Descripción:
    Ejemplo de funciones en Python que devuelven valores de diferentes tipos de datos.
    Se muestran funciones que retornan:
        - Enteros
        - Decimales
        - Cadenas de texto
        - Múltiples valores en una sola llamada
===================================================
"""

# --------------------------------------------------
# Definición de funciones con distintos tipos de retorno
# --------------------------------------------------

def entero():
    """Retorna un valor entero."""
    print("Este es un dato entero")
    return 10  # Retorna un entero


def decimal():
    """Retorna un valor decimal (float)."""
    print("Este es un dato decimal")
    return 90.99  # Retorna un decimal


def frase():
    """Retorna una cadena de texto."""
    return "Hola mundo"  # Retorna un string


def asignacion():
    """Retorna múltiples valores en forma de tupla."""
    return 1, 2, 3, 4, 5  # Retorna una tupla de enteros


# --------------------------------------------------
# Llamadas a las funciones y visualización de resultados
# --------------------------------------------------

# Para visualizar los valores retornados se imprimen en consola
print(entero())     # Muestra un entero
print(decimal())    # Muestra un decimal
print(frase())      # Muestra una cadena

# Asignación múltiple: cada variable recibe un valor del retorno
a, b, c, d, e = asignacion()
print(a, b, c, d, e)
