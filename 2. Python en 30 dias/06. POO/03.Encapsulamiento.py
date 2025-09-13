# ===================================================
# Clase Coche
# Representa un automóvil con marca, kilometraje y año.
# ===================================================
class Coche:
    def __init__(self, marca, km, anio):
        self.marca = marca
        self.km = km
        self.anio = anio
        print(f"Se ha creado el vehículo {self.marca}")

    def arrancar(self,arrancamos):
        self.enmarcha = arrancamos
        if(self.enmarcha):
            return "El auto esta encendido"
        else:
            return "El coche esta apagado "

    def __str__(self):
        return "El auto es un {}, tiene {} KM y es del año {}".format(
            self.marca, self.km, self.anio
        )
    


MiCoche = Coche("Audi", 200, 1993)

# Llamada implícita a __str__ al imprimir el objeto
print(str(MiCoche)) 

# Eliminación manual de la instancia (invoca __del__)
del MiCoche


