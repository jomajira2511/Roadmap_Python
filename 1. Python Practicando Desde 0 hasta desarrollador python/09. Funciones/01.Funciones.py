"""
===================================================
Script: 01.Funciones.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-09
Descripción:
    Introducción a la creación y uso de funciones en Python.
    Se definen dos funciones:
        - saludo(): imprime un mensaje simple en pantalla.
        - tabla7(): muestra la tabla de multiplicar del 7 del 0 al 10.
    Se demuestra la llamada a funciones para ejecutar su bloque de código.
===================================================
"""
# Creacion de funciones en python

def saludo():   # Definicion de funcion 
    print("Hola mundo") #Argumento de la funcion

def tabla7():  # Definimos el nombre de la funcion 
    # Declaramos un ciclo para que nos muestre la tabla del 7 del 1 al 10 
    for i in range(11):  
        print( "7 x {} = {}".format( i , i*7))   # Imprimo el valor de la iteracion 

saludo()  #llamamos la funcion, y ella ejecuta el argumento declarado dentro de la funcion

tabla7()  #llamamos al funcion que nos muestra la tabla del 7