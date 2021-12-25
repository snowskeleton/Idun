from classes.notes import Notes
from classes.parts import Parts

import json


class Device:
    serialNumber = str
    modelNumber = str
    assetTag = str
    claimNumber = str
    generalNote = str
    serviceNotes = [Notes]
    partsReplaced = [Parts]
    customer = str