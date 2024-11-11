class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.a = dict['nationality']
    
    def __str__(self):
        return self.name
