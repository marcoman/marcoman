import os
import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from bs4 import BeautifulSoup
#from selenium import webdriver
from seleniumwire import webdriver

driver = webdriver.Chrome()
global header_token

# Define the scopes
CLIENT_SECRETS_FILE='/home/marco/Downloads/client-secret.json'
TOKEN_FILE='/home/marco/Downloads/token.json'
# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
SCOPES = ['https://www.googleapis.com/auth/userinfo.email']

SNYK_ORG_ID = os.environ.get("SNYK_ORG_ID")
SNYK_URL = f'https://app.snyk.io/org/mr.marco.a.morales/projects'
# SNYK_URL = f'https://app.snyk.io/org/{SNYK_ORG_ID}/projects"'

headers = {}

def authenticate():
    # Run the OAuth 2.0 flow to get credentials
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    # Now, save the credentials files
    with open('/home/marco/Downloads/token.json', 'w') as token:
        token.write(creds.to_json())
    return creds

def get_snyk_projects(creds):
    driver.request_interceptor = interceptor
    print(f'Getting {SNYK_URL}')
    driver.get(SNYK_URL)
    page_source = driver.page_source
    driver.quit()
    
    print(f'Page source is {page_source}')

    soup = BeautifulSoup(page_source, 'html.parser')
    print (f'Title is {soup.title}')


def interceptor(request):
    del request.headers['Authorization']
    request.headers['Authorization'] = f'Bearer {header_token}'

if __name__ == '__main__':
    if os.path.exists(TOKEN_FILE):
        print('Authenticated by file.')
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, scopes=SCOPES)
    else:
        print('Authenticated by Google.')
        creds = authenticate()
    print(f'Creds are \n {creds}')
    header_token = creds.token
    print(f'Header token is {header_token}')
    
    get_snyk_projects(creds)
