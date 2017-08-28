import sys
from flask import Flask
from flask_jsonpify import jsonify
import pymongo
from pymongo import MongoClient
from bson import ObjectId
from flask import request
import settings
from settings import DB_AUTH
 
app = Flask(__name__)
qurl="/quiz/collection=<collection>"
print (qurl)
@app.route(qurl)

def get(collection='questions'):
	try:
        	connection = MongoClient(DB_AUTH['MONGO_HOST'], DB_AUTH['MONGO_PORT'])
        	db = connection[DB_AUTH['MONGO_DB']]
        	db.authenticate(DB_AUTH['MONGO_USER'], DB_AUTH['MONGO_PASS'])
		#print (DB_AUTH['MONGO_DB'], "boo")
	except:

        	return ("Unexpected db connection/auth error:", sys.exc_info()[0])
	
	try:
                # Convert from string to ObjectId:
		print (request.args.get('boo'))
                return jsonify(db[collection].find_one({"_id": ObjectId(request.args.get('_id'))}, {'_id':False,'clientId':False}))
	except:
                return "{'STATUS':'FAILED'}"


# We only need this for local development.
if __name__ == '__main__':
    app.run()

