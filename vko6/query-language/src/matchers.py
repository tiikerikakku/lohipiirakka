class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    def __init__(self):
        pass

    def test(self, player):
        return True


class Not:
    def __init__(self, a):
        self._a = a

    def test(self, player):
        return not self._a.test(player)


class HasFewerThan:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def test(self, player):
        return not HasAtLeast(self._a, self._b).test(player)


class Or:
    def __init__(self, *a):
        self._a = a

    def test(self, player):
        for x in self._a:
            if x.test(player):
                return True
            
        return False
