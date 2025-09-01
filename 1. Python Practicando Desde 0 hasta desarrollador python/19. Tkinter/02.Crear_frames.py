"""
===================================================
Script: 02.Crear_frames.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-31
Descripción:
    Ejemplo de uso de Frame en Tkinter.
    Se crea una ventana principal de 500x500 px,
    con un frame (marco) de 300x200 px, color gris
    y borde sólido, que servirá como contenedor
    para futuros widgets.
===================================================
"""

import tkinter as tk

# ============================
# Configuración de la ventana
# ============================
ventana = tk.Tk()
ventana.title("Frame")                 # Título de la ventana
ventana.geometry("500x500")            # Tamaño: ancho x alto
ventana.resizable(False, False)        # Evita que se pueda redimensionar

# ============================
# Creación de un Frame
# ============================
marco = tk.Frame(
    ventana,
    width=300, height=200,             # Dimensiones del marco
    bg="lightgray",                    # Color de fondo
    borderwidth=2,                     # Grosor del borde
    relief="solid"                     # Estilo de borde (relieve)
)

# Evita que el frame se ajuste al contenido interno
marco.pack_propagate(False)

# Posicionamiento del frame dentro de la ventana
marco.pack(pady=50)

# ============================
# Ejecutar ventana
# ============================
ventana.mainloop()
