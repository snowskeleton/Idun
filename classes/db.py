from pymongo import MongoClient
import classes.parts
import classes.notes


cluster = MongoClient(
    'mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000')
db = cluster["FixMe"]
tickets = db['tickets']


# returns an integer equal to n+1, where n is the previous ticket number issued.
def nextNumber():
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
    print(ticket.__dict__)


def fetchTicket(num):
    ticket = tickets.find_one({"_id": num})
    return ticket


def addParts(body):
    for part in body['parts']:
        _part = classes.parts.Parts(part)
        db['tickets'].update_one(
            {'_id': body['_id']},
            {"$push": {"parts": _part.__dict__}}
        )


def addNotes(body):
    note = classes.notes.Notes(body)
    db['tickets'].update_one(
        {'_id': body['_id']},
        {"$push": {"notes": note.__dict__}}
    )
