import unittest

from hamming import (distance, )

class RtHammingTest(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(distance('AACG','ATCG'), 1)
    def test_different_length(self):
        with self.assertRaises(ValueError) as err:
            distance("ATA", "AGTG")