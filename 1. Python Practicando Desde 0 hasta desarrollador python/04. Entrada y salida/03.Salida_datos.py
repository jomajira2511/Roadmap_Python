"""
===================================================
Script: 06.Salida_datos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-06
Descripción:
    Este script muestra ejemplos del uso de la salida de 
    datos en Python mediante la función `print()`. 
    Se exploran diferentes formas de presentar información
    al usuario en pantalla.
===================================================
"""
print ("-------------------------INGRESO DE DATOS POR TECLADO-------------------")
Nombre = input("Ingresa tu Nombre : ") ##Permite ingresar valores por teclado y se asignan a la variable 
Edad = int(input("Ingresa tu edad : ")) ##Permite ingresar un valor, que se asigna como entero

print ("-------------------------SALIDA DE DATOS POR PANTALLA-------------------")
print("Tu nombre es : ", Nombre)
print("Tu edad es : ", Edad)
print("Tu nombre es : ",Nombre, "y tu edad es :",Edad)  #Concatenacion de cadenas usando , para unirlas 
print("Hola {} Tienes {} años". format(Nombre, Edad))  #concatena cadenas usando la funcion format para unirlas 

