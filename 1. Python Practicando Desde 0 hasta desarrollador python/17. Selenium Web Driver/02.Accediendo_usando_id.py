"""
===================================================
Script: 02.Accediendo_usando_id.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-26
Descripción:
    Este script automatiza el inicio de sesión en el 
    portal "Validador RIPS Colombia" utilizando Selenium.
    Se abre el navegador Chrome, se completan los campos
    de usuario y contraseña, y se realiza el clic en el 
    botón de inicio de sesión.
===================================================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializar el navegador Chrome
controlador = webdriver.Chrome()

# Maximizar la ventana del navegador
controlador.maximize_window()

# Abrir la página de inicio de sesión del validador RIPS
controlador.get("https://validadorderipscolombia.com/iniciar-sesion")
time.sleep(1)

# Localizar el campo de usuario por ID e ingresar el correo
usuario = controlador.find_element(By.ID, "username")
usuario.send_keys("pedro@gmail.com")
time.sleep(1)

# Localizar el campo de contraseña por ID e ingresar la clave
password = controlador.find_element(By.ID, "password")
password.send_keys("pepe123456")
time.sleep(1)

# Localizar el botón de inicio de sesión por clase CSS y hacer clic
# Este metodo funciona, ya que es el unico boton que esta en la pagina 
boton = controlador.find_element(By.CLASS_NAME, "btn-primary")
boton.click()

# Esperar unos segundos para observar el resultado
time.sleep(5)

# Cerrar el navegador
controlador.quit()
