#Collecte de données sur le site internet de Brython

#Importation des librairies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd 
from langdetect import detect

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

pages = ["https://brython.info/index.html", 
                       "https://brython.info/static_tutorial/fr/index.html", 
                       "https://brython.info/demo.html",
                       "https://brython.info/static_doc/3.12/fr/intro.html",
                       "https://brython.info/gallery/gallery_fr.html",]


liens_brython = set()
liens_site = set()
len = len("https://brython")

for page in pages : 
    driver.get(page)

    liens = driver.find_elements(by = By.TAG_NAME, value = 'a')
    
    for lien in liens:
        lien2 = lien.get_attribute("href")
        if lien2 is not None and (lien2[0:len] == "https://brython" or lien2[0:len] == "http://www.brython") :
            liens_brython.add(lien2)
        else :
            liens_site.add(lien2)
    

print(liens_site)
print(liens_brython)



driver.quit()










'''
Objectef est de collecter dans un premier temps tous les liens du site 
Ensuite de cliquer sur les liens et de récupérer tous les sous liens 


# Définir le set avec des chaînes de caractères
mon_set = {"bonjour tout le monde", "salut", "bonjour à tous", "hello"}

# Parcourir chaque élément du set
for chaine in mon_set:
    # Vérifier si la sous-chaîne "bonjour" est présente dans la chaîne actuelle
    if "bonjour" in chaine:
        # Afficher la chaîne de caractères contenant "bonjour"
        print(chaine)
'''