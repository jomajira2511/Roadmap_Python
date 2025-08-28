"""
===================================================
Script: 02.Moviniento_tortuga.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-28
Descripción:
    Ejemplo práctico del uso de la librería Turtle.
    Se realizan movimientos absolutos (goto), un retorno al punto
    de origen (home) y movimientos relativos (forward, right).
===================================================
"""

import turtle  # Librería estándar para gráficos y dibujos

# Crear el lienzo (ventana) y la tortuga
s = turtle.Screen()
t = turtle.Turtle()

# Movimiento a coordenadas absolutas (x, y)
t.goto(120, 100)   # La tortuga se mueve al punto (120, 100)
t.goto(90, 300)    # La tortuga se mueve al punto (90, 300)

# Regresa a la posición inicial (0,0) con orientación por defecto
t.home()

# Movimientos relativos desde el origen
t.forward(100)     # Avanza 100 píxeles hacia adelante
t.right(40)        # Gira 40 grados a la derecha
t.forward(120)     # Avanza 120 píxeles hacia adelante

# Mantener abierta la ventana hasta que se cierre manualmente
turtle.done()
