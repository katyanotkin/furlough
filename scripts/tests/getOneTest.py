import sys
import requests

inputData={'_id':sys.argv[2]}
Url = "/quiz/collection=" + sys.argv[1]  
localUrl="http://127.0.0.1:5000" + Url
resp = requests.get(localUrl,params=inputData)
if resp.status_code != 200:
    	# This means something went wrong.
    	print ('GET ' + Url + ' {}'.format(resp.status_code))
else:
	print (resp.json())
	
