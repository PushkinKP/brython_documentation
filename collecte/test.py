from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd 
from langdetect import detect
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

# Format des liens :
# {(src, dest, lang)}

liens = set()

for nom, selecteur in pages_principales.items():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selecteur))
    )
    driver.find_element(By.CSS_SELECTOR, selecteur).click()
    sleep(2)

    src = driver.current_url
    lang = detect(driver.page_source)

    hrefs = {element.get_attribute('href') for element in driver.find_elements(By.TAG_NAME, "a")} # set() de tous les liens du site
    print(f"\n\nLiens de la page {src} :\n", hrefs)
    
    for href in hrefs:
        liens.add((src, href, lang))
    
print(liens)

driver.quit()


# Page cachée = page qui n'as plus de lien vers une autre page brython (https://brython...)