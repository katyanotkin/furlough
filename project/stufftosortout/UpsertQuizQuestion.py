import sys
import pymongo
import pprint
from pymongo import MongoClient
from flask import Flask, request, render_template, url_for
from json import dumps
from bson import ObjectId
import json
import urllib, json
from datetime import datetime 
import local_settings
from local_settings import DB_AUTH


try:
	connection = MongoClient(DB_AUTH['MONGO_HOST'], DB_AUTH['MONGO_PORT'])
	db = connection[DB_AUTH['MONGO_DB']]
	db.authenticate(DB_AUTH['MONGO_USER'], DB_AUTH['MONGO_PASS'])
except:
	
	print ("Unexpected db connection/auth error:", sys.exc_info()[0])


def get(collection, _id):
	try:
		# Convert from string to ObjectId:
		return db[collection].find_one({"_id": ObjectId(_id)}, {"_id": False,'clientId':False})
	except:
		return "'STATUS':'FAILED'"	

def post_doc(collection,data):
	publishDate=datetime.utcnow().isoformat()
	data['publishDate']=publishDate
	print (data)
	post_id = db[collection].insert_one(data)
	return post_id.inserted_id

def delete_doc(collection, _id):
	result = db[collection].delete_one({"_id": ObjectId(_id)})
	return result.deleted_count
	
def update_doc(collection, _id):
	updateDate=datetime.utcnow().isoformat(timespec='milliseconds')
	result = db[collection].update_one({"_id": ObjectId(_id)},{ '$set':{"clientId":ObjectId(_id), "overview": "Pretty lady, please remember me when you pray. OPHELIA.", "updateDate": updateDate}})
	print ("Upd", result.modified_count)
	return result.modified_count


collection='questions'

print post_doc('appUsers',"{'email':'ko@ko.com'}")
print ("inserted id", _id)

#print ('DELETED:', delete_doc(collection, jsonIn['testid']))

#_id='599796af029f306f0eeaba11'
print ("updated docs:" , update_doc(collection, _id))
print (get(collection, _id))





