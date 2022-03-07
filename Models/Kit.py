class Kit:
    id = -1
    name = ""
    cards = []
    hexStartColor = ""
    hexFinishColor = ""
    hexTitleColor = ""
    hexTextColor = ""

    def __init__(self, id, name, hexStartColor, hexFinishColor, hexTitleColor, hexTextColor):
        self.id = id
        self.name = name
        self.hexTextColor = hexTextColor
        self.hexStartColor = hexStartColor
        self.hexTitleColor = hexTitleColor
        self.hexFinishColor = hexFinishColor

    def __dict__(self):
        return {'id': self.id,
                'title': self.name,
                'cards': self.cards,
                'hexStartColor': self.hexStartColor,
                'hexFinishColor': self.hexFinishColor,
                'hexTitleColor': self.hexTitleColor,
                'hexTextColor': self.hexTextColor
                }
