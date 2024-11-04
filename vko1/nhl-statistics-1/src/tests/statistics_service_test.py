import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
  def get_players(self):
    return [
      Player('Bärlund', 'A', 1, 2),
      Player('Helganatt', 'A', 0, 29),
      Player('Pestosås', 'B', 7, 0),
      Player('Kartongsmakande', 'C', 0, 0)
    ]
  
class TestStatisticsService(unittest.TestCase):
  def setUp(self):
    self.a = StatisticsService(PlayerReaderStub())

  def test_a(self):
    q = self.a.search('Bärlund')
    self.assertEqual(q.name, 'Bärlund')

  def test_b(self):
    q = self.a.search('Mustakallio')
    self.assertEqual(q, None)

  def test_c(self):
    q = self.a.team('A')
    w = ['Bärlund', 'Helganatt']
    e = [x.name for x in q]
    self.assertEqual(e, w)

  def test_d(self):
    q = self.a.top(2)
    w = ['Helganatt', 'Pestosås']
    e = [x.name for x in q]
    self.assertEqual(w, e)

  def test_e(self):
    q = self.a.top(1, SortBy.GOALS)
    self.assertEqual(q[0].name, 'Pestosås')

  def test_f(self):
    q = self.a.top(1, SortBy.ASSISTS)
    self.assertEqual(q[0].name, 'Helganatt')
