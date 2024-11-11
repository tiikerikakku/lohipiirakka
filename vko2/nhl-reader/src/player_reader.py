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

        # self._b = set()

        # for x in self.players:
        #     self._b.add(x.a)
        
        # print(sorted(list(self._b)))
