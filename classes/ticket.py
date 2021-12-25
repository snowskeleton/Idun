# from classes import Notes, Device, Parts, Ticket
from datetime import time
from classes.notes import Notes
from classes.device import Device
from classes.parts import Parts


class Ticket:
    isCompletedOverride = bool
    ticketNumber = int
    creationDate = time
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