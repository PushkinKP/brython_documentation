from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from langdetect import detect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Fonction récursive pour collecter tous les liens à partir d'une page principale
def collect_links(driver, page_url, lang, visited_pages, all_links):
    # Ajouter la page actuelle aux pages visitées
    visited_pages.add(page_url)
    
    # Récupérer tous les liens de la page actuelle
    hrefs = {element.get_attribute('href') for element in driver.find_elements(By.TAG_NAME, "a")}
    
    for dest in hrefs:
        if dest is not None and dest not in visited_pages:
            all_links.add((page_url, dest, lang))
            driver.get(dest)  # Aller à la page de destination
            collect_links(driver, driver.current_url, lang, visited_pages, all_links)  # Appel récursif pour collecter les liens à partir de la page de destination

# Initialiser le navigateur
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://brython.info/index.html')

pages_principales = {
    "Accueil": "#banner_row > span.logo > a",
    "Tutoriel": "#banner_row > a:nth-child(2)",
    "Demo": "#banner_row > a:nth-child(3)", 
    "Documentation": "#banner_row > a:nth-child(4)", 
    "Console": "#banner_row > a:nth-child(5)",
    "Editeur": "#banner_row > a:nth-child(6)",
    "Galerie": "#banner_row > a:nth-child(7)"
}

# Ensemble pour stocker tous les liens
liens = set()

for nom, selecteur in pages_principales.items():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selecteur))
    )
    driver.find_element(By.CSS_SELECTOR, selecteur).click()
    sleep(2)

    src = driver.current_url
    lang = detect(driver.page_source)
    
    # Ensemble pour stocker les pages visitées
    visited_pages = set()
    # Appeler la fonction récursive pour collecter tous les liens à partir de la page principale actuelle
    collect_links(driver, src, lang, visited_pages, liens)

# Afficher tous les liens collectés
print(liens)
print("\nNombre total de liens:", len(liens))

# Fermer le navigateur
driver.quit()
