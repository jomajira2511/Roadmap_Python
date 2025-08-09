"""
===================================================
Script: 12.Condicionales_if_else.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-07
Descripción:
    Este script muestra el uso de estructuras condicionales 
    en Python utilizando `if` y `else` para tomar decisiones 
    basadas en la edad ingresada por el usuario.

    Contenido abordado:
    • Entrada de datos por teclado con `input()`.
    • Conversión de cadenas a enteros con `int()`.
    • Condicional `if` para verificar si una persona es mayor de edad.
    • Condicional `else` para manejar el caso contrario.
===================================================
"""
#vamos a verificar si es mayor de edad

#Ingreso de datos
Edad = int(input("Ingresa tu edad "))

#Incio condiciones
if Edad >= 18:   #condicional if (SI), en caso de que se cumpla, pasa a las acciones dentro del condicional 
    print(" \n Eres mayor de edad")
else: #condicional else (SINO), en casi de que la condicion principal no se cumpla, realiza las acciones dentro del condicional 
    print(" \n Eres menor de edad" )
