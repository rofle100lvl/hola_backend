class Developer:
    def __init__(self, id, name, description, imageUrl):
        self.id = str(id)
        self.name = name
        self.description = description
        self.imageUrl = imageUrl

    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'imageUrlString': self.imageUrl
        }
