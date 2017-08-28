
import sys
import pymongo
from pymongo import MongoClient
from bson import ObjectId
DB_AUTH = {
'MONGO_HOST' : "local",
'MONGO_PORT' :  27017,
'MONGO_DB': "quizzella",
'MONGO_USER': "",
'MONGO_PASS' : "",
}





def get_many(collection):
	try:
		connection = MongoClient(DB_AUTH['MONGO_HOST'], DB_AUTH['MONGO_PORT'])
		db = connection[DB_AUTH['MONGO_DB']]
		#db.authenticate(DB_AUTH['MONGO_USER'], DB_AUTH['MONGO_PASS'])
	except:
		print ("Unexpected db connection/auth error:", sys.exc_info()[0])
	print (db.collection_names())
	print (list(db[collection].find({'filterPlaceholder':None})))

	try:
		print (db.collection_names())
		print (list(db[collection].find({'filterPlaceholder':None})))
		return jsonify(list(db[collection].find({'filterPlaceholder':None},{"_id": False,'clientId':False})))
		#return jsonify(db[collection].find_one({"_id": ObjectId(request.args.get('_id'))}, {'_id':False,'clientId':False}))
		
	except:
		return ("Unexpected error:", sys.exc_info()[0]) 

if __name__ == '__main__':
	print(get_many('appUsers'))

