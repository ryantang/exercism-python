import unittest

from resistor_color import (color_code, colors)

class RtResistorColorTest(unittest.TestCase):
    def test_color(self):
        self.assertEqual(color_code('brown'), 1)
    def test_another_color(self):
        self.assertEqual(color_code('grey'), 8)
        