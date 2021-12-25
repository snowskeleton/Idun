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
import classes.db
import classes.parser


app = Flask(__name__)
api = Api(app)


# use this to make a ticket with the below information. add notes and parts later.
class CreateNewTicket(Resource): # called to  create new ticket with device details as arguments. returns ticket number.
    def post(self):
        args = classes.parser.parseThis(reqparse.RequestParser)

        device = Device.makeNew(args)

        ticket = Ticket()
        ticket.device = device.__dict__
        # ticket.creationDate = time.time #find a different way to keep track of date, since Mongo doesn't like this way.
        ticket.ticketNumber = classes.db.nextNumber()
        try:
            classes.db.persistTicket(ticket)
        except:
            return "Something went wrong while saving the ticket. Please try again.", 500

        return ticket.ticketNumber, 200


class AddNewCustomer(Resource):
    # TODO: make this function check if the customer already exists rather than just blindly adding whatever we're told.
    def post(self):
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
        # set True to add parts, set False to delete parts. should this be a DELETE request?
        parser.add_argument('Add', required=True, type=bool)
        parser.add_argument('Name', required=True, type=str)
        parser.add_argument('Ticket', required=True, type=str)
        args = parser.parse_args()

        # load ticket with ticket number
        # add part to ticket
        # I'll probably want to figure out how to send/accept an array of parts
        # until then, I'll have to accept one request per part, which works just fine.
        # TODO ^


class AddNoteToTicket(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("TicketNumber", required=True, type=str)
        parser.add_argument("Note", required=True, type=str)


class SetCompletedOverride(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("TicketNumber", required=True, type=str)
        # TODO set CompletedOverride value for given ticket number


class BulkTickets(Resource):
    def get(self):
        # get all tickets, with the arguments specifying if whether to return Open tickets, Closed tickets, or both.
        parser = reqparse.RequestParser()
        parser.add_argument('Open', required=False, type=bool)
        parser.add_argument('Closed', required=False, type=bool)

        # allows the user to specify a field by which they want to filter. Not sure how.
        parser.add_argument('Field', required=False, type=str)
        # a value for the above.
        parser.add_argument('Something', required=False, type=str)

        # return requested tickets.


class ListPartsFor(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        # list all parts compatible with specified model, as well as quantity surplus/deficit
        parser.add_argument('Model', required=True, type=str)


class AddUser(Resource):
    def post(self):  # something something, make new user. TODO: make secure
        parser = reqparse.RequestParser()
        parser.add_argument('Name', required=True, type=str)
        # set True for admin, False for non-admin. Password created elsewhere.
        parser.add_argument('Admin', required=True, type=bool)

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
