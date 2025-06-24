import unittest

from darts import (
    score,
)

class RtDartsTest(unittest.TestCase):
    def test_perfect_hit(self):
        self.assertEqual(score(0, 0), 10)
    def test_inner_circle(self):
        self.assertEqual(score(0.5, 0.5), 10)
    def test_edge_of_inner_circle(self):
        self.assertEqual(score(-1, 0), 10)
    def test_middle_circle(self):
        self.assertEqual(score(-1, 1), 5)
    def test_outer_circle(self):
        self.assertEqual(score(5, -5), 1)
    def test_miss(self):
        self.assertEqual(score(10, 12), 0)