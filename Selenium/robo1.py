from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])#Remove Webtools listening

print("Iniciando nosso robô...\n")


arq = open("res.txt", "w")
driver = webdriver.Chrome(options=options)
driver.get("https://registro.br/")
time.sleep(3)

with open("dominios.csv") as dominios:
    for dominio in dominios:
        pesquisa = driver.find_element(By.ID,"is-avail-field")
        pesquisa.clear() #Limpando a barra de pesquisa
        pesquisa.send_keys(dominio)
        pesquisa.send_keys(Keys.RETURN)
        time.sleep(2)

        resultados = driver.find_elements(By.TAG_NAME, "strong")
        texto = "Domínio %s %s" % (dominio, resultados[4].text)
        arq.write(texto)
arq.close
driver.close()