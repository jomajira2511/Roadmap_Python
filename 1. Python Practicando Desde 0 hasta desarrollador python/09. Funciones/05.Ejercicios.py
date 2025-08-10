
# Creamos la funcion para ingresar numero s
def numeros():  
    #Solicitamos los numero al usuario 
    valor1 = input("Ingresa un valor : ")
    valor2 = input("Ingresa un valor : ")
    #Hacemos las comparaciones para ingresar los valores
    if valor1 > valor2:
        print (1)
    elif valor1< valor2:
        print(-1)
    elif valor1 == valor2:
        print (0)
    return   #Retonarmos el valor 

numeros()