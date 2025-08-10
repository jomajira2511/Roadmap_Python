"""
===================================================
Script: 02.Ejercicios.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-09
Descripción:
    Este script desarrolla dos ejercicios prácticos para afianzar 
    el manejo de listas, funciones, condicionales y uso de librerías en Python.

    Ejercicio 1:
        - Crear una lista principal y dos listas secundarias (pares e impares).
        - Solicitar números al usuario mediante una función (pedir()).
        - Ordenar la lista y separar los valores pares e impares en listas diferentes.

    Ejercicio 2:
        - Crear una función (convertir()) que solicite un número entero positivo.
        - Calcular y mostrar su factorial usando math.factorial().
===================================================
"""

import math
print("----------------------EJERCICIO 1---------------------")

# Creamos las listas 
lista = []
pares  = []  
impares = [] 
num = 0

def pedir():  #Creamos la funcion para pedir los datos 
    i=0  # Declaramos el iterador o bandera 
    while i<=5: # Condicional para ingresar los datos 
        num = float(input("Ingresa un numero : "))  # Pedimos los datos 
        lista.append(num)  # Agregamos los datos a la lista usando la funcion .append()
        i += 1

def ordenar():
    lista.sort()  # Metodo para ordenar la lista
    for i in lista:  # For para separar los datos 
        if i %2 == 0: # Condicional para encontrar pares e impares
            pares.append(i) 
        else:
            impares.append(i)
    print(pares) 
    print(impares)

pedir() # LLamamos la funcion pedir 
ordenar() # LLamamos a funcion ordenar 


print("----------------------EJERCICIO 2---------------------")

def convertir(): # Creamos la funcion para convertir un numero  a factorial
    numero  = int(input("Ingresa un numero entero y positivo y te mostrare el numero vectorial correspondiente "))
    factorial = math.factorial(numero)  # Convertimos el numero a factorial 
    print("El numero ingresado es {} y el factorial es {}".format(numero, factorial))  # Mostramos el numero 

convertir() # llamamos la funcion 


