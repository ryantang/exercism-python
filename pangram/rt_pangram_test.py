import unittest

from pangram import (is_pangram, )

class RtPangramTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(is_pangram("foo"), False)
    def test_all_letters(self):
        self.assertEqual(is_pangram("abcdefghijklmnopqrstuvwxyz"), True)
    def test_works_with_additional_chars(self):
        self.assertEqual(is_pangram("abcdefghijklmnopqrstuvwxyz @$G882j"), True)
    def test_works_with_capitals(self):
        self.assertEqual(is_pangram("abCdefghijklmNopqrstuvwxyZ"), True)
    def test_works_with_capitals(self):
        famous_pangram = "The quick brown fox jumps over the lazy dog."
        self.assertEqual(is_pangram(famous_pangram), True)


