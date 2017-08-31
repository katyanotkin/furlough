import sys
import requests
import argparse
import json

#curl -i -X POST -H "Content-Type:application/json" http://127.0.0.1:5000/Users -d '{"email":"kno@kn.com", "phone":"1234567890", "name":"kno"}'

#print ("Example\n", "~/furlough/envv/bin/python postOneTest.py -c appUsers -i '{\"\"}') 

parser = argparse.ArgumentParser(
    description='host selection',
)

parser.add_argument('-c', action="store", dest="collection")
parser.add_argument('-i', action="store", dest="inputData")
parser.add_argument('--remotehost', '-r', action="store", dest="host")

optargs=parser.parse_args()
print(parser.parse_args())
print ('#'+str(optargs.host)+'#', (str(optargs.host)=='None'))
if (str(optargs.host)=='None'):
	host="http://127.0.0.1:5000"

print("host", host)
	

Url = "/post/collection=" + optargs.collection

myUrl = host + Url
headers = {'Content-type': 'application/json'}

data_json = json.dumps(optargs.inputData)
print("test:", data_json)
print("test1:", optargs.inputData)
resp = requests.post(myUrl,json=optargs.inputData, headers=headers)
print ('status code:', resp.status_code, 'reason:', resp.reason)
print (resp.text)
print (myUrl + ' {}'.format(resp.status_code))
#print (resp.json())
