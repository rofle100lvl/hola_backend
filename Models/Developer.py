class Developer:
    def __init__(self, id, name, description, imageUrl, networkUrl):
        self.id = id
        self.name = name
        self.description = description
        self.imageUrl = imageUrl
        self.networkUrl = networkUrl

    def __dict__(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'imageUrlString': self.imageUrl,
            'networkUrl': self.networkUrl
        }
