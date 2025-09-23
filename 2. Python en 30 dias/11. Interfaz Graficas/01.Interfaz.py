"""
===================================================
Script: 01.Interfaz.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-23
Descripción:
    Ejemplo básico de interfaz gráfica con Tkinter.
    - Creación de ventana principal.
    - Configuración de título, tamaño y redimensionamiento.
    - Personalización de icono de la aplicación.
===================================================
"""

# ===================================================
# Importación de librerías
# ===================================================
from tkinter import *   # Tkinter es la librería estándar de Python para interfaces gráficas

# ===================================================
# Creación de la ventana principal
# ===================================================
root = Tk()   # Instancia la ventana principal de la aplicación

# Título de la ventana
root.title("Primer programa")

# ===================================================
# Configuración de tamaño y redimensionamiento
# ===================================================
# root.resizable(width, height)
# - 0 = No permitir redimensionar
# - 1 = Permitir redimensionar
root.resizable(0, 0)  # No se puede redimensionar ni en ancho ni en alto
root.resizable(0, 1)  # Solo se puede modificar el alto
root.resizable(1, 1)  # Se puede modificar tanto el alto como el ancho

# ===================================================
# Personalización de icono
# ===================================================
# Reemplaza la ruta por la ubicación de tu archivo .ico
root.iconbitmap(r"C:\Users\$\Desktop\Road Map Python\2. Python en 30 dias\11. Interfaz Graficas\Logo.ico")

# ===================================================
# Bucle principal de la aplicación
# ===================================================
# Mantiene la ventana abierta hasta que el usuario la cierre
root.mainloop()
