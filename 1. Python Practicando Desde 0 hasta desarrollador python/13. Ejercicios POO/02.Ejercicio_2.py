"""
===================================================
Script: 02.Ejercicio_2.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-15
Descripción:
    Ejercicio 1:
    Realizar un programa en el cual se declaren dos valores enteros 
    por teclado utilizando el método __init__. Calcular después la suma, 
    resta, multiplicación y división. Utilizar un método para cada una 
    e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
=================
"""

class Calculadora:
    def __init__(self):
        """Inicializa la calculadora con dos números enteros."""
        self.num1 = int(input("Ingresa el primer número: "))
        self.num2 = int(input("Ingresa el segundo número: "))
        
    def suma(self):
        """Retorna la suma de los dos números."""
        return self.num1 + self.num2
    
    def resta(self):
        """Retorna la resta de los dos números."""
        return self.num1 - self.num2

    def multiplicacion(self):
        """Retorna la multiplicación de los dos números."""
        return self.num1 * self.num2

    def division(self):
        """Retorna la división de los dos números."""
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División entre cero"



# Creación del objeto y ejecución de operaciones
operacion = Calculadora()

print(f"La suma es: {operacion.suma()}")
print(f"La resta es: {operacion.resta()}")
print(f"La multiplicación es: {operacion.multiplicacion()}")
print(f"La división es: {operacion.division()}")
