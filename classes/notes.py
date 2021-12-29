from datetime import datetime
from classes.user import User


class Notes:
    timeStamp = datetime.now().strftime("%Y%m%d, %H:%M")
    note = str
    user = User