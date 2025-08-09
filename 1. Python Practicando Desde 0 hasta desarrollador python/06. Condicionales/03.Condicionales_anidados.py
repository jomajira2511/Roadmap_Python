"""
===================================================
Script: 14.Condicionales_Anidados.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-07
Descripción:
    Este script demuestra el uso de condicionales anidados en Python
    para validar múltiples condiciones encadenadas.

    El programa solicita al usuario que ingrese su nombre y edad.
    Luego evalúa si el nombre corresponde a "Jhon" (ignorando mayúsculas)
    y si es mayor de edad, mostrando un mensaje correspondiente.

    Contenido abordado:
    • Entrada de datos con `input()`.
    • Conversión de texto a minúscula con `.lower()`.
    • Conversión de texto a número con `int()`.
    • Condicionales simples y anidados con `if`, `else`.
===================================================
"""



#Declaracion de variables
Nombre = input("Ingresa tu nombre : ")  #ingresar nombre por teclado 
Edad = int(input("Ingresa tu edad : ")) #ingresar edad por teclado 
Validar = Nombre.lower() #convierte la cadena a minusculas para valdiarla en el condicional 

if Nombre == "jhon":  # primer condicional, para validar el nombre 
    if Edad >= 18:  #if anidado que permite validar 2 variables para la misma condicion 
        print("Tu eres Jhon, y eres mayor de edad") #mensaje a imprimir en caso de ser correctas ambas condiciones 
    else:
        print("Eres Jhon, pero no eres mayor de edad ") #mensaje en caso de que no se cumpla la segunda condicion 
else: 
    print("Tu no eres Jhon") #Mensaje a imprimir en caso de que no cumpla con las condiciones     

