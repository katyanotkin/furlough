import sys
from flask import Flask
from flask_jsonpify import jsonify
import pymongo
from pymongo import MongoClient
from bson import ObjectId
from flask import request
import local_settings
from local_settings import DB_AUTH
#import settings
#from settings import DB_AUTH
 
q = Flask(__name__)
qurl="/quiz/collection=<collection>"
print (qurl)
@q.route(qurl)

def get(collection='questions'):
	try:
		connection = MongoClient(DB_AUTH['MONGO_HOST'], DB_AUTH['MONGO_PORT'])
		db = connection[DB_AUTH['MONGO_DB']]
		db.authenticate(DB_AUTH['MONGO_USER'], DB_AUTH['MONGO_PASS'])
		#return (DB_AUTH['MONGO_DB'])
	except:
		return ("Unexpected db connection/auth error:", sys.exc_info()[0])
	try:
                # Convert from string to ObjectId:
		#return (request.args.get('_id'))
		return jsonify(db[collection].find_one({"_id": ObjectId(request.args.get('_id'))}, {'_id':False,'clientId':False}))
	except:
		return "{'STATUS':'FAILED'}"

# We only need this for local development.
if __name__ == '__main__':
    q.run()

