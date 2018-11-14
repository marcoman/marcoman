# I use this script with the code from https://github.com/khoubyari/spring-boot-rest-example.git .
# The aforementioned project lets me run a spring-boot application with a REST interface visible via swagger pages at:
#
# http://localhost:8090/swagger-ui.html
#
# As my initial python-for-REST test and experimentation script, I worked through the different REST operations of GET, POST, DELETE, GET, PUT.
# I worked through straight invocations to function calls.  I next added parameterization.

# TODO and wish list
# Let's run this from a command-line, with parameters fed into it. Something like this:
# hotels.py --delete _json.file_
# hotels.py --put --id 1 --city Nameofcity --description "my favorite description" --name "name of hotel" --rating newrating
# hotels.py --getall
# hotels.py 


import requests
import json
from botocore.client import ClientError

myUrl     = "http://localhost:8090/example/v1/hotels"
myHeaders = {'Content-type': 'application/json'}
myJson = {
    "city": "Chicago",
    "description": "My Kind of Town",
    "name": "Marco Hotel",
    "rating": 5
    }


def getcount (url) :
    print ("---getcount")
    r = requests.get(url + "?page=0&size=100")
    if (r.ok):
        jdata = json.loads(r.content)
        return (jdata['numberOfElements'])
    else :
        return 0
    

def getall (url) :
    print ("---getall")
    r = requests.get(url + "?page=0&size=100")
    if r.status_code != 200:
        #Something went wrong - notify the user
        raise ApiError ('GET /tasks/ {}'.format(r.status_code))
    if (r.ok):
        jdata = json.loads(r.content)
    return r.json()

def get (url, index) :
    print ("---get")
    r = requests.get(url + "/" + str(index))
    print ("Response is ", r.ok)
    print (r.json())
    if (r.ok):
        jdata = json.loads(r.content)
        print ("id is " , jdata['id'])
    return r.json()

def post (url, json, data) :
    print ("---put")
    r = requests.post(url, json=json, headers=myHeaders)
    return r.text

def delete (url, id) :
    print ("---delete")
    r = requests.delete(url + "/" + str(id))
    return

def prettyprint (text) :
    print (json.dumps(text, sort_keys=True, indent=4, separators=(',', ':')))
    return

def reportall (url) :
    print ("---reportall")
    r = requests.get(url + "?page=0&size=100")
    if (r.ok):
        jdata = json.loads(r.content)
        for key in jdata :
            print (key, ":" , jdata[key])
        content = jdata['content']
        for i in content:
            print ("Hotel id" , str(i['id']), "is named" , i['name'])
    return

def put (url, id) :
    myjson = { "description" : "Awesome hotel"  + str(id),
               "id" : id,
               "city" : "Chicago",
               "name" : "Marco Hotel",
               "rating" : "1"
               }
    r = requests.put(url + "/" + str (id), data=json.dumps(myjson), headers=myHeaders)
    if (r.ok) :
        print ("it worked!")
    else :
        print ("Failed!")
    
    return
    
print ("total count is: " + str(getcount(myUrl)))
prettyprint (post (myUrl, myJson, myHeaders))
prettyprint (getall (myUrl))
prettyprint (get (myUrl, 1))
put (myUrl, 1)
reportall(myUrl)

#prettyprint (getall (myUrl))

#prettyprint (delete (myUrl, 1))

#prettyprint (getall (myUrl))
