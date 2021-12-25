from pprint import pprint
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://snow:SH0zdIAD9scRU1if@cluster0.7luyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster["FixMe"]
collection = db['nextNumber']
post = {"_id": "sequence", "nextNumber": 0}
collection.insert_one(post)

