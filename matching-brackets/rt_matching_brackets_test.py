import unittest

from matching_brackets import (is_paired, )

class RtMatchingBrackets(unittest.TestCase):
    def test_nested_matched(self):
        self.assertTrue(is_paired("{what is (42)}"))
    def test_nested_unmatched(self):
        self.assertTrue(is_paired("{}()()[]"))
    def test_unmatched(self):
        self.assertFalse(is_paired("[text]}"), False)
