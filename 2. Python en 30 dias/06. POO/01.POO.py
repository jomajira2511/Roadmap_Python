#Programacion orientada a aobjetos o POO

class Gelatina():  ##estructura de una clase 
    def __init__(self, sabor, color, tamanio):   # creamos un contructor, qu eincializa las caracteristicas de la calse
        self.sabor = sabor #Estas son las caracterisitcas o el molde, tambine conocido como contructor
        self.color = color
        self.tamanio = tamanio 
    
    def imprimir(self):
        print(f"La gelatina es de {self.sabor}")
        print(f"La gelatina se ve {self.color}")
        print(f"La gelatina es de un tamanio {self.tamanio}")


gel1  = Gelatina("Fresa", "Rojo","Grande")  #Creamos una instancia de la clase 
gel2 = Gelatina("Mora", "morado" , "Mediana")

gel1.imprimir()   #llamamos la clase 
gel2.imprimir()





