from flask import Flask, request
from flask_restful import Resource, Api
import json

from classes.ticket import Ticket
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


# accepts ticket ID. returns ticket as json
class FetchTicketInfo(Resource):
    def get(self):
        body = request.json
        ticket = classes.db.fetchTicket(body['_id'])
        return json.dumps(ticket, default=str)


# accepts ticket ID and list of part objects. returns nothing.
class AddPartsToTicket(Resource):
    def post(self):
        try:
            classes.db.addParts(request.json)
        except:
            return "Unable to add parts to ticket", 500
        return 200

# accepts ticket ID and note. returns nothing
class AddNoteToTicket(Resource):
    def post(self):
        try:
            classes.db.addNotes(request.json)
        except:
            return "Unable to add note to ticket", 500
        return 200


api.add_resource(CreateNewTicket, '/api/createNewTicket')
api.add_resource(AddPartsToTicket, '/api/addPartsToTicket')
api.add_resource(AddNoteToTicket, '/api/addNoteToTicket')
api.add_resource(FetchTicketInfo, '/api/fetchTicketInfo')


if __name__ == "__main__":
    app.run(debug=True)
