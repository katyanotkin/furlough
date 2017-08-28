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


def get(collection, _id):
	try:
		# Convert from string to ObjectId:
		return db[collection].find_one({"_id": ObjectId(_id)}, {"_id": False,'clientId':False})
	except:
		return "'STATUS':'FAILED'"	

def get_many(collection, filter):
	try:
		print ("FILTER:", filter)
		return list(db[collection].find(filter, {"_id": False,'clientId':False}))
		
	except:
		return ("Unexpected error:", sys.exc_info()[0]) 



collection='questions'
data=jsonIn['data']

print (get_many('questions', {"overview": "Hamlet eternal"}))

app = Flask(__name__)
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
quizZy = Api(app)


quizurl="/quizZy/"
print(quizurl)

@app.route(quizurl,methods=["GET"])

def processor(id='', qcollection=collection):
		return jsonify(get_many(qcollection, data))

if __name__ == '__main__':

	#app.run(debug=True)
	app.run()

