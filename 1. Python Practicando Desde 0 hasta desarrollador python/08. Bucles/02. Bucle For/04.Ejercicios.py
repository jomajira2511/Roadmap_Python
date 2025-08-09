"""
===================================================
Script: 04.Ejercicios.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-09
Descripción:
    Ejercicios prácticos utilizando la función range()
    para recorrer secuencias numéricas con bucles for.

Ejercicio 1:
    Imprimir por pantalla los números del 1 al 10,
    luego, pedir al usuario dos números y mostrar
    el rango de números entre ambas cifras.

Ejercicio 2:
    Pedir al usuario que ingrese 2 números, después,
    se debe mostrar el rango de esos 2 números, pero,
    solo imprimiendo los números que sean impares.
===================================================
"""

print("-----------------------EJERCICIO 1-----------------")
print("Numero del 1 al 10 ")
#Bucle for que recorre del 1 al 10 (el último número del range no se incluye, por eso usamos 11)
for i in range(1,11):
    print(i)

print("\n Ingresa dos numero y te dare el rango de numero entre ellos ")
Numero1 = int(input("\nIngresa el primer numero : "))  #Solicitamos el primer numero 
Numero2 = int(input("\nIngresa el segundo numero : ")) #Solicutamos el segundo numero 

# Bucle que imprime desde Numero1 hasta Numero2 (sumamos +1 para incluir el último número en el rango)
for i in range(Numero1, Numero2+1):
    print(i)

print("-----------------------EJERCICIO 2-----------------")
#solicitud de datos por teclado 
print("\n Ingresa dos numero y te dare el rango, pero solo de numero impares ")
Numero1 = int(input("\nIngresa el primer numero : "))  #Solicitamos el primer numero 
Numero2 = int(input("\nIngresa el segundo numero : ")) #Solicutamos el segundo numero 

# Recorrer el rango desde Numero1 hasta Numero2
for i in range(Numero1 ,Numero2+1):
    # Saltar los números pares usando 'continue'
    if i % 2 == 0:
        continue
    print(i)

