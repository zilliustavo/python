from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])#Remove Webtools listening

pesquisa = input("Digite a pesquisa: ")

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

campo = driver.find_element(By.XPATH, "//input[@aria-label='Pesquisar']")
campo.send_keys(pesquisa)
campo.send_keys(Keys.ENTER)

resultados = driver.find_element(By.XPATH,"//div[@id='result-stats']").text
print(resultados)
numero_resultados = int(resultados.split("Aproximadamente ")[1].split(' resultados')[0].replace('.',''))
maximo_paginas = numero_resultados/10
pagina_alvo = int(input("%s páginas encontradas, até qual página quer ir?" % (maximo_paginas)))

url_pagina = driver.find_element(By.XPATH,"//a[@aria-label='Page 2']").get_attribute("href")

pagina_atual = 0
start = 10
lista_resultados = []

while pagina_atual <= pagina_alvo:
    if not pagina_atual == 0:
        url_pagina = url_pagina.replace("start=%s" % start, "start=%s" % (start+10)) 
        start += 10
        driver.get(url_pagina)
    pagina_atual += 1

    divs = driver.find_elements(By.XPATH,"//*[@id='search']")
    for div in divs:
        nome = div.find_element(By.TAG_NAME,"span")
        link = div.find_element(By.TAG_NAME,"a")
        resultado = "%s;%s" % (nome.text,link.get_attribute("href"))
        print(resultado)
        lista_resultados.append(resultado)

with open("resultados.txt", "w") as arquivo:
    for resultado in lista_resultados:
        arquivo.write("%s\n" % resultado)
    arquivo.close()
print ("%s resultados encontrados no google salvos no arquivo resultados.txt" %len(lista_resultados))