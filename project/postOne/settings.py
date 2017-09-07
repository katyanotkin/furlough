import sys
import getpass

CFG='/home/'+getpass.getuser()+'/furlough/project/config'
#print (CFG)
sys.path.append(CFG)

try:
	import local_settings
	from local_settings import *
except ImportError:
	print ("local_settings.py not found in config directory") 



