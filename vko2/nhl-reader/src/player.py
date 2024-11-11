class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.a = dict['nationality']
        self.b = dict['goals']
        self.c = dict['assists']
        self.bc = self.b + self.c
        self.d = dict['team']
    
    def __str__(self):
        return f'{self.name:<27} {self.a} {self.bc}'
