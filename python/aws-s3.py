import requests
import json
import boto3
from botocore.client import ClientError

s3 = boto3.resource('s3')
ec2 = boto3.client('ec2')

url = 'https://jsonplaceholder.typicode.com/todos/1'
data = '''{
}'''
#response = requests.post(url, data=data)
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

print ("Your buckets are: ")
for bucket in s3.buckets.all():
    print ("Bucket : ", bucket.name)

myBucket = 'my-bucket-marco-2313'
s3.create_bucket(Bucket=myBucket)

data = open ("instance-skeleton.json", "rb")

s3.Bucket(myBucket).put_object(Key="instance-skeleton.json", Body=data)

response = ec2.describe_instances()
print ("Instances are: " , response)
