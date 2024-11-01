import os
import requests

from bs4 import BeautifulSoup
from lxml import etree

from selenium import webdriver
driver = webdriver.Chrome()


SNYK_ORG_ID = os.environ.get("SNYK_ORG_ID")
SNYK_AUTH_TOKEN = os.environ.get("SNYK_AUTH_TOKEN")
SNYK_URL = 'file:///snyk-projects.html'

driver.get(SNYK_URL)
page_source = driver.page_source
driver.quit()
print(f'Page source is {page_source}')

# # The file loads just fine, but it is not workable because 
# # Read in a file into the variable page_source
# with open('/home/marco/Downloads/snyk-projects.html', 'r') as file:
#     page_source = file.read()

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

targets = soup.select('''html body div:first-child div div main div:nth-of-type(2) div div div:nth-of-type(2)''')

print (f"targets contains\n {targets}")

for target in targets:
    target_text = target.getText()
    print(target_text)
    
