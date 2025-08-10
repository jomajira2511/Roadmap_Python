"""
===================================================
Script: 07,Ejercicios.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Este script resuelve dos ejercicios prácticos enfocados en el uso de funciones
    con argumentos fijos y parámetros indefinidos (*args).

    Ejercicio 1:
        - Crear una función que calcule el área de un cuadrado 
            recibiendo altura y altura como parámetros.
        - Crear una función que calcule el área de un círculo 
            recibiendo el radio como parámetro.

    Ejercicio 2:
        - Crear una función que reciba una muestra de números
            y devuelva su media aritmética.

    Objetivos:
        - Aplicar conceptos de variables globales.
        - Usar parámetros con valores definidos y parámetros indefinidos (*args).
        - Implementar operaciones matemáticas básicas.
===================================================
"""
PI = 3.1416  # Defino un valor global 


def area_cuadrado(altura1,altura2):  # Recibo dos argumentos
    # Operacion para el area del cuadrado 
    return print("El area del cuadrado es igual : {}".format(altura1 * altura2))  


def area_circulo(radio): 
    # Operacion para el area del circulo 
    return print("El area del circulo es igual a : {} ".format((radio ** 2) * PI))

# Hace el  llamado a la funcion y envia los argumentos
area_cuadrado(10,10)

# Hace el  llamado a la funcion y envia los argumentos
area_circulo(10)


def media(*numeros):  # Declaramos la funcion y se prepara para recibir valores indefinidos 
    total = sum(numeros)  # Suma todos los valores que nos da el usuario
    cantidad = len(numeros) # Arroja la cantidad de elementos 
    return total / cantidad  # Calcula la media de elementos  y arroja el resultado 

# Hace el  llamado a la funcion y envia los argumentos
print(media(1, 2, 3, 4, 5, 6, 7))

