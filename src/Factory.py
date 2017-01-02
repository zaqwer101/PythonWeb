class Factory:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def make_item(self, item):
        self.inventory.append(item)

