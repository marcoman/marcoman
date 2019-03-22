import requests
import urllib
import xml.etree.ElementTree as ET

XLDHeaders = {'Content-type': 'application/xml'}
XLDUsername = 'admin'
XLDPassword = 'admin00'
XLDServer = 'desktop-5m38rp9'
XLDPort = 14516


# Get the users from XLD
def getUsers(server, port):
    print ("****************")
    getUrl = urllib.parse.urljoin('http://{}:{}'.format(server, port), 'deployit/security/user')
    print("url is: {}".format(getUrl))
    request = requests.get(getUrl, auth=(XLDUsername, XLDPassword))
    # Check status code for errors
    if (request.status_code > 200):
        print("ERROR: Status code {} error".format(request.status_code))
        print("RESPONSE:{}".format(request.text))
    else:
        print("XLD Response is {}".format(request.text))
        parseXML(request.text)

# Get the named user from XLD
def getUser(server, port, username):
    getUrl = urllib.parse.urljoin('http://{}:{}'.format(server, port), 'deployit/security/user/{}'.format(username))

    request = requests.get(getUrl, auth=(XLDUsername, XLDPassword))
    if (request.status_code > 200):
        print("ERROR: status_code is {}".format(request.status_code))
        print("RESPONSE:{}".format(request.text))
    else:
        print("text is {}".format(request.text))


# Create a new user
def postUser(server, port, username, password):
    postUrl = urllib.parse.urljoin('http://{}:{}'.format(server, port), "deployit/security/user/{}".format(username))

    userxml = '''<user admin="false">
    <username>{}</username>
    <password>{}</password>
</user>'''.format(username, password)

    print("User data is:{}".format(userxml))
    print("post URL is:{}".format(postUrl))
    response = requests.post(postUrl, auth=(XLDUsername, XLDPassword), data=userxml, headers=XLDHeaders)
    if (response.status_code > 200):
        print("ERROR: status_code is {}".format(response.status_code))
        print("RESPONSE:{}".format(response.text))
    else:
        print("text is {}".format(response.text))


def parseXML (xmldata) :
    root = ET.fromstring(xmldata)
    users = {}
    index = 0
    for child in root:
        print("user #{} is {} ".format(index, child.text))
        users[index] = child.text
        index += 1
    print("You have {} users".format(index))

getUsers(XLDServer, XLDPort)
getUser(XLDServer, XLDPort, "tom2")
getUser(XLDServer, XLDPort, "tom3")

# for x in range(1, 100):
#     postUser(XLDServer, XLDPort, "tom" + str(x), "tom123")
#     postUser(XLDServer, XLDPort, "dick" + str(x), "tom123")
#     postUser(XLDServer, XLDPort, "harry" + str(x), "tom123")

getUsers(XLDServer, XLDPort)