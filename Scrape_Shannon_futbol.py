#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 16:14:56 2025

@author: sergi
"""

import time
import io
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=r'/home/sergi/Downloads/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("--disable-search-engine-choice-screen")
options.add_argument("--disable-notifications")
options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})
driver = webdriver.Chrome(service=service, options=options)

historic = pd.DataFrame()
t1 = 1928
t2 = 29

while t1 != 2024:

    url = 'https://www.bdfutbol.com/t/t'+'%s'%(t1)+'-'+'%02d'%(t2)+'.html'
    
    driver.get(str(url))
    time.sleep(3)
    if t1 == 1928:
        webelement = driver.find_element(By.CLASS_NAME, 'fc-button-label')
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(webelement)).click()
    if t1 not in [1936, 1937, 1938]:   
        #Prendre dades classificacio i guardar en un dataframe
        titlepage = driver.find_element(By.CLASS_NAME, 'heroh1')
        textpage = str(titlepage.text)
        season = pd.read_html(io.StringIO(driver.page_source))[-1]
        season['Temp'] = textpage[-7:]
        historic = pd.concat([historic, season], ignore_index = True)
            
        #Actualitzar variable bucle
            
    t1 = t1 + 1
    t2 = (t2 + 1)%100
    
driver.quit()

historic.to_pickle('historic.pkl')