import unittest

from anagram import (find_anagrams, )

class RtAnagramTest(unittest.TestCase):
    def test_basic_anagram(self):
        self.assertEqual(find_anagrams('stop', ['pots', 'stone', 'top']), ['pots'])
    def test_exclude_self(self):
        self.assertEqual(find_anagrams('stop', ['stop']), [])
    def test_exclude_self_with_case_difference(self):
        self.assertEqual(find_anagrams('stop', ['StoP']), [])
    def test_basic_anagram(self):
        self.assertEqual(find_anagrams('stop', ['Pots', 'Stone', 'Top']), ['Pots'])