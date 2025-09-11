"""
===================================================
Script: 03.Enviar_valores.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-10
Descripción:
    Ejemplos de funciones en Python con parámetros 
    y valores de retorno:
    - La función `sumar(op1, op2)` recibe dos argumentos,
    realiza la suma y retorna el resultado.
    - La función `saludar(saludos)` retorna el mensaje
    que recibe como argumento, demostrando cómo se 
    pueden personalizar retornos.
===================================================
"""

# -------------------------------------------------
# Función con parámetros numéricos y retorno
# -------------------------------------------------
def sumar(op1, op2):  
    """
    Realiza la suma de dos números recibidos como parámetros.
    """
    resultado = op1 + op2  # Operación aritmética
    return resultado       # Retorna el valor calculado


print(sumar(2, 3))  # Se envían los valores 2 y 3 como argumentos


# -------------------------------------------------
# Función con parámetros de texto y retorno
# -------------------------------------------------
def saludar(saludos):
    """
    Retorna el mensaje recibido como argumento.
    """
    return saludos


print(saludar("Hola mundo"))  # Imprime el mensaje recibido
