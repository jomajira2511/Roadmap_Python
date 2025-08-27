"""
===================================================
Script: 01.Primer_script.py
Proyecto: Roadmap Python
Autor: Jhon Jiménez
GitHub: https://github.com/jomajira2511
Correo: jomajira2511@gmail.com
Fecha de creación: 2025-08-24
Descripción:
    Script de prueba para abrir el navegador Chrome 
    mediante Selenium, acceder a la URL de inicio de 
    sesión de Udemy en español, y posteriormente cerrar 
    la ventana del navegador.
===================================================
"""


from selenium import webdriver

# Inicializa el controlador de Chrome
driver = webdriver.Chrome()

# Maximiza la ventana del navegador
driver.maximize_window()

# Abre la página de login de Udemy con la URL especificada
driver.get("https://www.udemy.com/join/passwordless-auth/?locale=es_ES&next=https%3A%2F%2Fwww.udemy.com%2F%3Futm_source%3Dadwords%26utm_medium%3Dudemyads%26utm_campaign%3DBranded-Topic_la.ES_cc.LATAM%26campaigntype%3DSearch%26portfolio%3DBrandTopic%26language%3DES%26product%3DCourse%26test%3D%26audience%3DKeyword%26topic%3D%26priority%3D%26utm_content%3Ddeal4584%26utm_term%3D_._ag_122876139243_._ad_762942545252_._kw_cursos%2520en%2520l%25C3%25ADnea%2520udemy_._de_c_._dm__._pl__._ti_aud-2268488108639%3Akwd-1394266915329_._li_9213512_._pd__._%26matchtype%3Db%26gad_source%3D1%26gad_campaignid%3D12560398702%26gbraid%3D0AAAAADROdO1AgHQ0eZwTNVMlZ8rRrHjst%26gclid%3DCj0KCQjw8KrFBhDUARIsAMvIApavUQwQQlmkKN00911t7-M_FLIzz4hBiNa_7GaAsII8lkYOXxJBKNIaAgkREALw_wcB&response_type=html&action=login&mode")

# Cierra el navegador

driver.close()