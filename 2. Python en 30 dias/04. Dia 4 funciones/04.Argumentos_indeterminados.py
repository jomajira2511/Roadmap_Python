"""
===================================================
Script: 04.Argumentos_indeterminados.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-10
Descripción:
    Ejemplo del uso de *args en funciones de Python.
    - Se define una función `sumar(*args)` que recibe
    una cantidad indefinida de números y calcula su suma.
    - Se pide al usuario ingresar la cantidad de valores
    que desea sumar y posteriormente cada número.
    - Los datos se almacenan en una lista y luego se
    desempaquetan con `*` para enviarlos a la función.
===================================================
"""

# -------------------------------------------------
# Función con *args (argumentos variables)
# -------------------------------------------------
def sumar(*args):
    """
    Suma todos los valores recibidos como argumentos
    y muestra el resultado en pantalla.
    """
    suma = 0
    for num in args:   # Recorre cada número recibido
        suma += num    # Acumula el valor en la variable suma
    print("La suma total es:", suma)


# -------------------------------------------------
# Entrada de datos por teclado
# -------------------------------------------------
i = int(input("¿Cuántos valores deseas ingresar para sumarlos?: "))

# Lista donde se almacenarán los números ingresados
datos = []

while i > 0:
    dato = int(input("Ingresa un número: "))
    datos.append(dato)   # Se agrega el número a la lista
    i -= 1               # Se resta 1 al contador hasta llegar a 0

# -------------------------------------------------
# Llamada a la función usando desempaquetado
# -------------------------------------------------
# El operador * permite desempaquetar la lista y enviar
# cada elemento como un argumento independiente.
sumar(*datos)
