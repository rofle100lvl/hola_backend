class Question:
    id = -1
    name = ""
    question = ""

    def __init__(self, id, name, question):
        self.id = id
        self.name = name
        self.question = question

    def __dict__(self):
        return {'id': self.id,
                'question': self.question,
                'name': self.name}
