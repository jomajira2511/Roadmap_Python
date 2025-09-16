"""
===================================================
Script: 01.Cadenas.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-16
Descripción:
    Ejemplo de uso de métodos de cadenas en Python.
    Métodos aplicados:
    - upper(): convierte la cadena a mayúsculas.
    - lower(): convierte la cadena a minúsculas.
    - capitalize(): coloca la primera letra en mayúscula.
    - title(): coloca la primera letra de cada palabra en mayúscula.
    - isdigit(): verifica si la cadena contiene solo dígitos.
    - strip(): elimina espacios en blanco al inicio y final.
    - replace(): reemplaza un valor dentro de la cadena.
    - find(): busca la posición de un valor dentro de la cadena.
    - split(): divide la cadena en una lista por un separador.
    - join(): une elementos de una lista en una sola cadena.
    - startswith(): verifica si la cadena empieza con un valor.
    - endswith(): verifica si la cadena termina con un valor.
===================================================
"""

# ===================================================
# Entrada del usuario
# ===================================================
texto = input("Ingresa una frase: ")

# ===================================================
# Métodos de cadena
# ===================================================

# .upper() -> Convierte todo el texto a mayúsculas
print("En mayúsculas:", texto.upper())

# .lower() -> Convierte todo el texto a minúsculas
print("En minúsculas:", texto.lower())

# .capitalize() -> Convierte la primera letra en mayúscula
print("Capitalizado:", texto.capitalize())

# .title() -> Convierte la primera letra de cada palabra en mayúscula
print("Título:", texto.title())

# .isdigit() -> Verifica si es un valor numérico
print("¿Es un número?:", texto.isdigit())

# .strip() -> Elimina espacios al inicio y al final
print("Texto sin espacios extra:", texto.strip())

# .replace() -> Reemplaza un valor dentro de la cadena
print("Reemplazando 'a' por '@':", texto.replace("a", "@"))

# .find() -> Retorna la posición de la primera aparición
print("Posición de la palabra 'Python':", texto.find("Python"))

# .split() -> Divide la cadena en una lista
palabras = texto.split(" ")
print("Lista de palabras:", palabras)

# .join() -> Une elementos de una lista en una cadena
print("Lista unida con guiones:", "-".join(palabras))

# .startswith() -> Verifica si comienza con algo
print("¿Empieza con 'Hola'?:", texto.startswith("Hola"))

# .endswith() -> Verifica si termina con algo
print("¿Termina con 'fin'?:", texto.endswith("fin"))
