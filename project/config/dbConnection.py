import sys
import pymongo
from pymongo import MongoClient
from . import settings 
from settings import DB_AUTH


def dbConn():
        try:
                connection = MongoClient(DB_AUTH['MONGO_HOST'], DB_AUTH['MONGO_PORT'])
                db = connection[DB_AUTH['MONGO_DB']]
                db.authenticate(DB_AUTH['MONGO_USER'], DB_AUTH['MONGO_PASS'])
                return (db)
        except:
                return ("Unexpected db connection/auth error:", sys.exc_info()[0])

if __name__ == '__main__':
	print(dbConn)
