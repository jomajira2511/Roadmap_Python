"""
===================================================
Script: 05.Metodos_Listas.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-07
Descripción:
    Este script contiene ejemplos prácticos del uso de métodos
    disponibles para manipular listas en Python. Se incluyen
    operaciones como:
        - Agregar elementos (append, insert)
        - Contar ocurrencias (count)
        - Buscar posiciones (index)
        - Ordenar (sort, reverse)
        - Modificar valores directamente por posición
        - Eliminar elementos (pop, remove)
    Además, el script permite al usuario interactuar ingresando
    datos que son insertados o añadidos a la lista para ilustrar
    el funcionamiento de estos métodos.
===================================================
"""
# Metodos con listas
Lista = [1,2,3,4,5]
print("Esta es la lista actual que tenemos : {}". format(Lista))

# Metodo para agregar mas elementos a una lista .append()
Dato = input("Ingresa el dato que deseas agregar a la lista : ")
Lista.append(Dato)
print("Esta es la lista despues de haber agregado el nuevo dato {}".format(Lista))

# Metodo .insert() para agregar en un espacio especifico de la lista
Lugar = int(input("En que posicion de la lista desea agregar el dato? "))
Dato = input("Ingrese el dato que desea agregar en la lista ")
Lista.insert(Lugar , Dato)# Se inserta el dato en la posición indicada
print("Esta es la lista despues de agregar el nuevo valor : {} ".format(Lista))

# Método .count() permite contar cuántas veces aparece un valor en la lista
print("Cantidad de veces que aparece el número 1:", Lista.count(1))  
# Retorna la cantidad de veces que el valor 1 se encuentra en la lista

# Método .index() busca un valor y retorna la posición en la que se encuentra (primera coincidencia)
print("Posición del primer número 2:", Lista.index(2))  
# Retorna la posición de la primera aparición del número 2

# Método .sort() ordena la lista de forma ascendente
Lista.sort()
print("Lista ordenada de forma ascendente:", Lista)

# Método .reverse() invierte el orden actual de la lista 
Lista.reverse()
print("Lista en orden descendente:", Lista)

# Cambiar un valor en una lista en una posicion deseada
Lista[1] = "Nuevo_Dato"  
# Prmite agregar el nuevo dato en la posicion de la lista 

# Metodo .pop () permite eliminar el ultimo dato de la lista 
Lista.pop()
#Elimina el ultimo dato de la lista

# Metodo .remove() se le envia el valor que desea eliminarse 
Lista.remove('Dato_a_eliminar')
# Elimina el dato 

