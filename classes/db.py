from pprint import pprint
from pymongo import MongoClient

cluster = MongoClient(
    'mongodb+srv://snow:SH0zdIAD9scRU1if@cluster0.7luyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster["FixMe"]

def nextNumber():
    # cluster = MongoClient(
    #     'mongodb+srv://snow:SH0zdIAD9scRU1if@cluster0.7luyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    # db = cluster["FixMe"]
    nextNumberCollection = db['nextNumber'] # there should only be one result returned. NO ERROR HANDLING
    nextTicketNumberDict = nextNumberCollection.find_one({"_id": "sequence"})
    nextNumber = nextTicketNumberDict['nextNumber']
    try:
        nextNumberCollection.update_one({"_id": "sequence"}, {"$inc": {"nextNumber": 1}})
        return nextNumber
    except:
        # TODO: probably handle this better. maybe log it?
        raise Warning("Can't return proper ticket number")

def persistTicket(ticket):
    try:
        db['tickets'].insert_one(ticket)
    except:
        print("Danger, Will Robinson!")