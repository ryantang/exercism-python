import unittest

from secret_handshake import (commands, )

class RtSecretHandshakeTest(unittest.TestCase):
    def test_some_handshake(self):
        self.assertEqual(commands("00011"), ["wink", "double blink"])
    def test_all_actions(self):
        self.assertEqual(commands("01111"), ["wink", "double blink", "close your eyes", "jump"])
    def test_reverse(self):
        self.assertEqual(commands("11001"), ["jump", "wink"])