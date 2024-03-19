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

driver.get('https://brython.info/index.html')

pages_principales = {
    "Accueil": "",
    "Tutoriel": "#banner_row > a:nth-child(2)",
    "Demo": "#banner_row > a:nth-child(3)", 
    "Documentation": "#banner_row > a:nth-child(4)", 
    "Console": "#banner_row > a:nth-child(5)",
    "Editeur": "#banner_row > a:nth-child(6)",
    "Galerie": "#banner_row > a:nth-child(7)"
}

# Format des liens :
# [src, dest, lang]

liens = {}

for i in pages_principales.items():
    driver.find_element(By.CSS_SELECTOR, i).click
    sleep(2)
    
    for j in 
    src = driver.current_url
    dest = driver.find_element(By.CSS_SELECTOR, i)
    # lang = ??
    liens.add([src, dest])
    
print(liens)