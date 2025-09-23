"""
===================================================
Script: 01.Ficheros.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-22
Descripción:
    Ejemplo básico de manejo de ficheros en Python.
    - Escritura en archivos (modo "w" y "a").
    - Lectura completa de archivos (modo "r").
    - Uso del módulo io.open para compatibilidad.
===================================================
"""

from io import open

# ===================================================
# Escritura en archivo (modo "w") - Sobrescribe el contenido
# ===================================================
fichero = open("archivo.txt", "w")
texto = "Hola mundo \nEstoy estudiando Python"
fichero.write(texto)      # Escribe el texto en el archivo
fichero.close()           # Cierra el archivo después de usarlo

# ===================================================
# Escritura en archivo (modo "a") - Agregar contenido al final
# ===================================================
fichero = open("archivo.txt", "a")  
fichero.write("\nEste es un nuevo mensaje")  
fichero.close()

# ===================================================
# Lectura en archivo (modo "r")
# ===================================================
fichero = open("archivo.txt", "r")  
texto = fichero.read()      # Lee el contenido completo del archivo
fichero.close()             # Cierra el archivo después de usarlo

# ===================================================
# Mostrar contenido en consola
# ===================================================
print(texto)
