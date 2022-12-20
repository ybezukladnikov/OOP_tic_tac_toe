class Player:
    def __init__(self, name):
        self.name = name

    def make_step(self, dictionary, key, value):
        dictionary[key] = value