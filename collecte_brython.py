#Collecte de données sur Brython 

#Clément Husson 

#Packages 
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

sleep(2)

boutton_langue = driver.find_element(by = By.XPATH, value = '/html/body/div[2]/select')

boutton_langue.click()

string_language = []

selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[2]/select'))
length = len(selection.options)

sleep(2)

#Recuperer le nom de l'option

for i in range (0, length, 1) : 
    selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[2]/select'))
    selection.select_by_index(i)
    sleep(1)   
    chain = driver.find_element(by = By.XPATH, value = "//*[@id='content']/table[2]/tbody/tr/td[1]/p[1]").text
    print(detect(str(chain)))

sleep(5)

#Clic sur le bouton 
#choix option ( dois parcourir toutes les issus possibles)
# scraping du premier paragrphque 
#Analyse de la langue 
#Retour sur le resulats (avec nom de page)



