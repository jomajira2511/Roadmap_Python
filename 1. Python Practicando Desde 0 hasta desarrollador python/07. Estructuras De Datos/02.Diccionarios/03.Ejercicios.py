"""
===================================================
Script: 03.Ejercicios.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-08
Descripción:
    Ejercicios prácticos sobre el uso de diccionarios.
    Ejercicio 1:
        En el siguiente diccionario se encuentran capitales 
        de los países en el mundo. Debes realizar un programa 
        que pida un país al usuario y muestre la capital de ese 
        país. Si no se encuentra, mostrar un mensaje indicándolo.
    Ejercicio 2:
        Con el siguiente diccionario, debes crear un programa 
        que pregunte al usuario por un número y muestre el 
        jugador al que hace referencia ese número.
===================================================
"""
print("----------------------EJERCICIO 1-------------------------")

# Diccionario de países y capitales
Paises = {
    "Guatemala": "Ciudad de Guatemala", 
    "El Salvador": "San Salvador",
    "Honduras": "Honduras",
    "Nicaragua": "Managua",
    "Costa Rica": "San Jose",
    "Panama": "Panama",
    "Argentina": "Buenos Aires",
    "Colombia": "Bogota",
    "Venezuela": "Caracas",
    "España": "Madrid"
}

# Solicitar país al usuario
Pais = input("Ingrese un país para conocer su capital: ").title()

# Verificar existencia y mostrar resultado
if Pais in Paises:
    print("La capital de {} es: {}".format(Pais, Paises[Pais]))
else:
    print("El país '{}' no se encuentra dentro del diccionario.".format(Pais))


print("----------------------EJERCICIO 2-------------------------")

# Diccionario con números y jugadores
Jugadores = {
    1: "Casillas", 15: "Ramos",
    3: "Pique", 5: "Puyol",
    11: "Capdevila", 14: "Xabi Alonso",
    16: "Busquets", 8: "Xavi Hernandez",
    18: "Pedrito", 6: "Iniesta",
    7: "Villa"
}

# Solicitar número al usuario
numero = int(input("Ingrese un número de jugador: "))

# Comprobar y mostrar usando solo if-elif-else
if numero in Jugadores:
    print("El jugador con el número {} es: {}".format(numero, Jugadores[numero]))
else:
    print("El número {} no corresponde a ningún jugador.".format(numero))
