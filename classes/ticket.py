from datetime import datetime
from classes.notes import Notes

import classes.db
# from dataclasses import dataclass

# @dataclass


class Ticket:
    # _id: int
    isCompletedOverride: bool
    ticketNumber: int
    # creationDate = str
    customer: str
    # notes = [Notes]
    serialNumber: str
    modelNumber: str
    assetTag: str
    # parts = {}

    def __init__(self, args) -> None:
        # self._id = classes.db.nextNumber()
        self.isCompletedOverride = False
        self.ticketNumber = classes.db.nextNumber()
        self.serialNumber = args['serialNumber']
        self.modelNumber = args['modelNumber']
        self.assetTag = args['assetTag']


    #linkedTickets = [Ticket]
    def hasChanged():
        pass #this will probably use a hash of this object to see if it's changed since what we last expected, that way we don't overlap

    def new(device):
        ticket = Ticket()
        ticket.creationDate = datetime.now().strftime("%Y%m%d, %H:%M:%S")
        ticket.ticketNumber = classes.db.nextNumber()
        return ticket
    
    # def gimmeRealTicket(ticket):
    #     value =  Munch.fromDict(ticket)
    #     print(value)
    #     return value