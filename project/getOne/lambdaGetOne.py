import sys
from flask import Flask
from flask_jsonpify import jsonify
import pymongo
from pymongo import MongoClient
from bson import ObjectId
from flask import request
import json
import local_settings
from local_settings import DB_AUTH
import settings
#from settings import DB_AUTH
import dbConnection 
"""
try:
	from dbConnection import dbConn  
except ImportError:
	print ("dbConnection.py not found") 
"""
try:
                connection = MongoClient(DB_AUTH['MONGO_HOST'], DB_AUTH['MONGO_PORT'])
                db = connection[DB_AUTH['MONGO_DB']]
                db.authenticate(DB_AUTH['MONGO_USER'], DB_AUTH['MONGO_PASS'])
except:
                print ("Unexpected db connection/auth error:", sys.exc_info()[0])

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
 
q = Flask(__name__)
qurl="/quiz/collection=<collection>"
print (qurl)
@q.route(qurl)

def get(collection):
	#print ("dbConn {}".format(dbConn))
	#db=dbConn()	
	#print (list(db['appUsers'].find()))
	print(collection, db)
	checkColl = db[collection].count()
	if checkColl==0:
		return '{"ERROR":"Invalid or empty collection"}' 
	if not ObjectId.is_valid(request.args.get('_id')):
		return '{"ERROR":"Invalid _id"}'
	print (db[collection].find_one({"_id": ObjectId(request.args.get('_id'))}))
	try:
		return JSONEncoder().encode(db[collection].find_one({"_id": ObjectId(request.args.get('_id'))}, {'_id':False,'clientId':False}))
	except:
		print ("ERROR: {}".format(sys.exc_info()[1]))
		return ("6666")

# We only need this for local development.
if __name__ == '__main__':
    q.run()

