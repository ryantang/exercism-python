import unittest

from rotational_cipher import (rotate,)

class RtRotationalCipherTest(unittest.TestCase):
    def test_basic_cipher(self):
        self.assertEqual(rotate('abc', 4), 'efg')
    def test_rotation_across_boundary(self):
        self.assertEqual(rotate('vwxyz', 4), 'zabcd')
    def test_upper_case(self):
        self.assertEqual(rotate('Abc', 4), 'Efg')
    def test_non_alphabet_characters(self):
        self.assertEqual(rotate('5 More Minutes!', 1), '5 Npsf Njovuft!')