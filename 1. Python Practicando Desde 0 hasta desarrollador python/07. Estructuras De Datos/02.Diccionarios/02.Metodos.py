"""
===================================================
Script: 07.Metodos_Diccionarios.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-08
Descripción:
    Ejemplos prácticos del uso de métodos y operaciones 
    con diccionarios en Python. Métodos incluidos:
        - .keys() → obtener llaves
        - .values() → obtener valores
        - Acceso a un valor por llave
        - Inserción y modificación de elementos
        - .pop() → eliminar por llave
        - .get() → obtener valor de forma segura
        - .setdefault() → agregar si no existe
        - .update() → unir diccionarios
        - .clear() → vaciar diccionario
===================================================
"""

# Declaración de un diccionario
Diccionario = {
    "Nombre": "Jhon",
    "Apellido": "Jimenez",
    "Estatura": 1.85
}
Diccionario2 = {
    "Nacionalidad" : "Colombiano",
    "pais" : "Colombia"
}

# .keys() → Obtiene solo las llaves
print("Llaves del diccionario:", Diccionario.keys())

# .values() → Obtiene solo los valores
print("Valores del diccionario:", Diccionario.values())

# Acceder a un valor específico
print("Nombre:", Diccionario["Nombre"])

# Agregar un nuevo par llave-valor
Diccionario["Edad"] = 25
print("Diccionario con nueva llave 'Edad':", Diccionario)

# Modificar un valor existente
Diccionario["Edad"] = 56
print("Diccionario con 'Edad' modificada:", Diccionario)

#  .pop() -> Permite eliminar  un elemento del diccionario 
Diccionario.pop("Estatura")
print(Diccionario)

# .get() -> recibe un parametro (llave) y retorna el valor 
print(Diccionario.get("Nombre"))

# .setdeafault() -> Permite agregar valores al diccionario
Diccionario.setdefault("Pais" , "Colombia")
print(Diccionario)

# .update() -> Permite unificar dos diccionario 
Diccionario.update(Diccionario2)
print(Diccionario)

# .clear() -> Limpia el diccionario de elementos
Diccionario.clear()
print(Diccionario)
