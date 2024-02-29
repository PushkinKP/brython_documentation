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

def detection_langue() :

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    liste_des_liens = ["https://brython.info/index.html", 
                       "https://brython.info/static_tutorial/fr/index.html", 
                       "https://brython.info/demo.html",
                       "https://brython.info/static_doc/3.12/fr/intro.html",
                       "https://brython.info/gallery/gallery_fr.html",]
    

    for j in range (0, len(liste_des_liens), 1) : 
        lien = liste_des_liens[j]
        
        driver.get(lien)

        sleep(1)

        boutton_langue = driver.find_element(by = By.XPATH, value = '/html/body/div[2]/select')

        boutton_langue.click()

        langue_detect_1 = []
        langue_detect_2 = []


        selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[2]/select'))
        length = len(selection.options)

        sleep(1)

        if j == 0 :
            for i in range (1, length + 1, 1) : 
                xpath = '/html/body/div[2]/select/option[' + str(i) + ']'
                langue1 = driver.find_element(by=By.XPATH, value=str(xpath)).text
                langue_detect_1.append(langue1)
                #print('La langue détecté sur la selection est :')
                #print(langue1)
                sleep(0.5)
                

            for i in range (0, length, 1) : 
                selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[2]/select'))
                selection.select_by_index(i)
                sleep(0.5)   
                #Spécification pour chaque page 
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
                elif langue2 == 'no' :
                    langue2 = 'Brezhoneg'

                langue_detect_2.append(langue2)
                #print('La langue détecté sur le site est :')
                #print(langue2)

            sleep(2)

            count = 0
            langue_detect = ""

            for i in range (0, len(langue_detect_1), 1) :
                langue_detect = langue_detect +  str(langue_detect_1[i]) + " "
                if langue_detect_1[i] == langue_detect_2[i] :
                    count = count + 1
                else :
                    print("\n")
                    print('La page principale n\'est pas traduite correctement')
                    print("La ou l'une des erreurs proviens de la langue : " + langue_detect_1[i])
                
                if count == len(langue_detect_1) :
                    print("\n")
                    print('La page principale est traduite correctement')
            print("Les langues détectées sur la page " + str(j+1) + " sont : " + str(langue_detect))

        elif j == 1 :
            for i in range (1, length + 1, 1) : 
                xpath = '/html/body/div[2]/select/option[' + str(i) + ']'
                langue1 = driver.find_element(by=By.XPATH, value=str(xpath)).text
                langue_detect_1.append(langue1)
                #print('La langue détecté sur la selection est :')
                #print(langue1)
                sleep(0.5)
                

            for i in range (0, length, 1) : 
                selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[2]/select'))
                selection.select_by_index(i)
                sleep(0.5)   
                #Spécification pour chaque page 
                chain = driver.find_element(by = By.XPATH, value = '//*[@id="content"]/p[1]').text 
                
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
                elif langue2 == 'no' :
                    langue2 = 'Brezhoneg'

                langue_detect_2.append(langue2)
                #print('La langue détecté sur le site est :')
                #print(langue2)

            sleep(1)

            count = 0
            langue_detect = ""

            for i in range (0, len(langue_detect_1), 1) :
                langue_detect = langue_detect +  str(langue_detect_1[i]) + " "
                if langue_detect_1[i] == langue_detect_2[i] :
                    count = count + 1
                else :
                    print("\n")
                    print('La page "Tutoriel" n\'est pas traduite correctement')
                    print("La ou l'une des erreurs proviens de la langue : " + langue_detect_1[i])
                
                if count == len(langue_detect_1) :
                    print("\n")
                    print('La page "Tutoriel" est traduite correctement')
            print("Les langues détectées sur la page " + str(j+1) + " sont : " + str(langue_detect))
        
        elif j == 2 :
            for i in range (1, length + 1, 1) : 
                xpath = '/html/body/div[2]/select/option[' + str(i) + ']'
                langue1 = driver.find_element(by=By.XPATH, value=str(xpath)).text
                langue_detect_1.append(langue1)
                #print('La langue détecté sur la selection est :')
                #print(langue1)
                sleep(1)
                

            for i in range (0, length, 1) : 
                selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[2]/select'))
                selection.select_by_index(i)
                sleep(0.5)   
                #Spécification pour chaque page 
                chain = driver.find_element(by = By.XPATH, value = '//*[@id="home"]').text

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
                elif langue2 == 'no' :
                    langue2 = 'Brezhoneg'

                langue_detect_2.append(langue2)
                #print('La langue détecté sur le site est :')
                #print(langue2)

            sleep(2)

            count = 0
            langue_detect = ""

            for i in range (0, len(langue_detect_1), 1) :
                langue_detect = langue_detect +  str(langue_detect_1[i]) + " "
                if langue_detect_1[i] == langue_detect_2[i] :
                    count = count + 1
                else :
                    print("\n")
                    print('La page  "Demo" n\'est pas traduite correctement')
                    print("La ou l'une des erreurs proviens de la langue : " + langue_detect_1[i])
                
                if count == len(langue_detect_1) :
                    print("\n")
                    print('La page "Demo" est traduite correctement')
            print("Les langues détectées sur la page " + str(j+1) + " sont : " + str(langue_detect))
        
        elif j == 3 :
            for i in range (1, length + 1, 1) : 
                xpath = '/html/body/div[2]/select/option[' + str(i) + ']'
                langue1 = driver.find_element(by=By.XPATH, value=str(xpath)).text
                langue_detect_1.append(langue1)
                #print('La langue détecté sur la selection est :')
                #print(langue1)
                sleep(1)
                

            for i in range (0, length, 1) : 
                selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[2]/select'))
                selection.select_by_index(i)
                sleep(1)   
                #Spécification pour chaque page 
                chain = driver.find_element(by = By.XPATH, value = '//*[@id="content"]/blockquote[2]').text

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
                elif langue2 == 'no' :
                    langue2 = 'Brezhoneg'

                langue_detect_2.append(langue2)
                #print('La langue détecté sur le site est :')
                #print(langue2)

            sleep(2)

            count = 0
            langue_detect = ""

            for i in range (0, len(langue_detect_1), 1) :
                langue_detect = langue_detect +  str(langue_detect_1[i]) + " "
                if langue_detect_1[i] == langue_detect_2[i] :
                    count = count + 1
                else :
                    print("\n")
                    print('La page "Documentation" n\'est pas traduite correctement')
                    print("La ou l'une des erreurs proviens de la langue : " + langue_detect_1[i])
                
                if count == len(langue_detect_1) :
                    print("\n")
                    print('La page "Documentation" est traduite correctement')
            print("Les langues détectées sur la page " + str(j+1) + " sont : " + str(langue_detect))
        
        elif j == 4 :
            for i in range (1, length + 1, 1) : 
                xpath = '/html/body/div[2]/select/option[' + str(i) + ']'
                langue1 = driver.find_element(by=By.XPATH, value=str(xpath)).text
                langue_detect_1.append(langue1)
                #print('La langue détecté sur la selection est :')
                #print(langue1)
                sleep(1)
                

            for i in range (0, length, 1) : 
                selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[2]/select'))
                selection.select_by_index(i)
                sleep(1)   
                #Spécification pour chaque page 
                chain = driver.find_element(by = By.XPATH, value = '//*[@id="demos"]/tbody/tr/td[2]/h3').text

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
                elif langue2 == 'no' :
                    langue2 = 'Brezhoneg'

                langue_detect_2.append(langue2)
                #print('La langue détecté sur le site est :')
                #print(langue2)

            sleep(2)

            count = 0
            langue_detect = ""

            for i in range (0, len(langue_detect_1), 1) :
                langue_detect = langue_detect +  str(langue_detect_1[i]) + " "
                if langue_detect_1[i] == langue_detect_2[i] :
                    count = count + 1
                else :
                    print("\n")
                    print('La page "Gallerie" n\'est pas traduite correctement')
                    print("La ou l'une des erreurs proviens de la langue : " + langue_detect_1[i])
                
                if count == len(langue_detect_1) :
                    print("\n")
                    print('La page "Gallerie" est traduite correctement')
            print("Les langues détectées sur la page " + str(j+1) + " sont : " + str(langue_detect))
        
    driver.quit()



detection_langue()

