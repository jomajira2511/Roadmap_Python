
# Funcion Break
for i in range(1, 11):
    print(i)
    # Implementacion de break, para parar el ciclo, en caso de que la condicion sea verdad
    if i == 5:
        break  # Rompe el loop cuando la condicion sea verdadera 


# Funcion Continue

for i in range(1, 11):
    # Implementacion de Continua, en caso de que sea verdadera la condicion "Omite" el resultado y continua la ejecucion
    if i == 5:
        continue  # Continua con el loop, despues de hacer las operaciones
    print(i)