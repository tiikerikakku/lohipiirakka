from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, q=[], a=All()):
        self._q = q
        self._q.append(a)

    def build(self):
        return And(*self._q)

    def plays_in(self, *a):
        return QueryBuilder(self._q, PlaysIn(*a))

    def has_at_least(self, *a):
        return QueryBuilder(self._q, HasAtLeast(*a))

    def has_fewer_than(self, *a):
        return QueryBuilder(self._q, HasFewerThan(*a))
