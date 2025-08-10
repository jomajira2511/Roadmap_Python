"""
===================================================
Script: 01.Clases_y_objeto.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Ejemplo básico de Programación Orientada a Objetos (POO) en Python:
        - Creación de una clase vacía.
        - Instanciación de objetos a partir de la clase.
        - Verificación de tipos.
===================================================
"""

# Definición de clase vacía
class FabricaTelefonos:
    # 'pass' indica que por ahora la clase no contiene atributos ni métodos
    pass

# Verificar que 'FabricaTelefonos' es un tipo clase
print(type(FabricaTelefonos))  # <class 'type'>

# Creación de objetos (instancias) a partir de la clase
celular = FabricaTelefonos()
celular2 = FabricaTelefonos()

# Verificar que 'celular' y 'celular2' son objetos de tipo 'FabricaTelefonos'
print(type(celular))   # <class '__main__.FabricaTelefonos'>
print(type(celular2))  # <class '__main__.FabricaTelefonos'>
