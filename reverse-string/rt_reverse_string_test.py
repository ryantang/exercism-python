import unittest

from reverse_string import (reverse, )

class RtReverseStringTest(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse('stressed'), 'desserts')
    def test_empty_string(self):
        self.assertEqual(reverse(''), '')
    def test_a_word(self):
        self.assertEqual(reverse('robot'), 'tobor')
