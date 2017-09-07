# user: schema definition and document validation

import sys
import json
import jsonschema
from jsonschema import validate

import datetime

"""
class User(Document):
	uEmail = EmailField(required=True, unique=True)
	first_name = StringField(min_length=2)
	last_name = StringField(min_length=2)
	phone = IntField(length=10)
	docStatus = StringField(choices=("Active","Inactive", "Pending")) 
	dateCreated = DateTimeField(default=datetime.datetime.now)
	dateUpdated = DateTimeField()
"""

appUser_schema = {
    "type" : "object",
    "properties" : {
        "uEmail" : {"type" : "string"},
        "name" : {"type" : "string"},
	"phone": {"type" : "number"},
	"required": ["uEmail", "name"]
    },
}
	
	

