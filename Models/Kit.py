class Kit:
    id = -1
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __dict__(self):
        return {'id': self.id,
                'title': self.name}
