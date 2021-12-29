from os import pardir, rename
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from pprint import pprint
import json

from classes.ticket import Ticket
from classes.parser import Parser
import classes.db


app = Flask(__name__)
api = Api(app)

 # called to create new ticket with device details as arguments. returns ticket number.
class CreateNewTicket(Resource):
    def post(self):
        body = request.json
        ticket = Ticket(body)
        try:
            classes.db.persistTicket(ticket)
        except:
            return "Something went wrong while saving the ticket. Please try again.", 500

        return json.dumps(ticket._id, default=str), 200

# accepts ticket ID. returns ticket as json dictionary
class FetchTicketInfo(Resource):
    def get(self):
        body = request.json
        print(body['_id'])
        print("Look at me!")
        ticket = classes.db.fetchTicket(body['_id'])
        return json.dumps(ticket, default=str)


# accepts ticket ID and list of parts objects. returns nothing.
class AddPartsToTicket(Resource):
    def post(self):
        try:
            classes.db.addParts(request.json)
        except:
            return "Unable to add parts to ticket", 500
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
api.add_resource(AddPartsToTicket, '/api/addPartsToTicket')
api.add_resource(FetchTicketInfo, '/api/fetchTicketInfo')


if __name__ == "__main__":
    app.run(debug=True)
