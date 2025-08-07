"""
===================================================
Script: 11.Metodos_Booleanos_Cadenas.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-07
Descripción:
    Este script muestra el uso de métodos booleanos aplicados
    a cadenas de texto en Python. Estos métodos devuelven un
    valor booleano (`True` o `False`) según ciertas condiciones
    sobre el contenido de la cadena.

    Contenido abordado:
    • startswith(): Verifica si la cadena comienza con un carácter específico.
    • endswith(): Verifica si la cadena termina con un carácter específico.
    • isupper(): Verifica si todos los caracteres están en mayúscula.
    • islower(): Verifica si todos los caracteres están en minúscula.
===================================================
"""
#creacion de cadena a trabajar
Cadena = ("Estoy mostando metodos booleanos para strings")

#Metodos booleanos 
print(Cadena.startswith("E"))  #startwith(), permite "preguntar", si la cadena empieza con el digito que se esta pregutando en la funcion 
print(Cadena.endswith("s")) #endwith(), permite "preguntar", si la cadena termina con el digito que se esta preguntando en la funcion
print(Cadena.isupper()) #issuper(), verifica si toda la cadena esta en mayusculas 
print(Cadena.islower()) #islower(), verifica si toda la cadena esta en minisculas 