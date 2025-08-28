"""
===================================================
Script: 01.Comandos_basicos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-28
Descripción:
    Script de ejemplo utilizando la librería Turtle en Python.
    Se crean movimientos básicos de la tortuga para dibujar líneas 
    en diferentes direcciones sobre el lienzo.
===================================================
"""

import turtle  # Importamos la librería estándar de gráficos Turtle

# Crear el lienzo (ventana) para dibujar
s = turtle.Screen()

# Crear una instancia de la "tortuga" que realizará los dibujos
t = turtle.Turtle()

# Movimiento hacia atrás de 100 píxeles
t.backward(100)

# Girar la tortuga 90 grados a la derecha
t.right(90)

# Avanzar 100 píxeles hacia adelante
t.forward(100)

# Girar 100 grados a la izquierda
t.left(100)

# Avanzar 100 píxeles hacia adelante
t.forward(100)

# Mantener abierta la ventana hasta que el usuario la cierre
turtle.done()
