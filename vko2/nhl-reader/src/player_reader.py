import requests
from player import Player

class PlayerReader:
    def __init__(self, a):
        self._a = a

        self._r = requests.get(self._a).json()

        self.players = []

        for x in self._r:
            xx = Player(x)
            self.players.append(xx)
