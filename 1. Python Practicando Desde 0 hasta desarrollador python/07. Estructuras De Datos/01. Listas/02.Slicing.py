"""
===================================================
Script: 05.Listas_Slicing.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-07
Descripción:
    Este script contiene una lista de 20 lenguajes de programación
    y aplica técnicas de debanado (slicing) para obtener subconjuntos
    de elementos. Se muestra el uso de índices positivos, negativos,
    y rangos incompletos en listas.
===================================================
"""
# Lista de 20 lenguajes de programación
lenguajes_programacion = [ 
    "Python",
    "Java",
    "C",
    "C++",
    "C#",
    "JavaScript",
    "TypeScript",
    "Go",
    "Rust",
    "Ruby",
    "PHP",
    "Swift",
    "Kotlin",
    "R",
    "MATLAB",
    "SQL",
    "Shell (Bash)",
    "Perl",
    "Dart",
    "Scala"
]

#Debanado o slicing de listas
#sintaxis slicing variable[inicio:fin]
print(lenguajes_programacion[0:5])
print(lenguajes_programacion[:2]) #Cuando no se colocan valores python, lo toma como si fuera un 0 
print(lenguajes_programacion[1:]) 
print(lenguajes_programacion[-1]) #Al colocarle un numero negativo, empieza desde atras 
