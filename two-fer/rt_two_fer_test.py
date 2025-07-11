import unittest

from two_fer import (two_fer, )

class RtTwoFerTest(unittest.TestCase):
    def test_with_name(self):
        self.assertEqual("One for Juliet, one for me.", two_fer("Juliet"))
    def test_with_no_name(self):
        self.assertEqual("One for you, one for me.", two_fer())
        