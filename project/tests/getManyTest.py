import sys
import requests

Url = "/quizZy/collection=" + sys.argv[1]
localUrl="http://127.0.0.1:5000" + Url
resp = requests.get(localUrl)
if resp.status_code != 200:
    	# This means something went wrong.
    	raise ApiError('GET ' + Url + ' {}'.format(resp.status_code))
else:
	print (resp.json())
	
