import unittest

from etl import (transform,)

class RtEtlTest(unittest.TestCase):
    def test_basic_case(self):
        old = {1:['A']}
        new = {'a': 1}
        self.assertEqual(transform(old), new)