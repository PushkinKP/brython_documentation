# Collecte de données sur Brython - Détection des pages cachées

# Jules Cnockaert

# Packages

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd 

# Scrapping

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://brython.info/index.html")

sleep(2)

# A refaire en utilisant les selecteurs CSS, en faisant un "tableau"/dictionnaire pour les pages(redemander à Denis) 
# Pages cachées = liens dans les pages qui ne sont pas visibles(c-à-d pas dans les selecteurs)
#   |   |
#   |   |
#   v   v

links = []
len_links = []
for i in range(1,7): 
    page = driver.find_element(by = By.XPATH, value = f'/html/body/div[1]/a[{i}]')
    page.click()
    sleep(3) 
    if (i == 1):
        sleep(1)
    if (i == 2):
        links2 = driver.find_elements(by = By.XPATH, value = '/html/body/div[3]/div/div[1]/ul/li')
        res2 = links.append(links2)
        len_links.append(len(links2))
        sleep(1)
    elif (i == 3):
        links3 = driver.find_elements(by = By.XPATH, value = '/html/body/table/tbody/tr/td[1]/h4' and '/html/body/table/tbody/tr/td[1]/div/a')
        res3 = links.append(links3)
        len_links.append(len(links3))
        sleep(1)
    elif (i == 4):
        sleep(1)
    elif (i == 5):
        sleep(1)
    elif (i == 6): # ne fonctionne pas
        links6 = driver.find_elements(by = By.XPATH, value = '/html/body/div[3]/table/tbody/tr/td[1]/a' and '/html/body/div[3]/table/tbody/tr/td[2]/a')
        res6 = links.append(links6)
        len_links.append(len(links6))
        sleep(1)

links7 = driver.find_elements(by = By.XPATH, value = '/html/body/div[1]/table/tr[1]/td') # ne fonctionne pas
res7 = links.append(links7)
len_links.append(len(links7))
sleep(1)

print(links, len_links)
        
# Il y a 7 pages mais on se concentre seulement sur les 3 premières et les 2 dernières qui sont les plus intéressantes
# Dans la page 1 'Tutoriel' il y a des selecteurs de mais c'est toujours la meme page donc on ne les comptera pas
# Dans la page 2 'Démo' les selecteurs de pages sont en liste alors que dans la page 3 'Documentation' les selecteurs de pages sont en tableau (possible correction à apporter)
# La page 7 'Ressources' n'est pas une page à part entière, on ne peut donc pas l'inclure dans la boucle
 

 # Test

links_pages = {
    "Tutoriel": "banner_row > a:nth-child(2)", 
    "Demo": "banner_row > a:nth-child(3)", 
    "Documentation": "banner_row > a:nth-child(4)", 
    "Console": "banner_row > a:nth-child(5)",
    "Editeur": "banner_row > a:nth-child(6)",
    "Galerie": "banner_row > a:nth-child(7)"}

for i in links_pages:
    page = driver.find_element(By.CSS_SELECTOR, links_pages[i]).click()
    sleep(3)

    
sleep(10)