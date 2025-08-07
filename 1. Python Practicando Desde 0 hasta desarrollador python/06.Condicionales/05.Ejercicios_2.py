
"""
===================================================
Script: 05.Condicionales_String.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-07
Descripción:
    Este script contiene dos ejercicios que combinan condicionales y manipulación
    de cadenas en Python:
    
    Ejercicio 1:
    Escribe un programa que pida dos palabras y diga si riman o no. 
    Si coinciden las tres últimas letras tiene que decir que riman. 
    Si coinciden sólo las dos últimas tiene que decir que riman un poco 
    y si no, que no riman.

    Ejercicio 2:
    Crear un programa que permita al usuario elegir un candidato por el cual votar.
    Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, 
    candidato C por el partido azul. Según el candidato elegido (A, B ó C) se debe imprimir 
    el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. 
    Si el usuario ingresa una opción que no corresponde, indicar “Opción errónea”.
===================================================
"""

print ("-------------------EJERCICIO 1------------------------------------")
#Ingreso de datos por teclado 
print("\n Ingrese 2 palabras y le dire si riman o no ")
Palabra1 = input("Ingresa una palabra : ")
Palabra2 = input("Ingrese otra palabra :")

#Operacion e impresion de datos

if Palabra1[-3:] == Palabra2[-3:]:  #Valido si las ultimas 3 palabras son iguales 
    print("las palabas riman")
elif Palabra1[-2:] == Palabra2[-2:]:  #Valido si las ultimas 2 son iguales 
    print("las palabas riman un poco")
else:
    print("las palabras no riman") #Cuando no coincide ninguna


print ("-------------------EJERCICIO 2------------------------------------")
print("Bienvenido al sistema electoral, a continuacion te dire los posibles candidatos")
print("candidato A por el partido rojo")
print("candidato B por el partido verde")
print("candidato C por el partido azul")
#Ingreso de datos por teclado 
Voto = input("Ingrese la letra del candidato que desea votar")
#Operacion e impresion de datos 
if Voto.upper() == "A":
    print("Usted ha votado por el partido Rojo")
elif Voto.upper() == "B":
    print("Usted ha votado por el partido Verde")
elif Voto.upper() == "C":
    print("Usted ha votado por el partido Azul")
else:
    print("La letra ingresada no corresponde a ningun candidato ")
