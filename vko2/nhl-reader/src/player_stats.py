class PlayerStats:
    def __init__(self, a):
        self._a = a

    def top_scorers_by_nationality(self, q):
        a = []

        for x in self._a.players:
            if x.a == q:
                a.append(x)

        return sorted(a, key=lambda x: x.bc, reverse=True)
