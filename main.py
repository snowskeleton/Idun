from os import pardir
from flask import Flask
from flask_restful import Resource, Api, reqparse
import json
from pprint import pprint
import time
import pymongo
from pymongo import MongoClient

from classes.device import Device
from classes.ticket import Ticket


app = Flask(__name__)
api = Api(app)


# class Info(Resource):
    # def get(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('serialNumber', required=False, type=str)
    #     parser.add_argument('assetTag', required=False, type=str)
    #     args = parser.parse_args()
    #     if args['serialNumber'] != "":
    #         device.serialNumber = args['serialNumber']
    #     device.modelNumber = args['modelNumber']
    #     device.assetTag = args['assetTag']

class CreateNewTicket(Resource): #use this to make a ticket with the below information. add notes and parts later.
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('serialNumber', required=False, type=str)
        parser.add_argument('modelNumber', required=False, type=str)
        parser.add_argument('assetTag', required=False, type=str)
        parser.add_argument('customer', required=False, type=str)
        args = parser.parse_args()

        device = Device() #configure device for later adding to ticket.
        device.serialNumber = args['serialNumber']
        device.modelNumber = args['modelNumber']
        device.assetTag = args['assetTag']

        ticket = Ticket()
        ticket.device = device
        ticket.creationDate = time.time

        cluster = MongoClient('mongodb+srv://snow:SH0zdIAD9scRU1if@cluster0.7luyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        db = cluster["FixMe"]
        nextTicketNumber = db['nextTicketNumber']
        with open("./data/increment", "w+") as infile:
            num = infile + 1
            ticket.ticketNumber = num
            infile = num

        cluster = MongoClient('mongodb+srv://snow:SH0zdIAD9scRU1if@cluster0.7luyp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        db = cluster["FixMe"]
        collection = db["tickets"]

        post = device
        collection.insert_one(post)

        print(ticket.ticketNumber + "<< this is the ticket number")
        with open("./data/tickets.json", "a") as outfile:
            json.dump(ticket, outfile)
        
        with open("./data/sample.json", "a") as outfile:
            json.dump(device.__dict__, outfile)
        return device.__dict__, 200

    def get(self): #this will not have a GET request.
        return 204
    
class AddNewCustomer(Resource):
    def post(self): #TODO: make this function check if the customer already exists rather than just blindly adding whatever we're told.
        parser = reqparse.RequestParser()
        parser.add_argument('Name', required=True, type=str)
        args = parser.parse_args()
        customer = args['Name']
        with open("./data/customerList", "a") as infile:
            json.dump(customer, infile)

        return 200

class ChangePartsOnTickets(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Add', required=True, type=bool) #set True to add parts, set False to delete parts. should this be a DELETE request?
        parser.add_argument('Name', required=True, type=str)
        parser.add_argument('Ticket', required=True, type=str)
        args = parser.parse_args()

        # load ticket with ticket number
        # add part to ticket
        # I'll probably want to figure out how to send/accept an array of parts
        ##until then, I'll have to accept one request per part, which works just fine.
        #TODO ^

class AddNoteToTicket(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("TicketNumber", required=True, type=str)
        parser.add_argument("Note", required=True, type=str)

class SetCompletedOverride(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("TicketNumber", required=True, type=str)
        #TODO set CompletedOverride value for given ticket number

class BulkTickets(Resource):
    def get(self):
        parser = reqparse.RequestParser() # get all tickets, with the arguments specifying if whether to return Open tickets, Closed tickets, or both.
        parser.add_argument('Open', required=False, type=bool) 
        parser.add_argument('Closed', required=False, type=bool)
        
        parser.add_argument('Field', required=False, type=str) # allows the user to specify a field by which they want to filter. Not sure how.
        parser.add_argument('Something', required=False, type=str) # a value for the above.

        #return requested tickets.

class ListPartsFor(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Model', required=True, type=str) #list all parts compatible with specified model, as well as quantity surplus/deficit

class AddUser(Resource):
    def post(self): #something something, make new user. TODO: make secure
        parser = reqparse.RequestParser()
        parser.add_argument('Name', required=True, type=str)
        parser.add_argument('Admin', required=True, type=bool) #set True for admin, False for non-admin. Password created elsewhere.

#             json_file_path = "/path/to/example.json"

# with open(json_file_path, 'r') as j:
#      contents = json.loads(j.read())


        with open("./data/customerlist.json", "r") as read_file:
            data = json.load(read_file.to_dict())
            print(data)

        # # f = open("./data/customerList.json",)
        # # custoemrList = json.load(f.read())
        # # print(customerList)
        # # return 200
        # f = open("./data/customerList.json", "a")
        # # print(f)
        # # with open("./data/customerList.json", "a+") as outfile: #this is an attempt to standardize customer naming, for easier sorting later.
        # try:
        #     customerList = json.load(f)
        # except:
        #     customerList = {}
        # print(type(customerList))
        # # if (args['Name']) in customerList:
        # if any([True for k,v in customerList['CustomerList'] if v == args['Name']]):
        #     return "Customer already exists", 409
        # else:
        #     # customerList += args['Name']
        #     # json.dump(customerList, f)
        #     f.close()
        #     return 200
        
api.add_resource(CreateNewTicket, '/api/createNewTicket')
api.add_resource(AddNewCustomer, '/api/addNewCustomer')


if __name__ == "__main__":
    app.run(debug=True)