"""
===================================================
Script: 04.Ejercicios_Salida_Datos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-06
Descripción:
    Este script contiene ejercicios prácticos relacionados 
    con la manipulación de texto y la salida de datos en 
    pantalla utilizando la función `print()`.

    Ejercicio 1  Intercambio de mayúsculas y minúsculas:
    El programa solicita al usuario que ingrese:
        • Una vocal en minúscula.
        • Una letra en mayúscula.
    Luego, convierte la vocal a mayúscula y la letra a minúscula,
    y muestra el resultado concatenado.

    Ejercicio 2  Presentación de datos personales:
    El programa solicita al usuario su:
        • Nombre
        • Edad
        • Sexo
    Finalmente, imprime esta información en pantalla con formato:
        Te llamas: <nombre>
        Tu edad es: <edad>
        Eres: <sexo>
===================================================
"""
print("------------------EJERCICIO 1------------------------")
##ingreso de variables 
vocal = input("Ingresa 1 vocal en minuscula : ")
letra = input("Ingresa 1 letra en mayuscula : ")

#Impresion de valores 
print("La vocal ingresada fue : ",vocal," Ahora la vocal convertida es : ", vocal.upper())
print("La letra ingresada fue : ",letra," ahora la letra convertida es : ", letra.lower())
print("La solucion concatenada seria Vocal convertida {} y letra convertida {}".format(vocal.upper(), letra.lower()))

print("------------------EJERCICIO 2------------------------")
#Ingreso de datos
Nombre = input("Ingresa tu nombre : ")
Edad = int(input("Ingresa tu edad : "))
Sexo = input("Ingresa tu sexo ")

#Impresion de valores 
print("Te llamas : ", Nombre)
print("Tu edad es : ", Edad)
print("Eres : ", Sexo)
print("Concatenando la oracion tenemos : Tu nombre es {} Tu edad es {} y eres {}".format(Nombre,Edad,Sexo))

