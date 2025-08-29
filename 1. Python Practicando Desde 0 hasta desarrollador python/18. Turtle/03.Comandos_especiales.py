"""
===================================================
Script: 03.Comandos_especiales.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-29
Descripción:
    Este script utiliza la librería Turtle para realizar dibujos 
    geométricos y personalizar la apariencia de la tortuga y el lienzo.
    Se practican conceptos como:
        - Creación de círculos con y sin relleno.
        - Cambio de posición de la tortuga en el lienzo.
        - Personalización de color de fondo, título de ventana, 
        grosor del lápiz y color de los trazos.
        - Modificación del tamaño, forma y color de la tortuga.
===================================================
"""

import turtle

# Crear la ventana principal (screen) y el objeto tortuga
s = turtle.Screen()
t = turtle.Turtle()

# Configuración inicial de velocidad
t.speed(10)

# Dibujar un círculo de radio 100
t.circle(100)

# Dibujar un punto sólido (círculo relleno) de tamaño 40
t.dot(40)

# Ocultar la tortuga, moverla y volverla a mostrar
t.hideturtle()
t.setx(-500)
t.showturtle()
t.setx(100)

# Personalizar el lienzo
s.bgcolor("green")         # Cambiar color de fondo
s.title("Primer prueba")   # Cambiar título de la ventana

# Personalización de la tortuga
t.shapesize(10, 40, 2)     # Tamaño: alto=10, ancho=40, borde=2
t.fillcolor("blue")        # Color de relleno de la tortuga
t.pencolor("red")          # Color del lápiz (trazo)

# Dibujar un círculo de radio 200 con los ajustes actuales
t.circle(200)

# Cambiar grosor del lápiz
t.pensize(10)

# Cambiar tamaño de la tortuga nuevamente
t.shapesize(10, 10, 2)
t.color("gold", "brown")   # Color del trazo y relleno
t.circle(300)

# Dibujar un círculo relleno de radio 100
t.begin_fill()
t.circle(100)
t.end_fill()

# Cambiar la forma de la tortuga
t.shape("turtle")

# Dibujar otro círculo más grande
t.circle(300)

# Mantener la ventana abierta hasta que se cierre manualmente
turtle.done()
