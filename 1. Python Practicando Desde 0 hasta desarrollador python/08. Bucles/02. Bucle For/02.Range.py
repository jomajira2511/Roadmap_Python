"""
===================================================
Script: 01.Range.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-09
Descripción:
    Ejemplo práctico del uso de la función range()
    para generar secuencias numéricas e iterarlas
    con un bucle for.

    Conceptos clave:
        - range(inicio, fin) → Genera números desde 'inicio' hasta 'fin - 1'.
        - range(inicio, fin, paso) → Permite definir el incremento o salto.
        - El valor 'fin' nunca se incluye en la secuencia.
===================================================
"""
#Range -> funcion que permite recorrer un bucle, pero este solicita 2 argumentos (Inicio, final)

for i in range(1,11):  # 2 argumentos (Inicio, final ), normalmente, el final nunca es tomado en cuenta 
    print("Rango de 1 en 1 : {}".format(i))
    i+=1

for i in range(1,11, 2):  # 3 argumentos (Inicio, final, recorrido ), el 3 valor, es el recorrido que hace para el ejemplo va de 2 en 2 
    print("Rango de 2 en 2 : {}".format(i))
    i+=1
