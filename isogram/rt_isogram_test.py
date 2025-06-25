import unittest

from isogram import (is_isogram, )

class RtIsogramTest(unittest.TestCase):
    def test_basic_isogram(self):
        self.assertEqual(is_isogram('abc'), True)
    def test_non_isogram(self):
        self.assertEqual(is_isogram('caabc'), False)
    def test_capitals(self):
        self.assertEqual(is_isogram('CAabc'), False)
    def test_capitals_isograms(self):
        self.assertEqual(is_isogram('DabcE'), True)
    def test_other_characters(self):
        self.assertEqual(is_isogram('six-year-old'), True)

