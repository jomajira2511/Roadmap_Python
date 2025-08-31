"""
===================================================
Script: 01.Carrera_tortugas.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-30
Descripción:
    Juego simple de carrera de tortugas usando la librería `turtle`
    y tiradas de dado con `random`. Dos jugadores compiten hasta
    llegar a la meta.
    
    Recomendaciones de mejora:
    - Usar `xcor()` para verificar avance en el eje X, en lugar
      de comparar la tupla completa que retorna `.pos()`.
    - Reemplazar `input()` por un flujo automático o por eventos
      con `onkey()` para evitar bloqueos en la ejecución.
    - Crear una función auxiliar para mover tortugas y evitar
      duplicación de código.
    - Dibujar una línea de meta vertical en `x=200` para mayor
      claridad visual.
===================================================
"""

import turtle   # Librería para gráficos
import random   # Librería para el dado


# ============================
# Configuración de pantalla
# ============================
s = turtle.Screen()
s.title("Carrera de tortugas")
s.bgcolor("gray")


# ============================
# Creación de jugadores
# ============================
jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

# Estilo de jugadores
jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("green", "green")
jugador1.shapesize(2, 2, 2)
jugador1.pensize(3)

jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("blue", "blue")
jugador2.shapesize(2, 2, 2)
jugador2.pensize(3)


# ============================
# Dibujamos la meta (círculos)
# ============================
jugador1.penup()
jugador1.goto(200, 200)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-200, 225)
jugador1.showturtle()

jugador2.penup()
jugador2.goto(200, -200)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-200, -175)
jugador2.showturtle()


# ============================
# Configuración del dado
# ============================
dado = [1, 2, 3, 4, 5, 6]


# ============================
# Función auxiliar para mover
# ============================
def mover(jugador, dado):
    """
    Espera que el jugador presione Enter,
    tira el dado y mueve la tortuga.
    """
    input("Presiona Enter para avanzar")
    turno = random.choice(dado)
    print(f"Tu turno es {turno}, avanzas {turno*20}")
    jugador.pendown()
    jugador.forward(turno * 20)


# ============================
# Lógica de la carrera
# ============================
for i in range(20):
    if jugador1.xcor() >= 200:
        print("La tortuga verde ha ganado")
        break
    elif jugador2.xcor() >= 200:
        print("La tortuga azul ha ganado")
        break
    else:
        mover(jugador1, dado)
        mover(jugador2, dado)

turtle.done()
