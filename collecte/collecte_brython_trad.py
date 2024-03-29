'''
Collecte de données web sur le site de Brython

Détection des pages traduites et non traduites sur le site de Brython

'''


#Importation des librairies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from time import sleep
from langdetect import detect
import pandas as pd
import matplotlib.pyplot as plt


#Fonction principale qui détecte la langue de chaque page du site internet et produit un graphique récapilutatif
def detection_langue() :
    
    #Lors de l'execution du script le navigateur ouvert est masqué
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    try : 
        driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    except :
        print('Erreur lors de l\'ouverture du navigateur')
        return


    #Liste des liens à scrapper sur le site
    liste_des_liens = ["https://brython.info/index.html", 
                       "https://brython.info/static_tutorial/fr/index.html", 
                       "https://brython.info/demo.html",
                       "https://brython.info/static_doc/3.12/fr/intro.html",
                       "https://brython.info/gallery/gallery_fr.html",]
    
    #Nom des pages 
    liste_name_page = ["Principale",
                       "Tutoriel",
                       "Démonstration",
                       "Documentation",
                       "Galerie",]
    
    #Dictionnaire des langues
    langue_dict = {
                    'fr': 'Français',
                    'en': 'English',
                    'es': 'Español',
                    'de': 'Deutsch',
                    'it': 'Italiano',
                    'pt': 'Portuguese (Br.)',
                    'nl': 'Nederlands',
                    'no': 'Brezhoneg'
                }
    
    nb_pages = len(liste_name_page)
    nb_pages_traduites = 0
    nb_pages_non_traduites = 0

    #Boucle principale pour chaque page
    for j in range (0, len(liste_des_liens), 1) : 
        lien = liste_des_liens[j]
        
        driver.get(lien)

        sleep(1)

        boutton_langue = driver.find_element(by = By.CLASS_NAME, value =  'language')
        boutton_langue.click() 

        langue_detect_1 = []
        langue_detect_2 = []

        selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[2]/select'))
        length = len(selection.options)

        #Boucle qui détecte la langue sélectionnée de la page (Ajout de l'information dans la liste : langue_detect_1)
        for i in range (1, length + 1, 1) : 
            xpath = '/html/body/div[2]/select/option[' + str(i) + ']'
            langue1 = driver.find_element(by=By.XPATH, value=str(xpath)).text
            langue_detect_1.append(langue1)
            
        #Boucle qui détecte la langue de la page à partir du texte (spécifique à chaque page)
        for i in range (0, length, 1) : 
            selection = Select(driver.find_element(by=By.XPATH, value='/html/body/div[2]/select'))
            selection.select_by_index(i)   

            #Spécification pour chaque page 
            if liste_name_page[j] == "Principale" or liste_name_page[j] == "Tutoriel" :
                txt_page = ""
                Strings = driver.find_elements(by = By.TAG_NAME, value = 'p')
                for String in Strings : 
                    txt_page = txt_page +  str(String.text)


            elif liste_name_page[j] == "Démonstration" :
                txt_page = ""
                menu = driver.find_element(by = By.TAG_NAME, value = 'ul')
                len_menu = menu.find_elements(by = By.TAG_NAME, value = 'li')
                len_menu = len(len_menu)
                for k in range (0, len_menu, 1) :
                    boutton_menu = driver.find_elements(by = By.CLASS_NAME, value = 'menu')
                    boutton_menu[k].click()
                    Strings = driver.find_elements(by = By.TAG_NAME, value = 'p')
                    for String in Strings : 
                        txt_page = txt_page +  str(String.text)
            
            elif liste_name_page[j] == "Documentation" :
                txt_page = ""
                menu = driver.find_element(by = By.TAG_NAME, value = 'td')
                len_menu = menu.find_elements(by = By.TAG_NAME, value = 'a')
                len_menu = len(len_menu)
                for k in range (0, len_menu, 1) :
                    boutton_menu = driver.find_elements(by = By.CLASS_NAME, value = 'navig')
                    boutton_menu[k].click()
                    Strings = driver.find_elements(by = By.TAG_NAME, value = 'p')
                    for String in Strings : 
                        txt_page = txt_page +  str(String.text)

            
            elif liste_name_page[j] == "Galerie" :
                txt_page = ""
                Strings = driver.find_elements(by = By.TAG_NAME, value = 'a')
                for String in Strings : 
                    txt_page = txt_page +  str(String.text)

            #On ajoute la langue détectée dans la liste : langue_detect_2
            langue2 = langue_dict.get(detect(str(txt_page)))
            langue_detect_2.append(langue2)

            #L'obejctif est de comparer les deux listes (langue_detect_1 avec langue_detect_2) pour voir si la langue détectée est la bonne

        sleep(0.5)

        #Le compteur (count) permet de vérifier si l'entièreté de la page est traduite correctement
        count = 0
        langue_detect = ""
        

        #Boucle qui compare les deux listes pour vérifier si la langue détectée est la bonne
        for i in range (0, len(langue_detect_1), 1) :
            langue_detect = langue_detect +  str(langue_detect_1[i]) + " "

            if langue_detect_1[i] == langue_detect_2[i] :
                count = count + 1

            else :
                print("\n")
                print('La page '+ str(liste_name_page[j]) +' n\'est pas traduite correctement')
                print("La ou l'une des erreurs proviens de la langue : " + langue_detect_1[i])
            
            if count == len(langue_detect_1) :
                print("\n")
                print('La page '+ str(liste_name_page[j]) +' est traduite correctement')
                nb_pages_traduites = nb_pages_traduites + 1

        if count != len(langue_detect_1) : 
            nb_pages_non_traduites = nb_pages_non_traduites + 1

        print("Les langues détectées sur la page "+ str(liste_name_page[j]) +" sont : " + str(langue_detect))
        
    driver.quit()

    print("\n L'execution du programme est terminée")

    print("\n Nombre de pages traduites correctement : " + str(nb_pages_traduites) + " sur " + str(nb_pages))
    print("\n Nombre de pages non traduites correctement : " + str(nb_pages_non_traduites) + " sur " + str(nb_pages))

    data = {
        'Pages traduites' : [nb_pages_traduites],
        'Pages non traduites' : [nb_pages_non_traduites],
        'Total pages' : [nb_pages],
    }
    
    legende = ["Pages traduites", "Pages non traduites"]
    data = [nb_pages_traduites, nb_pages_non_traduites]

    plt.pie(data, labels = legende, autopct='%2f%%') 
    plt.title('Diagramme circulaire des traductions des pages du site Brython')    
    plt.show()     

detection_langue()
