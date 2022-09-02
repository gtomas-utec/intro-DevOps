import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#Ingreso al servidor de mi vm
driver.get("http://192.168.70.114:8117/")
#usuario y clave
elemento1 = driver.find_element(By.NAME, "user")
elemento1.clear()
elemento1.send_keys("root")
elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("password")
#ingreso
driver.find_element(By.CLASS_NAME, "btn").click()
#sugirieron refrescar la pagina
driver.get("http://192.168.70.114:8117/")
#asunto
elemento3 = driver.find_element(By.NAME, "Subject")
elemento3.clear()
elemento3.send_keys("Asunto del parcial")
#contenido
elemento4 = driver.find_element(By.NAME, "Content")
elemento4.clear()
elemento4.send_keys("Se pide para el parcial")
#Click en crear
driver.find_element(By.NAME, "SubmitTicket").click()

#esperamos
time.sleep(20)
#cerramos
driver.close()