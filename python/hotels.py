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
import sys
import getopt

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
    r = requests.get(url + "?page=0&size=100")
    if (r.ok):
        jdata = json.loads(r.content)
        return (jdata['numberOfElements'])
    else :
        return 0
    

def getall (url) :
    r = requests.get(url + "?page=0&size=100")
    if r.status_code != 200:
        #Something went wrong - notify the user
        raise ApiError ('GET /tasks/ {}'.format(r.status_code))
    if (r.ok):
        jdata = json.loads(r.content)
    return r.json()

def get (url, index) :
    r = requests.get(url + "/" + str(index))
    print ("RESPONSE:", r.ok)
    if (r.ok):
        jdata = json.loads(r.content)
        print ("ID is " , jdata['id'])
    else :
        print ("ID", str(id), "not present")
    return r.json()

def post (url, json, data) :
    r = requests.post(url, json=json, headers=myHeaders)
    if (r.ok) :
        print ("POSTED okay")
    else :
        print ("POST failed")
    return r.text

def post (url, city="Chicago", description="No description provided", name="simplename", rating="3") :
    print ("POST WITH ARGUMENTS")
    myj = {
        "city": city,
        "description": description,
        "name": name,
        "rating": rating
        }
    r = requests.post(url, json=myj, headers=myHeaders)
    if (r.ok) :
        print ("POST okay")
    else :
        print ("POST failed")
    return r.text

def delete (url, id) :
    r = requests.delete(url + "/" + str(id))
    if (r.ok) :
        print ("RESPONSE:", r.ok)
    else :
        print ("ID ", str(id), "does not exist")
    return

def prettyprint (text) :
    print (json.dumps(text, sort_keys=True, indent=4, separators=(',', ':')))
    return

def reportall (url) :
    r = requests.get(url + "?page=0&size=100")
    if (r.ok):
        jdata = json.loads(r.content)
        for key in jdata :
            print (key, ":" , jdata[key])
        content = jdata['content']
        for i in content:
            print ("Hotel id" , str(i['id']), "is named" , i['name'])
    return

def put (url, id, city, description, name, rating) :
    myjson = { "description" : description,
               "id" : id,
               "city" : city,
               "name" : name,
               "rating" : rating
               }
    r = requests.put(url + "/" + str (id), data=json.dumps(myjson), headers=myHeaders)
    if (r.ok) :
        print ("it worked!")
    else :
        print ("Failed!")
    
    return

def printhelp () :
    print (sys.argv[0], '''<options>:
    -h help
    -c total count
    --get <ID> get the named ID 
    --post create a new hotel with --city --description --name --rating data
    --delete <ID> delete the hotel per named ID
    --put <ID> update the hotel per named ID with --city --description --name --rating values
    --getall get the entire list of hotels
''')


def main(argv):
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hc",["get=","post","delete=","put=","getall",
                                                      "report","city=","description=","name=","rating="])
    except getopt.GetoptError:
        printhelp()
        sys.exit()
    for opt,arg in opts:
        if opt in ('-h'):
            printhelp()
            sys.exit()
        elif opt in ('-c'):
            print ("total count is: " + str(getcount(myUrl)))
            sys.exit()
        elif opt in ("--city") :
            print ("Assigning ", str(arg))
            city = arg
        elif opt in ("--description") :
            description = arg
        elif opt in ("--name") :
            name = arg
        elif opt in ("--rating") :
            rating = arg
        elif opt in ("--get"):
            print ("GET ID", str(arg))
            prettyprint (get (myUrl, arg))
        elif opt in ("--post") :
            post (myUrl, city, description, name, rating)
        elif opt in ("--delete") :
            print ("DELETE ID", str(arg))
            delete (myUrl, arg)
        elif opt in ("--put") :
            put (myUrl, arg, city, description, name, rating)
        elif opt in ("--getall"):
            prettyprint (getall (myUrl))
        elif opt in ("--report"):
            reportall(myUrl)
        else:
            sys.exit()

    #prettyprint (getall (myUrl))
    #prettyprint (delete (myUrl, 1))
    #prettyprint (getall (myUrl))


if __name__ == "__main__":
    main(sys.argv)
