"""
===================================================
Script: 01.Crear_ventana.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-31
Descripción:
    Primer programa con Tkinter.
    Se crea una ventana básica de 500x500 px.
=======================
"""

# Importe de librerias 
import tkinter as tk


# Configuración ventana
ventana = tk.Tk()
ventana.title("Primer programa en Tkinter")
ventana.geometry("500x500")  # tamaño ventana



# Ejecutar ventana para que no se cierre automaticamente 
ventana.mainloop()
