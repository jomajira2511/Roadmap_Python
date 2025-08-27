"""
===================================================
Script: 03.Accediendo_usando_name.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-26
Descripción:
    Este script automatiza el inicio de sesión en el 
    portal "Validador RIPS Colombia" utilizando Selenium.
    En esta versión se localizan los campos del formulario
    por el atributo 'name' y se ejecuta el proceso de login.
===================================================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializar el navegador Chrome
controlador = webdriver.Chrome()

# Abrir la página de inicio de sesión
controlador.get("https://validadorderipscolombia.com/iniciar-sesion")

# Localizar campo de usuario por NAME e ingresar correo
usuario = controlador.find_element(By.NAME, "_username")
usuario.send_keys("pedro@gmail.com")

# Localizar campo de contraseña por NAME e ingresar clave
clave = controlador.find_element(By.NAME, "_password")
clave.send_keys("pepe123456")

# Localizar el botón de login por clase CSS y hacer clic
boton = controlador.find_element(By.CLASS_NAME, "btn-primary")
boton.click()

# Esperar unos segundos para observar el resultado
time.sleep(5)

# Cerrar el navegador
controlador.quit()
