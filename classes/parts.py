
class Parts:
    name: str
    cost: float
    ordered: bool
    replaced: bool

    def __init__(self, dict):
        self.name = dict['name']
        self.cost = dict['cost']
        self.ordered = False
        self.replaced = False