"""
===================================================
Script: 01.Hilos.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-09-05
Descripción:
    Ejemplo práctico de creación y ejecución de hilos
    (threads) en Python usando la librería threading.

    Un hilo permite ejecutar tareas en paralelo, de forma
    concurrente, lo que mejora el rendimiento en procesos
    que requieren espera o múltiples operaciones simultáneas.

    En este script:
    - Se define una clase Hilo que hereda de threading.Thread.
    - Se sobrescribe el método run(), que contiene la lógica
      que ejecutará cada hilo.
    - Se lanzan múltiples hilos de forma controlada.
===================================================
"""

import threading  # Librería estándar para trabajar con hilos
import time       # Permite simular retardos o pausas en la ejecución

# ===================================================
# Definición de la clase Hilo (hereda de Thread)
# ===================================================
class Hilo(threading.Thread):
    def run(self):
        """
        Método que se ejecuta cuando el hilo inicia.
        Sobrescribe el método run() de la clase Thread.
        """
        print(f"🔵 Inicio : {self.getName()}")   # Mensaje de inicio del hilo
        time.sleep(1)                           # Simulación de tarea
        print(f"✅ Final : {self.getName()}")   # Mensaje al finalizar


# ===================================================
# Ejecución principal del programa
# ===================================================
if __name__ == "__main__":
    # Lanzamos 4 hilos de forma secuencial con un retardo entre ellos
    for i in range(4):
        hilo = Hilo(name=f"Hilo {i + 1}")  # Nombramos cada hilo
        hilo.start()                       # Iniciamos el hilo
        time.sleep(0.1)                    # Retardo breve para escalonar la ejecución
