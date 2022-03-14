class Question:
    id = -1
    question = ""

    def __init__(self, id, question):
        self.id = id
        self.question = question

    def __dict__(self):
        return {'id': self.id,
                'title': f"Карта {self.id}",
                'text': self.question}
