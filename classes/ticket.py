from datetime import datetime
from classes.notes import Notes
from classes.device import Device
# from classes.parts import Parts
# from munch import Munch

import classes.db
from dataclasses import dataclass

@dataclass


class Ticket:
    isCompletedOverride = bool
    ticketNumber = int
    creationDate = str
    notes = [Notes]
    device = Device
    partsNeeded = {}
    partsUsed = {}
    partsOrdered = {}

    #linkedTickets = [Ticket]
    def hasChanged():
        pass #this will probably use a hash of this object to see if it's changed since what we last expected, that way we don't overlap

    def new(device):
        ticket = Ticket()
        ticket.device = device.__dict__
        ticket.creationDate = datetime.now().strftime("%Y%m%d, %H:%M:%S")
        ticket.ticketNumber = classes.db.nextNumber()
        return ticket
    
    # def gimmeRealTicket(ticket):
    #     value =  Munch.fromDict(ticket)
    #     print(value)
    #     return value