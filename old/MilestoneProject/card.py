class Card:

    face_up = False

    def __init__(self, name,suite, *values):
        self.name = name
        self.suite = suite
        self.values = values
    
    def __str__(self):
        return f'{self.name} of {self.suite}'
    
    def toggle_face(self):
        self.face_up = not self.face_up
        return self.face_up


