"""
===================================================
Script: 02.Retorno_de_valores.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-10
Descripción:
    Ejemplo del uso de `return` en funciones:
    - El `return` devuelve un valor desde la función al punto
    donde fue llamada.
    - Una vez que se ejecuta `return`, la función finaliza
    y no se ejecutan las líneas posteriores.
    - Esto permite reutilizar el resultado en otras partes
    del programa.
===================================================
"""

# -------------------------------------------------
# Definición de función con retorno de valor
# -------------------------------------------------
def saludar():
    """
    Retorna un mensaje de saludo.
    """
    return "Hola mundo"  # El `return` devuelve el string "Hola mundo"
    # Nota: cualquier instrucción debajo de un return no se ejecutará


# -------------------------------------------------
# Uso de la función y visualización de su retorno
# -------------------------------------------------
print(saludar())  # Imprime el valor retornado por la función
