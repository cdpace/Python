class Card:

    def __init__(self, name,suite, *values):
        self.name = name
        self.suite = suite
        self.values = values
    
    def __str__(self):
        return f'{self.name} of {self.suite}'