"""
===================================================
Script: 15.Condicionales_Ejercicios.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-07
Descripción:
    Este script incluye dos ejercicios prácticos que aplican 
    estructuras condicionales en Python.

    Ejercicio 1:
        Crear un programa que pida al usuario una letra, y si es vocal, 
        muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal.

    Ejercicio 2:
        Escribir un programa que, dado un número entero, muestre su valor absoluto.
        Nota: para los números positivos su valor absoluto es igual al número (el 
        valor absoluto de 52 es 52), mientras que, para los negativos, su valor 
        absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

    Contenido abordado:
    • Entrada de datos con `input()`.
    • Conversión de texto a minúscula con `.lower()`.
    • Conversión de texto a número con `int()`.
    • Operadores relacionales y estructura condicional `if` y `else`.
===================================================
"""
print ("-------------------EJERCICIO 1------------------------------------")
#Ingreso de datos por teclado 
Vocal = input("Ingresa una vocal : ")
Vocal_minuscula = Vocal.lower()  #Convierte el dato ingresado a minuscula 

#Operacion e impresion de datos
if Vocal_minuscula in ('a','e','i','o','u') : # La condición pregunta si la vocal (convertida a minúscula) pertenece al grupo de vocales
    print("Ingresaste  la vocal {}".format(Vocal))
else:
    print(" {} No es una vocal \n".format(Vocal))


print ("-------------------EJERCICIO 2------------------------------------")
#Ingreso de datos por teclado 
Numero = int(input("Ingresa un numero y lo convertire a absoluto "))

#Operacion e impresion de datos
if Numero < 0:  #Valida la condicion para saber si es absoluto 
    Absoluto = Numero * -1 #En caso de que cumpla la condicion, lo convierte a absoluto para despues mostrarlo por pantalla
    print("El numero que ingresaste fue {} y su numero absoluto es {}" .format(Numero, Absoluto))
else:
    print("El numero que ingresaste fue {} y su numero absoluto es {}" .format(Numero, Numero ))

