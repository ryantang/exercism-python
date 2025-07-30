import unittest

from prime_factors import (factors,)

class RtPrimeFactorsTest(unittest.TestCase):
    def test_two(self):
        self.assertEqual(factors(2), [2])
    def test_six(self):
        self.assertEqual(factors(6), [2, 3])
    def test_twelve(self):
        self.assertEqual(factors(12), [2, 2, 3])