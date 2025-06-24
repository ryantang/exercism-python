import unittest

from perfect_numbers import (classify,)

class RtPerfectNumbersTest(unittest.TestCase):
    def test_six_is_perfect(self):
        self.assertEqual(classify(6), 'perfect')
    def test_twentyeight_is_perfect(self):
        self.assertEqual(classify(28), 'perfect')
    def test_twelve_is_abundant(self):
        self.assertEqual(classify(12), 'abundant')
    def test_thirteen_is_deficient(self):
        self.assertEqual(classify(13), 'deficient')
