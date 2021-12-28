from pprint import pprint
from pymongo import MongoClient

cluster = MongoClient('mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000')
db = cluster["FixMe"]
collection = db['nextNumber']
post = {"_id": "sequence", "nextNumber": 0}
collection.insert_one(post)

