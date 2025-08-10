"""
===================================================
Script: 05.Ejercicios.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-10
Descripción:
    Ejercicio 1:
        Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, 
        el programa debe retornar el valor 1; si el segundo es mayor al primero, 
        debe retornar -1; si ambos son iguales, debe retornar 0.

    Ejercicio 2:
        Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
        La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
        y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje 
        de IVA, deberá aplicar un 21%.
===================================================
"""
print("----------------------EJERCICIO 1---------------------")

# Creamos la funcion para ingresar numero s
def numeros():  
    #Solicitamos los numero al usuario 
    valor1 = input("Ingresa un valor : ")
    valor2 = input("Ingresa un valor : ")
    #Hacemos las comparaciones para ingresar los valores
    if valor1 > valor2:
        return 1 #Retonarmos el valor 
    elif valor1< valor2:
        return -1 #Retonarmos el valor 
    else:
        return 0 #Retonarmos el valor 

print(numeros())

print("----------------------EJERCICIO 2---------------------")

def iva():
    # Solicita el valor del producto
    total = float(input("Ingresa el valor del producto : "))
    # Solicita el porcentaje de IVA
    valor_iva = int(input("Cuanto es el porcentaje de iva a aplicar : "))
    # Si el IVA no es cero, procesar según sea positivo o negativo
    if valor_iva != 0:
        if valor_iva > 0:
            # Calcula el IVA ingresado por el usuario
            total_a_pagar = ((total * valor_iva) / 100) + total
            return total_a_pagar
        else:
            # Retorna mensaje si el IVA ingresado es negativo
            return "El monto del IVA es negativo"
    else:
        # Si el IVA es cero, aplica 21% por defecto
        total_a_pagar = (total * 0.21) + total
        return total_a_pagar


# Ejecución de la función y visualización del resultado
print("El total de su monto es : ", iva())