"""
===================================================
Script: 01.Errores_y_excepciones.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Este script solicita al usuario su edad y valida que
    el valor ingresado sea un número entero, utilizando
    manejo de excepciones con try-except-finally.
    
    Flujo:
        - Se solicita la edad por consola.
        - Si el usuario ingresa un valor no entero, se muestra
            un mensaje de error y se repite la solicitud.
        - El bloque `finally` ejecuta un mensaje de finalización
            en cada ciclo.
===================================================
"""

# Bucle infinito para pedir la edad hasta que el usuario ingrese un valor válido
while True:
    try:
        # Solicita la edad y convierte el valor a entero
        edad = int(input("Ingresa tu edad: "))
        
        # Muestra el resultado
        print("Tu edad es:", edad)
        
        # Rompe el bucle si la conversión fue exitosa
        break
    
    except ValueError:
        # Captura el error si el valor ingresado no es un entero
        print("Ingresaste un valor erróneo. Por favor, introduce un número entero.")
    
    finally:
        # Mensaje de finalización de ciclo (se ejecuta siempre)
        print("La ejecución ha finalizado.")
