"""
===================================================
Script: 01.Errores_y_excepciones.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-11
Descripción:
    Calculadora básica con manejo de errores y excepciones.
    - Funciones: sumar, restar, multiplicar, dividir.
    - Uso de `try/except` para controlar división por cero.
    - Entrada de datos desde teclado.
    - Selección de operación a realizar mediante if/elif/else.
===================================================
"""

# -------------------------------------------------
# Definición de funciones
# -------------------------------------------------
def restar(num1, num2):
    return num1 - num2

def sumar(num1, num2):
    return num1 + num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Error: no se puede dividir entre 0")
        return "Operación no válida"

# -------------------------------------------------
# Entrada de datos del usuario
# -------------------------------------------------
op1 = int(input("Introduce el primer valor: "))
op2 = int(input("Introduce el segundo valor: "))

# Menú de operaciones
operacion = input(
    "Introduce la operación a realizar ---> \n"
    "Sumar\nRestar\nDividir\nMultiplicar\nOpción: "
)

# -------------------------------------------------
# Ejecución de la operación seleccionada
# -------------------------------------------------
if operacion == "Sumar":
    print("Resultado:", sumar(op1, op2))

elif operacion == "Restar":
    print("Resultado:", restar(op1, op2))

elif operacion == "Multiplicar":
    print("Resultado:", multiplicar(op1, op2))

elif operacion == "Dividir":
    print("Resultado:", dividir(op1, op2))

else:
    print("ERROR: opción no válida")

print("Ejecutando nueva línea de código...")
