import sys
import requests
import argparse

parser = argparse.ArgumentParser(
    description='host selection',
)

parser.add_argument('-c', action="store", dest="collection")
parser.add_argument('-i', action="store", dest="inputData")
parser.add_argument('--remotehost', '-r', action="store", dest="host")

optargs=parser.parse_args()
print(parser.parse_args())
print (optargs.collection)
if not optargs.host:
	host="http://127.0.0.1:5000"

	

Url = "/quiz/collection=" + optargs.collection

myUrl = host + Url


resp = requests.get(myUrl,params=optargs.inputData)
#print (myUrl,optargs.inputData)
if resp.status_code != 200:
    	# This means something went wrong.
    	print ('GET ' + Url + ' {}'.format(resp.status_code))
else:
	print (resp.json())
	print ('status code:', resp.status_code)
	
