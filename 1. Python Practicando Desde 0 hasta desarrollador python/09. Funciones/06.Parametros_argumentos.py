"""
===================================================
Script: 06.Parametros_y_Argumentos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Ejemplo práctico sobre el uso de parámetros y argumentos en funciones.

    - Parámetros: variables declaradas en la definición de la función.
    - Argumentos: valores concretos que se pasan a los parámetros cuando 
    la función es llamada.

    Objetivo:
        - Definir una función 'suma' que reciba dos números y retorne su suma.
        - Demostrar cómo reutilizar la función enviando distintos argumentos.
===================================================
"""

def suma(num1 ,  num2 ):  # Funcion con parametros que la funcion va a utilizar 
    """
    Calcula la suma de dos números.
    
    Parámetros:
        num1 (int | float): Primer número a sumar.
        num2 (int | float): Segundo número a sumar.
    
    Retorna:
        int | float: Resultado de la suma.
    """
    return num1 + num2



# LLamado a la funcio -> le envio los argumentos para usar en la funcion (num1 , num 2)
print(suma(10 , 20 )) 

# Al usar parametros, y poder enviarle argumentos se puede reutilizar la funcion, ya que ella hace una funcion en especifico 
print(suma(10 , 2000 ))  
