import sys
import requests
import argparse


print ("Example\n", "~/furlough/envv/bin/python getOneTest.py -c questions -i \"_id=5994ad15029f303a6f031e74\"") 

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

	

Url = "/quiz/collection=" + optargs.collection

myUrl = host + Url

resp = requests.get(myUrl,params=optargs.inputData)
print (myUrl,optargs.inputData)
if resp.status_code != 200:
    	# This means something went wrong.
    	print ('GET ' + Url + ' {}'.format(resp.status_code))
else:
	print (resp.json())
	print ('status code:', resp.status_code)
	
