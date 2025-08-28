"""
===================================================
Script: 04.Restablecer_password_con_link.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-27
Descripción:
    Este script automatiza, mediante Selenium, el proceso de 
    recuperación de contraseña en el portal 
    https://validadorderipscolombia.com. 
    Localiza el enlace de "¿Olvidaste tu contraseña?", lo selecciona, 
    introduce un correo electrónico en el campo de recuperación y 
    permite visualizar el resultado antes de cerrar el navegador.
===================================================
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializar el navegador Chrome
controlador = webdriver.Chrome()

# Abrir la página de inicio de sesión del validador RIPS
controlador.get("https://validadorderipscolombia.com/iniciar-sesion")

# Buscar el enlace de recuperación de contraseña por su texto visible
link_recuperacion = controlador.find_element(By.LINK_TEXT, "¿Olvidaste tu contraseña?")
link_recuperacion.click()

# Localizar el campo de correo electrónico por su ID e ingresar el email
correo = controlador.find_element(By.ID, "forgot_password_email")
correo.send_keys("pedro@gmail.com")

# Pausa de 3 segundos para visualizar el resultado de la acción
time.sleep(3)

# Cerrar el navegador y finalizar la sesión de WebDriver
controlador.quit()
