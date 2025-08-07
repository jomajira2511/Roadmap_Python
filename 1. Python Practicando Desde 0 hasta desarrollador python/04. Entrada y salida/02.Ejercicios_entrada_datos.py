"""
===================================================
Script: 05.Ejercicios_Entrada_Salida.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-06
Descripción:
    Este script contiene dos ejercicios prácticos que
    hacen uso de la entrada por teclado y la salida por 
    pantalla para resolver problemas matemáticos comunes.

    Ejercicio 1  Fórmula General:
    El programa solicita al usuario los coeficientes “a”, “b” y “c”
    de una ecuación cuadrática de la forma ax² + bx + c = 0, y utiliza
    la fórmula general para calcular las soluciones. 
    Se muestra el resultado con el mensaje:
        **Ejercicios_entrada_datos.png**

    Ejercicio 2  Promedio del Alumno:
    Se desea tener un algoritmo que permita determinar y mostrar el 
    promedio que ha obtenido un alumno en un determinado curso, 
    conociendo las notas de: tres prácticas, el examen parcial y el examen final.
        • PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
            Donde: P1, P2, P3 : Practicas
            PP: promedio de práctica
            PROM: promedio
            EP: examen parcial
            EF: examen final
===================================================
"""
print("------------------EJERCICIO 1------------------------")
##ingreso de variables 
a = float(input("Ingresa el valor de a : "))
b = float(input("Ingresa el valor de b : "))
c = float(input("Ingresa el valor de c : "))

#Formula
x1 = (((-b + (((b ** 2) - (4*a*c))**0.5)) / (2*a)))
x2 = (((-b - (((b ** 2) - (4*a*c))**0.5)) / (2*a)))

#Impresion de valores 
print("Las posibles soluciones soluciones son:", x1, "y", x2)

print("------------------EJERCICIO 2------------------------")
#Ingreso de datos
p1 = float(input("Ingresa la nota de la practica 1 : "))
p2 = float(input("Ingresa la nota de la practica 2 : "))
p3 = float(input("Ingresa la nota de la practica 3 : "))
ep = float(input("Ingresa la nota del examen parcial  : "))
ef = float(input("Ingresa la nota del examen final : "))

#Formulas 
pp = ((p1 + p2 + p3)/3)
prom = ((pp + (2 * ep) + (3 * ef))/6)

#impresion de valores o resultados
print ("El promedio de la practica es igual a : ", pp )
print ("El promedio general es de : ", prom)





