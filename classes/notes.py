from datetime import datetime
from classes.user import User


class Notes:
    timeStamp: str
    note: str
    user: User

    def __init__(self, stats):
        self.note = stats['note']
        self.user = stats['user']
        self.timeStamp = datetime.now().strftime("%Y%m%d, %H:%M")