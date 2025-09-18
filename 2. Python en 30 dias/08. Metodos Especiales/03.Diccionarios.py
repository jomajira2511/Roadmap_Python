"""
===================================================
Script: 03.Diccionario.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-17
Descripción:
    Ejemplo práctico del uso de diccionarios en Python.
    Métodos aplicados:
    - get(): retorna el valor de una clave si existe.
    - keys(): retorna todas las claves.
    - values(): retorna todos los valores.
    - items(): retorna pares clave-valor como tuplas.
    - pop(): elimina una clave del diccionario.
    Además, se recorre el diccionario con un bucle for.
===================================================
"""

# ===================================================
# Declaración de diccionario
# ===================================================
personas = {
    "Martin": "Lopez",
    "Jhon": "Jimenez",
    "Pedro": "Suarez"
}

# ===================================================
# Uso de métodos de diccionario
# ===================================================

# .get() -> Retorna el valor asociado a la clave
print("Valor asociado a 'Jhon':", personas.get("Jhon"))

# .keys() -> Retorna todas las claves
print("Claves del diccionario:", personas.keys())

# .values() -> Retorna todos los valores
print("Valores del diccionario:", personas.values())

# .items() -> Retorna lista de pares (clave, valor)
print("Items del diccionario (clave, valor):", personas.items())

# Recorriendo el diccionario con clave y valor
print("\nRecorriendo el diccionario:")
for clave, valor in personas.items():
    print(f"Clave: {clave}, Valor: {valor}")

# .pop() -> Elimina un elemento por su clave
personas.pop("Martin")
print("\nDiccionario después de pop('Martin'):", personas)













