"""
===================================================
Script: 03.Ejercicio_Oplogicos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-08
Descripción:
    Ejercicio práctico que simula un login sencillo 
    utilizando operadores lógicos en Python.

    - Se valida usuario y contraseña.
    - Se usan operadores AND, OR y NOT para 
    establecer reglas de acceso.
===================================================
"""

# Datos simulados en el "sistema"
usuario_correcto = "admin"
password_correcta = "1234"

# Solicitud de datos al usuario
usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

# ===================================================
# Validación con operador AND
# Ambas condiciones deben cumplirse:
# - El usuario debe coincidir.
# - La contraseña debe ser correcta.
# ===================================================
if usuario == usuario_correcto and password == password_correcta:
    print(" Acceso concedido: Bienvenido al sistema")
# ===================================================
# Validación con operador OR
# Si el usuario es correcto O la contraseña es correcta,
# significa que el intento es sospechoso (casi acierta).
# ===================================================
elif usuario == usuario_correcto or password == password_correcta:
    print(" Intento de acceso sospechoso: Usuario o contraseña correctos, pero no ambos.")
# ===================================================
# Uso de operador NOT
# Si no se cumple ninguna condición, se bloquea el acceso.
# ===================================================
else:
    print("Acceso denegado")
