from matchers import All, And, Or, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, a=All()):
        self._a = a

    def build(self):
        return self._a

    def one_of(self, a, b):
        return QueryBuilder(Or(a, b))

    def plays_in(self, *a):
        return QueryBuilder(And(self._a, PlaysIn(*a)))

    def has_at_least(self, *a):
        return QueryBuilder(And(self._a, HasAtLeast(*a)))

    def has_fewer_than(self, *a):
        return QueryBuilder(And(self._a, HasFewerThan(*a)))
