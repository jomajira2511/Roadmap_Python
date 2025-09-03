"""
===================================================
Script: 03.Metodos_especiales.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-02
Descripción:
    Ejemplo práctico del uso de métodos especiales en Python
    (también llamados *dunder methods* o *magic methods*). 
    Estos permiten modificar el comportamiento de objetos
    creados a partir de clases personalizadas.

    Métodos implementados:
    - __str__ : Representación en forma de cadena del objeto.
    - __len__ : Define cómo se comporta la función len().
    - __del__ : Se ejecuta cuando un objeto es eliminado.
===================================================
"""

# ===================================================
# Clase Libro → uso de métodos especiales
# ===================================================

class Libro:
    def __init__(self, nombre, autor, paginas):
        """
        Constructor de la clase Libro.
        Inicializa los atributos de la instancia.
        """
        self.nombre = nombre
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        """
        Método especial __str__:
        Define la representación del objeto como texto (string).
        Se invoca automáticamente al usar print() o str(objeto).
        """
        return f'{self.nombre} escrito por {self.autor} y tiene {self.paginas} páginas'
    
    def __len__(self):
        """
        Método especial __len__:
        Permite que la función len() funcione con instancias de esta clase.
        En este caso devuelve el número de páginas del libro.
        """
        return self.paginas
    
    def __del__(self):
        """
        Método especial __del__:
        Se ejecuta automáticamente cuando un objeto es eliminado
        con la instrucción del o al finalizar el programa.
        """
        print(" Se ha eliminado un libro de la memoria.")


# ===================================================
# Uso de la clase Libro y sus métodos especiales
# ===================================================

# Crear un objeto (instancia de la clase Libro)
libro1 = Libro("Curso Python", "Jhon", 120)

# Usando __str__ automáticamente con print()
print(libro1)

# Usando __len__ con len()
print(len(libro1))

# Eliminando el objeto → invoca __del__
del libro1
