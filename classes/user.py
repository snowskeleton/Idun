class User:
    name = str
    isAdmin = bool

    def __init__(self, stats) -> None:
        self.name = stats['name']
        self.isAdmin = stats['isAdmin']