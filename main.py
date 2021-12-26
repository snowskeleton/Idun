from os import pardir, rename
from flask import Flask
from flask_restful import Resource, Api, reqparse
from pprint import pprint
import json
from munch import Munch
import collections

from classes.device import Device
from classes.ticket import Ticket
from classes.parser import Parser
import classes.db


app = Flask(__name__)
api = Api(app)
from collections import namedtuple

def convert(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            obj[key] = convert(value) 
        return namedtuple('GenericDict', obj.keys(),rename=True)(**obj)
    elif isinstance(obj, list):
        return [convert(item) for item in obj]
    else:
        return obj

class CreateNewTicket(Resource): # called to create new ticket with device details as arguments. returns ticket number.
    def post(self):
        args = Parser.parseThis(reqparse.RequestParser)
        device = Device.makeNew(args)
        ticket = Ticket.new(device)
        try:
            classes.db.persistTicket(ticket)
        except:
            return "Something went wrong while saving the ticket. Please try again.", 500

        return ticket.ticketNumber, 200


class AddPartsToTicket(Resource):
    def post(self):
        args = Parser.partsParse(reqparse.RequestParser)
        ticket = classes.db.fetchTicket(args['ticket']) # fetch ticket by number
        # ticket = Ticket.gimmeRealTicket(ticket)
        ticket = convert(ticket)
        print(ticket)
        ticket = classes.db.addParts(ticket=ticket, parts=args['parts']) #this accepts a Ticket object but parts are passed through HTTP Post? Seems fishy....... TODO: investigate
        ticket.partsNeeded.append(args['parts'])
        return json.dumps(ticket, default=str), 200
        

class AddNewCustomer(Resource):
    # TODO: make this function check if the customer already exists rather than just blindly adding whatever we're told.
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Name', required=True, type=str)
        args = parser.parse_args()
        customer = args['Name']
        # with open("./dta/customerList", "a") as infile:
            # json.dump(customer, infile)

        return 200
        
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

        # with open("./data/customerlist.json", "r") as read_file:
        #     data = json.loadk(read_file.to_dict())
        #     print(data)



api.add_resource(CreateNewTicket, '/api/createNewTicket')
api.add_resource(AddNewCustomer, '/api/addNewCustomer')
api.add_resource(AddPartsToTicket, '/api/addPartsToTicket')


if __name__ == "__main__":
    app.run(debug=True)
