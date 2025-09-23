"""
===================================================
Script: 02.Serializacion.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-22
Descripción:
    Ejemplo de serialización y deserialización en Python
    utilizando el módulo 'pickle'.
    - Guardar datos en un archivo binario.
    - Recuperar datos del archivo.
    - Manipular la información cargada (len, índices, bucles).
===================================================
"""

import pickle 

# Lista inicial a serializar
lista = ["Mario", "Pedro", "Jose", "Paola"]

# ===================================================
# Escritura en archivo binario
# ===================================================
# fichero = open("lista", "wb")   # Abrir archivo en modo escritura binaria
# pickle.dump(lista, fichero)     # Guardar la lista en el archivo
# fichero.close()

# ===================================================
# Lectura del archivo binario
# ===================================================
fichero = open("lista", "rb")     # Abrir archivo en modo lectura binaria
datos = pickle.load(fichero)      # Recuperar la lista desde el archivo
fichero.close()

# ===================================================
# Mostrar datos recuperados
# ===================================================
print("Lista completa:", datos)

# ===================================================
# Ejemplos prácticos con la lista deserializada
# ===================================================

# Longitud de la lista
print("Número de elementos:", len(datos))

# Acceso por índice
print("Primer elemento:", datos[0])
print("Último elemento:", datos[-1])

# Recorrido con un bucle
print("\nRecorriendo elementos:")
for nombre in datos:
    print("-", nombre)

# Acceso con slicing
print("\nSublista (del índice 1 al 3):", datos[1:3])
