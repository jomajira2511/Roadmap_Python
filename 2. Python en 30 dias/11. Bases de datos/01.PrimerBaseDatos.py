"""
===================================================
Script: MiPrimerBaseDatos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-10-14
Descripción:
    Este script demuestra la creación, inserción y lectura de datos
    en una base de datos SQLite utilizando la librería estándar `sqlite3`.
    
    Conceptos aplicados:
        - Conexión y creación de bases de datos SQLite
        - Creación de tablas con SQL
        - Inserción de datos individuales y múltiples registros
        - Ejecución de consultas SELECT
        - Confirmación de transacciones con `commit()`
        - Cierre seguro de la conexión
===================================================
"""

# ===================================================
# Importación de librerías
# ===================================================
import sqlite3


# ===================================================
# Conexión a la base de datos
# ===================================================
# Si el archivo 'MiBase.db' no existe, se crea automáticamente.
conexion = sqlite3.connect('MiBase.db')
cursor = conexion.cursor()


# ===================================================
# Creación de tabla (solo ejecutar una vez)
# ===================================================
# Descomenta la siguiente línea si deseas crear la tabla USUARIOS.
# cursor.execute("""
#     CREATE TABLE USUARIOS(
#         NOMBRE VARCHAR(50),
#         EDAD INTEGER,
#         SEXO VARCHAR(50)
#     )
# """)


# ===================================================
# Inserción de un solo registro
# ===================================================
# cursor.execute("INSERT INTO USUARIOS VALUES('Maria', 25, 'Femenino')")


# ===================================================
# Inserción de múltiples registros
# ===================================================
"""
usuarios = [
    ('Jose', 24, 'Masculino'),
    ('Raul', 66, 'Masculino')
]
cursor.executemany("INSERT INTO USUARIOS VALUES(?, ?, ?)", usuarios)
"""


# ===================================================
# Consulta de datos (lectura)
# ===================================================
"""
cursor.execute("SELECT * FROM USUARIOS")
usuarios = cursor.fetchall()  # Trae todos los registros de la tabla
for u in usuarios:
    print(u)
"""


# ===================================================
# Guardado y cierre de la conexión
# ===================================================
conexion.commit()   # Aplica los cambios a la base de datos
conexion.close()    # Cierra la conexión de manera segura
