# coding=utf-8

import unittest
from edad import Edad

class TestEdad(unittest.TestCase):

    def setUp(self):
        self.edad = Edad()

    def test_si_tienes_neg_5_anios_no_existes(self):
        self.assertEquals(self.obtener_resultado(-5),
                            u'No existes')

    def test_si_tienes_0_anios_eres_bebe(self):
        self.assertEquals(self.obtener_resultado(0),
                            u'Eres un bebe')

    def test_si_tienes_8_anios_eres_ninio(self):
        self.assertEquals(self.obtener_resultado(8),
                            u'Eres un nino')

    def test_si_tienes_15_anios_eres_adolescente(self):
        self.assertEquals(self.obtener_resultado(15),
                            u'Eres un adolescente')

    def test_si_tienes_50_anios_eres_adulto(self):
        self.assertEquals(self.obtener_resultado(50),
                            u'Eres un adulto')

    def test_si_tienes_100_anios_eres_adulto_mayor(self):
        self.assertEquals(self.obtener_resultado(100),
                            u'Eres un adulto mayor')

    def test_si_tienes_275_anios_eres_mummra(self):
        self.assertEquals(self.obtener_resultado(275),
                            u'Eres Mumm-Ra')

    def obtener_resultado(self, edad):
        return self.edad.evaluar_edad(edad)

    def tearDown(self):
        pass

if __name__ == '__main__': # pragma: no cover
    unittest.main() # pragma: no cover
