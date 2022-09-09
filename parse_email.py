from cgitb import html
from http.server import executable
from bs4 import BeautifulSoup
#import requests
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

with open('saved/10_annonces_de_vente_de_maisons/index.html', 'r') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    for link in soup.find_all(_label="Voir l'annonce", href=True):
        print(link['href'])

        # instance of Options class allows
        # us to configure Headless Chrome
        options = Options()
        
        # this parameter tells Chrome that
        # it should be run without UI (Headless)
        #options.headless = True
        
        # initializing webdriver for Chrome with our options
        driver = webdriver.Chrome(options=options)
        
        # getting GeekForGeeks webpage
        driver.get(link['href'])
        time.sleep(30)
        
        # We can also get some information
        print(">> " + driver.title)
        
        # close browser after our manipulations
        driver.close()



