"""
===================================================
Script: 06.Ejercicios_Listas.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-07
Descripción:
    Ejercicio 1:
        En la siguiente lista, debes hacer un programa que muestre
        los valores al usuario. A su vez, debe pedir dos datos y esos
        que sean ingresados deben ser sustituidos en el primer y segundo lugar:
        Lista base: [20, 50, "Curso", 'Python', 3.14]

    Ejercicio 2:
        Escribe una lista que tenga los números del 1 al 10. Luego,
        debes hacer que los datos que están en las posiciones 4, 7 y 9
        sean multiplicados por 2. Por último, mostrar la lista nueva
        con los nuevos datos.
===================================================
"""


print ("-------------------Ejercicio 1-----------------------")
# Definicion de la lista
Lista = [20, 50, "Curso", 'Python', 3.14]
# Imprime la lista
print("Estos son los datos que contiene la lista = {}". format(Lista))  
# Ingreso de datos por parte del usuario
Dato1 = input("Que dato deseas ingresar a la lista ")  
Dato2 = input("Que dato deseas ingresar a la lista ") 
# Insercion de datos en las posiciones de la lista
Lista[0] = Dato1
Lista[1] = Dato2
# Imprime la lista una vez modificada
print("Este es el estado actual de la lista despues de insertar los valores  = {}".format(Lista))


print ("-------------------Ejercicio 2-----------------------")
#Definicion de la lista 
Numeros = [1,2,3,4,5,6,7,8,9,10] 
# Modificacion de la lista
Numeros[4] = Numeros[4] * 2
Numeros[7] = Numeros[7] * 2
Numeros[9] = Numeros[9] * 2
# Imprime la cadena una vez modificada como lo solicita el ejercicio
print("Estado de la lista despues de agregar los nuevos valores = {}".format(Numeros))
