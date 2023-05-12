from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

#options = webdriver.ChromeOptions()
#options.add_experimental_option('excludeSwitches', ['enable-logging'])#Remove Webtools listening

class RoboYoutube():
    def __init__(self):
        self.webdriver = webdriver.Chrome()

    def busca(self, busca, paginas):
        videos = []
        pagina = 1

        url = "https://www.youtube.com/results?search_query=%s" % busca
        self.webdriver.get(url)

 
        while pagina <= paginas:
            titulos = self.webdriver.find_elements(By.XPATH,"//*[@id='video-title']")
            #arq = open("videosEncontrados.txt", "w", encoding="utf-8")
            for titulo in titulos:
                if titulo.text not in videos:
                    print("Vídeo encontrado: %s - Link : %s" % (titulo.text, titulo.get_attribute("href")))
                    videos.append("Vídeo encontrado: %s - Link : %s" % (titulo.text, titulo.get_attribute("href")))
                #arq.write(titulo.text + "/n")     
            self.proxima_pagina(pagina)
            pagina += 1

            with open("videosEncontrados.txt", "w", encoding="utf-8") as arquivo:
                for video in videos:
                    arquivo.write("%s\n" % video)
                arquivo.close()                

    def proxima_pagina(self, pagina):
        print("Mudando para pagina: %s"% (pagina + 1))
        bottom = pagina * 10000
        self.webdriver.execute_script("window.scrollTo(0, %s);" % bottom)
        time.sleep(3)

bot = RoboYoutube()
search = pyautogui.prompt('Qual é o tema da busca?')
pages = int(pyautogui.prompt('Quantas páginas quer buscar?'))
bot.busca(search, pages)

