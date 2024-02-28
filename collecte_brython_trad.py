# Collecte de données sur Brython - Détection des pages traduitent

# Clément Husson 

# Packages 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd 
from langdetect import detect

# Scrapping

#Page 1 du site Brython

def page1() :

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://brython.info/index.html")

    sleep(2)

    boutton_langue = driver.find_element(by = By.XPATH, value = '/html/body/div[2]/select')

    boutton_langue.click()

    langue_detect_1 = []
    langue_detect_2 = []


    selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[2]/select'))
    length = len(selection.options)

    sleep(2)


    for i in range (1, length + 1, 1) : 
        xpath = '/html/body/div[2]/select/option[' + str(i) + ']'
        langue1 = driver.find_element(by=By.XPATH, value=str(xpath)).text
        langue_detect_1.append(langue1)
        print('La langue détecté sur la selection est :')
        print(langue1)
        sleep(1)

    for i in range (0, length, 1) : 
        selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[2]/select'))
        selection.select_by_index(i)
        sleep(1)   
        chain = driver.find_element(by = By.XPATH, value = "//*[@id='content']/table[2]/tbody/tr/td[1]/p[1]").text
        langue2 = detect(str(chain))
        if langue2 == 'fr' :
            langue2 = 'Français'
        elif langue2 == 'en' :  
            langue2 = 'English'
        elif langue2 == 'es' :
            langue2 = 'Español'
        elif langue2 == 'de' :
            langue2 = 'Deutsch'
        elif langue2 == 'it' :
            langue2 = 'Italiano'
        elif langue2 == 'pt' :
            langue2 = 'Portuguese (Br.)'
        elif langue2 == 'nl' :
            langue2 = 'Nederlands'
        elif langue2 == 'br' :
            langue2 = 'Brezhoneg'

        langue_detect_2.append(langue2)
        print('La langue détecté sur le site est :')
        print(langue2)

    sleep(2)

    count = 0

    for i in range (0, len(langue_detect_1), 1) :
        if langue_detect_1[i] == langue_detect_2[i] :
            count = count + 1
        else :
            print("\n")
            print('La page n\'est pas traduite correctement')
            print("La ou l'une des erreurs proviens de la langue : " + langue1)
        
        if count == len(langue_detect_1) :
            print("\n")
            print('La page est traduite correctement')

    driver.quit()

page1()
