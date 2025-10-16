#02.PrimaryKey.py
import sqlite3

#CREACION DE LA BASE DE DATOS
conexion = sqlite3.connect("Productos.db")
cursor = conexion.cursor()

#CREACION DE CAMPOS DE LA DB
#cursor.execute('CREATE TABLE PRODUCTOS (CODIGO_P  VARCHAR(20) PRIMARY KEY, NOMBRE_P VARCHAR(20), SECCION_P VARCHAR(20))')
'''
#Agregamos datos 
productos = [
    ('AR1' , 'Leche' , 'Lacteos'),
    ('AR2' , 'Pan' , 'Panaderia'),
    ('AR3' , 'Lomo' , 'Carniceria'),
]
'''

#cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", productos)
conexion.commit()
conexion.close()


