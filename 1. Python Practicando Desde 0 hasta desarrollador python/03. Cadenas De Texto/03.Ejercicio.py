"""
===================================================
Script: 03.Ejercicio.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-06
Descripción:
    Ejercicio 1:
    Crear un programa que contenga una variable con la cadena:
    “Te quiero solo como amigo” 
    y muestre la siguiente información:
    • Los dos primeros caracteres.
    • Los tres últimos caracteres.
    • La cadena mostrada cada dos caracteres.
        Ejemplo: Si la cadena fuera “recta” imprimiría “rca”.
    • La cadena en sentido inverso.
        Ejemplo: Si la cadena fuera “hola mundo!” imprimiría “!odnum aloh”.
    • La cadena seguida de su versión invertida.
        Ejemplo: Si la cadena es “reflejo” imprimiría “reflejoojelfer”.
===================================================
"""
Cadena = "Te quiero solo como amigo"
print("Los primos dos caracteres son : ",Cadena[0:2])
print("Los tres ultimos caracteres son : ",Cadena[-3:])
print("La cadena mostrada cada 2 caracteres : ",Cadena[::2])
print("La cadena seguida de su version invertida : ",Cadena[::-1])
print("La cadena en un mismo sentido, y el inverso :",Cadena +  Cadena[::-1])