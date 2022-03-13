class Kit:
    def __init__(self, id, name,description, hexStartColor, hexFinishColor, hexTitleColor, hexTextColor):
        self.cards = []
        self.id = str(id)
        self.name = name
        self.hexTextColor = hexTextColor
        self.hexStartColor = hexStartColor
        self.hexTitleColor = hexTitleColor
        self.hexFinishColor = hexFinishColor
        self.description = description

    def __dict__(self):
        return {'id': self.id,
                'title': self.name,
                'description': self.description,
                'cards': self.cards,
                'hexStartColor': self.hexStartColor,
                'hexFinishColor': self.hexFinishColor,
                'hexTitleColor': self.hexTitleColor,
                'hexTextColor': self.hexTextColor
                }
