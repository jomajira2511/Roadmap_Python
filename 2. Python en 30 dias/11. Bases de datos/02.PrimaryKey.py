"""
===================================================
Script: 02.PrimaryKey.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-10-16
Descripción:
    Este script muestra cómo crear una tabla con clave primaria (PRIMARY KEY)
    utilizando SQLite. Se utiliza la librería estándar `sqlite3` para:
    
    - Crear una base de datos llamada 'Productos.db'
    - Definir una tabla llamada 'PRODUCTOS' con una clave primaria (CODIGO_P)
    - Insertar múltiples registros en la tabla
    - Confirmar los cambios y cerrar la conexión

    Conceptos aplicados:
        - Definición de clave primaria en SQL
        - Inserción de múltiples registros con `executemany()`
        - Confirmación de transacciones (`commit()`)
        - Cierre seguro de conexión a la base de datos
===================================================
"""

# ===================================================
# Importación de librerías
# ===================================================
import sqlite3


# ===================================================
# Conexión y creación de la base de datos
# ===================================================
conexion = sqlite3.connect("Productos.db")
cursor = conexion.cursor()


# ===================================================
# Creación de tabla con clave primaria
# ===================================================
# Ejecutar solo una vez para crear la tabla.
# cursor.execute("""
#     CREATE TABLE PRODUCTOS (
#         CODIGO_P VARCHAR(20) PRIMARY KEY,
#         NOMBRE_P VARCHAR(20),
#         SECCION_P VARCHAR(20)
#     )
# """)


# ===================================================
# Inserción de múltiples registros
# ===================================================
"""
productos = [
    ('AR1', 'Leche', 'Lácteos'),
    ('AR2', 'Pan', 'Panadería'),
    ('AR3', 'Lomo', 'Carnicería')
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?)", productos)
"""


# ===================================================
# Guardado y cierre de conexión
# ===================================================
conexion.commit()
conexion.close()
