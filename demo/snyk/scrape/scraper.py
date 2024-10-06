from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
import requests
import os

# Let's get my client_secrets.json file

CLIENT_SECRET_FILE = "/home/marco/Downloads/client-secret.json"
SCOPES = ['https://www.googleapis.com/auth/userinfo.profile','https://www.googleapis.com/auth/userinfo.email','openid']

# Run the OAuth flow to get my credentials
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_local_server(port=0)

# Given my credentials, let me get my access token

session = requests.Session()
session.headers.update({'Authorization': f'Bearer {credentials.token}'})

SNYK_ORG_ID = os.environ.get("SNYK_ORG_ID")
# SNYK_URL = f'https://app.snyk.io/org/{SNYK_ORG_ID}/projects"'
SNYK_URL = f'https://app.snyk.io/org/mr.marco.a.morales/projects'


response = session.get(SNYK_URL)
print(response.text)
if response.ok:
    print('Yay!')
    print(response.text)
else:
    print("Failed to retrieve page")
    print(response.status_code)
    print(response.headers)
    print(response.cookies)
    print(response.url)
