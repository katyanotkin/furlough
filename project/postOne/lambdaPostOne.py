import sys
from flask import Flask
from flask_jsonpify import jsonify
from flask_restful import Resource, Api
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import (request, make_response)
from datetime import datetime
import json
import settings
from settings import DB_AUTH
import dbConnection 
try:
	from dbConnection import dbConn 
except ImportError:
	print ("dbConnection.py not found") 

#print (dbConnection.dbConn)
"""
try:
                connection = MongoClient(DB_AUTH['MONGO_HOST'], DB_AUTH['MONGO_PORT'])
                db = connection[DB_AUTH['MONGO_DB']]
                db.authenticate(DB_AUTH['MONGO_USER'], DB_AUTH['MONGO_PASS'])
except:
                print ("Unexpected db connection/auth error:", sys.exc_info()[0])


"""

app = Flask(__name__)
qurl="/post/collection=<collection>"
print (qurl)
@app.route(qurl, methods=['POST'])

def postOne(collection='questions'):
	db=dbConn()	
	#print (list(db['appUsers'].find()))
	if not request.json:
		abort(400)
	else:
		data_json=request.json
		data_json["dateCreated"]=datetime.utcnow().isoformat(timespec='microseconds')
	if collection=='appUsers':
		data_json["status"]='Pending'
	#data_json = json.dumps(data)
	print (data_json)


	post_id = db[collection].insert_one(data_json)
	print("id", str(post_id))
	return (str(post_id.inserted_id))

# We only need this for local development.
if __name__ == '__main__':
	app.run()

