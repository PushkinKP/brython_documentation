# Collecte de données sur Brython - Détection des pages cachées

# Jules Cnockaert

# Packages

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import bs4
from time import sleep
import pandas as pd 

# Scrapping

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://brython.info/index.html")

sleep(2)

links_pages = {
    "Tutoriel": "#banner_row > a:nth-child(2)",
    "Demo": "#banner_row > a:nth-child(3)", 
    "Documentation": "#banner_row > a:nth-child(4)", 
    "Console": "#banner_row > a:nth-child(5)",
    "Editeur": "#banner_row > a:nth-child(6)",
    "Galerie": "#banner_row > a:nth-child(7)"
}

hidden_links_all_pages = {}
count_all = 0
count_real_hidden = 0

for page_name, css_selector in links_pages.items():
    driver.find_element(By.CSS_SELECTOR, css_selector).click()
    sleep(2)
    url_page = driver.current_url
    
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')

    all_links = soup.find_all('a')

    hidden_links = []
    real_hidden_links = []
    for link in all_links:
        href = link.get('href')
        if href:
            is_hidden = all(css_selector not in href for css_selector in links_pages.values())
            if is_hidden:
                hidden_links.append(href)
                count_all += 1
                if not href.startswith("https") and href not in ('/index.html', '/static_tutorial/fr/index.html', '/demo.html?lang=fr', '/static_doc/3.12/fr/intro.html', '/tests/console.html?lang=fr', '/tests/editor.html?lang=fr', '/gallery/gallery_fr.html'):
                    real_hidden_links.append(href)
                    count_real_hidden += 1

    hidden_links_all_pages[page_name] = hidden_links

print("Liens cachés pour toutes les pages :")
for page_name, hidden_links in hidden_links_all_pages.items():
    print("\n---------------------\n")
    print("Page :", page_name, "\nUrl : ", url_page, "\n")
    if hidden_links:
        for hidden_link in hidden_links:
            if hidden_link in real_hidden_links:
                print("Page cachée :", hidden_link)
            else:
                print("Page externe :", hidden_link)
    else:
        print("Aucun lien caché trouvé sur cette page.")

print("\n\nCompte total de pages cachées : ", count_all, "\nCompte de vrai pages cachées : ", count_real_hidden)
print("\n\nVrais liens cachées : \n", real_hidden_links)

driver.quit()

# On se concentre uniquement sur les pages du sites cachées, les pages externe type GitHub ne seront pas comptabilisé, les vraies pages cachées sont les pages de Brython qui ne sont pas référencer directement (c'est-à-dire par des liens).
# On ne comptabilise pas non plus ('/index.html', '/static_tutorial/fr/index.html', '/demo.html?lang=fr', '/static_doc/3.12/fr/intro.html', '/tests/console.html?lang=fr', '/tests/editor.html?lang=fr', '/gallery/gallery_fr.html') qui sont les pages principales du sites et donc par définition pas cachées