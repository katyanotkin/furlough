import sys
import pymongo
import pprint
from pymongo import MongoClient
from flask import Flask, request, render_template, url_for
from json import dumps
from bson import ObjectId
import json
import urllib, json
import enum
from enum import Enum, auto
from datetime import datetime 
import local_settings
from local_settings import DB_AUTH

try:
	json_str=sys.argv[1]
	print ("INPUT", json_str)
except:
	print ("Unexpected arg error:", sys.exc_info()[0])
try:
	jsonIn=json.loads(json_str)
	print (jsonIn)
except:
	print ("Unexpected json parsing error:", sys.exc_info()[0])

try:
	connection = MongoClient(DB_AUTH['MONGO_HOST'], DB_AUTH['MONGO_PORT'])
	db = connection[DB_AUTH['MONGO_DB']]
	db.authenticate(DB_AUTH['MONGO_USER'], DB_AUTH['MONGO_PASS'])
except:
	
	print ("Unexpected db connection/auth error:", sys.exc_info()[0])

class dbOps(Enum):
	GET = auto()
	POST = auto()
	PUT = auto()
	DELETE = auto()
	GET_ONE = auto()

print ('enum: {}'.format(dbOps.GET.name))
print ('enum: {}'.format(dbOps.GET.value))


def get(collection, _id):
	try:
		# Convert from string to ObjectId:
		return db[collection].find_one({"_id": ObjectId(_id)}, {"_id": False,'clientId':False})
	except:
		return "'STATUS':'FAILED'"	

def get_many(collection, filter):
	try:
		result={}
		print ("FILTER:", filter)
		for doc in db[collection].find({filter}), {"_id": False,'clientId':False})
			result.append(doc)
		return result	
		
	except e:
		return e



def post_doc(collection,data):
	publishDate=datetime.utcnow().isoformat(timespec='microseconds')
	data['publishDate']=publishDate
	print (data)
	post_id = db[collection].insert_one(data)
	return post_id.inserted_id

def delete_doc(collection, _id):
	result = db[collection].delete_one({"_id": ObjectId(_id)})
	return result.deleted_count
	
def update_doc(collection, _id):
	updateDate=datetime.utcnow().isoformat(timespec='milliseconds')
	result = db[collection].update_one({"_id": ObjectId(_id)},{ '$set':{"clientId":ObjectId(_id), "overview": "Pretty lady, please remember me when you pray. OPHELIA.", "updateDate": updateDate}} upsert=True)
	return result.modified_count


collection='questions'
data=jsonIn['data']

_id=post_doc('questions',data)

print ("inserted id", _id)

#print ('DELETED:', delete_doc(collection, jsonIn['testid']))

print ("updated docs:" , update_doc(collection, _id))
#print (get(collection, _id))
print get_many('questions', {"overview": "Hamlet eternal"})

app = Flask(__name__)
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
quiz = Api(app)



quizurl="/quiz/resource=<qcollection>/_id=<_id>/<qmethod>"
print(quizurl)

@app.route(quizurl,methods=["GET", "DELETE", "PUT"])
def processor(qcollection,_id, qmethod):
	if qmethod=="GET":
		print (qcollection,  _id)
		return jsonify(get(qcollection, _id))
	elif qmethod=="DELETE":
		return jsonify({"deleted": delete_doc(qcollection,_id)}) 
	elif qmethod=="PUT":
		return jsonify(get(qcollection, _id))
	
if __name__ == '__main__':

	#app.run(debug=True)
	app.run()

