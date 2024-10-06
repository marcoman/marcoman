import os
import requests
#from selenium import webdriver
from seleniumwire import webdriver

driver = webdriver.Chrome()
driver.request_interceptor = interceptor

from bs4 import BeautifulSoup
from lxml import etree

SNYK_ORG_ID = os.environ.get("SNYK_ORG_ID")
SNYK_AUTH_TOKEN = os.environ.get("SNYK_AUTH_TOKEN")
SNYK_URL = f'https://app.snyk.io/org/mr.marco.a.morales/projects"'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {SNYK_AUTH_TOKEN}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'

}

driver.get(SNYK_URL)
page_source = driver.page_source
driver.quit()

# now let's parse with beautiful soup
soup = BeautifulSoup(page_source, 'html.parser')
print (f'Title is {soup.title.text}')

# The full XPath to the targets are at this location:
# /html/body/div[1]/div/div/main/div[2]/div/div/div[2]

# This means we should iterate through the different elements to get our list in this order:
# Targets,
# Projects
# Project details such as the name, imported, tested, and Issues

# Let's get some basic information with beautiful soup

# targets = soup.select('''html body div:first-child div div main div:nth-of-type(2) div div div:nth-of-type(2)''')

# print (f"targets contains\n {targets}")

# for target in targets:
#     target_text = target.getText()
#     print(target_text)
    