import unittest

from rna_transcription import (to_rna, )

class RtRnaTranscriptionTest(unittest.TestCase):
    def test_basic_dna(self):
        self.assertEqual(to_rna('GCTA'), 'CGAU')