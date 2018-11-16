import requests
import json

url = 'https://jsonplaceholder.typicode.com/todos/1'
data = '''{
}'''
myHeaders = {'Content-type': 'application/json'}

def prettyprint (text) :
    print (json.dumps(text, sort_keys=True, indent=4, separators=(',', ':')))
    return

r = requests.get(url)
print ("Response is " , r.ok)
print (r.json())
if (r.ok):
    jData = json.loads(r.content)
    print ("The Response contains (0) properties".format(len(jData)))
    print ("\n")
    print ("title is ", jData['title'])
    for key in jData:
        print (key , " : " , jData[key])

myj = {
  "userId": 2,
  "id": 3,
  "title": "SAMPLE TITLE",
  "completed": "false"
}
r = requests.post(url, json=myj, headers=myHeaders)
if (r.ok) :
    jdata = json.loads(r.content)
    print (jdata)
else:
    print ("didn't work")
