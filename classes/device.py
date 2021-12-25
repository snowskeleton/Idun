from classes.notes import Notes
from classes.parts import Parts


class Device:
    serialNumber = str
    modelNumber = str
    assetTag = str
    claimNumber = str
    generalNote = str
    serviceNotes = [Notes]
    partsReplaced = [Parts]
    customer = str


    def makeNew(args):
        device = Device()
        device.serialNumber = args['serialNumber']
        device.modelNumber = args['modelNumber']
        device.assetTag = args['assetTag']

        return device