import unittest

from isbn_verifier import (is_valid,)

class RtIsbnVerifierTest(unittest.TestCase):
    def test_valid_isbn(self):
        self.assertEqual(is_valid('3-598-21508-8'), True)
    def test_invalid_isbn(self):
        self.assertEqual(is_valid('3-598-21508-X'), False)