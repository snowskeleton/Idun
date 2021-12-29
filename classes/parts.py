
class Parts:
    name: str
    cost: float
    ordered: bool
    replaced: bool

    def __init__(self, args):
        self.name = args['name']
        self.cost = args['cost']
        self.ordered = False
        self.replaced = False