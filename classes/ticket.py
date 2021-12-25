# from classes import Notes, Device, Parts, Ticket
from datetime import datetime
from classes.notes import Notes
from classes.device import Device
from classes.parts import Parts
import classes.db



class Ticket:
    isCompletedOverride = bool
    ticketNumber = int
    creationDate = str
    notes = [Notes]
    device = Device
    def partsNeeded():
        return [Parts]
    def partsOrdered():
        return [Parts]
    def partsUsed():
        [Parts]
    def partsRecovred():
        [Parts]
    # @partsUsed
    # @partsNeeded
    #def isRepaired():
        #if partsNeeded.len == partsUsed.len and partsNeeded != 0:
            #return True
        #else:
            #return False
    
    #linkedTickets = [Ticket]
    def hasChanged():
        pass #this will probably use a hash of this object to see if it's changed since what we last expected, that way we don't overlap

    def new(device):
        ticket = Ticket()
        ticket.device = device.__dict__
        ticket.creationDate = datetime.now().strftime("%Y%m%d, %H:%M:%S")
        ticket.ticketNumber = classes.db.nextNumber()
        return ticket