"""
===================================================
Script: 01.Ejercicio_1.py
Proyecto: Roadmap Python 
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-13
Descripción:
    Ejercicio basado en el enunciado:

    "Ejercicio 1

    Realizar un programa que conste de una clase llamada Estudiante,
    que tenga como atributos el nombre y la nota del alumno. 
    Definir los métodos para inicializar sus atributos, imprimirlos 
    y mostrar un mensaje con el resultado de la nota y si ha aprobado o no."

===================================================
"""
class Estudiante:
    def __init__(self, nombre, nota):
        """Constructor que inicializa el nombre y la nota del estudiante."""
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        """Imprime el nombre y la nota del estudiante."""
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        """Muestra si el estudiante aprobó o no."""
        if self.nota >= 3.0:
            print(f"Felicidades {self.nombre}, aprobaste con nota {self.nota}")
        else:
            print(f"Lo sentimos {self.nombre}, reprobaste con nota {self.nota}")


# Ejecución del programa
nombre = input("Ingrese el nombre del estudiante: ")
nota = float(input("Ingrese la nota del estudiante: "))

estudiante = Estudiante(nombre, nota)
estudiante.imprimir_datos()
estudiante.resultado()
