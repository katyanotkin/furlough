import sys, os
home_dir=os.path.expanduser("~")
python_pack_dir=os.path.join("/home/enot/furlough/envv/lib/python3.6/site-packages/")
sys.path.append(python_pack_dir)
import mongoengine
from mongoengine import *
from User import *
try:
	u=User(docStatus=False, uEmail='kno@gmail.com', first_name='K', last_name='N', phone='234567890')
	u.save
	print ("uuuu")
except : 
	print ("problem1", sys.exc_info()[0])
	raise
try:
	uu=User( docStatus='Activee',  first_name='K', last_name='N', phone='234567890')
	uu.save
except:
	print ("prob2")

uuu=User( docStatus='Activee', uEmail='kno.com', first_name='K', last_name='N', phone='234567890')
uuu.save
