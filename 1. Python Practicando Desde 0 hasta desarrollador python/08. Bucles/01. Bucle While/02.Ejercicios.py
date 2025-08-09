"""
===================================================
Script: 11.Ejercicios_While.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-09
Descripción:
    Este script contiene dos ejercicios prácticos usando 
    bucles `while` para resolver problemas interactivos.

    Ejercicio 1:
        - Solicitar un número al usuario.
        - Mostrar la tabla de multiplicar de ese número del 1 al 10.
    
    Ejercicio 2:
        - Solicitar la edad del usuario.
        - Mostrar por pantalla todos los años que ha cumplido
            desde 1 hasta su edad actual.
===================================================
"""
print("-------------------------EJERCICIO 1---------------------------------")

# Solicitud de datos al usuario 
Numero = int(input("Ingresa un numero y te dire la tabla de multiplicar del 1 al 10 ")) 
i = 0 #creamos la variable iteradora
while i <= 10:
    print("{} x {} : {}".format(Numero, i,(Numero*i)) )
    i +=1



print("-------------------------EJERCICIO 2---------------------------------")

#Solicitud de datos al usuario
Edad = int(input("Ingrese su edad y te dire el total cumplido : "))
j = 0  # se crea la variable iteradora 
while j < Edad:
    j += 1
    print("Haz cumplido {} años ".format(j))
    

