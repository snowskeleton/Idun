import pymongo
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://snow:SH0zdIAD9scRU1if@cluster0.7luyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster["test"]
collection = db["test"]

post = {"_id": 0, "name": "tim", "score": 10000000000}
collection.insert_one(post)