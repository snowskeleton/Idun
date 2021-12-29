from datetime import datetime
import classes.db
import classes.notes

class Ticket:
    _id: int
    creationDate: str
    serialNumber: str
    modelNumber: str
    assetTag: str
    customer: str
    parts: list
    notes: list

    def __init__(self, body):
        self._id = classes.db.nextNumber()
        self.creationDate = datetime.now().strftime("%Y%m%d, %H:%M")
        self.serialNumber = body['serialNumber']
        self.modelNumber = body['modelNumber']
        self.assetTag = body['assetTag']
        self.notes = []
        self.parts = []

    def completed(self) -> bool:
        return False # TODO fix this later