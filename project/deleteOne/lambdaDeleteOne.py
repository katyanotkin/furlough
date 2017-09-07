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
#from settings import DB_AUTH
import dbConnection 
#import customErrors
from customErrors import customErrors
try:
	from dbConnection import dbConn 
except ImportError:
	print ("dbConnection.py not found") 

#print (dbConnection.dbConn)

app = Flask(__name__)
qurl="/collection=<collection>"
print (qurl)
@app.route(qurl, methods=['DELETE'])

def deleteOne(collection):
	db=dbConn()	
	#print (db)
	if db[collection].count()==0:
		return customErrors['COLLECTION']
	id=request.args.get('_id')
	if not id:
		return customErrors['MISSINGARG']
	if not ObjectId.is_valid(id):
		return customErrors['INVALIDID'] 
	try: 
		result = db[collection].delete_one({"_id": ObjectId(id)})
		print ("collection {} count {}, deleted cnt {}".format(collection, db[collection].count(), result.deleted_count))
		return jsonify('DELETED : {}'.format(result.deleted_count))
	except:
		print("error delete {} {}".format(sys.exc_info()[0], sys.exc_info()[1]))
		return customErrors['FAILEDDELETE'] 

# We only need this for local development.
if __name__ == '__main__':
	app.run()
