"""
===================================================
Script: 01.Sentencia_if.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-08
Descripción:
    Ejemplo del uso de la sentencia condicional if-elif-else.
    El programa solicita al usuario su edad y determina:
    - Si es menor de edad.
    - Si es un adulto.
    - Si es un adulto mayor.
    Se implementan también operadores lógicos para ampliar
    las condiciones.
===================================================
"""

# -----------------------------------------
# Solicitar al usuario su edad y convertir
# el valor ingresado en un número entero
# -----------------------------------------
print("Ingresa tu edad para determinar si eres mayor de edad")
edad = int(input("Ingresa tu edad: "))

# -----------------------------------------
# Condicional principal
# Se evalúa la edad con distintos rangos:
# - Entre 18 y 65 -> Adulto
# - Mayor de 65   -> Adulto mayor
# - Menor de 18   -> Menor de edad
# -----------------------------------------
if edad > 18 and edad < 65:  
    print("Eres un adulto")
elif edad > 65:  
    print("Eres un adulto mayor")
else:  
    print("Eres menor de edad")
