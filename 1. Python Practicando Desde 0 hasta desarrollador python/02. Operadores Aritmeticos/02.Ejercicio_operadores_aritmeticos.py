"""
===================================================
Script: 02.Ejercicio_operadores_aritmeticos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-04
Descripción:
    Es un ejercicio práctico para aplicar operadores
    aritméticos en Python como suma, multiplicación,
    división y potenciación.
===================================================
"""

"""
===================================================
    Este script resuelve la expresión matemática:
    ((3 + 2) / (2 * 5)) al cuadrado. (Ejercicio.png)
    Es un ejercicio práctico para aplicar operadores
    aritméticos en Python como suma, multiplicación,
    división y potenciación.
===================================================
"""
Resultado = ((3+2)/(2*5))**2
Funcion_pow = pow((3+2)/(2*5),2)
print ("\nEl resultado de la operacion es : ", Resultado)
print ("\nEl resultado de la operacion usando la funcion POW es : ", Funcion_pow)


"""
===================================================
Descripción:
    Este script calcula el peso total de un pedido de
    juguetes realizado por un cliente. La juguetería vende
    payasos y muñecas, cuyos pesos son 112 g y 75 g respectivamente.
    El pedido contiene 23 payasos y 54 muñecas. El programa
    muestra el peso total en gramos del pedido completo.
===================================================
"""
Payasos = 112
Muñecas = 75

pedido_payasos = Payasos * 23
pedido_muñecas = Muñecas * 54
peso_total = pedido_payasos + pedido_muñecas
print(f"\nEl peso total de los payasos es de: {pedido_payasos} gr")
print(f"\nEl peso total de las muñecas es de: {pedido_muñecas} gr")
print(f"\nEl peso total del pedido es de: {peso_total} gr")
