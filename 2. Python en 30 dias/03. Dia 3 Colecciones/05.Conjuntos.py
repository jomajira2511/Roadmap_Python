"""
===================================================
Script: conjuntos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-09
Descripción:
    Ejemplo de uso de conjuntos (set) en Python:
    - Los conjuntos son colecciones desordenadas y no permiten duplicados.
    - Permiten realizar operaciones matemáticas de conjuntos como
    unión, intersección y diferencia.
    - Ideales cuando se necesita garantizar elementos únicos.
===================================================
"""

# -------------------------------------------------
# Declaración de un conjunto vacío y conjunto con elementos
# -------------------------------------------------
conjunto = set()  # Inicialización de un conjunto vacío
conjunto = {2, "Python", True}  # Conjunto con elementos mixtos
print(conjunto)  # Se imprime (el orden puede variar al ser desordenado)

# -------------------------------------------------
# Agregar elementos a un conjunto
# -------------------------------------------------
conjunto.add("pedro")  # Se inserta en posición aleatoria (no hay orden fijo)
print(conjunto)

# -------------------------------------------------
# Eliminar un elemento específico
# -------------------------------------------------
conjunto.discard("pedro")  # Si no existe, no genera error (a diferencia de remove)
print(conjunto)

# -------------------------------------------------
# Verificar si un elemento existe dentro del conjunto
# -------------------------------------------------
print("Python" in conjunto)  # Retorna True si el elemento está presente

# -------------------------------------------------
# Eliminar todos los elementos del conjunto
# -------------------------------------------------
conjunto.clear()
print(conjunto)  # Ahora es un conjunto vacío -> set()
