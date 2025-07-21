import unittest 
from acronym import (abbreviate, )

class RtAcronymTest(unittest.TestCase):
    def test_asap(self):
        self.assertEqual(abbreviate('As Soon As Possible'), 'ASAP')

    def test_lcd(self):
        self.assertEqual(abbreviate('Liquid-crystal display'), 'LCD')

    def test_skip_multiple_separators(self):
        self.assertEqual(abbreviate("Situation normal -- all f'ed up"), 'SNAFU')