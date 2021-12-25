from pymongo import MongoClient

cluster = MongoClient(
    'mongodb+srv://snow:SH0zdIAD9scRU1if@cluster0.7luyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster["FixMe"]


def nextNumber(): #returns an integer equal to n+1, where n is the previous ticket number issued.
    collection = db['nextNumber']
    nextNumber = collection.find_one({"_id": "sequence"})['nextNumber']
    try:
        collection.update_one(
            {"_id": "sequence"}, {"$inc": {"nextNumber": 1}})
        return nextNumber
    except:
        # TODO: probably handle this better. maybe log it?
        raise Warning("Can't return proper ticket number")


def persistTicket(ticket):
    db['tickets'].insert_one(ticket.__dict__)