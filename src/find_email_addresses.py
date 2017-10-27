import sys
import argparse
import validators 
import requests
import requests.exceptions
from bs4 import BeautifulSoup 		# wow, not working with Python3.6, using Python3.5 
import re
from collections import deque
email_pattern = re.compile("[\w\.-]+@[\w\.-]+")


def findObjects(rootUrl):
		processed_urls=set()	# unique items
		emails=set()		# unique items
		urls=deque([rootUrl])	# good FIFO
		# obtain urls beyond root 
		while len(urls):
			urlnext=urls.popleft()
			if not urlnext in processed_urls:
				processed_urls.add(str(urlnext))
				try:
					response=requests.get(urlnext)
					page=BeautifulSoup(response.text, 'html.parser')
					
					#print("Collecting emails from {}".format(urlnext))
					emailSet=set(re.findall(email_pattern, str(page)))
					emails=emails.union(emailSet)
					# collect href references
					for atag in page.find_all("a"):
						if "href" in atag.attrs: 
							if  atag.attrs['href'] != None:
								if atag.attrs['href'] not in processed_urls:
									urls.append(atag.attrs["href"])
				except:
					continue	
		#{ print(u) for u in processed_urls }
					

		if len(emails)>0:
			print("Found emails:")
			{ print (em) for em in emails if validators.email(em)}
		else:
			print("Disappointment: somehow no emails were collected")
		return	True 



if __name__ == '__main__':
	prsr = argparse.ArgumentParser()
	prsr.add_argument("rootDomain")
	args = prsr.parse_args()
	if args.rootDomain:
		# validate url
		rootUrl=args.rootDomain
		""" http / https / ... protocol specification may require more work, taking simplistic approach for the sake of time """ 
		if not rootUrl.startswith("http"):
			rootUrl = "http://"+rootUrl
		if not validators.url(rootUrl):
			print("Invalid input domain {}, exiting...".format(args.rootDomain))
			exit(1)
		else:
			print("Looking for email addresses in {} and beyond".format(rootUrl))
			findObjects(rootUrl)
