"""
===================================================
Script: 03.Autoincremento.py
Proyecto: Roadmap Python 
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-10-16
Descripción:
    Este script demuestra cómo crear una tabla con un campo 
    autoincremental en SQLite, utilizando la cláusula 
    `INTEGER PRIMARY KEY AUTOINCREMENT`.

    La tabla 'MisProductos' almacena productos junto con su 
    sección, asignando automáticamente un ID incremental 
    para cada nuevo registro insertado.

    Conceptos aplicados:
        - Creación de tablas con `AUTOINCREMENT`
        - Inserción múltiple de registros con `executemany()`
        - Uso de `NULL` en la inserción para activar el autoincremento
        - Confirmación de cambios (`commit()`)
        - Cierre seguro de la conexión
===================================================
"""

# ===================================================
# Importación de librerías
# ===================================================
import sqlite3


# ===================================================
# Conexión y creación de la base de datos
# ===================================================
conexion = sqlite3.connect("MisProductos.db")
cursor = conexion.cursor()


# ===================================================
# Creación de tabla con campo autoincremental
# ===================================================
# Ejecutar solo una vez para crear la tabla.
# cursor.execute("""
#     CREATE TABLE MisProductos(
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NOMBRE VARCHAR(20),
#         SECCION VARCHAR(20)
#     )
# """)


# ===================================================
# Inserción de registros
# ===================================================
productos = [
    ('Frutas', 'Verdurería'),
    ('Perfume', 'Perfumería'),
    ('Perros', 'Veterinaria')
]

# Se usa NULL en el campo ID para que SQLite asigne el valor automáticamente
cursor.executemany("INSERT INTO MisProductos VALUES (NULL, ?, ?)", productos)


# ===================================================
# Guardado y cierre de conexión
# ===================================================
conexion.commit()
conexion.close()
