import requests
import json
from requests.auth import HTTPBasicAuth

username = "admin"
password = "admin"
sampleTemplateName = "Sample Release Template"
url = "http://e25db37a.ngrok.io"
myHeaders = {'Content-type': 'application/json', 'Accept' : 'application/json'}
myReleasename = "MM Test 123"

def prettyPrint (text) :
    print (json.dumps(text, sort_keys=True, indent=4, separators=(',', ':')))
    return


def listTemplates() :
    print ("list")
    response = requests.get(url + "/api/v1/templates", auth=HTTPBasicAuth(username, password), timeout=60)
    print ("RESPONSE:", response.ok)
    if (response.ok) :
        jdata = json.loads(response.content)
        return (jdata)
    
def listTemplateNames() :
    print ("LIST TEMPLATE NAMES")
    response = requests.get(url + "/api/v1/templates", auth=HTTPBasicAuth(username, password), timeout=60)
    print ("RESPONSE:", response.ok)
    if (response.ok) :
        data = response.json()
        for template in data:
            print ("Template title/name is: ", template['title'])
            print ("\tID is: ", template['id'])
            #print ("id is: ", template['id'])

def locateSampleTemplate (templateName):
    print ("LOCATE SAMPLE TEMPLATE")
    response = requests.get(url + "/api/v1/templates?title=" +templateName, auth=HTTPBasicAuth(username, password), timeout=60)
    if (response.ok) :
        # Get the JSON
        data = response.json()
#        print (data)
    else:
        print ("It did not work")
    return data
    
def createReleaseFromTemplate(myjson) :
    print ("CREATE RELEASE FROM TEMPLATE")
    # Given json for a template, create a release.
    # We have the json, find the value of "id"
    for template in myjson:
        if template['title'] == sampleTemplateName :
            print ("name is:" , template['title'])
            print ("id is" , template['id'])
#            createRelease (template['id'])
            startRelease (template['id'])


def createRelease(id) :
    print ("CREATE RELEASE " + id)
    myjson = {
      "releaseTitle" : myReleasename,
      "folderId" : "null",
      "variables" : { },
      "releaseVariables" : { "ACC environment" : "1" , "QA environment" : "QA", "package" : "mypackage" },
      "releasePasswordVariables" : { },
      "scheduledStartDate" : "null",
      "autoStart" : "false"
    }

    myUrl = url + "/api/v1/templates/" + str(id) + "/create"
    print ("URL is: ", myUrl)

    
    response = requests.post(url + "/api/v1/templates/" + str(id) + "/create",
                             json = myjson,
                             auth = HTTPBasicAuth(username, password),
                             headers=myHeaders, timeout=60)
    if (response.ok) :
        print ("create release POST worked")
    else:
        print ("create release POST did not", response.status_code)
        

def startRelease (id):
    print ("START RELEASE")
    response = requests.post(url + "/api/v1/templates" + str(id) + "/start",
                             auth=HTTPBasicAuth(username, password),
                             headers=myHeaders, timeout=60)
    print ("RESPONSE:", response.ok)
    

    
def findReleaseId (myName):
    print ("FIND RELEASE ", myName)
    response = requests.get(url + "/api/v1/releases/byTitle?releaseTitle=" + myName, auth=HTTPBasicAuth(username, password), timeout=60)
    if (response.ok) :
        print ("find release worked")
        data = response.json()
        for release in data:
            print ("id is" , data['id'])
    else:
        print ("find release did not work")
        
    

def listReleaseNames() :
    print ("LIST RELEASE NAMES")
    response = requests.get(url + "/api/v1/templates", auth=HTTPBasicAuth(username, password), timeout=60)
    print ("RESPONSE:", response.ok)
    if (response.ok) :
        data = response.json()
        for template in data:
            print ("Release title/name is: ", template['title'])
            print ("\tID is: ", template['id'])



def completeRelease ():
    print ("list")


listTemplateNames()
templateData = locateSampleTemplate(sampleTemplateName)
myreleaseId = findReleaseId(myReleasename)
#createReleaseFromTemplate(templateData)

#listReleaseNames()

