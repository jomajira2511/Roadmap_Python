"""
===================================================
Script: 02.Metodos_cadenas.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-06
Descripción:
    Este script muestra cómo se realiza el debanado de cadenas
    (string slicing) en Python, permitiendo extraer partes 
    específicas de un texto mediante índices y saltos.
    y al mismo tiempo metodos para la manipulacion de strings
===================================================
"""
Cadena = "Ejemplo Para Cadenas En Python"
print ("-------------------DEBANADO DE CADENAS-----------------------------------")
print(Cadena[2])  #permite retornar un caracter ubicado en esa posicion del string 
print(Cadena[0:10]) #toma valores desde la casilla 0 hasta la 10, empieza desde la "
print(Cadena[10:]) #toma valores desde la posicion 10 hasta la posicion final 

print ("-------------------METODOS DE CADENAS-----------------------------------")
print("El tamaño de la cadena es de :",len(Cadena)) ##metodo len permite ver la cantidad o longitud de la cadena 
print(Cadena.lower())#Este metodo convierte todos los caracteres de la cadena a minusculas 
print(Cadena.upper())#Este metodo convierte todos los caracteres de la cadena a mayusculas 
print(Cadena.capitalize())#Este metodo conviernte a letra capital 
print(Cadena.title())#Este metodo convierte cada una de las letra inciail de palabra a mayusculas 
print(Cadena.swapcase())#Este metodo convierte masyuculas a minusculas y minusculas a mayusculas 
