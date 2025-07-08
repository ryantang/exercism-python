import unittest

from space_age import (SpaceAge, )

class RtSpaceAge(unittest.TestCase):
    def test_on_earth(self):
        self.assertEqual(SpaceAge(1000000000).on_earth, 31.69)