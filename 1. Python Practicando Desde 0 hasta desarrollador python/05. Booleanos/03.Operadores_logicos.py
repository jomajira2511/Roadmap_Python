"""
===================================================
Script: 10.Operadores_Logicos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-07
Descripción:
    Este script muestra el uso de operadores lógicos en Python,
    los cuales permiten combinar o modificar condiciones booleanas.

    Los operadores lógicos evalúan expresiones que resultan en 
    valores booleanos (`True` o `False`) y se usan comúnmente en 
    estructuras de decisión.

    Contenido abordado:
    • `and`: Devuelve True solo si ambas condiciones son verdaderas.
    • `or` : Devuelve True si al menos una condición es verdadera.
    • `not`: Invierte el valor lógico de una condición (True ↔ False).
===================================================
"""


print(10>2) #condicion de mayor 
print(10 > 2 and 9 < 100)  #condicional and (Y), ambas deben ser verdaderas, cuando una de las dos es falsa, da FALSE
print(88 <=  789 or 60 >110) #condicional or (O), que acepta que una sea verdadera 
print(not 90 != 90) #condicional not (NO), que cambia el valor de salida, true-> false false -> true 