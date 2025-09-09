"""
===================================================
Script: 01.Listas.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-09
Descripción:
    Ejemplo práctico del uso de listas en Python.
    - Declaración de una lista con diferentes elementos.
    - Acceso a elementos por índice (positivo y negativo).
    - Eliminación de elementos mediante 'del'.
    - Inserción de elementos en una posición específica.
    - Uso del método 'append' para agregar elementos al final.
===================================================
"""

# -------------------------------------------------
# Declaración de una lista con nombres de personas
# -------------------------------------------------
personas = ["Jhon", "Pedro", "Alejandro", "Sara", "Matias"]  
# Nota: Las listas en Python pueden almacenar cualquier tipo de dato.

# -------------------------------------------------
# Acceso a elementos de la lista
# -------------------------------------------------
print(personas)        # Imprime la lista completa
print(personas[1])     # Imprime el segundo elemento (índice 1 → "Pedro")
print(personas[-1])    # Imprime el último elemento ("Matias")

# -------------------------------------------------
# Eliminación de un elemento por índice
# En este caso eliminamos el primer elemento ("Jhon")
# -------------------------------------------------
del personas[0]        
print(personas)

# -------------------------------------------------
# Inserción de un elemento en una posición específica
# En este caso en la posición 0
# -------------------------------------------------
personas.insert(0, "Nuevo Elemento")  
print(personas)

# -------------------------------------------------
# Uso de append() para añadir un elemento al final de la lista
# En este caso, agregamos un número entero (10)
# -------------------------------------------------
personas.append(10)  
print(personas)
