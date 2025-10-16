"""
===================================================
Script: 04.CRUD.py
Proyecto: Roadmap Python 
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-10-16
Descripción:
    Este script demuestra las operaciones CRUD (Create, Read, Update, Delete)
    sobre una base de datos SQLite llamada 'MisProductos.db'.
    
    Conceptos aplicados:
        - CREATE: Inserción de datos
        - READ: Lectura o consulta de registros
        - UPDATE: Actualización de datos existentes
        - DELETE: Eliminación de registros
        - Confirmación de cambios con `commit()`
        - Cierre seguro de la conexión con `close()`
===================================================
"""

# ===================================================
# Importación de librerías
# ===================================================
import sqlite3


# ===================================================
# Conexión a la base de datos
# ===================================================
conexion = sqlite3.connect('MisProductos.db')
cursor = conexion.cursor()


# ===================================================
# READ – Lectura de datos
# ===================================================
# Permite seleccionar uno o varios registros de la base de datos.
"""
cursor.execute('SELECT * FROM MisProductos WHERE SECCION = "Panadería"')
productos = cursor.fetchall()
for producto in productos:
    print(producto)
"""


# ===================================================
# UPDATE – Actualización de datos
# ===================================================
# Permite modificar valores de un campo específico.
"""
cursor.execute('UPDATE MisProductos SET SECCION = "Panaderia" WHERE SECCION = "Panadería"')
"""


# ===================================================
# DELETE – Eliminación de registros
# ===================================================
# Elimina un registro según un criterio (por ejemplo, ID = 1).
cursor.execute('DELETE FROM MisProductos WHERE ID = 1')


# ===================================================
# Guardado y cierre de conexión
# ===================================================
conexion.commit()
conexion.close()





