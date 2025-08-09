"""
===================================================
Script: 13.Condicionales_Elif.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-07
Descripción:
    Este script muestra el uso de estructuras condicionales 
    múltiples en Python mediante `if`, `elif` y `else`, 
    permitiendo tomar decisiones en función de varias opciones.

    El programa solicita al usuario que ingrese una vocal.
    Luego, utilizando `lower()` para evitar errores con mayúsculas,
    evalúa qué vocal fue ingresada y muestra un mensaje correspondiente.

    Contenido abordado:
    • Entrada de datos con `input()`.
    • Conversión de texto a minúscula con `.lower()`.
    • Condicionales múltiples con `if`, `elif`, `else`.
===================================================
"""

#Ingreso de valores por teclado
Vocal = input("Ingresa una vocal ")
V = Vocal.lower()

if V == 'a':  #condicional if, para validar una vocal ingresada por teclado, y usamos el metodo lower para poder validarla
    print("Tu vocal es la {} ". format(Vocal))  
elif V == 'e':  #condicional elif, para validar una vocal ingresada por teclado,funciona de igual manera que if
    print("Tu vocal es la {} ". format(Vocal)) 
elif V  == 'i':  #condicional elif, para validar una vocal ingresada por teclado,funciona de igual manera que if
    print("Tu vocal es la {} ". format(Vocal)) 
elif V  == 'o':  #condicional elif, para validar una vocal ingresada por teclado,funciona de igual manera que if
    print("Tu vocal es la {} ". format(Vocal)) 
elif V == 'u':  #condicional elif, para validar una vocal ingresada por teclado,funciona de igual manera que if
    print("Tu vocal es la {} ". format(Vocal)) 
else:  #Al ser la ultima condicion que se debe de cumplir, podemos usar el else para cerrar el ciclo de condicionalesu
    print("El dato ingresado no corresponde a una vocal" ) 

