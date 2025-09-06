"""
===================================================
Script: iteracion.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-05
Descripción:
    Ejemplo práctico de iteraciones en Python.

    En este script se trabajan dos casos:
    1. Recorrer una lista de elementos con un bucle `for`.
    2. Iterar sobre las líneas de un archivo de texto.
===================================================
"""

# ===================================================
# Iteración sobre una lista
# ===================================================
lenguajes = ["java", "php", "python", "ruby", "c"]

for i in lenguajes:  
    # Cada ciclo toma un valor de la lista 'lenguajes'
    print(f"Me encuentro en el lenguaje {i}")  


# ===================================================
# Iteración sobre un archivo de texto
# ===================================================
# Nota: el archivo 'doc.txt' debe existir en la ruta especificada
#       para que el script funcione correctamente.
for j in open("2. Python para Profesionales. Mejora tu Desarrollo/04. Iteracion/doc.txt"):
    # Se imprimen las líneas del archivo, una por una
    print(j.strip())  # strip() elimina saltos de línea extra
