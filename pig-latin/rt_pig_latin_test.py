import unittest

from pig_latin import (translate, )

class RtPigLatinTest(unittest.TestCase):
    def test_translate_begin_with_vowel(self):
        self.assertEqual(translate('apple'),'appleay')
    def test_translate_begin_with_xr(self):
        self.assertEqual(translate('xray'),'xrayay')
    def test_translate_begin_with_yt(self):
        self.assertEqual(translate('yttria'),'yttriaay')
    def test_translate_begin_with_1constant(self):
        self.assertEqual(translate('pig'),'igpay')
    def test_translate_begin_with_3constant(self):
        self.assertEqual(translate('chair'),'airchay')
    def test_translate_begin_with_3constant(self):
        self.assertEqual(translate('thrush'),'ushthray')
    def test_translate_begin_with_qu(self):
        self.assertEqual(translate('quick'),'ickquay')
    def test_translate_begin_with_squ(self):
        self.assertEqual(translate('square'),'aresquay')
    def test_translate_has_const_then_y(self):
        self.assertEqual(translate('my'),'ymay')
    def test_translate_has_const_then_y2(self):
        self.assertEqual(translate('rhythm'),'ythmrhay')
    def test_trasnlate_non_alpha(self):
        with self.assertRaises(ValueError):
            translate('12345')