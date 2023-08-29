import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def send_whatsapp_message():
    # Inicializar el navegador
    driver = webdriver.Chrome()  # Asegúrate de tener ChromeDriver instalado

    # Abrir WhatsApp Web
    driver.get("https://web.whatsapp.com/")
    time.sleep(10)  # Dar tiempo para escanear el código QR y cargar la página

    # Buscar el contacto al que deseas enviar un mensaje
    contact_name = "Nata"
    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"]')
    search_box.send_keys(contact_name)
    time.sleep(2)

    # Abrir el chat del contacto
    contact = driver.find_element_by_xpath(f'//span[@title="{contact_name}"]')
    contact.click()
    time.sleep(2)

    # Escribir y enviar el mensaje
    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
    message = "¡Hola! Este es un mensaje enviado desde Python."
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

    # Cerrar el navegador
    driver.quit()

# Programar la tarea para que se ejecute todos los días a la misma hora
schedule.every().day.at("20:07").do(send_whatsapp_message)  # Cambia "08:00" a la hora deseada

while True:
    schedule.run_pending()
    time.sleep(1)
