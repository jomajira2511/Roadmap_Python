"""
===================================================
Script: 04.Parametros_Indefinidos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Ejemplo de uso de parámetros indefinidos (*args) en Python.

    - *args permite recibir un número variable de argumentos 
        posicionales en forma de tupla.
    - Esto es útil cuando no conocemos de antemano cuántos valores 
        se pasarán a la función.

    Objetivo:
        - Definir una función 'argumento' que acepte múltiples valores 
            y retorne el tipo de dato recibido.
===================================================
"""

# Definición de la función con *num para aceptar múltiples argumentos
def argumento(*num):
    return type(num)


# Llamada a la función enviando múltiples argumentos
print(argumento(1, 2, 3, 4, 5, 6))
