
import sys
from flask import Flask
from flask_jsonpify import jsonify
import pymongo
from pymongo import MongoClient
from bson import ObjectId
import local_settings
from local_settings import DB_AUTH



app = Flask(__name__)
qurl="/quizZy/collection=<collection>"
print (qurl)
@app.route(qurl)


def get_many(collection):
	try:
		connection = MongoClient(DB_AUTH['MONGO_HOST'], DB_AUTH['MONGO_PORT'])
		db = connection[DB_AUTH['MONGO_DB']]
		#db.authenticate(DB_AUTH['MONGO_USER'], DB_AUTH['MONGO_PASS'])
	except:
		print ("Unexpected db connection/auth error:", sys.exc_info()[0])

	try:
		print (db.collection_names())
		print (list(db[collection].find({'filterPlaceholder':None})))
		return jsonify(list(db[collection].find({'filterPlaceholder':None},{"_id": False,'clientId':False})))
		
	except:
		return ("Unexpected error:", sys.exc_info()[0]) 

if __name__ == '__main__':
    app.run()

