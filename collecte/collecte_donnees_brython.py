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

driver.get("https://brython.info/index.html")


liens = driver.find_elements(by = By.TAG_NAME, value = 'a')

for lien in liens:
    print(lien.get_attribute("href"))

driver.quit()


'''
Objectef est de collecter dans un premier temps tous les liens du site 
Ensuite de cliquer sur les liens et de récupérer tous les sous liens 

'''