"""
===================================================
Script: diccionarios.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-09
Descripción:
    Ejemplo práctico del uso de diccionarios en Python.
    - Definición de diccionarios (colecciones no ordenadas de pares clave:valor).
    - Acceso a valores mediante su clave.
    - Inserción de nuevos elementos.
    - Modificación de valores existentes.
    - Eliminación de pares clave:valor.
    Nota: Los diccionarios son mutables, por lo que sus valores pueden 
    cambiar o eliminarse dinámicamente.
===================================================
"""

# -------------------------------------------------
# Definición de un diccionario con diferentes claves y valores
# -------------------------------------------------
persona = {"Fresa": "Roja", "Jhon": 25, "Banano": "Amarillo"}
print(persona)  # Imprime el diccionario completo

# -------------------------------------------------
# Acceso a un valor mediante su clave
# -------------------------------------------------
print(persona["Banano"])  # Retorna el valor asociado a la clave "Banano" → "Amarillo"

# -------------------------------------------------
# Agregar un nuevo elemento al diccionario
# -------------------------------------------------
persona["Pedro"] = 32
print(persona)  # Ahora incluye la clave "Pedro"

# -------------------------------------------------
# Modificar un valor existente
# -------------------------------------------------
persona["Jhon"] = 30
print(persona)  # El valor de la clave "Jhon" ahora es 30

# -------------------------------------------------
# Eliminar un elemento del diccionario
# -------------------------------------------------
del persona["Pedro"]
print(persona)  # Elimina la clave "Pedro" y su valor
