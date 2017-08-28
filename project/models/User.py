# Class User, model definition and document validation
import sys, os
home_dir=os.path.expanduser("~")
python_pack_dir=os.path.join("/home/enot/furlough/envv/lib/python3.6/site-packages/")
sys.path.append(python_pack_dir)
#print (sys.path)

import mongoengine
from mongoengine import *
import datetime


class User(Document):
	uEmail = EmailField(required=True, unique=True)
	first_name = StringField(min_length=2)
	last_name = StringField(min_length=2)
	phone = IntField(length=10)
	docStatus = StringField(choices=('Active','Inactive', 'Pending')) 
	dateCreated = DateTimeField(default=datetime.datetime.now)
	dateUpdated = DateTimeField()
	
	

