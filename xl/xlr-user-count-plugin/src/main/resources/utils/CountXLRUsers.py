import json
import requests
import urllib

XLRHeaders = {'Content-type': 'application/json'}
XLRUsername = 'admin'
XLRPassword = 'admin00'
XLRServer = 'desktop-5m38rp9'
XLRPort = 15516


# Get the users from XLR
def getusers(server, port):
    print("****************")
    totalcount = 0;
    morepages=True
    pagenum = 0
    while morepages:

        geturl = urllib.parse.urljoin('http://{}:{}'.format(server, port), 'api/v1/users?resultsPerPage=10&page={}'.format(pagenum))

        request = requests.get(geturl, auth=(XLRUsername, XLRPassword))
        # Check status code for errors
        if (request.status_code == 200):
            if (int (request.headers['content-length']) < 5):
                print("{} END OF LIST".format(request.status_code, request.text))
                morepages =False
            else:
                print("{} {} :: ".format(request.status_code, geturl))
                # Count the users in the response
                json_object = json.loads(request.text)
                users = []
                for user in json_object:
                    totalcount += 1
                    print("{} - {}".format (totalcount, user['username']))
                pagenum += 1
        else:
            print("ERROR: status_code is {}".format(request.status_code))
            print("RESPONSE:{}".format(request.text))

    print("Total number of users: {}".format(totalcount))
    return


# Get the named user from XLR
def getuser(server, port, username):
    geturl = urllib.parse.urljoin('http://{}:{}'.format(server, port), 'api/v1/users/{}'.format(username))

    request = requests.get(geturl, auth=(XLRUsername, XLRPassword))
    if request.status_code > 200:
        print("ERROR: status_code is {}".format(request.status_code))
        print("RESPONSE:{}".format(request.text))
    else:
        print("text is {}".format(request.text))
    return


# Create a new user
def postuser(server, port, username, password):
    posturl = urllib.parse.urljoin('http://{}:{}'.format(server, port), "api/v1/users/{}".format(username))

    userjson = {'fullName': username,
                'loginAllowed': 'true',
                'password': password}

    print("User data is:{}".format(userjson))
    print("post URL is:{}".format(posturl))
    response = requests.post(posturl, auth=(XLRUsername, XLRPassword), json=userjson, headers=XLRHeaders)
    if response.status_code > 200:
        print("ERROR: status_code is {}".format(response.status_code))
        print("RESPONSE:{}".format(response.text))
    else:
        print("text is {}".format(response.text))


def prettyprint(text):
    print(json.dumps(json.loads(text), indent=4, separators=(',', ":")))
    return


getusers(XLRServer, XLRPort)
getuser(XLRServer, XLRPort, "tom1")
getuser(XLRServer, XLRPort, "admin")

# for x in range(1, 100):
#     postuser(XLRServer, XLRPort, "tom" + str(x), "tom123")
#     postuser(XLRServer, XLRPort, "dick" + str(x), "tom123")
#     postuser(XLRServer, XLRPort, "harry" + str(x), "tom123")
#

getusers(XLRServer, XLRPort)
