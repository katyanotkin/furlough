import sys
import argparse
import validators 
import requests
import requests.exceptions
from bs4 import BeautifulSoup 		# wow, not working with Python3.6, using Python3.5 
import re


def collectUrls(url):
	#print("\n{}\n=======".format(sys._getframe().f_code.co_name))
	urlSet=set()
	try:
		response=requests.get(url)
	except:
		print("Failed to open {}".format(url))
		return {'success':False}
	if False:	
		page=BeautifulSoup(response.text, 'html.parser')
		for u in page.find_all("<a"):
			if "href" in u.attr:
				link=u.attr["href"]
				setUrls.append(link)
		return {'success':True , 'result':urlSet}
	else:
		return {'success':True, 'result':([url])}

def collectEmails(url):
	#print("\n{}\n=======".format(sys._getframe().f_code.co_name))
	print("Collecting emails from {}".format(url))
	try:
		response=requests.get(url)
	except:
		print("Failed to open {}".format(url))
		return {'success':False}
	page=str(BeautifulSoup(response.text, 'html.parser'))
	#print(page)
	emailSet=set(re.findall(r'[\w\.-]+@[\w\.-]+', page))
	return {'success':True , 'result':emailSet}
	

if __name__ == '__main__':
	prsr = argparse.ArgumentParser()
	prsr.add_argument("rootDomain")
	args = prsr.parse_args()
	if args.rootDomain:
		# validate url
		rootUrl=args.rootDomain
		""" http / https / ... protocol specification may require more work, taking simplistic approach for the sake of time """ 
		if rootUrl[:4] != "http":
			rootUrl = "http://"+rootUrl
		if not validators.url(rootUrl):
			print("Invalid input domain {}, exiting...".format(args.rootDomain))
			exit(1)
		else:
			print("Looking for email addresses in {} and beyond".format(rootUrl))
			# obtain urls beyond root 
			resp=collectUrls(rootUrl)	# not ready and better have one run throgh page for urls and emails
			if resp['success']:
				urls=resp['result']
			processed_urls=set()
			emails=set()
			for u in urls:
				if not u in processed_urls:
					processed_urls.add(u)
					r=collectEmails(u)
					#print("{}: {}".format(u,r['result']))
					if r['success']:
						emails=emails.union(r['result'])
			if len(emails)>0:
				print("Found emails:")
				{ print (em) for em in emails if validators.email(em)}
			else:
				print("Disappointment: somehow no emails were collected")



