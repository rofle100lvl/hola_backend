import json


class Kit:
    id = -1
    number_of_questions = -1
    name = ""

    def __init__(self, id, number, name):
        self.id = id
        self.number_of_questions = number
        self.name = name


    def __dict__(self):
        return {'id': self.id,
                'title': self.name}