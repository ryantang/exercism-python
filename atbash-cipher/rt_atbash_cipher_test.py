import unittest

from atbash_cipher import (encode, decode)

class RtAtbashCipherTest(unittest.TestCase):
    def test_encode_test(self):
        self.assertEqual(encode('test'),'gvhg')
    def test_encode_loger(self):
        self.assertEqual(encode('x123yes'),'c123b vh')
    def test_decode_test(self):
        self.assertEqual(decode('gvhg'),'test')
    def test_decode_longer(self):     
        self.assertEqual(decode('gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt'),'thequickbrownfoxjumpsoverthelazydog')

